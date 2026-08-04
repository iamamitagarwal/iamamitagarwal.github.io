# Project Memory

## Project Purpose
Personal website for Amit Agarwal built on Jekyll + Minimal Mistakes, optimized for consistent rendering across Chrome, Safari, desktop, and mobile.

## Current Focus / Recent Work
- Publications and patents were normalized: author display uses comma-separated “First Last” order, titles standardized, and ordering adjusted (priority for first-author papers).
- Added/updated 2025–2026 publications (new files under `_publications/`) and corrected venues/URLs for specific papers.
- “What’s next” content refreshed and reordered in `_data/whats_next.yml`.
- Media page styling refined for readability in light/dark modes; `qq.com` visibility improved. Media layout now uses 2 columns on desktop to avoid overly small cards.
- Added Oracle AI blog media item and set it to the first slot using a remote poster image URL; removed `referrerpolicy="no-referrer"` from remote media images to allow Oracle-hosted image loading.
- Added the ACL 2026 publication `Do Image-Text Metrics Respect Semantic Invariances?` and the GSM-SEM arXiv preprint.
- Corrected the lifecycle-aware clustering publication to `AACL 2025`, fixed visible corrupted evaluation/SweEval/VLMEvalKit titles, and refreshed right-rail items for ACL 2026, completed GRAIL-V@CVPR 2026, and WACV 2026.
- Updated the media page data to feature GRAIL-V@CVPR 2026 with a local image asset and separate Event/Oracle Blog links.
- Added a CVPR 2026 GRAIL-V workshop talk entry using an optimized 16:9 image derived from `IMG_0475.HEIC`.
- Added active-state highlighting for top-level masthead navigation links and cleaned the GRAIL-V media poster text.
- Cross-checked Hitesh Laxmichand Patel's publications page against local `_publications`; added missing Amit co-authored 2026 entries for the entropy-decoding paper and the PAKDD cultural-bias review, promoted CommonLID/RECOR/Judging to ACL/ICML venue labels, and corrected stale shared-paper author metadata.
- Completed a strict publication-record audit: every current paper destination was checked against its title, authors, venue, and year rather than HTTP reachability alone. Corrected unrelated ACL records for RECOR (`2026.findings-acl.129`), Can LLMs Narrate (`2025.emnlp-industry.60`), CommonLID (`2026.acl-long.1527`), and Do Image-Text Metrics (`2026.findings-acl.1948`); replaced confirmed preprints with IJERT, IAEME, Springer, ACM, IEEE, CVF, and ACL destinations; completed the PAKDD record; and normalized confirmed track/workshop labels. Retained arXiv only where no verified public proceedings page is available (BenchHub, DAIQ, GSM-SEM, Judging, and Think Twice).
- Publication recognition is data-driven through `highlight`, `highlight_rank`, `recognition`, and `recognition_type`: AccessEval is marked as EMNLP 2025 Best Social Impact Paper Award and Judging What We Cannot Solve as an ICML 2026 Spotlight Paper. The shared row renderer shows their badges, `priority: 0` places them first for their years, and the home page derives its Research Highlights section from this metadata.

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
