# -*- coding: utf-8 -*-
"""CILS 模拟题库生成器（修正版）：将 5 份 CILS markdown 转为 CELI 风格交互式 HTML。"""
import re, os, sys, html, asyncio

SRC_DIR = r"D:\意大利语材料\italiano-esami\_src_cils"
OUT_BASE = r"D:\意大利语材料\italiano-esami\CILS"
VOICE = "it-IT-ElsaNeural"
AUDIO_ENABLED = False  # 本环境 edge-tts 网络不稳，默认关闭，听力以文本呈现；可改 True 重试

LEVEL_ORDER = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
LEVEL_NAMES = {
    'A1': 'CILS Standard', 'A2': 'CILS', 'B1': 'CILS UNO',
    'B2': 'CILS DUE', 'C1': 'CILS TRE', 'C2': 'CILS QUATTRO'
}
MODULE_ORDER = ['Ascolto', 'Lettura', 'Analisi', 'Scritta', 'Orale']
MODULE_ZH = {'Ascolto': '听力', 'Lettura': '阅读', 'Analisi': '语法分析', 'Scritta': '写作', 'Orale': '口语'}

CILS_CSS = """:root{--wine:#0f766e;--wine2:#14b8a6;--ink:#23211f;--paper:#fbf8f4;--line:#e4ddd2;--ok:#1b7a3d;--no:#c0392b;}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,"Segoe UI",Roboto,"Helvetica Neue","PingFang SC","Microsoft YaHei",sans-serif;color:var(--ink);background:var(--paper);line-height:1.65}
header.top{background:linear-gradient(135deg,var(--wine),var(--wine2));color:#fff;padding:26px 20px;box-shadow:0 2px 10px rgba(0,0,0,.15)}
header.top .back{color:#ffd9df;text-decoration:none;font-size:14px}header.top .topnav{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:4px}header.top .back:hover{text-decoration:underline;opacity:.85}
header.top .ttl{font-size:26px;font-weight:800;margin-top:6px}
header.top .ttl .lvl{display:inline-block;background:#fff;color:var(--wine);border-radius:8px;padding:2px 10px;margin-right:10px;font-size:20px}
header.top .sub{opacity:.9;margin-top:4px;font-size:15px}
main{max-width:880px;margin:0 auto;padding:24px 18px 120px}
section.module{margin:30px 0;background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px 22px;box-shadow:0 1px 4px rgba(0,0,0,.04)}
section.module h2{margin:0 0 14px;color:var(--wine);font-size:20px;border-bottom:2px solid var(--line);padding-bottom:8px}
section.module h3{color:#444;font-size:16px;margin:22px 0 10px}
.mnote{background:#f6f1e9;border-left:4px solid var(--wine);border-radius:8px;padding:10px 14px;margin:12px 0;font-size:13.5px;color:#6b5b4a;line-height:1.7}
/* ====== 模块题目说明气泡（每个板块开头一段说明） ====== */
.mod-instr{margin:14px 0;padding:14px 18px;background:linear-gradient(135deg,#0f766e,#14b8a6);color:#fff;border-radius:14px;box-shadow:0 3px 12px rgba(15,118,110,.18)}
.mod-instr-h{font-weight:800;font-size:16px;margin-bottom:6px;display:flex;align-items:center;gap:8px;letter-spacing:.2px}
.mod-instr-h::before{content:"📋";font-size:18px}
.mod-instr-b{font-size:14px;line-height:1.75;opacity:.96;white-space:pre-wrap}
.text{background:#f6f1e9;border-left:4px solid var(--wine);border-radius:8px;padding:12px 14px;margin:12px 0}
.text h4{margin:0 0 6px;font-size:14px;color:var(--wine)}
pre{white-space:pre-wrap;margin:0;font-family:"Courier New",monospace;font-size:14px}
/* ====== Ascolto 听力（布局与 CELI 一致：🎧 标题头 + 原生音频控件 + 折叠原文） ====== */
.audio-block{background:#eafaf7;border:1px solid #bfe3da;border-left:4px solid #0d9488;border-radius:12px;padding:14px 16px;margin:14px 0}
.audio-block h4{margin:0 0 10px;color:#0f766e;font-size:15px;font-weight:700}
.audio-block audio{width:100%;margin:0 0 10px;display:block}
.transcript{margin-top:2px}
.transcript summary{cursor:pointer;color:#0f766e;font-weight:600;font-size:14px;user-select:none;list-style:none;display:flex;align-items:center;gap:4px}
.transcript summary::-webkit-details-marker{display:none}
.transcript summary:hover{text-decoration:underline}
.transcript .t-open{display:none}
.transcript[open] .t-closed{display:none}
.transcript[open] .t-open{display:inline}
.transcript[open] summary{margin-bottom:8px}
.transcript pre{margin-top:0;background:#fff;border:1px solid #d6ece6;border-radius:10px;padding:12px 14px;color:#234e52;font-size:14px;line-height:1.7}
/* ====== Ascolto 听力题（独立编号卡片） ====== */
.asc-q{display:flex;gap:12px;align-items:flex-start;background:linear-gradient(180deg,#fff,#f6fbfd);border:1px solid #d7e8f0;border-left:4px solid #0369a1;border-radius:12px}
.asc-q__no{flex:0 0 auto;width:30px;height:30px;border-radius:50%;background:#0369a1;color:#fff;font-weight:800;display:inline-flex;align-items:center;justify-content:center;font-size:14px;margin-top:2px}
.asc-q__main{flex:1 1 auto;min-width:0}
.asc-q .q-stem{margin:0 0 10px;font-size:15.5px;line-height:1.5}
.asc-opts{display:flex;flex-direction:column;gap:8px}
.asc-opt{align-items:center;gap:10px;padding:9px 12px;border:1px solid #dce8ef;border-radius:10px;background:#fff;transition:.15s}
.asc-opt:hover{background:#eef6fb;border-color:#9cc4dd}
.asc-opt__k{flex:0 0 auto;width:26px;height:26px;border-radius:7px;background:#e3f0f7;color:#0369a1;font-weight:800;display:inline-flex;align-items:center;justify-content:center;font-size:13px}
.asc-opt__v{flex:1 1 auto;font-size:15px}
.asc-opt:has(input:checked){border-color:#0369a1;background:#e8f4fb;box-shadow:0 0 0 2px rgba(3,105,161,.15)}
.asc-opt:has(input:checked) .asc-opt__k{background:#0369a1;color:#fff}
.items{margin-top:14px}
.q-item{margin:14px 0;padding:12px 14px;border:1px solid var(--line);border-radius:10px;background:#fffdf9}
.q-item.correct{border-color:var(--ok);background:#f1faf3}
.q-item.wrong{border-color:var(--no);background:#fdf1f0}
.q-stem{margin:0 0 8px;font-weight:600}
.opts{display:flex;flex-direction:column;gap:6px}
.opt{display:flex;align-items:center;gap:8px;cursor:pointer;padding:4px 6px;border-radius:6px}
.opt:hover{background:#f3ede3}
.match-sel{font-size:15px;padding:5px 8px;border-radius:6px;border:1px solid #bbb;margin-top:4px}
.blank{font-size:15px;padding:3px 6px;border:1px solid #bbb;border-radius:6px;margin:0 4px;min-width:90px}
.blank.correct{border-color:var(--ok);background:#eafaf0}
.blank.wrong{border-color:var(--no);background:#fdeceb}
.anshint{color:var(--no);font-size:13px;margin-left:6px}
textarea.ans{width:100%;font-size:15px;padding:10px;border:1px solid #ccc;border-radius:8px;font-family:inherit;resize:vertical}
.q-subj .ref{margin-top:10px;padding:10px 12px;background:#eef6fb;border-left:4px solid #2a7fb8;border-radius:8px;font-size:14px;white-space:pre-line}
.q-note{margin-top:8px;font-weight:700;font-size:14px}
.q-note.ok{color:var(--ok)} .q-note.no{color:var(--no)}
.q-note.ans{color:var(--wine)}
.q-oral{background:#fbf7ef;border:1px solid #ecd9b0;border-radius:12px;padding:16px 18px;margin:14px 0}
.q-oral .q-stem{margin:0 0 12px;font-size:15px;line-height:1.7;white-space:pre-wrap}
.oral-scoring{background:#fff;border:1px solid #e7dcc4;border-radius:10px;padding:12px 14px;margin-bottom:12px}
.score-head{font-weight:700;color:#9a6b00;margin-bottom:8px;font-size:14px}
.dims{margin:0;padding-left:20px;font-size:14px;line-height:1.9}
.dims li{margin-bottom:2px}
.rubric-note{margin-top:8px;padding-top:8px;border-top:1px dashed #e0d3b6;font-size:13px;color:#5a4a2a;line-height:1.7}
.oral-ref{background:#eef6fb;border:1px solid #cfe0ea;border-radius:10px;padding:12px 14px}
.ref-head{font-weight:700;color:#1f5f80;margin-bottom:8px;font-size:14px}
.ref-it{font-weight:400;color:#5b87a0;font-style:italic;font-size:12px}
.oral-ref pre{margin:8px 0 0;white-space:pre-wrap;word-break:break-word;font-size:14px;line-height:1.75;background:#fff;border:1px solid #dce8f0;border-radius:8px;padding:10px 12px}
.oral-audio{margin:6px 0 10px}
.otranscript{margin-top:8px}
.otranscript summary{cursor:pointer;color:#1f5f80;font-weight:600;font-size:13px;user-select:none;list-style:none}
.otranscript summary::-webkit-details-marker{display:none}
.otranscript .o-open{display:none}
.otranscript[open] .o-closed{display:none}
.otranscript[open] .o-open{display:inline}
.transcript{margin-top:10px}
.transcript summary{cursor:pointer;color:#1f5f80;font-weight:600;font-size:14px;user-select:none;list-style:none}
.transcript summary::-webkit-details-marker{display:none}
.transcript summary:hover{text-decoration:underline}
.transcript .t-open{display:none}
.transcript[open] .t-closed{display:none}
.transcript[open] .t-open{display:inline}
.transcript[open] summary{margin-bottom:8px}
.transcript pre{margin-top:0}
.soluzioni{margin:28px 0;background:#fff;border:2px dashed var(--wine);border-radius:14px;padding:18px 20px}
.soluzioni h2{margin:0 0 12px;color:var(--wine);font-size:18px}
.soluzioni pre{white-space:pre-wrap;font-size:13.5px;line-height:1.8;background:#fbf6f0;border-radius:8px;padding:12px;font-family:"Courier New",monospace}
#btn-check{position:fixed;left:50%;bottom:22px;transform:translateX(-50%);background:var(--wine);color:#fff;border:none;font-size:17px;font-weight:700;padding:13px 30px;border-radius:30px;cursor:pointer;box-shadow:0 4px 14px rgba(15,118,110,.4);z-index:10}
#btn-check:hover{background:var(--wine2)}
#btn-reset{position:fixed;left:50%;bottom:22px;transform:translateX(-50%);margin-left:170px;background:#555;color:#fff;border:none;font-size:15px;padding:13px 22px;border-radius:30px;cursor:pointer;z-index:10}
#result{margin-top:20px;padding:18px 20px;border-radius:12px;background:#fff;border:2px solid var(--wine);text-align:center}
.res-score{font-size:18px;margin-bottom:10px}
.res-grade{display:inline-block;color:#fff;font-weight:800;font-size:22px;padding:6px 22px;border-radius:10px;margin-bottom:8px}
.res-note{font-size:14px;color:#555;margin-top:8px}
.index-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px;margin-top:20px}
.card{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px;box-shadow:0 1px 4px rgba(0,0,0,.05);transition:.15s}
.card:hover{transform:translateY(-3px);border-color:var(--wine)}
.card .lvl{display:inline-block;background:var(--wine);color:#fff;border-radius:8px;padding:3px 12px;font-weight:800;font-size:18px}
.card .nm{font-weight:700;margin:8px 0 4px;font-size:16px}
.card .sb{font-size:13px;color:#666}
.intro{max-width:880px;margin:24px auto;padding:0 18px;color:#555}
.vol-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px;margin-top:24px}
.vol{display:block;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px;box-shadow:0 1px 4px rgba(0,0,0,.05);transition:.15s}
.vol:hover{transform:translateY(-3px);border-color:var(--wine)}
.vol .vno{display:inline-block;background:var(--wine);color:#fff;border-radius:8px;padding:3px 12px;font-weight:800;font-size:14px}
.vol .vt{font-weight:700;margin:10px 0 6px;font-size:18px}
.vol .vs{font-size:13px;color:#666}
.vol .vgo{margin-top:12px;font-weight:700;color:var(--wine);font-size:14px}"""

