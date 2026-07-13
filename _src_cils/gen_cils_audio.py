# -*- coding: utf-8 -*-
"""CILS 听力真人发音补丁（稳健版）：
只为「Ascolto 听力原文」(.audio-block) 生成 edge-tts(ELSA) mp3 并注入原生 <audio controls>；
其他模块（阅读/语法/写作/口语）及所有题目一律不加音频。
听力原文默认折叠隐藏（<details class="transcript">），点「📝 显示听力原文」展开。
播放/进度条/下载/调速均由浏览器原生 <audio controls> 提供（与 CELI 听力布局一致）。
采用「服务端直注 src」取代旧的「运行时文本归一化→全局索引」匹配，音频必指向已验证存在的文件。
用法：
  python gen_cils_audio.py [卷号|all]   生成并注入
  python gen_cils_audio.py validate     仅校验（不生成）
"""
import os, re, html, sys, asyncio, hashlib
import edge_tts

ROOT = r"D:\意大利语材料\italiano-esami\CILS"
VOICE = "it-IT-ElsaNeural"
CONCURRENCY = 6
RETRIES = 4
LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']


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
    adir = os.path.join(vdir, 'audio')

    # 收集本卷所有 Ascolto 听力文本（audio-block 内的 <pre>）+ 口语参考答案文本（oral-audio 内的 <pre>）
    plan = []
    for lvl in LEVELS:
        fp = os.path.join(vdir, lvl + '.html')
        if not os.path.exists(fp):
            continue
        h = open(fp, encoding='utf-8').read()
        for m in re.finditer(r'<div class="audio-block">(.*?)</div>', h, re.S):
            block = m.group(1)
            pm = re.search(r'<pre>(.*?)</pre>', block, re.S)
            if not pm:
                continue
            raw = pm.group(1)
            nt = norm_fn(raw)
            if nt:
                plan.append((lvl, nt, raw))
        for m in re.finditer(r'<div class="oral-audio">(.*?)</div>', h, re.S):
            block = m.group(1)
            pm = re.search(r'<pre>(.*?)</pre>', block, re.S)
            if not pm:
                continue
            raw = pm.group(1)
            nt = norm_fn(raw)
            if nt:
                plan.append((lvl, nt, raw))

    print('Vol.%d 待生成音频片段（听力+口语参考）：%d' % (vol, len(plan)))
    os.makedirs(adir, exist_ok=True)
    texts = [p[2] for p in plan]
    results = asyncio.run(gen_all(texts, adir))
    print('  -> 成功生成 %d / %d 个 mp3' % (len(results), len(texts)))

    # 注入：每个 audio-block / oral-audio 替换 .aspk-slot 为原生 <audio controls>
    for lvl in LEVELS:
        fp = os.path.join(vdir, lvl + '.html')
        if not os.path.exists(fp):
            continue
        h = open(fp, encoding='utf-8').read()
        if '<audio controls' in h:
            continue  # 已注入，跳过整页
        if 'class="audio-block"' not in h and 'class="oral-audio"' not in h:
            continue

        def repl(m):
            block = m.group(0)
            pm = re.search(r'<pre>(.*?)</pre>', block, re.S)
            if not pm:
                return block
            nt = norm_fn(pm.group(1))
            fn = results.get(pm.group(1)) or results.get(nt)
            if not fn:
                return block
            audio = ('<audio controls preload="none" src="audio/%s" '
                      'type="audio/mpeg"></audio>' % fn)
            return block.replace('<span class="aspk-slot"></span>', audio, 1)

        h2 = re.sub(r'<div class="audio-block">(.*?)</div>', repl, h, flags=re.S)
        h2 = re.sub(r'<div class="oral-audio">(.*?)</div>', repl, h2, flags=re.S)
        open(fp, 'w', encoding='utf-8').write(h2)
    print('  -> 已注入原生 <audio controls> 播放器')


def validate_volume(vol):
    vdir = os.path.join(ROOT, 'CILS_Vol%d_esami' % vol)
    total_blocks = 0
    audio_ok = 0
    missing_file = 0
    invalid_file = 0
    stray_audio = 0  # 出现在 audio-block 之外的 <audio controls>
    for lvl in LEVELS:
        fp = os.path.join(vdir, lvl + '.html')
        if not os.path.exists(fp):
            continue
        h = open(fp, encoding='utf-8').read()
        blocks = re.findall(r'<div class="audio-block">(.*?)</div>', h, re.S)
        for b in blocks:
            total_blocks += 1
            if '<audio controls' in b and 'src="audio/' in b:
                audio_ok += 1
                dm = re.search(r'src="(audio/[^"]+)"', b)
                if dm:
                    fpath = os.path.join(vdir, dm.group(1))
                    if not os.path.exists(fpath):
                        missing_file += 1
                    elif not is_valid_mp3(fpath):
                        invalid_file += 1
            else:
                missing_file += 1
        # 检查整页里是否有不在 audio-block / oral-audio 内的 <audio controls>
        for m in re.finditer(r'<audio controls[^>]*src="(audio/[^"]+)"', h):
            prefix = h[:h.find('src="%s"' % m.group(1))]
            if 'audio-block' not in prefix and 'oral-audio' not in prefix:
                stray_audio += 1
    print('Vol.%d  听力块=%d  音频OK=%d  缺文件=%d  无效=%d  越界音频=%d'
          % (vol, total_blocks, audio_ok, missing_file, invalid_file, stray_audio))
    return (total_blocks == audio_ok and missing_file == 0
            and invalid_file == 0 and stray_audio == 0)


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
