#!/usr/bin/env python3
"""Build lamasat's Arabic catalogs from the translated batches.

`part_NN` lines are `<m|f><TAB><JSON string>` (m: locales/ar.json, f: locales/ar-formats.json);
`tr_NN` holds one translation per line in the same order (JSON escapes such as \\n are allowed).
The existing `ar.json` and `ar-formats.json` here are the base, so rows merged by hand survive a rerun.
Every key the other locales use (`crates/ui-egui/locales/*.json`, `*-formats.json`) that still has no
Arabic gets its English text, so the build's "every catalog carries every key" check never breaks.
Writes `ar.json` and `ar-formats.json` here; move them to crates/ui-egui/locales/ when complete.

    python3 studio/ar-work/assemble.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PH = re.compile(r'\{[^{}]*\}')
def load(name):
    path = HERE / name
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}


msgs, fmts, problems = load('ar.json'), load('ar-formats.json'), []
for part in sorted(HERE.glob('part_*')):
    tr = HERE / part.name.replace('part_', 'tr_')
    if not tr.exists():
        continue
    keys = part.read_text(encoding='utf-8').rstrip('\n').split('\n')
    vals = tr.read_text(encoding='utf-8').rstrip('\n').split('\n')
    if len(keys) != len(vals):
        problems.append(f'{part.name}: {len(keys)} keys, {len(vals)} translations')
        continue
    for line, v in zip(keys, vals):
        kind, k = line.split('\t', 1)
        k = json.loads(k)
        if v.strip() == '-':
            continue  # not translated yet: the app shows the English text
        v = json.loads('"' + v.replace('"', '\\"') + '"')
        # Keep the source's leading and trailing spaces (they join fragments).
        v = k[:len(k) - len(k.lstrip(' '))] + v.strip(' ') + k[len(k.rstrip(' ')):]
        if kind == 'f':
            # format!: named placeholders as a set, positional ones in the same order and number
            # (`{:.0}` stands in for a positional English plural suffix and prints nothing).
            def split(t):
                ph = PH.findall(t.replace('{{', '').replace('}}', ''))
                named = sorted(set(p.strip('{}').split(':')[0] for p in ph if re.match(r'\{[A-Za-z_]', p)))
                return named, len([p for p in ph if not re.match(r'\{[A-Za-z_]', p)])
            if split(k) != split(v):
                problems.append(f'{part.name}: placeholders differ: {k!r} -> {v!r}')
        elif sorted(PH.findall(k)) != sorted(PH.findall(v)):
            problems.append(f'{part.name}: placeholders differ: {k!r} -> {v!r}')
        (fmts if kind == 'f' else msgs)[k] = v
# English fallback for every key the other locales carry but Arabic does not (the build needs them all).
LOCALES = HERE.parent.parent / 'crates' / 'ui-egui' / 'locales'
upstream = {'m': set(), 'f': set()}
for path in LOCALES.glob('*.json'):
    if path.name.startswith('ar') or path.stem == 'en':
        continue
    if path.stem.endswith('-formats'):
        upstream['f'].update(json.loads(path.read_text(encoding='utf-8')))
    else:
        upstream['m'].update(json.loads(path.read_text(encoding='utf-8')))
fallback = {'m': 0, 'f': 0}
for key in sorted(upstream['m'] - set(msgs)):
    msgs[key] = key
    fallback['m'] += 1
for key in sorted(upstream['f'] - set(fmts)):
    fmts[key] = key
    fallback['f'] += 1
print(f"English fallback: {fallback['m']} messages, {fallback['f']} formats")
(HERE / 'ar.json').write_text(json.dumps(msgs, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(HERE / 'ar-formats.json').write_text(json.dumps(fmts, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(msgs)} messages, {len(fmts)} formats')
for p in problems:
    print('problem:', p)
