# -*- coding: utf-8 -*-
"""CILS 题库真人发音音频补丁：
为每道题（.q-item 的题干）与每段听力/阅读文本（.text 的 pre）生成 edge-tts(ELSA) mp3，
并往各等级页注入 🔊 播放按钮。映射用「归一化文本 -> 文件名」，运行时由 JS 按相同归一化匹配，
不改动任何现有判分逻辑。可重入：已存在的 mp3 会跳过，已注入脚本的页会跳过。
用法：python gen_cils_audio.py [卷号|all]
"""
import os, re, html, sys, asyncio, json, hashlib
import edge_tts

ROOT = r"D:\意大利语材料\italiano-esami\CILS"
VOICE = "it-IT-ElsaNeural"
CONCURRENCY = 6
RETRIES = 4
LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

SPK_CSS = (
    ".q-item,.text{position:relative}\n"
    ".spk{position:absolute;top:8px;right:8px;z-index:2;border:none;"
    "background:rgba(123,30,43,.08);color:var(--wine);border-radius:50%;"
    "width:30px;height:30px;font-size:15px;cursor:pointer;line-height:1;"
    "display:flex;align-items:center;justify-content:center;transition:.15s}\n"
    ".spk:hover{background:var(--wine);color:#fff}\n"
    ".spk.playing{background:var(--wine2);color:#fff}\n"
)

PLAYER_JS = r"""
(function(){
  function normQ(s){ return s.replace(/^\s*\d+\s*[\.\)]\s*/,'').replace(/\s+/g,' ').trim().toLowerCase(); }
  function normP(s){ return s.replace(/\s+/g,' ').trim().toLowerCase(); }
  var cur=null, curBtn=null;
  function addSpk(el, file){
    var b=document.createElement('button');
    b.className='spk'; b.type='button'; b.textContent='\u{1F50A}'; b.title='Ascolta la pronuncia';
    b.addEventListener('click', function(e){ e.stopPropagation(); toggle(b,file); });
    el.appendChild(b);
  }
  function toggle(b,file){
    if(cur && curBtn!==b){ cur.pause(); curBtn.textContent='\u{1F50A}'; curBtn.classList.remove('playing'); }
    if(b._a && !b._a.paused){ b._a.pause(); b._a=null; b.textContent='\u{1F50A}'; b.classList.remove('playing'); if(curBtn===b)curBtn=null; return; }
    var a=new Audio(file); a.play().catch(function(){});
    b._a=a; cur=a; curBtn=b; b.textContent='\u{1F508}'; b.classList.add('playing');
    a.onended=function(){ b.textContent='\u{1F50A}'; b.classList.remove('playing'); if(curBtn===b)curBtn=null; };
  }
  function run(){
    var A=window.CILS_AUDIO||{};
    document.querySelectorAll('.q-item').forEach(function(el){
      var s=el.querySelector('.q-stem'); if(!s) return;
      var t=normQ(s.textContent); if(A[t]) addSpk(el, A[t]);
    });
    document.querySelectorAll('.text').forEach(function(el){
      var p=el.querySelector('pre'); if(!p) return;
      var t=normP(p.textContent); if(A[t]) addSpk(el, A[t]);
    });
  }
  if(document.readyState!=='loading') run(); else document.addEventListener('DOMContentLoaded', run);
})();
"""


def strip_tags(s):
    return re.sub(r'<[^>]+>', ' ', s)


def norm_qstem(inner):
    t = strip_tags(inner)
    t = html.unescape(t).lower()
    t = t.replace('\u00a0', ' ')
    t = re.sub(r'^\s*\d+\s*[\.\)]\s*', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def norm_pre(inner):
    t = strip_tags(inner)
    t = html.unescape(t).lower()
    t = t.replace('\u00a0', ' ')
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def extract_targets(html_text):
    qstems, pres = set(), set()
    for m in re.finditer(r'<p class="q-stem">(.*?)</p>', html_text, re.S):
        n = norm_qstem(m.group(1))
        if n:
            qstems.add(n)
    for m in re.finditer(r'<div class="text[^"]*">(.*?)</div>', html_text, re.S):
        block = m.group(1)
        pm = re.search(r'<pre>(.*?)</pre>', block, re.S)
        if pm:
            n = norm_pre(pm.group(1))
            if n:
                pres.add(n)
    return qstems, pres


async def gen_one(text, out_path):
    for _ in range(RETRIES):
        try:
            comm = edge_tts.Communicate(text, VOICE)
            await comm.save(out_path)
            if os.path.getsize(out_path) > 200:
                return True
        except Exception:
            await asyncio.sleep(1.5)
    return False


async def gen_all(texts, audio_dir):
    sem = asyncio.Semaphore(CONCURRENCY)
    results = {}

    async def worker(text):
        h = hashlib.md5(text.encode('utf-8')).hexdigest()[:16]
        fp = os.path.join(audio_dir, h + '.mp3')
        if os.path.exists(fp) and os.path.getsize(fp) > 200:
            results[text] = h + '.mp3'
            return
        async with sem:
            ok = await gen_one(text, fp)
            if ok:
                results[text] = h + '.mp3'

    await asyncio.gather(*[worker(t) for t in texts])
    return results


def inject(html_text, index_dict):
    if 'CILS_AUDIO' in html_text:
        return html_text  # 已注入，跳过
    if '.spk{' not in html_text:
        html_text = html_text.replace('</style>', SPK_CSS + '</style>', 1)
    idx_json = json.dumps(index_dict, ensure_ascii=False)
    scripts = ('<script src="audio_index.js"></script>\n'
               '<script>' + PLAYER_JS + '</script>\n')
    html_text = html_text.replace('</body>', scripts + '</body>', 1)
    return html_text


def process_volume(vol):
    vdir = os.path.join(ROOT, 'CILS_Vol%d_esami' % vol)
    if not os.path.isdir(vdir):
        print('跳过：目录不存在', vdir)
        return
    all_q, all_p = set(), set()
    for lvl in LEVELS:
        fp = os.path.join(vdir, lvl + '.html')
        if not os.path.exists(fp):
            continue
        with open(fp, encoding='utf-8') as f:
            h = f.read()
        q, p = extract_targets(h)
        all_q |= q
        all_p |= p
    texts = list(all_q | all_p)
    print('Vol.%d 待生成音频片段：%d（题干 %d / 文本 %d）' % (vol, len(texts), len(all_q), len(all_p)))
    audio_dir = os.path.join(vdir, 'audio')
    os.makedirs(audio_dir, exist_ok=True)
    results = asyncio.run(gen_all(texts, audio_dir))
    print('  -> 成功生成 %d / %d 个 mp3' % (len(results), len(texts)))
    index = {t: 'audio/' + results[t] for t in results}
    with open(os.path.join(vdir, 'audio_index.js'), 'w', encoding='utf-8') as f:
        f.write('window.CILS_AUDIO=' + json.dumps(index, ensure_ascii=False) + ';')
    # 注入脚本到各等级页
    for lvl in LEVELS:
        fp = os.path.join(vdir, lvl + '.html')
        if not os.path.exists(fp):
            continue
        with open(fp, encoding='utf-8') as f:
            h = f.read()
        if 'CILS_AUDIO' in h:
            continue
        h2 = inject(h, index)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(h2)
    print('  -> 已注入播放器脚本到各等级页')


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else 'all'
    vols = [int(arg)] if arg != 'all' else range(1, 6)
    for v in vols:
        process_volume(v)


if __name__ == '__main__':
    main()