CILS_JS = """var SUBJMAX=20;
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]/g,'');}
function gradeOf(p){if(p>=85)return['Eccellente','#1b7a3d'];if(p>=70)return['Buono','#2e7d32'];if(p>=55)return['Discreto','#b8860b'];if(p>=40)return['Insufficiente','#c0392b'];return['Grave','#7b1e2b'];}
function verifica(){
  var items=document.querySelectorAll('.q-item');
  var score=0,total=0;
  items.forEach(function(el){
    var t=el.dataset.type;
    var corr=el.dataset.correct;
    if(t!=='cloze' && !corr){ el.querySelectorAll('input,select').forEach(function(i){i.disabled=true;}); return; }
    if(t==='mc'||t==='tf'||t==='match'){
      total++;
      var ok=false;
      if(t==='match'){var sel=el.querySelector('select');if(sel&&sel.value===corr)ok=true;}
      else{var inp=el.querySelector('input:checked');if(inp&&inp.value===corr)ok=true;}
      el.classList.add(ok?'correct':'wrong');
      var n=document.createElement('div');n.className='q-note '+(ok?'ok':'no');
      n.textContent=ok?'✅ Corretto':'❌ Risposta corretta: '+el.dataset.ctext;
      el.appendChild(n);
      el.querySelectorAll('input,select').forEach(function(i){i.disabled=true;});
    } else if(t==='cloze'){
      var ans=[];
      el.querySelectorAll('input.blank').forEach(function(inp){
        if(!inp.dataset.correct){inp.disabled=true;return;}
        total++;
        var v=norm(inp.value);
        var alts=String(inp.dataset.correct).split('/');
        var ok2=v.length>0 && alts.some(function(a){return v.indexOf(norm(a))>=0;});
        if(ok2)score++;
        inp.classList.add(ok2?'correct':'wrong');
        ans.push(inp.dataset.correct);
        inp.disabled=true;
      });
      if(ans.length){
        var cn=document.createElement('div');cn.className='q-note ans';
        cn.textContent='📝 正确答案：'+ans.join('　');
        el.appendChild(cn);
      }
    }
  });
  document.querySelectorAll('.q-subj').forEach(function(el){el.querySelectorAll('.ref').forEach(function(r){r.hidden=false;});});
  document.querySelectorAll('.q-oral').forEach(function(el){el.querySelectorAll('.oral-ref').forEach(function(r){r.hidden=false;});});
  var pct= total? Math.round(score/total*100):0;
  var g=gradeOf(pct);
  var box=document.getElementById('result');
  box.hidden=false;
  box.innerHTML='<div class="res-score">客观题正确率：<b>'+score+' / '+total+'</b> （'+pct+'%）</div>'+
    '<div class="res-grade" style="background:'+g[1]+'">'+g[0]+'</div>'+
    '<div class="res-note">写作 / 口语请在上方展开的参考答案与评分要点自评（本卷主观题满分 '+SUBJMAX+' 分）。</div>';
  box.scrollIntoView({behavior:'smooth'});
  document.getElementById('btn-check').hidden=true;
  document.getElementById('btn-reset').hidden=false;
}
function resetta(){location.reload();}
document.addEventListener('play', function(e){
  if(e.target && e.target.tagName === 'AUDIO'){
    document.querySelectorAll('audio').forEach(function(a){ if(a!==e.target) a.pause(); });
  }
}, true);"""


def esc(s):
    return html.escape(str(s), quote=True)

def has_cjk(s):
    return any('\u4e00' <= ch <= '\u9fff' for ch in s)


# ---------- 答案键解析 ----------
def mod_from_label(label):
    if label.startswith('Produzione scritta'):
        return 'Scritta'
    if label.startswith('Produzione orale'):
        return 'Orale'
    for m in MODULE_ORDER:
        if label.startswith(m):
            return m
    return None


NUM_ANS_RE = r'(?<![0-9])([0-9]+)\s*[-:.]\s*([A-Za-zàèéìòù\'’\-/]+(?:\s+[A-Za-zàèéìòù\'’\-/]+){0,3})'


