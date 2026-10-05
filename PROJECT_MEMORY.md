# Project Memory

## Project Purpose
Personal website for Amit Agarwal built on Jekyll + Minimal Mistakes, optimized for consistent rendering across Chrome, Safari, desktop, and mobile.

## Current Focus / Recent Work
- October 5 media ordering: feature GRAIL-V first with Ahmedabad Mirror beside it in the desktop opening pair; keep remaining workshop/press masonry below. Mobile retains GRAIL-V then Ahmedabad Mirror. Preserve Mirror PDF and source links and suppress duplicate static-image rendering.
- October 5 workshop media: replaced the organizing prose with two image cards using official SURGeLLM ACL 2026 and DocInsights EMNLP 2026 committee screenshots, captured October 5. Local assets in assets/media/workshops preserve source-page links and include Amit in each view.
- October 5 balanced-profile alignment: Home now uses Enterprise AI Systems with four equal pillars (agents/automation, search/knowledge, multimodal/document intelligence, evaluation/responsible AI), followed by six concise research-to-product examples. Opening explicitly connects science, engineering and product; Fusion’s dated production contribution remains separate from current Support/long-horizon work. Projects cards follow the same four areas, site description is aligned, and the existing layout/award band remain intact.
- October 5 final metadata check: citation venue classification now treats versioned arXiv labels and the `arxiv` venue token as preprints, avoiding a false conference tag for VLMEvalKit v5. ScholarlyArticle JSON-LD contains no conference/publisher attribution and required no change. Temporary production build confirmed no conference tag on versioned/plain arXiv pages and preserved the ACL conference tag.
- October 5 VLMEvalKit version correction: retained the existing URL, but now explicitly catalogs arXiv v5 (July 6, 2026) with its full 44-author list. The original ACM 2024 record does not include Amit; a visible version note prevents attributing that publication to him. Venue, year, source links and crawler metadata derive from the corrected source.
- October 5 source audit: added the missing graph-data augmentation patent US11989964B2 (May 21, 2024 grant; 2021 priority grouping), updated domain-adapting graph networks to US12602547B2 (April 14, 2026), and restored Sandeep Jana in two inventor lists. Corrected GSM-SEM’s 14-author record/spelling and MVTamperBench author order against publisher metadata. The cultural-bias chapter’s publisher 2027 versus existing 2026 date discrepancy remains unresolved; its date was not changed. Agent-story cross-links now use its new title; llms.txt derives titles/descriptions automatically.
- October 5 agent-scope follow-up: broadened Home, Projects and the agentic story to support agents, ticket automation, incident triage/resolution and evidence-to-action workflows. Long-horizon tasks, multimodal agents and memory are explicitly current research directions based on the author’s stated focus; no deployment, autonomy, savings or success-rate claims were added. Preserved the current layout and public research links.
- October 5 follow-up: clarified the homepage introduction to combine hands-on model and evaluation work with research priorities, architecture, science/engineering collaboration and product decisions, reflecting the shared technical and leadership profile.
- October 5: consolidated homepage into four research/leadership areas, removed duplicate story lists from Projects, fixed Liquid/Markdown portfolio boundaries, added organizer links and ICML recognition, and refreshed two patent grant links. Public CV now exposes one neutral download (V7A), with a two-line domains headline covering retrieval, agents, multimodal models and evaluation. V7B remains a private application variant; its PDF is excluded from site output. Earlier two-download notes below are historical.
- October 2 discovery follow-up: added three evidence-linked stories on enterprise retrieval, agentic knowledge systems, and multimodal evaluation; linked them from Home/Projects and the optional generated agent index. Replaced broad portfolio claims with scoped contributions and research comparisons. Narrow project grids now fit mobile columns. Search Console review found only three indexed pages in the September 20 report and a January sitemap fetch failure; account actions and outcomes are recorded privately outside the site.
- October 2 homepage content refresh in the existing layout: current title and career continuity, explicit technical leadership, bounded first/co-first-author research findings, science co-ownership of the Fusion image-to-text production contribution, and linked workshop organizing. Removed the opening quote, universal quality/safety assertions and unconfirmed IIIT credential. Hero, sidebar, navigation and existing recognition component remain in the current design; the separate visual redesign stays local.
- October 2, 2026 discoverability fixes: plain `robots.txt`; explicit Googlebot, OAI-SearchBot and Google-Extended allow rules preserving the prior allow-all policy; explicit `jekyll-feed`; build exclusions for operational documents and generated/scratch directories.
- Local and production builds now use the existing Gemfile-pinned Minimal Mistakes 4.24.0 gem. The remote-theme download encountered a local certificate CRL error; certificate verification remains enabled. The theme version is unchanged.
- Publication metadata shares comma-separated author normalization in `_includes/publication_metadata.html`. Numeric years are emitted directly, citation tags use separate authors, and conference names are no longer mislabeled as publishers. Home ProfilePage and Person share a stable `/#person` identity with the actual current title.
- CV now has readable HTML and two labeled reviewed resume downloads. AccessEval's official paper recognition label is "EMNLP 2025 Social Impact Award", superseding the older wording below. VLMEvalKit's unrelated abstract was replaced by a labeled summary and publisher link; this is not a full abstract or an indexing guarantee.
- Added a small data-driven `llms.txt` navigation aid; it is optional agent convenience, not a ranking promise or crawler policy. The blog feed retains the existing post collection.
- A separate `codex/website-redesign-preview` worktree holds the proposed visual redesign for local review. It is not part of the immediate production changes.
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
- Home-page Research Highlights uses a compact two-column recognition band on desktop and stacks only on mobile. It gives award and spotlight items independent hierarchy with type-colored top rules, concise `home_highlight_title` links, and no duplicated venue/year metadata.

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
- October 5 agent-scope copy: production build passed to `/private/tmp/profile-agent-scope-20261005`; generated Home, Projects and agentic-story HTML contains the new copy, headings and project-card fields. Scoped source `git diff --check` passed. Existing theme Sass deprecations remain; no tests added.
- October 2 production-config `JEKYLL_ENV=production bundle exec jekyll build --destination /private/tmp/amit-profile-production-20261002 --disable-disk-cache` passed using the documented conda Ruby invocation. Generated metadata for all 38 publications was inspected, feed/sitemap XML parsed, and listed development paths were absent. No automated tests added or run. Do not generate into the tracked local `_site` when reviewing this task.
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
