# Repository Guidelines

The goal of this project is to -

1. Have the personal website for the author compatible with Chrome, Safari and mobile devices.
2. Ensure any changes that are made is compatible and gives the same experience across Chrome,Safari, Desktop and Mobile Devices.


## Project Structure & Content
- Jekyll site using Minimal Mistakes theme. Key paths:
  - `_config.yml` / `_config.local.yml` – site settings (production vs local gem theme).
  - `_pages/` – top-level pages (About, Publications, Projects, Patents, Media).
  - `_publications/`, `_patents/`, `_talks/`, `_awards/`, `_media/` – collection items.
  - `_data/` – navigation, projects, venues, “What’s next”, media lists.
  - `_includes/` – custom UI (masthead, right-rail widgets, publication row).
  - `assets/css/brand.css` – brand overrides; `images/`, `assets/` for media.

## Build, Serve, and Local Development
- Prereq: conda env `jekyll` with Ruby 3.1; use local Minimal Mistakes gem to avoid SSL issues.
- Install deps: `bundle install` (run inside env).
- Serve locally (preferred):
  `bundle exec jekyll serve --livereload --config _config.yml,_config.local.yml`
- Production build check:
  `bundle exec jekyll build --config _config.yml,_config.local.yml`

## Coding Style & Naming
- Markdown/front matter: YAML keys lower_snake; arrays for tags; wrap strings in quotes.
- Titles: Title Case, accurate acronyms (LLM, NLP, NER, SEA-VL).
- Authors/inventors: “First Last” order, semicolon-separated.
- CSS: keep overrides in `assets/css/brand.css` or scoped `<style>` blocks in includes; prefer REM/px already used; avoid inline `!important` unless matching existing patterns.

## Testing / Validation
- No automated tests; validate by building locally (`jekyll build`) and loading key pages:
  - `/publications/` filters and badges,
  - right-rail “What’s next” + contact modal,
  - dark/light toggle behavior.
- Check console for 404s and layout regressions after edits.

## Content Update Tips
- Publications/Patents: ensure `paper_url` or `uspto_url` points to proceedings/official pages; keep badges and venue tokens accurate.
- Data-driven sections: edit `_data/*.yml`; follow existing schema.
- Images: place under `images/` or `assets/`; update paths in front matter.

## Commit & PR Guidelines
- Commit messages: concise imperative (“Fix publication badges”, “Update patent titles”).
- PRs: describe scope, mention affected pages/data, include before/after screenshots for UI changes, and note local `jekyll build`/serve verification.
