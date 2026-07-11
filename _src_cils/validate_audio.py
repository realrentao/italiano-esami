# -*- coding: utf-8 -*-
"""校验：模拟浏览器 textContent 提取每个 .q-stem / .text pre，
按 JS 同样的归一化规则，确认都能在 audio_index.js 的键中命中。"""
import os, re, json, html, sys
from html.parser import HTMLParser

ROOT = r"D:\意大利语材料\italiano-esami\CILS"


def js_norm_q(s):
    t = re.sub(r'^\s*\d+\s*[\.\)]\s*', '', s)
    t = re.sub(r'\s+', ' ', t).strip().lower()
    return t


def js_norm_p(s):
    t = re.sub(r'\s+', ' ', s).strip().lower()
    return t


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []          # list of (kind, text)
        self.stack = []        # open tags (tag name)
        self.classes = []      # parallel class attr
        self.in_qstem = False
        self.in_textdiv = False
        self.in_pre = False
        self.buf = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        cls = d.get('class', '')
        self.stack.append(tag)
        self.classes.append(cls)
        if tag == 'p' and 'q-stem' in cls:
            self.in_qstem = True
            self.buf = []
        if tag == 'div' and 'text' in cls.split():
            self.in_textdiv = True
        if tag == 'pre' and self.in_textdiv:
            self.in_pre = True
            self.buf = []

    def handle_endtag(self, tag):
        if tag == 'p' and self.in_qstem:
            self.out.append(('q', ''.join(self.buf)))
            self.in_qstem = False
            self.buf = []
        if tag == 'pre' and self.in_pre:
            self.out.append(('p', ''.join(self.buf)))
            self.in_pre = False
            self.buf = []
        if tag == 'div' and self.in_textdiv and self.stack and self.stack[-1] == 'div':
            # 离开 .text 块（简化：遇到 div 关闭且当前在 textdiv）
            self.in_textdiv = False
        if self.stack:
            self.stack.pop()
        if self.classes:
            self.classes.pop()

    def handle_data(self, data):
        if self.in_qstem or self.in_pre:
            self.buf.append(data)


def load_index(vdir):
    p = os.path.join(vdir, 'audio_index.js')
    with open(p, encoding='utf-8') as f:
        c = f.read()
    c = c.strip()
    if c.startswith('window.CILS_AUDIO='):
        c = c[len('window.CILS_AUDIO='):]
    if c.endswith(';'):
        c = c[:-1]
    return json.loads(c)


def main():
    vol = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    vdir = os.path.join(ROOT, 'CILS_Vol%d_esami' % vol)
    index = load_index(vdir)
    keys = set(index.keys())
    total = 0
    hit = 0
    miss = []
    for lvl in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
        fp = os.path.join(vdir, lvl + '.html')
        if not os.path.exists(fp):
            continue
        with open(fp, encoding='utf-8') as f:
            h = f.read()
        ex = Extractor()
        ex.feed(h)
        for kind, txt in ex.out:
            t = js_norm_q(txt) if kind == 'q' else js_norm_p(txt)
            if not t:
                continue
            total += 1
            if t in keys:
                hit += 1
            else:
                miss.append((lvl, kind, txt[:60]))
    print('Vol.%d  提取片段=%d  映射命中=%d  缺失=%d' % (vol, total, hit, total - hit))
    if miss:
        print('--- 缺失样例（前10）---')
        for m in miss[:10]:
            print(m)


if __name__ == '__main__':
    import sys
    main()
