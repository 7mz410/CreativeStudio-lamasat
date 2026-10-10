# ShibShib ttshat: changes from upstream LightCraft

Required by the Apache License 2.0 (section 4b): files we changed carry this notice through
this list.

- Branding (user-visible only, applied by `shibshib/rebrand.py`): the app name ShibShib ttshat,
  the bundle id `com.shibshib.ttshat`, Help links to shibshib.art and this repository, and the
  upstream Discord labelled as the upstream community. Crate names and file formats keep their
  upstream names.
- App icon: the ShibShib ttshat tile (`assets/app-icon/`).
- Removed upstream's ArtCraft brand assets (`docs/brand/`), as their brand terms require of forks.
- README and NOTICE: the fork, its credits and the ShibShib suite.
- Right-to-left interface for Arabic: the patched egui from ShibShib rsm in `vendor/egui`
  (`shibshib/RTL.md`), side panels change sides, `crates/ui-egui/tests/rtl.rs`.
- Arabic groundwork: IBM Plex Sans Arabic (OFL) as the Arabic UI font, `crates/ui-egui/src/bidi.rs`
  (Arabic in visual order for egui), and Arabic format strings put in visual order after they are
  filled in (`build.rs`). The Arabic catalog is being translated in `shibshib/ar-work/` and joins
  the language list when complete.
