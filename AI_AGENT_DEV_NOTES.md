# AI Agent Development Notes

## Original User Requirements

**Core Purpose:**
- Build a personal site used primarily by its owner (a senior Product Manager) to:
  - Run personal data projects (health, wealth, life metrics)
  - Generate clear, actionable insights from those projects
  - Take real-world actions based on insights

**Secondary Purpose:**
- Host a highly accessible, ATS-friendly CV for external viewing

**Non-Goals:**
- Do not include personal background, relationships, health, or neuro info
- Add blog spam, thought leadership fluff, or marketing language
- Overengineer architecture or introduce unnecessary services
- Assume existing datasets (use placeholders)

**CV Requirements:**
- Renders an existing CV verbatim (content to be supplied later)
- Supports three formats: Web-first readable version, Downloadable PDF (ATS-friendly, clean, max 2 pages), Plain-text ATS version
- Is very easy to read for both humans and screen readers
- Has no salary history
- Is simple to update by editing one source file

**Projects & Data Work:**
- Create a Projects section with clear placeholders for future projects
- Each project supports: Python-based data processing, Interactive visualisation (charts/dashboards), AI-assisted insight summaries (e.g. "What this data suggests")
- Projects can be extended incrementally over time
- No real data yet — include dummy data and TODO markers only.

**Tech & Architecture:**
- Choose a simple, beginner-friendly stack and explain why it was chosen.
- Strong preferences: Easy to reason about, Minimal moving parts, Good design + UX defaults, Supports data visualisation, Allows optional protection of sensitive pages later
- May choose: Fully static generation or light backend …but default to simplest viable option.
- Also: Decide hosting (GitHub Pages, Vercel, etc.), Explain folder structure, Explain how the owner will extend it over time

**Design & Accessibility:**
- Visual style: minimal / brutalist + polished startup
- Tone: crisp, factual
- Accessibility: WCAG AA
- Keyboard navigable
- Screen-reader friendly
- No unnecessary animation

**Output Requirements:**
- Produce everything needed to run the site, except real project data
- File/folder structure, Core pages, CV scaffolding, Project placeholders, Basic styling, Clear comments and TODOs, Short setup instructions
- Do not: Explain obvious basics, Repeat requirements, Add long theory sections, Be concise and implementation-focused.

**Final Instruction:**
- If a tradeoff is required: Prefer simplicity over cleverness, Prefer clarity over flexibility, Prefer maintainability over abstraction

## Implementation Decisions

- **Stack:** Hugo static site generator
  - Why: Simple, minimal config, fast, supports Markdown, easy JS embedding for viz, no backend.
- **Hosting:** GitHub Pages with CI/CD.
- **Structure:** Standard Hugo layout with custom minimal templates.
- **Viz:** Plotly.js for interactive charts.
- **CV:** Markdown source, pandoc for PDF/text generation.
- **Accessibility:** Semantic HTML, skip links, ARIA labels.

## Future Extensions
- Add real data processing scripts in Python.
- Integrate AI APIs for insights.
- Add authentication if needed for sensitive pages.