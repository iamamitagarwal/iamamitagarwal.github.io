[README.md](https://github.com/user-attachments/files/23675637/README.md)
# Amit Agarwal — Personal Site (Minimal Mistakes + custom widgets)

Production: https://iamamitagarwal.github.io
Theme: [Minimal Mistakes Jekyll](https://mmistakes.github.io/minimal-mistakes/) (remote theme)

Extras added here:
- Right-side **What’s next** slide-out (populated from `_data/whats_next.yml`)
- **“Say hi”** contact form (Formspree)
- **Dark-mode** toggle in the masthead (persists to `localStorage`)
- Small brand / typography / layout overrides

This README is the “how it works + how to maintain it” brain dump.

---

## Quick start

```bash
conda activate jekyll
export PATH="/Users/aamita/miniconda3/envs/jekyll/bin:$PATH"
export SDKROOT=$(xcrun --show-sdk-path)
# prereqs: Ruby (3.x), Bundler
bundle install
bundle exec jekyll serve --livereload --config _config.yml,_config.local.yml
# visit http://127.0.0.1:4000
```

> GitHub Pages builds from `main`. Pushing to `main` redeploys the site.

---

## Repository map (what to edit)

```
.
├─ _config.yml                 # Site + theme config (title, author, social, google_analytics, etc.)
├─ _data/
│  ├─ navigation.yml           # Header nav items
│  ├─ projects.yml             # Project cards data (cards on /projects)
│  ├─ venues.yml               # Short names → full venue names (used in pubs pages)
│  ├─ media.yml, metrics.yml   # Misc data lists used by pages
│  ├─ best_papers.yml          # Curated list used by publications page
│  └─ whats_next.yml           # ← RIGHT RAIL content (see below)
├─ _includes/
│  ├─ head/custom.html         # Fonts, brand.css, dark-mode bootstrap, masthead toggle script
│  ├─ footer/custom.html       # Only includes the widgets: {% include whatsnext_and_contact.html %}
│  ├─ whatsnext_and_contact.html  # ← the whole “What’s next” + contact UI + JS
│  ├─ publication_row.html     # Rendering helper for pubs lists
│  └─ site-logo.html           # Logo snippet in masthead
├─ _layouts/                   # Theme/section layout overrides (if any)
├─ _pages/                     # Content pages (About, Publications, Projects, etc.)
├─ _posts/                     # Blog posts (optional)
├─ assets/css/brand.css        # Your brand styling overrides
├─ images/                     # Favicon, avatar, screenshots
└─ README.md
```

---

## The custom widgets

### 1) What’s next (right rail)

- Lives in: `_includes/whatsnext_and_contact.html`
- Content: `_data/whats_next.yml`
- Collapsed by default. On desktop it “remembers” the last state in `localStorage['wnx-open']`.

**YAML shape** (follow existing entries):

```yaml
- title: "Hosting workshop at ACL"
  desc: ""                  # optional
  when: "July, 2026"
  tag: "Workshop"
  link: "https://2026.aclweb.org/"
```

**Position / spacing knobs**
- Move tab up/down: `.wnx-tab { top: 110px; }`
- Panel clearance under header: `.wnx-panel { top: 96px; }`
- Make it default-closed again for everyone: clear `localStorage['wnx-open']`

### 2) Contact form (Formspree)

- Trigger: round mail FAB (bottom-right).
- Opens a **centered modal** sized to fit on one screen; the form body scrolls if long.
- Endpoint: `https://formspree.io/f/mwpydbpb` (update directly in the `<form>` element inside `_includes/whatsnext_and_contact.html`).

**View submissions:**
Formspree dashboard → your form → **Submissions**
Direct: https://formspree.io/forms/mwpydbpb

**Sizing knobs (already tuned)**
```css
.contact-card   { max-height: 86vh; }  /* modal fits viewport */
.cd-body        { overflow: auto; }    /* internal scroll for fields */
.cd-actions     { position: sticky; bottom: 0; }  /* buttons always visible */
```

### 3) Dark mode

- Early theme bootstrap in **head** to prevent FOUC:
  ```js
  try { if (localStorage.getItem('theme') === 'dark')
    document.documentElement.classList.add('theme-dark');
  } catch(e){}
  ```
- Bubble-style toggle **in the masthead** (script in `_includes/head/custom.html` inserts it next to the search icon).
- Persists as `localStorage['theme'] = 'dark' | 'light'`.

If you ever see a floating toggle overlapping the FAB, you still have an old fixed-position CSS rule for `#theme-toggle`. Remove it.

---

## Content authoring

### Navigation
Edit `_data/navigation.yml`. Add, remove, or reorder links.

### About page sidebar (avatar size)
Minimal Mistakes constrains the author avatar. You’re overriding it in `head/custom.html`:

```css
.page__sidebar .author__avatar,
.page__sidebar .author__avatar img{
  width: 500px !important;
  height: 500px !important;
  max-width: none !important; /* keeps image from shrinking */
}
@media (max-width: 540px){
  .page__sidebar .author__avatar,
  .page__sidebar .author__avatar img{
    width: 400px !important;
    height: 400px !important;
  }
}
```

Also make sure `_config.yml` → `author` → `avatar` points to your **high-res** image (`/images/profile.jpeg` etc.).

### Projects / Publications / Patents
- `projects.yml` drives the cards on `/projects` (year, tags, short bullets).
- Publications/patents pages use helpers like `_includes/publication_row.html` and various data files (venues, best_papers). Follow the existing entries for field names.

---

## Branding and look

- Fonts loaded in `head/custom.html` (`Space Grotesk`).
- Custom CSS goes in `assets/css/brand.css`.
  Dark-mode color tokens and component styles for the widgets live at the top of `_includes/whatsnext_and_contact.html` under `:root` and `html.theme-dark`.

---

## Analytics

- Google Analytics **Measurement ID**: `G-351QZEBS4T`
  Snippet is already in `head/custom.html`.
  Check data in GA: https://analytics.google.com/

> GA only records on the production hostname unless you configure debug/preview.

---

## Deployment (GitHub Pages)

- Repo name matches the personal Pages pattern: `iamamitagarwal.github.io`.
- Settings → Pages → Build from branch `main` (root).
- Site auto-builds on push.

---

## Common tweaks

- **Move the What’s next tab a bit lower**: `.wnx-tab { top: 110px; }` → bump the pixel value.
- **Panel clips under the header**: raise `.wnx-panel { top: 96px; }`.
- **Modal feels too tall**: lower `.contact-card { max-height: ... }` (e.g., `82vh`).

---

## Troubleshooting

- Widget missing? Make sure `_includes/footer/custom.html` contains:
  ```liquid
  {% raw %}{% include whatsnext_and_contact.html %}{% endraw %}
  ```
- White text in light mode? You likely deleted the CSS tokens at the top of `whatsnext_and_contact.html`. Restore the `:root` and `html.theme-dark` blocks.
- Avatar still tiny? The theme might be inserting inline sizes. Keep the `!important`s above and ensure the image source is actually large.
- Toggle not visible? The masthead query in the toggle script looks for `.masthead .greedy-nav`. If you ever change the header markup, update the selector and re-insert the button near `.search__toggle`.

---

## Notes to future-you

- The right-rail **remembers** open/closed on desktop. If you’re testing “fresh” behavior, clear site data or run in a private window.
- The contact modal’s **actions** stick to the bottom so users don’t have to scroll to hit Send.
- Dark-mode applies site-wide (headers, body, syntax, footer) using the extra CSS in `head/custom.html`. If a component stays light, give it a `html.theme-dark ...` rule.

---

## License

- Content (text, images): © Amit Agarwal.
- Code customizations in this repo: MIT unless noted.
- Minimal Mistakes: see the theme’s license.
