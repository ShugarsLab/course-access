#!/usr/bin/env python3
'''
pdf_audit.py -- inventory a PDF's tag structure (a tagged-PDF audit).

    python3 pdf_audit.py paper.pdf [other.pdf ...]      # counts, language, figures and alt text
    python3 pdf_audit.py --headings paper.pdf           # heading tags with their text, in order

Walks the WHOLE structure tree (every child at every level). An early version stopped after the
first child of each node and reported a fully tagged paper as nearly empty -- if a count looks
implausibly low, suspect the walker before the file.
'''
import sys
from collections import Counter, defaultdict
import pikepdf


def walk(node, pages, visit, pg=None, seen=None):
    seen = set() if seen is None else seen
    if isinstance(node, pikepdf.Array):
        for child in node:
            walk(child, pages, visit, pg, seen)
        return
    if not isinstance(node, pikepdf.Dictionary):
        return
    if node.is_indirect:
        if node.objgen in seen:
            return
        seen.add(node.objgen)
    p = node.get('/Pg')
    if p is not None:
        pg = pages.get(p.objgen, pg)
    if node.get('/S') is not None:
        visit(node, pg)
    kids = node.get('/K')
    if kids is not None:
        walk(kids, pages, visit, pg, seen)


def audit(path):
    pdf = pikepdf.open(path)
    pages = {p.objgen: i + 1 for i, p in enumerate(pdf.pages)}
    counts = Counter(); figures = []
    def visit(node, pg):
        s = str(node.get('/S')); counts[s] += 1
        if s in ('/Figure', '/Formula'):
            alt = node.get('/Alt')
            figures.append((pg, s, str(alt) if alt is not None else None))
    st = pdf.Root.get('/StructTreeRoot')
    if st is not None:
        walk(st.get('/K'), pages, visit)
    print(f'===== {path}')
    print(f'  Lang: {pdf.Root.get("/Lang")!s}   tagged: {st is not None}   pages: {len(pdf.pages)}')
    print('  tags: ' + ', '.join(f'{k[1:]} {v}' for k, v in counts.most_common()))
    per_page = defaultdict(list)
    for pg, s, alt in figures:
        per_page[pg].append(alt)
    print(f'  figures: {len(figures)}, with alt text: {sum(1 for f in figures if f[2])}')
    for pg in sorted(per_page, key=lambda x: (x is None, x)):
        alts = per_page[pg]
        print(f'    p{pg}: {len(alts)} figure(s); ' + '; '.join((a[:60] + '...') if a else '(no alt)' for a in alts))


def headings(path):
    import pdfplumber
    pdf = pikepdf.open(path); pl = pdfplumber.open(path)
    pages = {p.objgen: i for i, p in enumerate(pdf.pages)}
    cache = {}
    def mcid_text(pi):
        if pi not in cache:
            d = defaultdict(str)
            for ch in pl.pages[pi].chars:
                if ch.get('mcid') is not None:
                    d[ch['mcid']] += ch['text']
            cache[pi] = d
        return cache[pi]
    def mcids(node, pg):
        out = []
        if isinstance(node, pikepdf.Array):
            for c in node:
                out += mcids(c, pg)
            return out
        if isinstance(node, pikepdf.Dictionary):
            p = node.get('/Pg'); pg = pages.get(p.objgen, pg) if p is not None else pg
            if '/MCID' in node and '/S' not in node:
                return [(pg, int(node.MCID))]
            if node.get('/K') is not None:
                out += mcids(node.K, pg)
            return out
        try:
            return [(pg, int(node))]
        except (TypeError, ValueError):
            return []
    wanted = {'/Title', '/H', '/H1', '/H2', '/H3', '/H4', '/H5', '/H6'}
    pages1 = {k: v + 1 for k, v in pages.items()}
    def visit(node, pg):
        s = str(node.get('/S'))
        if s in wanted:
            refs = mcids(node.get('/K'), pages.get(node.Pg.objgen) if node.get('/Pg') is not None else None)
            text = ''.join(mcid_text(a)[b] for a, b in refs if a is not None).strip()
            first = refs[0][0] + 1 if refs and refs[0][0] is not None else '?'
            print(f'  {s[1:]:6} p{first:<3} {text[:90]}')
    print(f'===== {path}')
    walk(pdf.Root.StructTreeRoot.get('/K'), pages1, visit)


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description="Inventory a PDF's tags: language, tag counts, figures "
                                             'with the start of their alt text, and (with --headings) the headings in order.')
    ap.add_argument('pdfs', nargs='+', metavar='pdf', help='one or more PDF files')
    ap.add_argument('--headings', action='store_true', help='list the heading tags with their text, in order')
    args = ap.parse_args()
    for p in args.pdfs:
        headings(p) if args.headings else audit(p)
