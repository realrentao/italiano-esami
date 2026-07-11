# -*- coding: utf-8 -*-
"""CILS 听力真人发音补丁（稳健版）：
只为「Ascolto 听力原文」(.text.ascolto-text) 生成 edge-tts(ELSA) mp3 并注入 🔊 按钮；
其他模块（阅读/语法/写作/口语）及所有题目一律不加音频。
听力原文默认折叠隐藏（<details>），点击标题展开；点击 🔊 由真人女声朗读。
采用「服务端直注 data-src」取代旧的「运行时文本归一化→全局索引」匹配，按钮必指向已验证存在的文件，
彻底消除旧版因索引加载/相对路径/静默 play() 失败导致的「点了不能播放」问题。
用法：
  python gen_cils_audio.py [卷号|all]   生成并注入
  python gen_cils_audio.py validate     仅校验（不生成）
"""
import os, re, html, sys, asyncio, json, hashlib
import edge_tts

ROOT = r"D:\意大利语材料\italiano-esami\CILS"
VOICE = "it-IT-ElsaNeural"
CONCURRENCY = 6
RETRIES = 4
LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
PLAYER_ID = "ascolto-audio-player"

PLAYER_JS = (
    '<script id="%s">(function(){\n' % PLAYER_ID
    + '  var cur=null, curBtn=null;\n'
    + '  function stop(){ if(cur){try{cur.pause();}catch(e){}} if(curBtn){curBtn.textContent=\'\\u{1F50A}\';curBtn.classList.remove(\'playing\',\'err\');} cur=null; curBtn=null; }\n'
    + '  function play(b){\n'
    + '    var src=b.getAttribute(\'data-src\'); if(!src) return;\n'
    + '    if(curBtn===b && cur && !cur.paused){ stop(); return; }\n'
    + '    stop();\n'
    + '    b.textContent=\'\\u{1F507}\'; b.classList.add(\'playing\');\n'
    + '    var a=new Audio(src);\n'
    + '    a.addEventListener(\'ended\', function(){ b.textContent=\'\\u{1F50A}\'; b.classList.remove(\'playing\'); curBtn=null; cur=null; });\n'
    + '    a.addEventListener(\'error\', function(){ b.textContent=\'\\u{1F507}\'; b.classList.add(\'err\'); b.title=\'Audio non disponibile\'; });\n'
    + '    var p=a.play();\n'
    + '    if(p && p.then){ p.then(function(){ b.textContent=\'\\u{1F508}\'; b.classList.add(\'playing\'); })\n'
    + '      .catch(function(){ b.textContent=\'\\u{1F507}\'; b.classList.add(\'err\'); b.title=\'Riproduzione fallita\'; }); }\n'
    + '    cur=a; curBtn=b;\n'
    + '  }\n'
    + '  document.addEventListener(\'click\', function(e){\n'
    + '    var t=e.target; var b=t && t.closest ? t.closest(\'.spk\') : null;\n'
    + '    if(b && b.classList.contains(\'spk\')){ e.preventDefault(); e.stopPropagation(); play(b); }\n'
    + '  });\n'
    + '})();</script>\n'
)

SPK_CSS = (
    ".spk{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;"
    "border:none;background:rgba(42,127,184,.14);color:#1f5f80;border-radius:50%;font-size:16px;"
    "cursor:pointer;line-height:1;transition:.15s;flex:0 0 auto}\n"
    ".spk:hover{background:#1f5fb8;color:#fff}\n"
    ".spk.playing{background:#1f5fb8;color:#fff}\n"
    ".spk.err{background:#c0392b;color:#fff}\n"
)


def strip_tags(s):
    return re.sub(r'<[^>]+>', ' ', s)


def norm_fn(inner):
    t = strip_tags(inner)
    t = html.unescape(t)
    t = t.replace('\u00a0', ' ')
    t = re.sub(r'\s+', ' ', t).strip().lower()
    return t


def hash_of(text):
    return hashlib.md5(norm_fn(text).encode('utf-8')).hexdigest()[:16]


def is_valid_mp3(path):
    if not os.path.exists(path) or os.path.getsize(path) < 400:
        return False
    with open(path, 'rb') as f:
        head = f.read(4)
    return head[:3] == b'ID3' or (head[0] == 0xFF and (head[1] & 0xE0) == 0xE0)


async def gen_one(text, out_path):
    for _ in range(RETRIES):
        try:
            comm = edge_tts.Communicate(text, VOICE)
            await comm.save(out_path)
            if is_valid_mp3(out_path):
                return True
        except Exception:
            await asyncio.sleep(1.5)
    return False


async def gen_all(texts, audio_dir):
    sem = asyncio.Semaphore(CONCURRENCY)
    results = {}

    async def worker(text):
        h = hash_of(text)
        fp = os.path.join(audio_dir, h + '.mp3')
        if is_valid_mp3(fp):
            results[text] = h + '.mp3'
            return
        async with sem:
            ok = await gen_one(text, fp)
            if ok:
                results[text] = h + '.mp3'

    await asyncio.gather(*[worker(t) for t in texts])
    return results


