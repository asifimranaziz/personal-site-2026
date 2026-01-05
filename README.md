# Personal Website

Static site built with Hugo for personal data projects and CV hosting.

## Setup

1. Install Hugo: Download from https://gohugo.io/getting-started/installing/

2. Clone or copy this repo.

3. Run `hugo server` to preview locally.

4. Run `hugo` to build static files to `public/`.

## Hosting

Deploy `public/` to GitHub Pages, Vercel, or any static host.

For GitHub Pages: Push to `username.github.io` repo, enable Pages from `gh-pages` branch or root. Workflow included for auto-deploy.

## Design

Calm, minimal CSS inspired by nekozenworld.jp: clean typography (Inter font), generous spacing, soft accent colors (blue, green, orange), WCAG AA accessibility, responsive, with optional dark mode support.

## CV Updates

Edit `content/cv/_index.md`.

Generate PDF: `pandoc content/cv/_index.md -o static/cv.pdf`

Generate text: `pandoc content/cv/_index.md -t plain -o static/cv.txt`

## Data Analysis

Use Jupyter notebooks in `notebooks/` for ETL and analysis:
- `health_analysis.ipynb`: Health data processing and viz.
- `wealth_analysis.ipynb`: Financial tracking.
- `life_analysis.ipynb`: Life balance metrics.

Run locally with Jupyter. Export results to update site viz.

## Extension

- Add projects: Create new dirs in `content/projects/`, add `_index.md` with viz and TODOs.

- Update CV: Edit `content/cv/_index.md`, regenerate PDF/text as needed.

- Data processing: Run Python scripts locally, output JSON/CSV to `static/data/`, load in JS.

- AI insights: Integrate API calls in JS or pre-generate.

## Stack Choice

Hugo: Simple static generator, minimal config, fast builds, supports Markdown + custom layouts. Chosen for ease, no backend needed, good for data viz via JS.