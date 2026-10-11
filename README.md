<p align="center">
  <img alt="ttshat" src="docs/studio/ttshat.svg" width="140">
</p>

<h1 align="center">ttshat</h1>

<p align="center">
  <b>Free, open-source photo library and raw development — part of the Creative Studio creative suite.</b><br>
  <b>مكتبة صور وتحميض ملفات RAW، مجاني ومفتوح المصدر — جزء من حزمة Creative Studio.</b>
</p>

<p align="center">
  <a href="https://studio.creative.ps/">studio.creative.ps</a>
</p>

<p align="center">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-555555">
  <img alt="Based on LightCraft" src="https://img.shields.io/badge/based%20on-LightCraft-f2a516">
</p>

## Built on LightCraft

ttshat is a fork of **[LightCraft](https://github.com/storytold/lightcraft)**, the
open-source, clean-room photo library and non-destructive raw developer written in Rust by the
**[ArtCraft](https://getartcraft.com/)** team and the LightCraft contributors. Almost everything
that makes this app work is their work. Thank you. If you like ttshat, please star and
support the upstream project as well.

What we add: the Creative Studio identity, a full Arabic interface laid out right to left, and Arabic
features to come. Our changes are listed in [`studio/CHANGES.md`](studio/CHANGES.md).
Upstream's own README, with the full feature list and build instructions, is in
[`docs/UPSTREAM-README.md`](docs/UPSTREAM-README.md).

## The Creative Studio suite

| App | What it's for | Based on |
|---|---|---|
| [Creative Studio rsm](https://github.com/7mz410/CreativeStudio-rsm) | Vector illustration | VectorCraft |
| **ttshat** | Photo library and raw development | LightCraft |

More apps are on the way: see [studio.creative.ps](https://studio.creative.ps/).

## Building

```sh
cargo run --release -p lightcraft
# after merging upstream:
git fetch upstream && git merge upstream/main && python3 studio/rebrand.py
```

## Licence

Code: MIT OR Apache-2.0 (`LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE`), like upstream. The Creative Studio
name and logos in `docs/studio/` belong to the Creative Studio project.
