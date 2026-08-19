# CLAUDE.md — Mujo-website

Marketing and content site for **MuJo Panacea Ltd**. Astro static site, Markdown/MDX content in-repo, deployed on Netlify. This replaces the legacy WordPress site at mujofitness.com. Staging is `beta.mujofitness.com`; `noindex` is on every page until cutover.

## Read this before writing copy

Content work on this repo is governed by the **`mujo-web-copy` skill** at `.claude/skills/mujo-web-copy/`. Read its `SKILL.md` before drafting, rewriting or reviewing any page copy, headline, meta description, bio, FAQ answer or evidence write-up — even for a one-line change. It carries the verified fact register, the regulated-claims boundary, the brand voice and this repo's MDX conventions.

Three standing rules, which the skill explains in full:

1. **Do not state a fact about MUJO from memory or from the legacy WordPress site.** Check `references/company-facts.md`. It rates every fact `Verified` / `Site-stated` / `Contradicted`, and section 10 lists seven open contradictions that must not appear in copy until Gerard settles them. Much of the old site is now wrong in ways that matter.

2. **This is a regulated medical device company.** Measurement and capability language is safe; therapeutic and outcome language is not, for any product without conformity marking for that claim. Mujo 2.0 is not CE or UKCA marked and appears only in future tense. See `references/claims-guardrails.md`.

3. **`/investors` carries live financial-promotion risk.** The page states a raise amount, equity and valuation on an open page, which engages s21 FSMA 2000 and s755 Companies Act 2006. Do not extend or restyle that content without reading `claims-guardrails.md` §7. Flag it, don't fix it.

**Statistics:** every figure needs its source, the year the data refers to, and its true scope. `references/evidence-library.md` has the verified set and the trap in each, plus a list of figures MUJO does *not* have — consult it rather than reaching for a plausible number.

## Keeping the fact register current

`references/company-facts.md` is a living document. When a contradiction gets resolved, a permission is granted, a date is confirmed or a regulatory position changes, **update the register in the same commit as the copy change.** A stale register is worse than none, because it gets trusted.

Its source material — Confluence, Google Drive, the 2015 brand guidelines — is not reachable from this machine. Refreshes from source happen in a Cowork session with those connectors; this repo holds the authoritative copy. `.claude/skills/mujo-web-copy.skill` is a packaged snapshot for re-installing to a Claude account; repackage it if the skill changes materially.

## Commands

```bash
npm install
npm run dev      # astro dev
npm run build    # astro build — run before committing content changes
npm run preview
```

## Layout

| Path | Contents |
| --- | --- |
| `src/pages/**` | Marketing pages, one `.mdx` per URL. `PageLayout` renders `title` as H1 and `description` as the lede — do not write an H1 in the body. |
| `src/content/posts/` | Evidence and resource posts. `category` frontmatter routes them. |
| `src/content/team/`, `src/content/partners/` | Collections; schemas in `src/content/config.ts`. |
| `src/components/` | `ReviewBanner`, `MediaRow`, `Partners`, `PostCard`, `ContactForm`, `Header`, `Footer`. Do not invent components. |
| `public/_redirects` | 301 map for every legacy WordPress URL. Update it whenever a path changes. |
| `docs/requirements.md`, `docs/sitemap.md`, `docs/checklist.md` | Project source of truth. Confluence mirrors these; when they disagree, the repo wins. |

The header nav is a hardcoded array at the top of `src/components/Header.astro` — adding a page does not add it to the nav.

## Conventions

British English, metric, sentence-case headings, trailing slashes on internal links, ISO dates, `&mdash;` for em dashes to match existing files. Alt text on every image (WCAG 2.1 AA is a stated requirement). Anything needing sign-off from Gerard, Andre or a solicitor goes in a `<ReviewBanner>` on the page — one short paragraph, no lists — as well as in your reply.