def parse_key(key_text):
    answers = {m: {None: {}} for m in MODULE_ORDER}
    raw = {m: '' for m in MODULE_ORDER}
    parts = re.split(r'^\*\s+\*\*(.+?)\*\*\s*[:：]', key_text, flags=re.M)
    for i in range(1, len(parts), 2):
        label = parts[i].strip()
        content = parts[i + 1] if i + 1 < len(parts) else ''
        mod = mod_from_label(label)
        if mod is None:
            continue
        # 去掉 markdown 分隔线（*** / --- / ___），避免渲染成多余的乱码
        content = '\n'.join(ln for ln in content.split('\n')
                            if ln.strip() not in ('***', '---', '___', '* * *', '- - -'))
        raw[mod] += content.strip() + '\n'
        # 按 P1:/P2:/P3: 切分（CILS 语法模块常把若干子部分答案写在同一段，避免题号互相覆盖）
        segs = re.split(r'P([1-4])\s*[:：]', content)
        if len(segs) == 1:
            for nm in re.finditer(NUM_ANS_RE, content):
                num = int(nm.group(1))
                if num not in answers[mod][None]:
                    answers[mod][None][num] = nm.group(2).strip().strip("'").strip("’")
        else:
            # segs[0] 是首个 P 标记之前的内容（通常为 P1 答案，但源文件常省略 "P1:" 前缀）。
            # 若不补到 P1，这部分答案会被整体丢弃，导致对应填空题 data-correct 为空（提交后无判定/无答案）。
            fill0 = answers[mod].setdefault('P1', {})
            for nm in re.finditer(NUM_ANS_RE, segs[0]):
                num = int(nm.group(1))
                if num not in fill0:
                    fill0[num] = nm.group(2).strip().strip("'").strip("’")
            for k in range(1, len(segs), 2):
                pnum = 'P' + segs[k]
                seg_content = segs[k + 1] if k + 1 < len(segs) else ''
                fill = answers[mod].setdefault(pnum, {})
                for nm in re.finditer(NUM_ANS_RE, seg_content):
                    num = int(nm.group(1))
                    if num not in fill:
                        fill[num] = nm.group(2).strip().strip("'").strip("’")
    return answers, raw


def parse_key_lookup(ans_mod, subpart, num):
    if subpart and subpart in ans_mod and num in ans_mod[subpart]:
        return ans_mod[subpart][num]
    if None in ans_mod and num in ans_mod[None]:
        return ans_mod[None][num]
    return None


# ---------- 主观题参考答案解析（写作范例 + 口语评分要点）----------
# CILS 源文件的 Soluzioni 段里，写作范例 / 口语评分要点 的标签无法映射到
# MODULE_ORDER（如「Scrittura 范例 P1」「口语评分要点」），被 parse_key 丢弃，
# 导致主观题参考答案从未展示。这里单独抽取，供 render_subjective 生成与 CELI
# 完全一致的主观题「题目 + 参考答案」组件。
def _extract_write_examples(content):
    """从 Soluzioni 的写作范例段落抽取各 Prova 范文，兼容 5 卷不同写法：
       - Vol4：段落内含多行「* Prova N (...): _text」子弹，逐条抽出
       - Vol1：引用块「> ...」拼成一篇
       - Vol2/Vol3：行内多 Prova 切分（**P2**：… / Prova1 (…)«…»）
    """
    content = content.strip()
    if not content:
        return []
    # Vol4 风格：* Prova N (...): _text （可能跨多行子弹）
    prova_lines = re.findall(r'^\*\s*Prova\s*\d+\b.*?[:：]\s*_?\s*(.+)$', content, flags=re.M)
    if prova_lines:
        out = [x.strip() for x in prova_lines if x.strip()]
        if out:
            return out
    # 引用块（Vol1 等）：逐行 > 拼成一篇（保留换行，便于填表模板多行展示）
    bq = [re.sub(r'^>\s?', '', ln).strip() for ln in content.split('\n') if ln.strip().startswith('>')]
    if bq:
        txt = '\n'.join(bq).strip()
        if txt:
            return [txt]
    # 行内多 Prova 切分（Vol2: **P2**：… ；Vol3: Prova1 (…)«…» Prova2 (…)）
    segs = re.split(r'(?:\*\*P\d+\*\*|P\d+\s*[:：]|Prova\s*\d+)', content)
    out = [s.strip(' *\n') for s in segs[1:] if s.strip()]
    if out:
        return out
    return [content]


def _extract_body_examples(body):
    """Vol5 等：写作范文写在正文 **Esempio（范例）** 下的「> Prova N: ...」引用块。"""
    refs = {}
    for ln in body.split('\n'):
        s = ln.strip()
        m = re.match(r'^>\s*(?:\*\s*)?Prova\s*(\d+)\s*[:：]?\s*(.+)$', s)
        if m:
            refs.setdefault(int(m.group(1)), []).append(m.group(2).strip())
    return [' '.join(refs[k]).strip() for k in sorted(refs) if refs.get(k)]


def parse_subjective_refs(key_text):
    write_refs = []   # 写作范例，按出现顺序（末端对齐到写作任务）
    oral_scoring = '' # 口语评分说明（rubric note，文本）
    oral_dims = []    # [(名称, 描述), ...] 口语评分维度（CELI 布局：5 维清单）
    oral_max = '20'   # 口语满分（默认 20，标签可写「满分 NN 分」）
    oral_answers = {} # {prova_num(int) 或 0: 口语参考答案原文}（按 Prova 拆分，用于音频 + 折叠展示）
    SEP = ('***', '---', '___', '* * *', '- - -')
    # 标签行：支持「* **标签**：」（子弹+粗体）与「**标签**：」（纯粗体）两种写法
    parts = re.split(r'^\s*(?:\*\s+)?\*\*(.+?)\*\*\s*[:：]', key_text, flags=re.M)
    for i in range(1, len(parts), 2):
        label = parts[i].strip()
        content = parts[i + 1] if i + 1 < len(parts) else ''
        # 去掉 markdown 分隔线（*** / --- / ___），避免渲染成多余的乱码
        content = '\n'.join(ln for ln in content.split('\n') if ln.strip() not in SEP)
        # 写作范例：标签含「范例」（Scrittura / Scrit / 写作，可带括号）
        if re.search(r'(?:Scrit(?:tura)?|写作)\s*[（(]?\s*范例', label):
            # Vol5 等用「范例见上」占位，真实范文在正文，跳过此处占位
            if '见上' in content:
                continue
            examples = _extract_write_examples(content)
            write_refs.extend(examples)
            continue
        # 口语评分维度（标签可含「满分 NN 分」）：抽取子弹「- **名称** — 描述」
        if '口语评分维度' in label or ('评分维度' in label and 'Orale' in label):
            mm = re.search(r'满分\s*(\d+)\s*分', label)
            if mm:
                oral_max = mm.group(1)
            for ln in content.split('\n'):
                lt = ln.strip()
                if not lt or (not lt.startswith('-') and not lt.startswith('*')):
                    continue
                dm = re.match(r'^[-*]\s*(?:\*\*)?(.+?)(?:\*\*)?\s*[—–-]\s*(.+)$', lt)
                if dm:
                    oral_dims.append((dm.group(1).strip(), dm.group(2).strip()))
            continue
        # 口语参考答案原文（model answer）：支持按 Prova 拆分（口语参考答案 Prova 1 / Prova 2）
        if '口语参考答案' in label or ('参考答案' in label and 'Orale' in label):
            pm = re.search(r'Prova\s*(\d+)', label)
            pnum = int(pm.group(1)) if pm else 0
            txt = ' '.join(l.strip() for l in content.split('\n') if l.strip())
            if txt:
                oral_answers[pnum] = txt
            continue
        # 口语评分说明（rubric note）
        if '口语评分说明' in label or ('评分说明' in label and 'Orale' in label):
            txt = content.strip()
            if txt:
                oral_scoring = txt
            continue
        # 旧版兼容：单行「口语评分要点」（无维度清单时回退使用）
        if '口语评分要点' in label or ('评分要点' in label and 'Orale' in label):
            txt = content.strip()
            if txt and not oral_scoring:
                oral_scoring = txt
            continue
    return write_refs, oral_scoring, oral_dims, oral_answers, oral_max