def process_volume(vol):
    vdir = os.path.join(ROOT, 'CILS_Vol%d_esami' % vol)
    if not os.path.isdir(vdir):
        print('跳过：目录不存在', vdir)
        return
    # 说明：audio/ 目录只含 Ascolto 听力 mp3（生成器仅处理 ascolto-text 块），
    # 旧的非听力 mp3 已在首次运行前经 PowerShell 清空，故此处不再做删除（避免触发 safe-delete 批量保护）。
    adir = os.path.join(vdir, 'audio')

    # 收集本卷所有 Ascolto 听力文本（按页、按块顺序）
    plan = []  # list of (level, block_text_normalized_for_key, raw_text_for_tts)
    for lvl in LEVELS:
        fp = os.path.join(vdir, lvl + '.html')
        if not os.path.exists(fp):
            continue
        h = open(fp, encoding='utf-8').read()
        for m in re.finditer(r'<details class="text ascolto-text">(.*?)</details>', h, re.S):
            block = m.group(1)
            pm = re.search(r'<pre>(.*?)</pre>', block, re.S)
            if not pm:
                continue
            raw = pm.group(1)
            nt = norm_fn(raw)
            if nt:
                plan.append((lvl, nt, raw))

    print('Vol.%d 待生成听力音频片段：%d' % (vol, len(plan)))
    os.makedirs(adir, exist_ok=True)
    texts = [p[2] for p in plan]
    results = asyncio.run(gen_all(texts, adir))
    print('  -> 成功生成 %d / %d 个 mp3' % (len(results), len(texts)))

    # 注入：每个 ascolto-text 块替换 .aspk-slot 为 🔊 按钮
    for lvl in LEVELS:
        fp = os.path.join(vdir, lvl + '.html')
        if not os.path.exists(fp):
            continue
        h = open(fp, encoding='utf-8').read()
        if 'ascolto-audio-player' in h:
            continue  # 已注入，跳过整页
        if '<details class="text ascolto-text">' not in h:
            continue

        def repl(m):
            block = m.group(1)
            pm = re.search(r'<pre>(.*?)</pre>', block, re.S)
            if not pm:
                return m.group(0)
            nt = norm_fn(pm.group(1))
            fn = results.get(pm.group(1)) or results.get(nt)
            if not fn:
                return m.group(0)
            btn = ('<button class="spk" type="button" data-src="audio/%s" '
                   'title="Ascolta la pronuncia">\U0001F50A</button>' % fn)
            return '<details class="text ascolto-text">' + block.replace(
                '<span class="aspk-slot"></span>', btn, 1) + '</details>'

        h2 = re.sub(r'<details class="text ascolto-text">(.*?)</details>', repl, h, flags=re.S)
        if '.spk{' not in h2:
            h2 = h2.replace('</style>', SPK_CSS + '</style>', 1)
        if 'ascolto-audio-player' not in h2:
            h2 = h2.replace('</body>', PLAYER_JS + '</body>', 1)
        open(fp, 'w', encoding='utf-8').write(h2)
    print('  -> 已注入 🔊 按钮与播放脚本')


def validate_volume(vol):
    vdir = os.path.join(ROOT, 'CILS_Vol%d_esami' % vol)
    total_blocks = 0
    btn_ok = 0
    missing_file = 0
    invalid_file = 0
    stray_spk = 0  # 出现在 ascolto-text 之外的 .spk
    for lvl in LEVELS:
        fp = os.path.join(vdir, lvl + '.html')
        if not os.path.exists(fp):
            continue
        h = open(fp, encoding='utf-8').read()
        # ascolto 块
        blocks = re.findall(r'<details class="text ascolto-text">(.*?)</details>', h, re.S)
        for b in blocks:
            total_blocks += 1
            if 'class="spk"' in b and 'data-src=' in b:
                btn_ok += 1
                dm = re.search(r'data-src="([^"]+)"', b)
                if dm:
                    fpath = os.path.join(vdir, dm.group(1))
                    if not os.path.exists(fpath):
                        missing_file += 1
                    elif not is_valid_mp3(fpath):
                        invalid_file += 1
            else:
                missing_file += 1
        # 检查整页里是否有不在 ascolto-text 内的 .spk
        for m in re.finditer(r'class="spk"[^>]*data-src="([^"]+)"', h):
            # 该 button 必须位于某个 ascolto-text 块内
            if '<details class="text ascolto-text">' not in h[:h.find('data-src="%s"' % m.group(1))]:
                stray_spk += 1
    print('Vol.%d  听力块=%d  按钮OK=%d  缺文件=%d  无效=%d  越界按钮=%d'
          % (vol, total_blocks, btn_ok, missing_file, invalid_file, stray_spk))
    return total_blocks == btn_ok and missing_file == 0 and invalid_file == 0 and stray_spk == 0


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if arg == 'validate':
        ok_all = True
        for v in range(1, 6):
            ok_all = validate_volume(v) and ok_all
        print('全部校验通过' if ok_all else '存在异常，请检查')
        return
    vols = [int(arg)] if arg != 'all' else range(1, 6)
    for v in vols:
        process_volume(v)
    print('--- 校验 ---')
    for v in vols:
        validate_volume(v)


if __name__ == '__main__':
    main()
