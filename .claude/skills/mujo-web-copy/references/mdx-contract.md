# MDX contract

The real content model of the `Mujo-website` repo, verified from the repository in August 2026. Copy delivered in this shape drops straight into the build; copy delivered as prose creates work for someone else.

**Repo:** `Mujo-website`, GitHub organisation `Mujo-Panacea`. On Gerard's machine usually `~/Documents/GitHub/Mujo-website`; through the device bridge the mounted path is `$HOME/mnt/<folder>/Mujo-website`. If the expected path misses, list the mount root rather than guessing.
**Stack:** Astro (static) · Markdown/MDX in repo · Netlify · Netlify Forms. No CMS — content is versioned with the code. Decap CMS is the intended later layer if browser editing becomes a need.

**Working rule:** read the current file before rewriting it. Match its imports, component usage and heading levels. Never invent a component.

**Where the repo and this file disagree, the repo wins** — with one exception. Follow the repo on entities (`&mdash;`, `&amp;`), on product-version naming (the repo writes "Mujo 1.5" and "Mujo 2.0" with a lowercase j, against the brand's "MuJo"), and on layout conventions. Do *not* follow the repo on the phrases listed under "Already live — do not propagate" in `voice-and-brand.md`; those are known defects, not house style.

## Marketing pages

Live at `src/pages/**`. One `.mdx` file per page; the file path is the URL.

```mdx
---
layout: ../layouts/PageLayout.astro
title: "For Athletes"
description: "MuJo for athletic performance and post-injury shoulder rehabilitation — used by the English Institute of Sport, Wasps Rugby, and GB Weightlifting."
brand: "sports"
---

import ReviewBanner from '../components/ReviewBanner.astro';
import MediaRow from '../components/MediaRow.astro';

<ReviewBanner>What still needs sign-off before this page goes public.</ReviewBanner>

Opening paragraph — no H1. The layout renders `title` as the H1 and
`description` as the lede, so the body starts at H2.
```

| Field | Notes |
| --- | --- |
| `layout` | `../layouts/PageLayout.astro` for standard pages. Adjust depth for nested pages (`../../layouts/…`). |
| `title` | Rendered as the page H1 **and** as the browser title. Sentence case. Keep it short — it has to work in both places. |
| `description` | Rendered as the on-page lede **and** as the meta description. This is the single highest-leverage sentence on any page: it is what appears in search results and what the reader sees under the headline. Aim 120–155 characters, lead with the substantive noun, include a checkable specific. |
| `brand` | Optional. `"sports"` switches the page to Elite Sports Blue via `data-brand` on `<html>`. Omit for the default Medical & Rehabilitation mint. |

**Do not write an H1 in the body.** The layout supplies it. Body content starts at `##`.

## Components

Only these exist. Import them explicitly in the MDX file.

| Component | Use |
| --- | --- |
| `ReviewBanner` | Wraps a note about what is unresolved on the page. Use it for anything needing Gerard's, Andre's or a solicitor's sign-off, so the flag travels with the page. **Write it as one short paragraph — the component only styles `<p>`, and a markdown list inside it inherits the prose list size and renders oversized inside the small banner box.** Semicolons, not bullets. |
| `MediaRow` | Alternating text/image band. Props: `image` (path), `alt` (required), `flip` (reverses order), `background` — `"white"` for product shots already on white, `"subtle"` for photographic/clinical/sports scenes, `"grey"` for a high-contrast inverted callout. Markdown headings and copy go inside as children. |
| `Partners` | Institution logo strip. |
| `PostCard` | Evidence/resource card. |
| `ContactForm` | Netlify Forms with honeypot; posts to `/contact/thanks/`. |
| `Header`, `Footer` | Chrome — not used directly in page content. |

## Content collections

Defined in `src/content/config.ts`. Frontmatter must validate against these schemas or the build fails.

**`posts`** — `src/content/posts/*.{md,mdx}`, powering `/evidence/<slug>` and `/resources/<slug>`.

```yaml
title: string                 # required
description: string           # required
publishedDate: date           # required
updatedDate: date             # optional
category: evidence | resources  # required — this alone routes the post
tags: string[]                # default []
author: string                # default "MUJO Panacea"
heroImage: string             # optional, /images/posts/<slug>/...
archived: boolean             # default false
legacyId: number              # optional — WordPress post ID
legacyUrl: url                # optional — original URL, keep for provenance
```

**`team`** — `src/content/team/*.md`.

```yaml
name: string        # required
role: string        # required
order: number       # required — display order
photo: string       # optional, /images/team/<slug>.png
linkedin: url       # optional
summary: string     # optional — one line, used on the card
```

Body is the full bio, 80–120 words.

**`partners`** — `src/content/partners/*`. `name`, `logo` (an image reference, not a string path), optional `url`, `order` (default 999), `active` (default true).

## Conventions

- **Images** live under `public/images/`: `/images/posts/<slug>/…`, `/images/team/…`, `/images/site/…`. Alt text is required on every image — WCAG 2.1 AA is a stated non-functional requirement of the rebuild. **Write alt text only for an image you have actually looked at.** If you are placing an image from the manifest below without viewing it, say so in the handover so someone checks the alt text rather than trusting a guess on an accessibility-critical field.

  Available in `public/images/site/` as of August 2026: `audience-medical.jpg` · `audience-medical-physio.jpg` · `audience-sport.jpg` · `audience-sport-athlete.jpg` · `mujo-clinical.jpg` · `mujo-device-1.jpg` · `mujo-device-5.jpg` · `mujo-device-10.jpg` · `mujo-tablet-mockup.png` · `reporting.jpg`. Team portraits in `public/images/team/` (four named PNGs plus `placeholder-avatar.svg`); partner logos in `public/images/partners/` (RNOH, EIOS, Circle, Coventry, Manchester, Innovate UK, HERC, IET).
- **Internal links** use trailing slashes: `/about/team/`, `/contact/`, `/evidence/`.
- **Entities:** the existing files use `&mdash;` and `&amp;` in MDX. Follow whatever the file already does.
- **Legacy URLs:** every retired WordPress path has a 301. If a rewrite changes a URL, the redirect map in the repo needs updating too — say so rather than assuming someone will notice.
- **`noindex` is currently on every page.** Nothing is crawlable until cutover, so search-visibility work is preparation, not live optimisation.
- **Dates** are ISO (`2026-08-19`) and are coerced to dates by the schema — don't quote them as strings with month names.

## Delivering copy

Write the finished file to its repo path so it can be reviewed in place or diffed, rather than pasting prose into chat. If the page is new, say where the file goes and whether the nav, sitemap doc or redirect map needs a corresponding change.

For a review rather than a rewrite, deliver a prioritised list where each item names the file, quotes the current wording, gives the exact replacement, and says why. General advice about tone is not actionable.