def split_task_header(s):
    """识别写作任务的标题行，兼容三种写法：
       - **Modulo N** / **Prova N**（纯粗体，Vol1/2A1A2/3/5）
       - * **Prova N**（子弹+粗体，Vol2 B1–C2）
       - ### Prova N（标题形式，Vol4）
       返回 (标题, 同行余下提示)。"""
    s = s.strip()
    s = re.sub(r'^#+\s+', '', s)   # 标题形式 ### Prova N
    s = re.sub(r'^\*\s+', '', s)   # 子弹形式 * **Prova N**
    m = re.match(r'^\*\*(.+?)\*\*', s)
    if m:
        title = m.group(1).strip()
        rest = s[m.end():].strip()
    else:
        # 纯文本标题（Vol4 去掉 # 后）：Prova 1 — ...
        if re.match(r'^(?:Prova|Modulo)\s*[0-9]', s, re.I):
            title = s
            rest = ''
        else:
            return None, None
    rest = re.sub(r'^[：:]\s?', '', rest).strip()
    if re.search(r'(?:Modulo|Prova)\s*[0-9]', title, re.I):
        return title, rest
    return None, None


def group_oral_provas(stem_lines):
    """把口语任务要点行按「Prova N」拆成多个任务块；无 Prova 标记则整段作为一个块（num=0）。"""
    provas = []
    cur = None
    for ln in stem_lines:
        m = re.match(r'^\*\s*\*\*\s*Prova\s*(\d+)\b', ln) or re.match(r'^\*\*\s*Prova\s*(\d+)\b', ln)
        if m:
            if cur is not None:
                provas.append(cur)
            cur = {'num': int(m.group(1)), 'lines': [ln]}
        else:
            if cur is None:
                cur = {'num': 0, 'lines': [ln]}
            else:
                cur['lines'].append(ln)
    if cur is not None:
        provas.append(cur)
    return provas


def fmt_stem_line(s):
    """把口语任务要点行（* **X**：rest）渲染为 <b>X</b>：rest。"""
    s = re.sub(r'^\*\s*', '', s)
    m = re.match(r'^\*\*(.+?)\*\*\s*[:：]?\s*(.*)$', s)
    if m:
        return '<b>%s</b>%s' % (esc(m.group(1)), (': ' + esc(m.group(2))) if m.group(2) else '')
    return esc(s)


def render_subjective(mod_name, body, subj, level_code, vol_num):
    """渲染主观题（写作/口语），输出与 CELI 完全一致的组件：
       - 写作：每题 .q-item.q-subj（题目 + 文本框 + 提交后展开的 .ref 参考答案）
       - 口语：.q-item.q-oral（题目 + .oral-scoring 评分要点 + 提交后展开的 .oral-ref）
    """
    write_refs = subj.get('write', [])
    oral_scoring = subj.get('oral', '')
    # Vol5 等：Soluzioni 用「范例见上」占位，真实范文在正文，从正文抽取
    if not write_refs:
        write_refs = _extract_body_examples(body)
        if write_refs:
            subj = dict(subj)
            subj['write'] = write_refs
    lines = merge_stem_options(preprocess_body(body))
    instr_head = None
    instr_body = []
    tasks = []            # 写作任务: {'title','prompt':[]}
    cur = None
    oral_inline_scoring = ''
    oral_intro_head = None
    oral_intro_body = []
    oral_stem = []        # 口语任务要点行
    SEP = ('***', '---', '___', '* * *', '- - -')

    for raw_line in lines:
        s = raw_line.strip().replace('\\_', '_')
        s = re.sub(r'^\*\*题目?\*\*', '', s).strip()
        if not s:
            continue
        if s in SEP:
            continue
        # 口语评分要点（可能写在模块体内，如 C1/C2）
        if '评分要点' in s and mod_name == 'Orale':
            t = re.sub(r'^\*\s*', '', s)
            t = re.sub(r'^\*\*口语评分要点\*\*[：:]', '', t)
            t = re.sub(r'^\*\*评分要点\*\*[：:]', '', t)
            t = re.sub(r'^\*\*', '', t)
            t = re.sub(r'\*\*$', '', t).strip()
            if t:
                oral_inline_scoring = t
            continue

        if mod_name == 'Scritta':
            th, rest = split_task_header(s)
            if th:
                if cur is not None:
                    tasks.append(cur)
                cur = {'title': th, 'prompt': []}
                if rest:
                    cur['prompt'].append(rest)
                continue
            if cur is None:
                # 模块开头说明 → mod-instr
                if instr_head is None:
                    instr_head = s
                elif s.startswith('>'):
                    instr_body.append(re.sub(r'^>\s?', '', s).strip())
                else:
                    instr_body.append(s)
            else:
                if s.startswith('>'):
                    t = re.sub(r'^>\s?', '', s).strip()
                    if t:
                        cur['prompt'].append(t)
                else:
                    cur['prompt'].append(s)
        else:  # Orale
            # 说明：在首个任务要点（* **...）之前的内容 → mod-instr
            if not oral_stem and not s.startswith('* **'):
                if s.startswith('>'):
                    oral_intro_body.append(re.sub(r'^>\s?', '', s).strip())
                elif oral_intro_head is None:
                    oral_intro_head = s
                else:
                    oral_intro_body.append(s)
                continue
            oral_stem.append(s)

    if cur is not None:
        tasks.append(cur)
    eff_oral = oral_scoring or oral_inline_scoring

    out = []
    # 模块说明气泡（与客观模块一致）
    if mod_name == 'Scritta' and (instr_head or instr_body):
        h = esc(instr_head) if instr_head else ''
        b = esc('\n'.join(instr_body).strip()) if instr_body else ''
        out.append('<div class="mod-instr">')
        if h:
            out.append('<div class="mod-instr-h">%s</div>' % h)
        if b:
            out.append('<div class="mod-instr-b">%s</div>' % b)
        out.append('</div>')
    elif mod_name == 'Orale' and (oral_intro_head or oral_intro_body):
        out.append('<div class="mod-instr">')
        if oral_intro_head:
            out.append('<div class="mod-instr-h">%s</div>' % esc(oral_intro_head))
        if oral_intro_body:
            out.append('<div class="mod-instr-b">%s</div>' % esc('\n'.join(oral_intro_body).strip()))
        out.append('</div>')

    if mod_name == 'Scritta':
        out.append('<div class="items">')
        n = len(tasks)
        m = len(write_refs)
        for idx, tk in enumerate(tasks):
            ref_idx = idx - (n - m)   # 末端对齐（写作范例匹配最后一个写作任务）
            ref = write_refs[ref_idx] if (0 <= ref_idx < m) else ''
            title = tk['title']
            prompt = '\n'.join(tk['prompt']).strip()
            wm = re.search(r'(\d+)\s*[-–]\s*(\d+)\s*词', title + ' ' + prompt)
            limit = ('%s–%s 词' % (wm.group(1), wm.group(2))) if wm else ''
            out.append('<div class="q-item q-subj" data-type="write">')
            out.append('<p class="q-stem"><b>%s</b>' % esc(title))
            if prompt:
                out.append('<br>%s' % esc(prompt))
            if limit:
                out.append('<br><i>字数：%s</i>' % esc(limit))
            out.append('</p>')
            out.append('<textarea class="ans" rows="9" placeholder="La tua risposta..."></textarea>')
            if ref:
                out.append('<div class="ref" hidden><b>写作范例 / Risposta di riferimento：</b><br>%s</div>' % esc(ref))
            out.append('</div>')
        out.append('</div>')
    else:  # Orale
        oral_dims = subj.get('oral_dims') or []
        oral_max = subj.get('oral_max') or '20'
        oral_answers = subj.get('oral_answers') or {}
        has_per_prova = bool(oral_answers)
        out.append('<div class="items">')

        if not has_per_prova:
            # 旧版：单块（兼容未提供按 Prova 拆分的卷，行为不变）
            stem_html = '<br>'.join(fmt_stem_line(x) for x in oral_stem)
            out.append('<div class="q-item q-oral" data-type="oral">')
            out.append('<p class="q-stem">%s</p>' % stem_html)
            if oral_dims or eff_oral:
                out.append('<div class="oral-scoring">')
                out.append('<div class="score-head">📋 评分维度 · Criteri di valutazione（满分 %s 分）</div>' % esc(oral_max))
                if oral_dims:
                    out.append('<ul class="dims">')
                    for dn, dd in oral_dims:
                        out.append('<li><b>%s</b> — %s</li>' % (esc(dn), esc(dd)))
                    out.append('</ul>')
                if eff_oral:
                    out.append('<div class="rubric-note">%s</div>' % esc(eff_oral))
                out.append('</div>')
            if eff_oral:
                out.append('<div class="oral-ref" hidden>')
                out.append('<div class="ref-head">🗣️ 参考答案 <span class="ref-it">Risposta di riferimento</span></div>')
                out.append('<details class="otranscript"><summary><span class="o-closed">📝 显示口语指导 / 评分要点</span><span class="o-open">📝 隐藏口语指导 / 评分要点</span></summary><pre>%s</pre></details>' % esc(eff_oral))
                out.append('</div>')
            out.append('</div>')
        else:
            # 新版（CELI 布局）：共享评分维度 + 每个 Prova 独立参考答案（Prova 2 也做类似参考）
            if oral_dims or eff_oral:
                out.append('<div class="oral-scoring">')
                out.append('<div class="score-head">📋 评分维度 · Criteri di valutazione（满分 %s 分）</div>' % esc(oral_max))
                if oral_dims:
                    out.append('<ul class="dims">')
                    for dn, dd in oral_dims:
                        out.append('<li><b>%s</b> — %s</li>' % (esc(dn), esc(dd)))
                    out.append('</ul>')
                if eff_oral:
                    out.append('<div class="rubric-note">%s</div>' % esc(eff_oral))
                out.append('</div>')
            for pv in group_oral_provas(oral_stem):
                pv_num = pv['num']
                ans = oral_answers.get(pv_num) or oral_answers.get(0, '')
                stem_html = '<br>'.join(fmt_stem_line(x) for x in pv['lines'])
                label = ('Prova %d' % pv_num) if pv_num else 'Risposta di riferimento'
                out.append('<div class="q-item q-oral" data-type="oral">')
                out.append('<p class="q-stem">%s</p>' % stem_html)
                if ans:
                    out.append('<div class="oral-ref" hidden>')
                    out.append('<div class="ref-head">🗣️ %s · <span class="ref-it">Risposta di riferimento</span></div>' % esc(label))
                    # 注意：<pre> 必须置于 .oral-audio 内部，音频脚本才能抽取文本生成并注入 <audio>
                    out.append('<div class="oral-audio"><span class="aspk-slot"></span>'
                               '<details class="otranscript"><summary><span class="o-closed">📝 显示参考答案原文</span>'
                               '<span class="o-open">📝 隐藏参考答案原文</span></summary><pre>%s</pre></details></div>' % esc(ans))
                    out.append('</div>')
                out.append('</div>')
        out.append('</div>')
    return '\n'.join(out)


