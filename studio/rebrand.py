#!/usr/bin/env python3
"""Apply the ttshat branding on top of upstream LightCraft.

Only user-visible text is rebranded; crate names, file formats and other internals keep their
upstream names so `git merge upstream/main` stays easy. The script is idempotent: after merging
upstream, resolve any conflicts in favour of upstream and run it again.

    python3 studio/rebrand.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = 'ttshat'
REPO = 'https://github.com/7mz410/CreativeStudio-ttshat'
SITE = 'https://studio.creative.ps'
# Persisted names that saved catalogs and presets refer to; renaming them would break those.
KEEP = ('LightCraft Default', 'not a LightCraft backup')

# Exact replacements, applied before the general rename (and kept idempotent: skipped once done).
SPECIFIC = {
    'crates/ui-egui/src/links.rs': [
        ('pub const WEBSITE: &str = "https://getartcraft.com";', f'pub const WEBSITE: &str = "{SITE}";'),
        ('pub const APP_PAGE: &str = "https://getartcraft.com/apps/lightcraft";', f'pub const APP_PAGE: &str = "{SITE}";'),
        ('pub const GITHUB: &str = "https://github.com/storytold/lightcraft";', f'pub const GITHUB: &str = "{REPO}";'),
        ('pub const HELP: &str = "https://github.com/storytold/lightcraft/tree/main/docs";', f'pub const HELP: &str = "{REPO}/tree/main/docs";'),
        ('pub const FEEDBACK: &str = "https://github.com/storytold/lightcraft/issues/new";', f'pub const FEEDBACK: &str = "{REPO}/issues/new";'),
        ('        assert!(APP_PAGE.ends_with(&format!("/apps/{APP}")));\n        assert!(GITHUB.ends_with(&format!("/storytold/{APP}")));',
         f'        assert_eq!(APP_PAGE, "{SITE}");\n        assert_eq!(GITHUB, "{REPO}");'),
    ],
}
# Exact replacements inside string literals and catalogs, before the general rename.
LITERALS = [
    ('Join the ArtCraft Discord', 'Upstream Community on Discord'),
    ('Join the ArtCraft community on Discord', 'The upstream ArtCraft community on Discord'),
    ('ArtCraft Website', 'Creative Studio Website'),
]

STRING = re.compile(r'"(?:[^"\\\n]|\\.)*"')


def rename(text: str) -> str:
    for a, b in LITERALS:
        text = text.replace(a, b)
    if any(k in text for k in KEEP):
        return text
    return text.replace('LightCraft', NAME)


def rebrand_rust(path: Path) -> bool:
    src = path.read_text(encoding='utf-8')
    out = src
    for a, b in SPECIFIC.get(path.relative_to(ROOT).as_posix(), []):
        if not b or b not in out:
            out = out.replace(a, b)
    out = STRING.sub(lambda m: rename(m.group(0)), out)
    if out != src:
        path.write_text(out, encoding='utf-8')
    return out != src


def rebrand_locale(path: Path) -> bool:
    src = path.read_text(encoding='utf-8')
    data = json.loads(src)
    renamed = {rename(k): rename(v) if isinstance(v, str) else v for k, v in data.items()}
    out = json.dumps(renamed, ensure_ascii=False, indent=2) + "\n"
    if out != src:
        path.write_text(out, encoding='utf-8')
    return out != src


def rebrand_plist(path: Path) -> bool:
    src = path.read_text(encoding='utf-8')
    out = re.sub(r'(<key>CFBundle(?:Display)?Name</key>\s*<string>)LightCraft(</string>)', rf'\g<1>{NAME}\2', src)
    out = out.replace('<string>ai.storyteller.lightcraft</string>', '<string>ps.creative.studio.ttshat</string>')
    if out != src:
        path.write_text(out, encoding='utf-8')
    return out != src


def RUST_FILES():
    return sorted((ROOT / 'crates/ui-egui/src').rglob('*.rs')) + sorted((ROOT / 'apps/lightcraft/src').rglob('*.rs'))


def main():
    changed = [p for p in RUST_FILES() if rebrand_rust(p)]
    changed += [p for p in sorted((ROOT / 'crates/ui-egui/locales').glob('*.json')) if rebrand_locale(p)]
    web = ROOT / 'apps/lightcraft-web/index.html'
    html = web.read_text(encoding='utf-8')
    branded = html.replace('<title>LightCraft</title>', f'<title>{NAME}</title>').replace('Loading LightCraft…', f'Loading {NAME}…').replace('content="LightCraft:', f'content="{NAME}:')
    if branded != html:
        web.write_text(branded, encoding='utf-8')
        changed.append(web)
    plist = ROOT / 'packaging/macos/Info.plist.in'
    if plist.exists() and rebrand_plist(plist):
        changed.append(plist)
    for p in changed:
        print('rebranded', p.relative_to(ROOT))


if __name__ == '__main__':
    main()
