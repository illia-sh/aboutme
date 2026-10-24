# Illia Shpak - personal page

A static portfolio hosted on GitHub Pages. No build step is required.

## Local preview

Run `python3 -m http.server 8000` from this directory, then open `http://localhost:8000`.

## Files

- `index.html`: content, navigation, and sharing metadata.
- `style.css`: responsive layout, contrast, focus styles, and reduced-motion support.
- `script.js`: progressive mobile navigation and the copyright year.
- `profile.jpg`: existing portrait.
- `illia-shpak-cv.pdf`: two-page CV covering role scope, achievements, technical capabilities, and products built, compiled from the original public page.
- `social-preview.png` and `social-preview.svg`: sharing card and editable source.
- `favicon.svg`: browser icon.

The page works without JavaScript, including navigation and all outcome metrics.

After changing CSS or JavaScript, update its version query string in `index.html` so returning visitors load the current asset.

To regenerate the CV, install `reportlab` and `pypdf` in a Python environment and run `python3 scripts/build_cv.py`. This is an optional maintenance command; hosting the site needs no Python dependencies. The social card can be edited in `social-preview.svg` and exported to a 1200 x 630 PNG.

## Content maintenance

Keep the CV, page, and social preview consistent when experience changes. The CV is an experience summary based on the public page.

Before adding availability figures, specify the service and measurement window. Before adding a savings rate, specify whether the figure is annual, monthly, or a one-time total. Credential names do not imply a currently verified certification status.

## Publishing

The canonical and social-image URLs assume GitHub Pages at `https://illia-sh.github.io/aboutme/`. Update them if the domain changes. The existing Google Analytics property is retained.