# ---------- 选项切分（修正：按标记位置切片，不排斥 a-d 字母）----------
def split_options(s):
    marks = list(re.finditer(r'(?<![\wàèéìòù])[A-Da-d]\)', s))
    if len(marks) < 2:
        return None
    opts = []
    for k in range(len(marks)):
        start = marks[k].end()
        end = marks[k + 1].start() if k + 1 < len(marks) else len(s)
        opts.append((marks[k].group(0)[0].upper(), s[start:end].strip()))
    return opts


# ---------- 单题渲染 ----------
def render_mc(num, stem, options, ans_letter, variant=''):
    if ans_letter and len(ans_letter) == 1 and ans_letter.isalpha():
        ans_letter = ans_letter.upper()
    try:
        idx = [o[0] for o in options].index(ans_letter)
    except Exception:
        idx = -1
    if idx < 0:
        return None
    if variant == 'asc':
        opts_html = ''.join(
            '<label class="opt asc-opt"><input type="radio" name="r%d" value="%d">'
            '<span class="asc-opt__k">%s</span><span class="asc-opt__v">%s</span></label>' % (
                num, i, esc(o[0]), esc(o[1])) for i, o in enumerate(options))
        return ('<div class="q-item asc-q" data-type="mc" data-correct="%d" data-ctext="%s">'
                '<span class="asc-q__no">%d</span><div class="asc-q__main">'
                '<p class="q-stem">%s</p><div class="opts asc-opts">%s</div></div></div>' % (
                    idx, esc(options[idx][1]), num, esc(stem), opts_html))
    opts_html = ''.join(
        '<label class="opt"><input type="radio" name="r%d" value="%d"> %s) %s</label>' % (
            num, i, esc(o[0]), esc(o[1])) for i, o in enumerate(options))
    return ('<div class="q-item" data-type="mc" data-correct="%d" data-ctext="%s">'
            '<p class="q-stem">%d. %s</p><div class="opts">%s</div></div>' % (
                idx, esc(options[idx][1]), num, esc(stem), opts_html))

def render_tf(num, stem, ans_vf, variant=''):
    val = '0' if ans_vf == 'V' else ('1' if ans_vf == 'F' else '')
    if not val:
        return None
    ctxt = 'Vero' if ans_vf == 'V' else 'Falso'
    if variant == 'asc':
        opts_html = ('<label class="opt asc-opt"><input type="radio" name="r%d" value="0">'
                     '<span class="asc-opt__k">V</span><span class="asc-opt__v">Vero</span></label>'
                     '<label class="opt asc-opt"><input type="radio" name="r%d" value="1">'
                     '<span class="asc-opt__k">F</span><span class="asc-opt__v">Falso</span></label>' % (num, num))
        return ('<div class="q-item asc-q" data-type="tf" data-correct="%s" data-ctext="%s">'
                '<span class="asc-q__no">%d</span><div class="asc-q__main">'
                '<p class="q-stem">%s</p><div class="opts asc-opts">%s</div></div></div>' % (
                    val, esc(ctxt), num, esc(stem), opts_html))
    opts_html = ('<label class="opt"><input type="radio" name="r%d" value="0"> Vero</label>'
                 '<label class="opt"><input type="radio" name="r%d" value="1"> Falso</label>' % (num, num))
    return ('<div class="q-item" data-type="tf" data-correct="%s" data-ctext="%s">'
            '<p class="q-stem">%d. %s</p><div class="opts">%s</div></div>' % (
                val, esc(ctxt), num, esc(stem), opts_html))

def render_cloze_line(num, body, answer, variant=''):
    """渲染一道填空行，支持一行内多个 '___ (hint)' 空。
    answer 为该题号答案：含 '/' 时，若空数与 '/' 拆分出的答案数一致则逐空对应（如 "amico/amiche" 配两空），
    否则所有空共用完整答案（含 '/'），由 verifica() 兼容任选其一。"""
    dc_parts = [a.strip() for a in answer.split('/')] if answer else []
    blanks = list(re.finditer(r'_{2,}\s*\(([^)]*)\)', body))
    nb = len(blanks)
    out = []
    last = 0
    idx = 0
    for m in blanks:
        out.append(esc(body[last:m.start()]))
        hint = m.group(1)
        if dc_parts:
            # 多空且答案按 '/' 拆出与空数一致 → 逐空对应；否则所有空共用完整答案（含 '/'）
            if nb > 1 and len(dc_parts) == nb:
                dc = dc_parts[idx]
            else:
                dc = '/'.join(dc_parts)
        else:
            dc = ''
        inp = '<input class="blank"'
        if dc:
            inp += ' data-correct="%s"' % esc(dc)
        inp += '>'
        if hint:
            inp += ' (%s)' % esc(hint)
        out.append(inp)
        idx += 1
        last = m.end()
    out.append(esc(body[last:]))
    inner = ''.join(out)
    if variant == 'asc':
        return ('<div class="q-item asc-q" data-type="cloze">'
                '<span class="asc-q__no">%d</span><div class="asc-q__main">'
                '<p class="q-stem">%s</p></div></div>' % (num, inner))
    return '<div class="q-item" data-type="cloze"><p class="q-stem">%d. %s</p></div>' % (num, inner)

def render_cloze_passage(text, ans_mod, subpart):
    def repl(m):
        n = int(m.group(1))
        an = parse_key_lookup(ans_mod, subpart, n)
        dc = ' data-correct="%s"' % esc(an) if an else ''
        return '<input class="blank"%s>' % dc
    # 先转义用户文本（防 XSS），再注入原始 <input> 标签，避免 input 被二次转义
    safe = esc(text)
    safe = re.sub(r'_{2,}\s*\(\s*(\d+)\s*\)', repl, safe)
    safe = re.sub(r'_{2,}', '<input class="blank">', safe)
    return '<div class="q-item" data-type="cloze"><p class="q-stem">%s</p></div>' % safe

