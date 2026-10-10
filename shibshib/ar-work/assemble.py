#!/usr/bin/env python3
"""Build ttshat's Arabic catalogs from the translated batches.

`part_NN` lines are `<m|f><TAB><JSON string>` (m: locales/ar.json, f: locales/ar-formats.json);
`tr_NN` holds one translation per line in the same order (JSON escapes such as \\n are allowed).
Writes `ar.json` and `ar-formats.json` here; move them to crates/ui-egui/locales/ when complete.

    python3 shibshib/ar-work/assemble.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PH = re.compile(r'\{[^{}]*\}')
msgs, fmts, problems = {}, {}, []
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
        v = json.loads('"' + v.replace('"', '\\"') + '"')
        # Keep the source's leading and trailing spaces (they join fragments).
        v = k[:len(k) - len(k.lstrip(' '))] + v.strip(' ') + k[len(k.rstrip(' ')):]
        if sorted(PH.findall(k)) != sorted(PH.findall(v)):
            problems.append(f'{part.name}: placeholders differ: {k!r} -> {v!r}')
        (fmts if kind == 'f' else msgs)[k] = v
(HERE / 'ar.json').write_text(json.dumps(msgs, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(HERE / 'ar-formats.json').write_text(json.dumps(fmts, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(msgs)} messages, {len(fmts)} formats')
for p in problems:
    print('problem:', p)
