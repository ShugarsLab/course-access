'''mathspeech.py -- spoken reading of Office Math, walked as a tree.

Reading a linearized STRING of the maths loses structure: a sub-and-superscript (d_i squared)
comes out as "di2", a summation's limits run together ("j equals 1nx"), and a bar over a
subscripted symbol breaks the parse. This reads the m:oMath tree directly and applies the
equation-reading rules in the guide's equations chapter:

- operations spelled out ("minus", "times", "squared", "to the negative 8");
- fractions by length: "a divided by b" when short, otherwise "a fraction where the numerator
  is ... and the denominator is ...";
- "end of the square root" only when nothing else marks where the radical stops;
- grouping parentheses kept literal; implied multiplication read as "times";
- a bar changes the symbol: mu bar, mu bar sub i.

speak(maths) -> str, where maths is a list of m:oMath elements (ElementTree or lxml).
'''
import re
import unicodedata

M = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'

GREEK = {
    'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta', 'ε': 'epsilon', 'ζ': 'zeta',
    'η': 'eta', 'θ': 'theta', 'κ': 'kappa', 'λ': 'lambda', 'μ': 'mu', 'ν': 'nu', 'ξ': 'xi',
    'π': 'pi', 'ρ': 'rho', 'σ': 'sigma', 'τ': 'tau', 'φ': 'phi', 'ϕ': 'phi', 'χ': 'chi',
    'ψ': 'psi', 'ω': 'omega', 'Δ': 'capital delta', 'Σ': 'capital sigma', 'Ω': 'capital omega',
    'Φ': 'capital phi', 'Γ': 'capital gamma', 'Λ': 'capital lambda', 'Π': 'capital pi',
}
OPS = {
    '=': 'equals', '≠': 'is not equal to', '<': 'is less than', '>': 'is greater than',
    '≤': 'is less than or equal to', '≥': 'is greater than or equal to', '≈': 'is approximately',
    '+': 'plus', '−': 'minus', '-': 'minus', '±': 'plus or minus', '×': 'times', '·': 'times',
    '⋅': 'times', '∗': 'times', '/': 'divided by', '÷': 'divided by', '∈': 'is an element of',
    '∞': 'infinity', '→': 'goes to', '∝': 'is proportional to', '~': 'is distributed as',
    '∼': 'is distributed as', '%': 'percent',
}
RELATIONS = {'=', '≠', '<', '>', '≤', '≥', '≈', '∈', '→', '~', '∼', '∝'}
NARY = {'∑': 'sum', '∏': 'product', '∫': 'integral'}
FUNCS = {'min': 'the minimum of', 'max': 'the maximum of', 'log': 'the log of',
         'ln': 'the natural log of', 'exp': 'e to the', 'sin': 'sine of', 'cos': 'cosine of'}
ACCENTS = {'̂': 'hat', '̃': 'tilde', '̇': 'dot', '⃗': 'vector',
           '̄': 'bar', '̅': 'bar'}


def _norm(ch):
    n = unicodedata.normalize('NFKC', ch)
    return n if n else ch


class Item:
    '''One spoken piece: kind is "op" (operator/relation), "operand", or "open"/"close".'''
    def __init__(self, text, kind='operand', simple=True):
        self.text, self.kind, self.simple = text, kind, simple


def _local(e):
    return e.tag.split('}')[-1]


def _children(e, name):
    return e.find(M + name)


def _run_items(text):
    '''Characters of an m:r -> items. Letters and digits group into operands.'''
    items, buf = [], ''

    def flush():
        nonlocal buf
        if buf:
            items.append(Item(buf))
            buf = ''
    for ch in text:
        c = _norm(ch)
        if c in OPS:
            flush()
            items.append(Item(c, 'op'))
        elif c in GREEK:
            flush()
            items.append(Item(GREEK[c]))
        elif c in '([{':
            flush(); items.append(Item(c, 'open'))
        elif c in ')]}':
            flush(); items.append(Item(c, 'close'))
        elif c == ',':
            flush(); items.append(Item(',', 'comma'))
        elif c.isspace():
            flush()
        elif c in NARY:
            flush(); items.append(Item(f'the {NARY[c]} of', 'prefix'))
        else:
            buf += c
    flush()
    return items


def _items(e):
    out = []
    if e is None:
        return out
    for c in e:
        out.extend(_node(c))
    return out


def _lim(text):
    return text.replace('is not equal to', 'not equal to')


def _sum_lead(word, lo, hi):
    if lo and hi:
        return f'the {word} from {lo} to {hi} of'
    if lo:
        return f'the {word} over {lo} of'
    if hi:
        return f'the {word} to {hi} of'
    return f'the {word} of'


def _seq(e):
    '''Speak the children of a container (m:e, m:num, m:sub, m:oMath ...) as one phrase.'''
    return _join(_items(e))