def render_mc_cloze_passage(text, ans_mod, subpart):
    parts = re.split(r'(\(\d+\)\s*_{2,})', text)
    out_html = []
    i = 1
    while i < len(parts) - 1:
        blank = parts[i]
        opts_text = parts[i + 1]
        nm = re.search(r'\((\d+)\)', blank)
        if not nm:
            i += 2
            continue
        num = int(nm.group(1))
        opts = split_options(opts_text)
        if opts and len(opts) >= 2:
            an = parse_key_lookup(ans_mod, subpart, num)
            r = render_mc(num, '', opts, an)
            if r:
                out_html.append(r)
            else:
                out_html.append('<div class="mnote">%s %s</div>' % (esc(blank), esc(opts_text)))
        else:
            out_html.append('<div class="mnote">%s %s</div>' % (esc(blank), esc(opts_text)))
        i += 2
    return '<div class="items">%s</div>' % '\n'.join(out_html)


# ---------- 正文预处理（规范化各卷不一致的写法）----------
def preprocess_body(body):
    """把各卷不一致的写法规整为「每题一行」：
    1) **标题**紧跟题目内容 → 拆成「**标题**」与「题目」两行；
    2) 一行内挤了多道题（如 1. ... 2. ... 3. ...）→ 按 " N." 边界拆分。"""
    raw = body.split('\n')
    out = []
    for line in raw:
        s = line.strip()
        m = re.match(r'^(\*\*[^*]+\*\*)(.+)$', s)
        if m and re.search(r'\d+\s*[\.\)]\s*', m.group(2)):
            out.append(m.group(1))
            out.append(m.group(2).strip())
            continue
        out.append(line)
    final = []
    for line in out:
        s = line.strip()
        # 同行多题：在 ". 2." / ") 2." / "? 2." 这类题号边界处拆分
        if re.match(r'^\s*\d+\s*[\.\)]', s) and len(re.findall(r'(?<=[\.\)\?])\s+\d+\s*[\.\)]\s*', s)) >= 1:
            parts = re.split(r'(?<=[\.\)\?])\s+(?=\d+\s*[\.\)]\s*)', s)
            final.extend(p.strip() for p in parts)
        else:
            final.append(line)
    return final


# ---------- 题干与选项的跨行合并 ----------
def merge_stem_options(lines):
    """部分卷（如 Vol.2/3）把题干与 a)/b)/c) 选项分两行写：
    题干行（数字开头、本行无选项） + 下一行（a) 开头）→ 合并为一行再解析。"""
    def norm(line):
        s = line.strip().replace('\\_', '_')
        s = re.sub(r'^\*\*题目?\*\*', '', s).strip()
        return s
    out = []
    i = 0
    n = len(lines)
    while i < n:
        s = norm(lines[i])
        if re.match(r'^\s*\d+\s*[\.\)]', s) and not re.search(r'[A-Da-d]\)', s) and i + 1 < n:
            nxt = norm(lines[i + 1])
            if re.match(r'^\s*[A-Da-d]\)', nxt):
                out.append(lines[i].rstrip() + ' ' + lines[i + 1].strip())
                i += 2
                continue
        out.append(lines[i])
        i += 1
    return out


# ---------- 模块渲染 ----------
def render_module(mod_name, body, ans_mod, level_code, vol_num, subj=None):
    # 主观题（写作/口语）走专用渲染，输出与 CELI 一致的主观题组件
    if mod_name in ('Scritta', 'Orale'):
        return render_subjective(mod_name, body, subj or {'write': [], 'oral': ''}, level_code, vol_num)
    out = []
    lines = merge_stem_options(preprocess_body(body))
    cur_transcript = []
    in_transcript = False
    cur_subpart = None
    cur_dialog_title = None
    cur_reading = []
    cur_reading_title = None
    variant = 'asc' if mod_name == 'Ascolto' else ''
    CIRCLED = '①②③④'
    # 模块题目说明气泡：捕获模块开头的标题行 + 说明文字，合并为一个气泡卡片
    instr_done = False
    mod_instr_head = None
    mod_instr_body = []

    def flush_instr():
        nonlocal instr_done, mod_instr_head, mod_instr_body
        if mod_instr_head or mod_instr_body:
            h = esc(mod_instr_head) if mod_instr_head else ''
            b = esc('\n'.join(mod_instr_body).strip()) if mod_instr_body else ''
            html = '<div class="mod-instr">'
            if h:
                html += '<div class="mod-instr-h">%s</div>' % h
            if b:
                html += '<div class="mod-instr-b">%s</div>' % b
            html += '</div>'
            out.append(html)
        mod_instr_head = None
        mod_instr_body = []
        instr_done = True

    def flush_reading():
        nonlocal cur_reading, cur_reading_title
        if cur_reading:
            txt = '\n'.join(cur_reading).strip()
            if txt:
                if cur_reading_title:
                    out.append('<div class="text"><h4>%s</h4><pre>%s</pre></div>'
                               % (esc(cur_reading_title), esc(txt)))
                else:
                    out.append('<div class="text"><pre>%s</pre></div>' % esc(txt))
        cur_reading.clear()
        cur_reading_title = None

    def flush_transcript():
        nonlocal in_transcript, cur_dialog_title
        flush_reading()
        if cur_transcript:
            txt = '\n'.join(cur_transcript).strip()
            if txt:
                dlg_t = cur_dialog_title or 'Ascolto'
                if mod_name == 'Ascolto':
                    # CELI 风格听力块：🎧 标题头 + 原生 <audio controls>（自带播放/进度条/下载/调速） + 折叠原文
                    out.append('<div class="audio-block">'
                               '<h4>🎧 %s</h4>' % esc(dlg_t)
                               + '<span class="aspk-slot"></span>'
                               + '<details class="transcript"><summary>'
                                 '<span class="t-closed">📝 显示听力原文</span>'
                                 '<span class="t-open">📝 隐藏听力原文</span>'
                               '</summary><pre>%s</pre></details></div>' % esc(txt))
                else:
                    out.append('<div class="text"><pre>%s</pre></div>' % esc(txt))
        cur_transcript.clear()
        in_transcript = False
        cur_dialog_title = None

    for raw_line in lines:
        s = raw_line.strip().replace('\\_', '_')
        s = re.sub(r'^\*\*题目?\*\*', '', s).strip()  # 源文件用 \_ 表示空白，归一化为 _
        # ---- 模块题目说明捕获（合并标题行+说明为单一气泡）----
        if not instr_done:
            if not s:
                continue
            is_content = False
            if parse_question_line(s, ans_mod, cur_subpart, variant):
                is_content = True
            elif s.startswith('>') and ('_____' in s or re.search(r'\(\d+\)\s*_{2,}', s)):
                is_content = True
            elif re.match(r'^\*\*(.+?)\*\*', s):
                is_content = True
            elif re.match(r'^_?\s*(Dialogo\b.*)$', s, re.I):
                is_content = True
            elif re.match(r'^#{1,3}\s+(.+)$', s):
                is_content = True
            elif re.match(r'^[—–]', s):
                is_content = True
            elif '口语评分要点' in s:
                is_content = True
            elif mod_name == 'Ascolto' and not has_cjk(s) and re.match(r'^[A-Za-zÀ-ÿ][\wàèéìòù\'’ ]*:\s', s):
                is_content = True
            if is_content:
                flush_instr()  # 遇到首个真实内容，先flush说明气泡，再走正常分支渲染该内容
            else:
                if mod_instr_head is None:
                    mod_instr_head = s
                elif s.startswith('>'):
                    t = re.sub(r'^>\s?', '', s).strip()
                    if t:
                        mod_instr_body.append(t)
                else:
                    mod_instr_body.append(s)
                continue
        # ---- 说明捕获结束 ----
        if not s:
            if mod_name == 'Ascolto' and in_transcript:
                cur_transcript.append('')
            elif mod_name == 'Lettura' and cur_reading:
                cur_reading.append('')
            continue
        # markdown 子标题（模块内 ### / ## 标题，如 Vol.4 的「听力原文」「理解题」）
        hm_head = re.match(r'^#{1,3}\s+(.+)$', s)
        if hm_head:
            flush_reading()
            htxt = hm_head.group(1).strip()
            # Ascolto 的 Dialogo/Testo/Prova 标题：捕获为 audio-block 的 🎧 头，不再单独发 h3
            if mod_name == 'Ascolto' and re.match(r'(?i)(dialogo|testo|prova)\b', htxt):
                flush_transcript()
                cur_dialog_title = htxt
            else:
                out.append('<h3>%s</h3>' % esc(htxt))
            continue
        # 行内加粗小标题
        hm = re.match(r'^\*\*(.+?)\*\*', s)
        if hm:
            htxt = hm.group(1).strip()
            is_section = bool(re.search(r'(Dialogo|Prova|Testo|Modulo|题|[%s])' % CIRCLED, htxt))
            if is_section:
                flush_transcript()
                sp = None
                mc = re.match(r'^([%s])' % CIRCLED, htxt)
                if mc:
                    sp = 'P' + str(CIRCLED.index(mc.group(1)) + 1)
                mp = re.search(r'(?:Prova|Modulo)\s*([0-9])', htxt)
                if mp:
                    sp = 'P' + mp.group(1)
                if sp:
                    cur_subpart = sp
                if mod_name == 'Ascolto' and re.match(r'(?i)(dialogo|testo|prova)\b', htxt):
                    cur_dialog_title = htxt
                elif mod_name == 'Lettura' and re.match(r'(?i)(testo)\b', htxt):
                    cur_reading_title = htxt
                else:
                    out.append('<h3>%s</h3>' % esc(htxt))
                rest = s[hm.end():].strip()
                if rest and mod_name == 'Ascolto' and not has_cjk(rest):
                    cur_transcript.append(rest)
                    in_transcript = True
                continue
        # 下划线样式小标题：_Dialogo 1 — ...（部分卷如 Vol.2 仅前导下划线、无闭合）
        um = re.match(r'^_?\s*(Dialogo\b.*)$', s, re.I)
        if um:
            flush_transcript()
            if mod_name == 'Ascolto':
                cur_dialog_title = um.group(1).strip()
            else:
                out.append('<h3>%s</h3>' % esc(um.group(1).strip()))
            in_transcript = True
            continue
        # 引用块
        if s.startswith('>'):
            t = re.sub(r'^>\s?', '', s).strip()
            if '_____' in t or re.search(r'\(\d+\)\s*_{2,}', t):
                flush_transcript()
                if re.search(r'\([A-Da-d]\)', t):
                    out.append(render_mc_cloze_passage(t, ans_mod, cur_subpart))
                else:
                    out.append(render_cloze_passage(t, ans_mod, cur_subpart))
                continue
            if has_cjk(t):
                flush_reading()
                out.append('<div class="mnote">%s</div>' % esc(t))
            else:
                if mod_name == 'Ascolto':
                    cur_transcript.append(t)
                elif mod_name == 'Lettura':
                    cur_reading.append(t)
                else:
                    out.append('<div class="text"><pre>%s</pre></div>' % esc(t))
            continue
        # 对话行
        if re.match(r'^[—–]', s):
            flush_reading()
            if has_cjk(s):
                out.append('<div class="mnote">%s</div>' % esc(s))
            elif mod_name == 'Ascolto':
                cur_transcript.append(s)
            else:
                out.append('<div class="text"><pre>%s</pre></div>' % esc(s))
            continue
        # 口语评分要点
        if '口语评分要点' in s or ('评分要点' in s and mod_name == 'Orale'):
            flush_transcript()
            t = re.sub(r'^\*\s*', '', s)
            t = re.sub(r'^\*\*口语评分要点\*\*[：:]', '', t)
            out.append('<div class="q-item q-oral" data-type="oral"><div class="oral-scoring">'
                       '<div class="score-head">📋 Criteri di valutazione（口语评分要点）</div>'
                       '<div class="rubric-note">%s</div></div></div>' % esc(t))
            continue
        # 题目
        q = parse_question_line(s, ans_mod, cur_subpart, variant)
        if q:
            flush_transcript()
            out.append(q)
            continue
        # Ascolto 对话行：Speaker: testo（如 Vol.2 的 Lucia: ... / Insegnante: ...，逐行归入听力原文）
        if mod_name == 'Ascolto' and not has_cjk(s) and re.match(r'^[A-Za-zÀ-ÿ][\wàèéìòù\'’ ]*:\s', s):
            cur_transcript.append(s)
            in_transcript = True
            continue
        if not s.startswith('*'):
            flush_reading()
            out.append('<div class="mnote">%s</div>' % esc(s))
    flush_instr()
    flush_transcript()
    return '\n'.join(out)


