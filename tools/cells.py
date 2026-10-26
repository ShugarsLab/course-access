#!/usr/bin/env python3
'''
cells.py -- find and empty table cells that are covered up on a build slide.

A build that reveals a table a piece at a time is usually made by painting an
opaque rectangle over the parts that are not meant to be visible yet. That hides
them from the eye and from nobody else: the text is still in the cell, so a
screen reader reads the whole finished table on every slide of the build, and
a screen-reader user hears the answer several slides before the class is shown it.

Splitting the table apart would keep the text honest but wreck the formatting.
Emptying the covered cells does the same job and leaves the cell, its fill, its
borders and the table geometry untouched -- the slide looks identical, because
the covering rectangle is still on top of it either way.

    detect   report cells whose rectangle is hidden behind an opaque shape
             drawn later in z-order
    blank    empty the listed cells, keeping paragraph properties so the text
             can be pasted back or re-typed in the same style

Detection is geometry, not judgement: it can only see that something opaque is
on top, not whether you meant it to be. Read the report before running blank.
'''

import argparse, re
from lxml import etree
from pptx import Presentation
from pptx.oxml.ns import qn

A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
P = 'http://schemas.openxmlformats.org/presentationml/2006/main'
NS = {'a': A, 'p': P}

# Anything at or below this alpha is a wash rather than a cover.
OPAQUE_ALPHA = 0.90
COVER_FRAC = 0.75


def _bbox(el):
    xfrm = el.find(f'.//{{{A}}}xfrm')
    if xfrm is None:
        xfrm = el.find(f'.//{{{P}}}xfrm')
    if xfrm is None:
        return None
    off, ext = xfrm.find(f'{{{A}}}off'), xfrm.find(f'{{{A}}}ext')
    if off is None or ext is None:
        return None
    x, y = int(off.get('x')), int(off.get('y'))
    return (x, y, x + int(ext.get('cx')), y + int(ext.get('cy')))


def _alpha(el):
    a = el.find(f'.//{{{A}}}alpha')
    return int(a.get('val')) / 100000 if a is not None else 1.0


FILLS = ('solidFill', 'blipFill', 'gradFill', 'pattFill')


def _is_opaque_fill(el):
    """True only if the shape itself carries an opaque fill.

    The fill lives in the shape's own p:spPr (p:grpSpPr for a group) and has to
    be read from its DIRECT children. Searching the subtree instead finds the
    solidFill inside a:ln, so a rectangle drawn as an outline -- a highlight box
    around a table row -- reads as an opaque cover and gets reported as hiding
    the row it is drawing attention to.
    """
    pr = None
    for child in el:
        if child.tag.split('}')[1] in ('spPr', 'grpSpPr'):
            pr = child
            break
    if pr is None:
        return False
    for child in pr:
        tag = child.tag.split('}')[1]
        if tag == 'noFill':
            return False
        if tag in FILLS:
            a = child.find(f'.//{{{A}}}alpha')
            val = int(a.get('val')) / 100000 if a is not None else 1.0
            return val >= OPAQUE_ALPHA
    return False


def _cell_boxes(frame):
    '''-> {(row, col): (x0, y0, x1, y1)} in slide coordinates.'''
    box = _bbox(frame)
    tbl = frame.find(f'.//{{{A}}}tbl')
    if box is None or tbl is None:
        return {}
    x0, y0 = box[0], box[1]
    grid = [int(c.get('w')) for c in tbl.findall(f'{{{A}}}tblGrid/{{{A}}}gridCol')]
    xs, acc = [], x0
    for w in grid:
        xs.append((acc, acc + w))
        acc += w
    out, y = {}, y0
    for r, row in enumerate(tbl.findall(f'{{{A}}}tr')):
        h = int(row.get('h'))
        for c, (cx0, cx1) in enumerate(xs):
            out[(r, c)] = (cx0, y, cx1, y + h)
        y += h
    return out


def _overlap(a, b):
    ix = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    iy = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    area = (a[2] - a[0]) * (a[3] - a[1])
    return (ix * iy) / area if area else 0.0


def detect(deck):
    '''-> [(slide, shape_id, row, col, text, frac)]'''
    prs = Presentation(deck)
    found = []
    for n, slide in enumerate(prs.slides, start=1):
        tree = slide._element.find(f'.//{{{P}}}cSld/{{{P}}}spTree')
        kids = [k for k in tree if k.tag.split('}')[1]
                not in ('nvGrpSpPr', 'grpSpPr')]
        for i, kid in enumerate(kids):
            if kid.find(f'.//{{{A}}}tbl') is None:
                continue
            boxes = _cell_boxes(kid)
            if not boxes:
                continue
            nv = kid.find(f'.//{{{P}}}cNvPr')
            later = [k for k in kids[i + 1:] if _is_opaque_fill(k)]
            tbl = kid.find(f'.//{{{A}}}tbl')
            rows = tbl.findall(f'{{{A}}}tr')
            for (r, c), cb in sorted(boxes.items()):
                frac = 0.0
                for k in later:
                    kb = _bbox(k)
                    if kb:
                        frac = max(frac, _overlap(cb, kb))
                if frac < COVER_FRAC:
                    continue
                tc = rows[r].findall(f'{{{A}}}tc')[c]
                text = ''.join(t.text or '' for t in tc.iter(f'{{{A}}}t')).strip()
                if text:
                    found.append((n, nv.get('id'), r, c, text, round(frac, 2)))
    return found


def blank(deck, slide_no, cells, out=None):
    '''Empty the given (row, col) cells of the first table on a slide.'''
    prs = Presentation(deck)
    slide = prs.slides[slide_no - 1]
    tbl = slide._element.find(f'.//{{{A}}}tbl')
    if tbl is None:
        return []
    rows = tbl.findall(f'{{{A}}}tr')
    done = []
    for r, c in cells:
        tc = rows[r].findall(f'{{{A}}}tc')[c]
        was = ''.join(t.text or '' for t in tc.iter(f'{{{A}}}t')).strip()
        for para in tc.iter(f'{{{A}}}p'):
            for run in para.findall(f'{{{A}}}r'):
                para.remove(run)
            for br in para.findall(f'{{{A}}}br'):
                para.remove(br)
            if para.find(f'{{{A}}}endParaRPr') is None:
                etree.SubElement(para, f'{{{A}}}endParaRPr').set('dirty', '0')
        done.append((r, c, was))
    prs.save(out or deck)
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['detect', 'blank'])
    ap.add_argument('deck')
    ap.add_argument('--slide', type=int)
    ap.add_argument('--cells', help='r,c;r,c  (0-indexed)')
    ap.add_argument('-o', '--out')
    a = ap.parse_args()
    if a.mode == 'detect':
        for row in detect(a.deck):
            n, sid, r, c, text, frac = row
            print(f'slide {n:>3} table {sid:>5}  cell ({r},{c})  {frac:>4}  {text!r}')
    else:
        cells = [tuple(int(v) for v in pair.split(','))
                 for pair in a.cells.split(';')]
        for r, c, was in blank(a.deck, a.slide, cells, a.out):
            print(f'emptied ({r},{c}): {was!r}')


if __name__ == '__main__':
    main()
