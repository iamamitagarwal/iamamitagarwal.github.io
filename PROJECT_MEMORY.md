# Project Memory

## Project Purpose
Personal website for Amit Agarwal built on Jekyll + Minimal Mistakes, optimized for consistent rendering across Chrome, Safari, desktop, and mobile.

## Current Focus / Recent Work
- Publications and patents were normalized: author display uses comma-separated “First Last” order, titles standardized, and ordering adjusted (priority for first-author papers).
- Added/updated 2025–2026 publications (new files under `_publications/`) and corrected venues/URLs for specific papers.
- “What’s next” content refreshed and reordered in `_data/whats_next.yml`.
- Media page styling refined for readability in light/dark modes; `qq.com` visibility improved. Media layout now uses 2 columns on desktop to avoid overly small cards.
- Added Oracle AI blog media item and set it to the first slot using a remote poster image URL; removed `referrerpolicy="no-referrer"` from remote media images to allow Oracle-hosted image loading.
- Added two ACL 2026 publication entries: `Do Image-Text Metrics Respect Semantic Invariances?` and `GSM-SEM`.
- Corrected the lifecycle-aware clustering publication to `AACL 2025`, fixed visible corrupted evaluation/SweEval/VLMEvalKit titles, and refreshed right-rail items for ACL 2026, completed GRAIL-V@CVPR 2026, and WACV 2026.
- Updated the media page data to feature GRAIL-V@CVPR 2026 with a local image asset and separate Event/Oracle Blog links.
- Added a CVPR 2026 GRAIL-V workshop talk entry using an optimized 16:9 image derived from `IMG_0475.HEIC`.
- Added active-state highlighting for top-level masthead navigation links and cleaned the GRAIL-V media poster text.
- Cross-checked Hitesh Laxmichand Patel's publications page against local `_publications`; added missing Amit co-authored 2026 entries for the entropy-decoding paper and the PAKDD cultural-bias review, promoted CommonLID/RECOR/Judging to ACL/ICML venue labels, and corrected stale shared-paper author metadata.

## Key Files / Locations Touched
- Media layout and styles: `_pages/media.md`
- Publications rendering: `_includes/publication_row.html`, `_layouts/paper.html`
- Right-rail widgets: `_includes/whatsnext_and_contact.html`
- Site head/meta: `_includes/head/custom.html` (and `_includes/seo.html` if present)
- Data files: `_data/media.yml`, `_data/whats_next.yml`
- Publications data: `_publications/*.md`
- Site branding: `assets/css/brand.css`

## Decisions / Assumptions
- Media list supports data-defined items with `image:` URLs in `_data/media.yml`, rendered before file-based media entries.
- Desktop media grid capped at 2 columns to preserve readability for text-heavy screenshots.
- Oracle-hosted media image requires referrer and fails with `no-referrer`; keep default referrer behavior for remote media images.

## Commands / Tests Run
- `bundle exec jekyll build --config _config.yml,_config.local.yml` (passes; Sass deprecation warnings from theme).
- `bundle exec jekyll serve --livereload --config _config.yml,_config.local.yml` used for local verification.
- Playwright used for viewport checks on `/media/`.
- Direct conda Ruby build command currently works when the `bundle` shim is confused:
  `/Users/aamita/miniconda3/envs/jekyll/bin/ruby /Users/aamita/miniconda3/envs/jekyll/bin/bundle exec jekyll build --config _config.yml,_config.local.yml`
- Browser checks on `http://127.0.0.1:4000/`, `/publications/`, and `/media/` verified the ACL papers, GRAIL-V media card, right-rail updates, and mobile media layout.
- `git diff --check` and the direct conda Ruby Jekyll build passed after the Hitesh-publications comparison; localhost `/publications/` was verified against the running Jekyll server on `127.0.0.1:4000`.

## Open Issues / Risks / Next Steps
- Working tree may still contain generated `_site/` artifacts and `.playwright-cli/` output locally; avoid committing those.
- If the Oracle media poster fails to load in some environments, fallback to a local image under `assets/media/pictures/`.
- Keep an eye on Safari rendering of media cards and “What’s next” widget when adjusting CSS.
- The 2024 Springer labels visible on Hitesh's page should be revisited once a stable publisher/proceedings URL is available; current local records still keep the arXiv links.

## Workflow Notes
- Local setup uses conda env `jekyll` with Ruby 3.1 and `SDKROOT` set via `xcrun --show-sdk-path`.
- Prefer changes in source files; `_site/` is generated and should remain untracked.
