# Raghava Gatadi — Application Security Portfolio

[Live site](https://raghava-gatadi.github.io/Portfolio/)

A static, accessible portfolio focused on web and API security, source review, security automation, and software supply-chain contributions. Hosted at the existing GitHub Pages project URL.

## Develop locally

No Node.js, package manager, build process, external fonts, or runtime CDN is required.

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. Python 3.9+ serves the site; the checker requires Python 3.9+.

```sh
python3 tools/check_site.py
```

The checker validates local links and fragments, assets, unique headings and IDs, metadata, sitemap coverage, and compatibility with the static CSP. The same check runs on pull requests and main-branch pushes. Browser checks should cover the homepage review steps, writing filters/search/empty results, native mobile menu, keyboard focus, and representative long-form articles.

## Structure

- `index.html`: introduction, selected projects, experience, writing, about, and contact.
- `assets/css/site.css`: shared design tokens, responsive layouts, article styles, reduced-motion and print styles.
- `assets/js/site.js`: progressive enhancements for the review illustration, writing search/filtering, and mobile menu dismissal.
- `pages/writing.html`: the full searchable archive. All notes remain visible when JavaScript is unavailable.
- `pages/projects.html`, `pages/research.html`, `pages/certifications.html`, `pages/contact.html`: supporting pages.
- `projects/appsec-assistant.html`: source-review tooling case study.
- `posts/`: the 12 original article URLs, preserved with the shared design.
- `sitemap.xml`, `.nojekyll`: GitHub Pages metadata.

All site resources use relative paths so the `/Portfolio/` project prefix works. To add an article, copy an article shell, give it a unique title/description/canonical URL, add an archive row, and update `sitemap.xml`. Keep the shared header/footer consistent between pages. Verify claims and ownership before publication. Keep training, employment, research, and collaborative contributions distinct. Label illustrative code clearly.

The current site uses the existing public portrait, optimized as WebP. Social previews are local static artwork. Credential verification uses ordinary links to Credly, without embedded scripts or iframes. There are no analytics, tracking, forms, or third-party runtime requests.

## Resume

The historical PDF is retained in the repository for continuity, but the site links to an email request for a current resume. The historical document contains outdated availability and retired metrics and should be replaced only after a current resume is reviewed. Do not restore its download link as-is.

## Publishing

The site is ordinary static HTML and remains compatible with the repository’s existing GitHub Pages deployment. Serve the repository root from the selected Pages branch. No framework hosting, environment variables, secrets, or new service accounts are needed. Before merging, run the checker and inspect desktop/mobile layouts. A previous design remains recoverable in Git history.