def parse_question_line(line, ans_mod, subpart, variant=''):
    work = line
    dm = re.search(r'Domanda:\s*(.*?)(?=）)', line)
    if dm:
        work = dm.group(1)
    numm = re.match(r'\s*(\d+)\s*[\.\)]', work)
    # Vero/Falso：支持 (V)/(F) 或 (Vero / Falso) 或 (V/F)
    tfm = re.search(r'\((?:Vero\s*/\s*Falso|V/F|([VF]))\)\s*$', work)
    if tfm and numm:
        num = int(numm.group(1))
        stem = re.sub(r'^\s*\d+\s*[\.\)]\s*', '', work)
        stem = re.sub(r'\((?:Vero\s*/\s*Falso|V/F|[VF])\)\s*$', '', stem).strip()
        an = parse_key_lookup(ans_mod, subpart, num) or 'V'
        return render_tf(num, stem, an, variant)
    # MC
    if re.search(r'[A-Da-d]\)', work):
        opts = split_options(work)
        # 首选项必须是 A，避免把 "_____ (La/Il)" 中的 "l)" 误判为选择题
        if opts and len(opts) >= 2 and opts[0][0] == 'A' and not has_cjk(opts[0][1]) and not has_cjk(opts[-1][1]):
            if numm:
                num = int(numm.group(1))
                first = re.search(r'[A-Da-d]\)', work)
                stem = work[:first.start()].strip()
                stem = re.sub(r'^\s*\d+\s*[\.\)]\s*', '', stem)
                stem = re.sub(r'Domanda:\s*', '', stem).strip()
                an = parse_key_lookup(ans_mod, subpart, num)
                return render_mc(num, stem, opts, an, variant)
    # Cloze 项：支持一行内多个 "______ (提示)" 填空（如 "Un ___ (amico) e due ___ (amica)"）
    clm = re.search(r'(\d+)\s*[\.\)]\s*(.*)$', line)
    if clm and re.search(r'_{2,}\s*\(', clm.group(2)):
        num = int(clm.group(1))
        body = clm.group(2).strip()
        an = parse_key_lookup(ans_mod, subpart, num)
        return render_cloze_line(num, body, an, variant)
    return None


