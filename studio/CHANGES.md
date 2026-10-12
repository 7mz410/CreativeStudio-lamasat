# lamasat: changes from upstream LightCraft

Required by the Apache License 2.0 (section 4b): files we changed carry this notice through
this list.

- Branding (user-visible only, applied by `studio/rebrand.py`): the app name lamasat,
  the bundle id `ps.creative.studio.lamasat`, Help links to studio.creative.ps and this repository, and the
  upstream Discord labelled as the upstream community. Crate names and file formats keep their
  upstream names.
- App icon: the lamasat tile (`assets/app-icon/`).
- Removed upstream's ArtCraft brand assets (`docs/brand/`), as their brand terms require of forks.
- README and NOTICE: the fork, its credits and the Creative Studio suite.
- Right-to-left interface for Arabic: the patched egui from Creative Studio rsm in `vendor/egui`
  (`studio/RTL.md`), side panels change sides, `crates/ui-egui/tests/rtl.rs`.
- Arabic groundwork: IBM Plex Sans Arabic (OFL) as the Arabic UI font, `crates/ui-egui/src/bidi.rs`
  (Arabic in visual order for egui), and Arabic format strings put in visual order after they are
  filled in (`build.rs`). The Arabic catalog is being translated in `studio/ar-work/` and joins
  the language list when complete.
