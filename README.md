<p align="center">
  <img alt="ShibShib ttshat" src="docs/shibshib/ttshat.svg" width="140">
</p>

<h1 align="center">ShibShib ttshat</h1>

<p align="center">
  <b>Free, open-source photo library and raw development — part of the ShibShib creative suite.</b><br>
  <b>مكتبة صور وتحميض ملفات RAW، مجاني ومفتوح المصدر — جزء من حزمة شبشب.</b>
</p>

<p align="center">
  <a href="https://shibshib.art/">shibshib.art</a>
</p>

<p align="center">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-555555">
  <img alt="Based on LightCraft" src="https://img.shields.io/badge/based%20on-LightCraft-f2a516">
</p>

## Built on LightCraft

ShibShib ttshat is a fork of **[LightCraft](https://github.com/storytold/lightcraft)**, the
open-source, clean-room photo library and non-destructive raw developer written in Rust by the
**[ArtCraft](https://getartcraft.com/)** team and the LightCraft contributors. Almost everything
that makes this app work is their work. Thank you. If you like ShibShib ttshat, please star and
support the upstream project as well.

What we add: the ShibShib identity, a full Arabic interface laid out right to left, and Arabic
features to come. Our changes are listed in [`shibshib/CHANGES.md`](shibshib/CHANGES.md).
Upstream's own README, with the full feature list and build instructions, is in
[`docs/UPSTREAM-README.md`](docs/UPSTREAM-README.md).

## The ShibShib suite

| App | What it's for | Based on |
|---|---|---|
| [ShibShib rsm](https://github.com/7mz410/ShibShib-rsm) | Vector illustration | VectorCraft |
| **ShibShib ttshat** | Photo library and raw development | LightCraft |

More apps are on the way: see [shibshib.art](https://shibshib.art/).

## Building

```sh
cargo run --release -p lightcraft
# after merging upstream:
git fetch upstream && git merge upstream/main && python3 shibshib/rebrand.py
```

## Licence

Code: MIT OR Apache-2.0 (`LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE`), like upstream. The ShibShib
name and logos in `docs/shibshib/` belong to the ShibShib project.