# ---------- 级别页 ----------
def render_level(level_code, level_body, vol_num, vol_theme_it, level_sub_it, level_sub_zh):
    km = re.search(r'###\s*✅.*', level_body, flags=re.S)
    main_body = level_body[:km.start()] if km else level_body
    key_text = level_body[km.start():] if km else ''
    answers, raw = parse_key(key_text)   # 客观题答案：严格沿用 ### ✅ 匹配，行为不变
    # 主观题参考答案：用更宽的 #{2,3} ✅ 匹配，使 Vol4（## ✅）也能抽取写作/口语范文；
    # 仅用于主观题解析，不影响上面的 parse_key（客观题）行为。
    skm = re.search(r'#{2,3}\s*✅.*', level_body, flags=re.S)
    subj_key_text = level_body[skm.start():] if skm else ''
    write_refs, oral_scoring, oral_dims, oral_answers, oral_max = parse_subjective_refs(subj_key_text)
    subj = {'write': write_refs, 'oral': oral_scoring,
            'oral_dims': oral_dims, 'oral_answers': oral_answers, 'oral_max': oral_max}

    mods = re.split(r'^#{2,3}\s*(\d+)\.\s*', main_body, flags=re.M)
    mod_html = []
    mnum = 1
    for j in range(1, len(mods), 2):
        mnum_here = int(mods[j])
        mname_full = mods[j + 1]
        # 按编号映射模块最稳（源标题可能是 "Produzione scritta"，短名 "Scritta" 无法靠 startswith 匹配）
        if 1 <= mnum_here <= len(MODULE_ORDER):
            mod_key = MODULE_ORDER[mnum_here - 1]
        else:
            mod_key = MODULE_ORDER[0]
        ans_mod = answers.get(mod_key, {})
        rendered = render_module(mod_key, mname_full, ans_mod, level_code, vol_num, subj)
        title = '%d. %s（%s）' % (mnum, mod_key, MODULE_ZH[mod_key])
        mod_html.append('<section class="module"><h2>%s</h2>%s</section>' % (esc(title), rendered))
        mnum += 1

    # 底部「参考答案与评分」整块删除（已改为各模块内联展开，与 CELI 布局一致）
    sol_html = ''

    sub = level_sub_it
    if level_sub_zh:
        sub += ' · ' + level_sub_zh
    intro = ('本级主题：%s。CILS 五大模块（Ascolto / Lettura / Analisi delle strutture / Produzione scritta / Produzione orale）。'
             '听力原文默认折叠隐藏，点「📝 显示听力原文」展开；每段听力配原生音频控件（▶ 播放 / 进度条 / 下载 / 调速），由真人女声朗读；阅读/语法/写作/口语模块不含音频。'
             '提交后客观题自动判分；写作 / 口语主观题点击「提交」后，在上方展开参考答案与评分要点供自评。'
             % esc(vol_theme_it))
    return ('<!DOCTYPE html><html lang="it"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>CILS %s — %s</title><style>%s</style></head><body>'
            '<header class="top"><nav class="topnav">'
            '<a href="index.html" class="back">← Indice CILS Vol.%d</a>'
            '<a href="../CILS.html" class="back">🏠 CILS 导航页</a></nav>'
            '<div class="ttl"><span class="lvl">%s</span> %s</div>'
            '<div class="sub">%s</div></header><main>'
            '<p class="intro">%s</p>%s%s'
            '<button id="btn-check" onclick="verifica()">Verifica le risposte（提交判分）</button>'
            '<button id="btn-reset" hidden onclick="resetta()">Ricomincia（重做）</button>'
            '<div id="result" hidden></div></main>'
            '<script>%s</script></body></html>' % (
                level_code, LEVEL_NAMES[level_code], CILS_CSS, vol_num, level_code,
                LEVEL_NAMES[level_code], esc(sub), intro, '\n'.join(mod_html), sol_html, CILS_JS))


# ---------- 卷解析 ----------
def parse_volume(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    mt = re.search(r'^#\s*(.+)$', text, flags=re.M)
    title_full = mt.group(1) if mt else 'CILS'
    vn = re.search(r'第(\d+)卷', title_full)
    vol_num = int(vn.group(1)) if vn else 1
    theme_zh = ''
    theme_it = ''
    bar = title_full.split('｜')
    if len(bar) > 1:
        theme_zh = bar[1].split('（')[0].strip()
    par = re.search(r'（([^（）]+)）\s*$', title_full)
    if par:
        theme_it = par.group(1).strip()
    sub_map = {}
    sm = re.search(r'##\s*本卷结构.*?(?=\n\*\*\*|\n##\s)', text, flags=re.S)
    if sm:
        for line in sm.group(0).split('\n'):
            lm = re.match(r'\*\s*\*\*(A[12]|B[12]|C[12])\*\*[：:]\s*([^（(]+)', line)
            if lm:
                code = lm.group(1)
                it = lm.group(2).strip()
                zh = ''
                zm = re.search(r'（([^（）]+)）', line)
                if zm:
                    zh = zm.group(1).strip()
                sub_map[code] = (it, zh)
    parts = re.split(r'^#{1,2}\s*(A1|A2|B1|B2|C1|C2)\b', text, flags=re.M)
    levels = {}
    for i in range(1, len(parts), 2):
        levels[parts[i]] = parts[i + 1]
    return vol_num, title_full, theme_zh, theme_it, sub_map, levels


def render_volume_index(vol_num, title_full, theme_it, theme_zh, sub_map):
    cards = []
    for code in LEVEL_ORDER:
        it, zh = sub_map.get(code, ('', ''))
        sub = it
        if zh:
            sub += ' · ' + zh
        cards.append('<a class="card" href="%s.html"><span class="lvl">%s</span>'
                     '<div class="nm">%s</div><div class="sb">%s</div></a>' % (
                         code, code, LEVEL_NAMES[code], esc(sub)))
    sub_line = theme_it
    if theme_zh:
        sub_line += ' — ' + theme_zh
    return ('<!DOCTYPE html><html lang="it"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>CILS 模拟题库 · 第%d卷（A1–C2）</title><style>%s</style></head><body>'
            '<header class="top"><nav class="topnav">'
            '<a href="../CILS.html" class="back">🏠 CILS 导航页</a></nav>'
            '<div class="ttl">CILS 模拟题库 · 第%d卷</div>'
            '<div class="sub">%s — 六个等级（A1–C2）考试页面</div></header>'
            '<main><p class="intro">本卷严格按锡耶纳大学（CILS）真题五大模块结构命题。'
            '点击任意等级进入对应考试页面：含听力（文本呈现）、阅读、语法分析、写作、口语。'
            '提交后客观题自动判分，写作/口语展开参考答案与评分要点供自评。</p>'
            '<div class="index-grid">%s</div></main></body></html>' % (
                vol_num, CILS_CSS, vol_num, esc(sub_line), '\n'.join(cards)))


def generate_volume(vol_path, vol_num):
    vol_num, title_full, theme_zh, theme_it, sub_map, levels = parse_volume(vol_path)
    vdir = os.path.join(OUT_BASE, 'CILS_Vol%d_esami' % vol_num)
    os.makedirs(vdir, exist_ok=True)
    with open(os.path.join(vdir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(render_volume_index(vol_num, title_full, theme_it, theme_zh, sub_map))
    for code in LEVEL_ORDER:
        if code in levels:
            it, zh = sub_map.get(code, ('', ''))
            doc = render_level(code, levels[code], vol_num, theme_it, it, zh)
            with open(os.path.join(vdir, code + '.html'), 'w', encoding='utf-8') as f:
                f.write(doc)
    return vol_num, title_full, theme_it, theme_zh


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else 'all'
    volumes = []
    if arg == 'all':
        for n in range(1, 6):
            p = os.path.join(SRC_DIR, 'cils_v%d.md' % n)
            if os.path.exists(p):
                volumes.append((n, p))
    else:
        n = int(arg)
        p = os.path.join(SRC_DIR, 'cils_v%d.md' % n)
        if os.path.exists(p):
            volumes.append((n, p))
    meta = []
    for n, p in volumes:
        print('Generating volume', n)
        vn, tf, ti, tz = generate_volume(p, n)
        meta.append((vn, tf, ti, tz))
        print('  -> CILS_Vol%d_esami' % vn)
    cards = []
    for vn, tf, ti, tz in meta:
        sub = ti
        if tz:
            sub += ' — ' + tz
        cards.append('<a class="vol" href="CILS_Vol%d_esami/index.html">'
                     '<span class="vno">Vol.%d</span><div class="vt">%s</div>'
                     '<div class="vs">%s</div><div class="vgo">进入 →</div></a>' % (
                         vn, vn, esc(sub), esc(sub)))
    html_doc = ('<!DOCTYPE html><html lang="it"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width, initial-scale=1">'
                '<title>CILS 模拟题库 · 全套（Vol.1–5，A1–C2）</title><style>%s</style></head><body>'
                '<header class="top"><div class="ttl">CILS 模拟题库 · 全套</div>'
                '<div class="sub">Vol.1 – Vol.5 · 每卷 A1–C2 五级 · 自动判分 + 口语/写作评分要点</div></header>'
                '<main><div class="intro">本套题库严格按 CILS（锡耶纳大学 Università per Stranieri di Siena）近年真题五大模块结构命题，'
                '每卷一个宏观主题，五级子主题螺旋上升。每卷含听力、阅读、语法分析、写作、口语五大模块。'
                '提交后客观题自动判分，写作/口语展开参考答案与评分要点供自评。点击任意卷进入对应考试页面。</div>'
                '<div class="vol-grid">%s</div></main>'
                '<footer>CILS 模拟题库生成系统 · 基于技能「CELI模拟题生成」改编</footer>'
                '</body></html>' % (CILS_CSS, '\n'.join(cards)))
    with open(os.path.join(OUT_BASE, 'CILS.html'), 'w', encoding='utf-8') as f:
        f.write(html_doc)
    print('Done. CILS.html written with', len(meta), 'volumes.')


if __name__ == '__main__':
    main()
