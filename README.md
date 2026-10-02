# Naufal Azmi Alghifari — Portfolio

Static developer portfolio served from `index.html`. No server or JavaScript
framework is required: open the file in a browser or deploy the repository to
any static host (for example GitHub Pages).

## Project structure

```
index.html                 Page markup, inline icon sprite, and page scripts
src/styles.css             Tailwind source (base styles and shared components)
tailwind.config.js         Design tokens (colors, radius, spacing, fonts)
assets/css/styles.css      Compiled, minified stylesheet that the page loads
assets/certificates/       Certificate files and lightweight WebP previews
assets/favicon.svg         Site icon
tests/test_portfolio.py    Dependency-free page contract tests
```

## Editing styles

The page loads a precompiled stylesheet instead of the Tailwind Play CDN, so it
renders instantly without runtime JavaScript. After adding or changing Tailwind
classes in `index.html` or `src/styles.css`, rebuild the stylesheet:

```sh
npm install
npm run build      # one-off minified build
npm run dev        # rebuild automatically while editing
```

Commit the regenerated `assets/css/styles.css`; CI fails if it is out of date.

## Tests

Run the dependency-free page contract suite with:

```sh
python3 -m unittest discover -s tests -v
```

The suite validates internal navigation targets and unique element IDs,
external link protection, the CV request action, the published certificate
assets and previews, accessible social links, the mobile-menu state, a single
`h1` with ordered headings, SEO metadata, image alt text and dimensions, icon
sprite references, and that no runtime CDN scripts are loaded.
