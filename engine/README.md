# Smile Jo render engine

Renders brand reels (1080x1920 MP4, 30fps, silent AAC track) and story/cover JPEGs from HTML + Web Animations, using Playwright Chromium and ffmpeg.

- `build.py`: base CSS (brand tokens, Noto Sans Arabic), `html()`, `an()`, `endcard()`, `render_reel(page,name,doc,seconds)`, `still(page,name,doc,t)`. Output goes to `engine/out/`.
- `build3.py`: parameterised templates: `qa()` (question cards over an image), `chat()` (family group chat story), `doc()` (documentary subtitles), `versus()` (two images compared), `lst()` (numbered list / ✓✗ list). See `REELS3` for examples.
- `build2.py`: one-off formats: rules sheet, POV phone booking, gift reveal.
- `stories.py` / `stories2.py` / `st3.py`: story frames (`S()` helper, 1080x1920, sticker space left empty).
- Assets: `assets/` (logo-crop.png, service-*.webp from smilejo.shop), `fonts/`.

Rules: no prices, no lab mention, no medical promises, label AI/acted scenes (قصة تمثيلية / صورة تمثيلية / تمثيل), service lines from smilejo.shop copy only, the treatment disclaimer line on clinical services.

Daily posts live in `days/YYYY-MM-DD/` and `schedule.json` (captions + sticker steps).