def _join(items):
    '''Items -> text: operators spelled out, unary minus as "negative", juxtaposed operands as "times".'''
    out, prev = [], None
    for it in items:
        if prev is not None and getattr(prev, 'rad', False) and getattr(prev, 'multi', False) \
                and not prev.text.endswith('square root,'):
            out.append(', end of the square root,')   # a multi-term radical followed by more maths
        if prev is not None and getattr(prev, 'frac', False) and it.kind in ('operand', 'open', 'prefix'):
            out.append(',')          # "1 divided by n, times the sum ...": the comma closes the fraction
        if it.kind == 'op':
            unary = it.text in '−-' and (prev is None or prev.kind in ('op', 'open', 'comma'))
            if unary:
                out.append('negative')
                prev = Item('', 'op')
                continue
            if it.text == '+' and (prev is None or prev.kind in ('op', 'open', 'comma')):
                continue
            out.append(OPS[it.text])
        elif it.kind == 'open':
            # Grouping is spoken, not punctuated (parentheses read badly aloud). "the quantity ... ," follows spoken-maths practice; the comma is the
            # end marker, since pauses alone do not carry scope (ETS 2016).
            if prev is not None and prev.kind in ('operand', 'close', 'postfix'):
                out.append('times')
            out.append('the quantity')
        elif it.kind == 'close':
            out.append(',')
        elif it.kind == 'comma':
            out.append(',')
        elif it.kind == 'prefix':
            if prev is not None and prev.kind in ('operand', 'close', 'postfix'):
                out.append(', times' if prev.kind == 'postfix' else 'times')
            out.append(it.text)
            prev = Item('', 'op')
            continue
        elif it.kind == 'postfix':
            out.append(it.text)
        else:
            if prev is not None and prev.kind == 'operand' and prev.text == 'S' and \
                    (it.text in ('E', 'D') or it.text.startswith(('E ', 'D '))):
                out[-1] = 'S' + it.text
                prev = Item(out[-1])
                continue
            if prev is not None and prev.kind in ('operand', 'close', 'postfix'):
                out.append(', times' if prev.kind == 'postfix' else 'times')
            txt = it.text
            if txt in ('...', '…', '⋯'):
                txt = 'and so on'
            if re.fullmatch(r'\.\d+', txt):
                txt = '0' + txt
            out.append(txt)
        prev = it
    s = ' '.join(x for x in out if x)
    s = re.sub(r'([(\[{]) ', r'\1', s)
    s = re.sub(r' ([)\]}])', r'\1', s)
    s = re.sub(r' ,', ',', s)
    s = re.sub(r',(\s*,)+', ',', s)
    # a group that already opens with its own scope word needs no "the quantity"
    s = re.sub(r'the quantity (the |a fraction)', r'\1', s)
    return s.strip().rstrip(',').strip()


def _is_simple(text):
    '''Short enough to read as "a divided by b" without losing the scope.'''
    if re.fullmatch(r'the square root of \S+', text):
        return True
    words = text.split()
    return len(words) <= 3 and not any(w in ('plus', 'minus', 'times', 'fraction', 'sum') for w in words)


def _power(sup):
    s = sup.strip()
    if s == '2':
        return 'squared'
    if s == '3':
        return 'cubed'
    return f'to the {s}'


