# Copilot Instructions for Personal Website Development

## Project Overview
This is a personal website for a Senior Product Manager, serving as a tool for data projects (health, wealth, life metrics) and hosting an accessible CV. Built with Hugo static site generator, deployed on GitHub Pages.

## Core Goals
- **Primary:** Personal decision-support tool for data analysis and insights.
- **Secondary:** ATS-friendly CV hosting.
- **Non-goals:** Personal background, blog, overengineering.

## Tech Stack
- **Generator:** Hugo (static site)
- **Styling:** Vanilla CSS (calm, minimal, inspired by nekozenworld.jp)
- **Data Viz:** Plotly.js for interactive charts
- **Data Processing:** Python/Jupyter notebooks (local ETL)
- **Hosting:** GitHub Pages with CI/CD
- **Accessibility:** WCAG AA compliant

## File Structure
```
/
├── config.toml              # Site config (baseURL, title)
├── content/                 # Markdown content
│   ├── _index.md           # Home page
│   ├── cv/_index.md        # CV content
│   └── projects/           # Data projects
│       ├── _index.md       # Projects list
│       └── health/_index.md # Individual projects
├── layouts/_default/       # HTML templates
│   ├── baseof.html         # Base layout with nav
│   ├── single.html         # Single page template
│   └── list.html           # List page template
├── static/                 # Static assets
│   ├── css/style.css       # Main stylesheet
│   ├── cv.pdf              # Generated CV PDF
│   └── cv.txt              # Plain text CV
├── notebooks/              # Jupyter analysis notebooks
├── .github/workflows/      # CI/CD for deployment
└── README.md               # Setup and docs
```

## Content Guidelines
- **Tone:** Crisp, factual, no fluff.
- **CV:** Structured sections (Experience, Qualifications, Skills), bold roles, italic dates, bullet points. Update one source file, generate PDF/text separately.
- **Projects:** Each has overview, viz (Plotly), AI insights placeholder. Add incrementally.
- **Home:** Brief intro to purpose.

## Styling Principles
- **Colors:** High contrast text, soft accents (blue #3498db, green #27ae60, orange #e67e22), auto dark mode.
- **Typography:** Inter font, generous spacing, strong hierarchy.
- **Layout:** Container max-width 800px, responsive (mobile-first).
- **Accessibility:** Semantic HTML, skip links, focus styles, ARIA where needed.
- **Navbar:** Sticky header with site title left, links right.

## Development Workflow
1. **Local Development:** `hugo server` for preview.
2. **Content Edits:** Update Markdown in `content/`.
3. **Styling:** Modify `static/css/style.css`.
4. **Data Projects:** Run Jupyter notebooks locally, export viz data to JS.
5. **CV Updates:** Edit `content/cv/_index.md`, regenerate formats with pandoc.
6. **Commit & Deploy:** Push to main triggers GitHub Actions build/deploy.

## Extension Patterns
- **New Projects:** Create `content/projects/newproject/_index.md` with viz and TODOs.
- **Custom Pages:** Add to `content/` with frontmatter.
- **Backend Needs:** Avoid unless necessary; keep static.
- **AI Integration:** Pre-generate insights or use client-side APIs.
- **Testing:** Check accessibility with WAVE, responsiveness manually.

## Key Constraints
- Prefer simplicity over complexity.
- Maintain WCAG AA.
- No frameworks (vanilla CSS/JS).
- One source for CV, generate variants.
- Personal tool first, external CV second.

## Deployment
- Repo: https://github.com/asifimranaziz/personal-site-2026
- Live: https://asifimranaziz.github.io/personal-site-2026/
- Workflow: Auto-build on push to main, deploy to gh-pages.

Use this guide for consistent development, prioritizing maintainability and user experience.