def _node(e):
    tag = _local(e)
    if tag in ('rPr', 'ctrlPr', 'oMathParaPr', 'fPr', 'radPr', 'dPr', 'naryPr', 'sSubPr',
               'sSupPr', 'sSubSupPr', 'barPr', 'accPr', 'funcPr', 'eqArrPr', 'boxPr',
               'borderBoxPr', 'limLowPr', 'limUppPr', 'groupChrPr', 'mPr', 'sPrePr'):
        return []
    if tag == 'r':
        t = ''.join(x.text or '' for x in e.iter(M + 't'))
        return _run_items(t)
    if tag == 'f':
        num = _seq(_children(e, 'num'))
        den = _seq(_children(e, 'den'))
        ftype = e.find(M + 'fPr/' + M + 'type')
        if _is_simple(num) and _is_simple(den):
            it = Item(f'{num} divided by {den}', simple=False)
        else:
            it = Item(f'a fraction where the numerator is {num} and the denominator is {den}', simple=False)
        it.frac = True
        return [it]
    if tag == 'rad':
        inner = _seq(_children(e, 'e'))
        deg = _children(e, 'deg')
        dtxt = _seq(deg) if deg is not None else ''
        root = 'the square root of' if not dtxt else f'the {dtxt} root of'
        it = Item(f'{root} {inner}', simple=False)
        it.multi = not _is_simple(inner)
        it.rad = True
        return [it]
    if tag in ('sSup', 'sSub', 'sSubSup'):
        base_items = _items(_children(e, 'e'))
        sub = _children(e, 'sub')
        sup = _children(e, 'sup')
        if len(base_items) == 1 and base_items[0].kind == 'prefix':      # a sum written as a symbol with scripts
            word = base_items[0].text[len('the '):-len(' of')]
            lo = _lim(_seq(sub)) if sub is not None else ''
            hi = _seq(sup) if sup is not None else ''
            return [Item(_sum_lead(word, lo, hi), 'prefix')]
        if base_items and base_items[-1].kind == 'close' and sup is not None and sub is None:
            return base_items + [Item(_power(_seq(sup)), 'postfix')]   # (a minus b) split as ( ... )^2
        base = _join(base_items)
        text = base
        if sub is not None:
            text += f' sub {_seq(sub)}'
        if sup is not None:
            text += f' {_power(_seq(sup))}'
        return [Item(text)]
    if tag in ('bar', 'acc'):
        word = 'bar'
        if tag == 'acc':
            ch = e.find(M + 'accPr/' + M + 'chr')
            word = ACCENTS.get(ch.get(M + 'val') if ch is not None else '̂', 'accent')
        else:
            pos = e.find(M + 'barPr/' + M + 'pos')
            if pos is not None and pos.get(M + 'val') == 'bot':
                word = 'underbar'
        base_el = _children(e, 'e')
        # mu-bar sub i: the accent belongs to the symbol, the subscript to the accented symbol
        kids = [k for k in base_el if _local(k) not in ('ctrlPr',)] if base_el is not None else []
        if len(kids) == 1 and _local(kids[0]) == 'sSub':
            b = _seq(_children(kids[0], 'e')); s = _seq(_children(kids[0], 'sub'))
            return [Item(f'{b} {word} sub {s}')]
        return [Item(f'{_seq(base_el)} {word}')]
    if tag == 'nary':
        chr_el = e.find(M + 'naryPr/' + M + 'chr')
        ch = chr_el.get(M + 'val') if chr_el is not None else '∫'
        word = NARY.get(ch, 'sum')
        sub = _children(e, 'sub'); sup = _children(e, 'sup')
        st = _seq(sub) if sub is not None else ''
        su = _seq(sup) if sup is not None else ''
        body = _seq(_children(e, 'e'))
        lead = _sum_lead(word, _lim(st), su)
        return [Item(f'{lead} {body}', simple=False)]
    if tag == 'd':
        beg = e.find(M + 'dPr/' + M + 'begChr')
        end = e.find(M + 'dPr/' + M + 'endChr')
        b = beg.get(M + 'val') if beg is not None else '('
        en = end.get(M + 'val') if end is not None else ')'
        parts = [_seq(x) for x in e.findall(M + 'e')]
        if b == '|' and en == '|':
            return [Item(f'the absolute value of {" , ".join(parts)}')]
        inner = ', '.join(parts)
        return [Item(b, 'open'), Item(inner), Item(en, 'close')] if b else [Item(inner)]
    if tag == 'func':
        name = _seq(_children(e, 'fName')).strip()
        arg_el = _children(e, 'e')
        # min(k-1, r-1): read the arguments joined by "and"
        dk = [k for k in arg_el if _local(k) == 'd'] if arg_el is not None else []
        if len(dk) == 1 and len([k for k in arg_el if _local(k) not in ('ctrlPr',)]) == 1:
            args = ' and '.join(_seq(x) for x in dk[0].findall(M + 'e'))
        else:
            args = _seq(arg_el)
        lead = FUNCS.get(name, f'{name} of')
        return [Item(f'{lead} {args}', simple=False)]
    if tag in ('limLow', 'limUpp'):
        base_items = _items(_children(e, 'e'))
        lim = _seq(_children(e, 'lim'))
        if len(base_items) == 1 and base_items[0].kind == 'prefix':
            t = base_items[0].text
            if tag == 'limLow':
                word = t[len('the '):-len(' of')]
                return [Item(_sum_lead(word, _lim(lim), ''), 'prefix')]
            if ' over ' in t:                        # the sum over j equals 1 of -> from ... to n
                head, lo = t[:-len(' of')].split(' over ', 1)
                return [Item(f'{head} from {lo} to {lim} of', 'prefix')]
            return [Item(t[:-len(' of')] + f' to {lim} of', 'prefix')]
        return [Item(f'{_join(base_items)} {"under" if tag == "limLow" else "over"} {lim}')]
    if tag in ('oMath', 'e', 'num', 'den', 'sub', 'sup', 'deg', 'fName', 'box', 'borderBox',
               'eqArr', 'oMathPara', 'groupChr', 'limLow', 'limUpp', 'lim'):
        sub_items = _items(e)
        if len(sub_items) == 1 or (sub_items and all(i.kind == 'op' for i in sub_items)):
            return sub_items
        txt = _join(sub_items)
        return [Item(txt)] if txt else []
    items = []
    for c in e:
        items.extend(_node(c))
    return items


def _seq_with_rad_ends(e):
    return _seq(e)


def speak(maths):
    '''List of m:oMath elements -> spoken reading.'''
    parts = []
    for m in maths:
        items = []
        kids = [c for c in m]
        for i, c in enumerate(kids):
            got = _node(c)
            # "end of the square root" only when a multi-term radical is followed by more maths
            for it in got:
                if getattr(it, 'rad', False) and getattr(it, 'multi', False) and \
                        any(_node(x) for x in kids[i + 1:]):
                    it.text += ', end of the square root,'
            items.extend(got)
        parts.append(_join(items))
    s = ' '.join(p for p in parts if p)
    s = re.sub(r'\s+', ' ', s).replace(' ,', ',').replace(',,', ',').strip(' ,')
    return s
