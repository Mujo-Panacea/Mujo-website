# Mujo Website — Current Sitemap & Disposition

**Version:** 0.1 · **Date:** July 2026 · **Status:** Draft for Review · **Owner:** Mujo Panacea Ltd

**Purpose:** Phase 1 audit output. Every current URL on [mujofitness.com](https://mujofitness.com), captured via the WordPress REST API on 2026-07-31, with a proposed disposition and target path on the new site. This document, once approved, drives Phase 3 content migration and the 301-redirect map at Phase 5 cutover.

## Sources

Data was pulled from the live WordPress REST API — the API is public and returned everything without needing admin credentials:

* Pages — `GET /wp-json/wp/v2/pages?per_page=100` — 40 pages, 1 page of results
* Posts — `GET /wp-json/wp/v2/posts?per_page=100` — 42 posts, 1 page of results
* Categories — `GET /wp-json/wp/v2/categories?per_page=100` — 12 categories
* Tags — `GET /wp-json/wp/v2/tags?per_page=100` — 0 tags (unused)
* Media — 162 media items across 2 pages (not yet pulled — deferred to Phase 3)

Raw JSON is stored in `docs/audit/*.json` for reference.

Live site chrome (nav, footer, analytics, partner logos, embedded widgets) was captured from a fetch of the homepage on the same date.

## Site Chrome (Current)

| Element | Detail |
| --- | --- |
| Primary nav | Treatments · Technology · Evidence · Consulting · News · About us · Book Now |
| Footer nav | Adds Home · Research · Blog · FAQs · Terms · Privacy · Contact Us · Employers · Health Care Providers · Individuals · **My Portal** |
| Social | Facebook · Twitter · LinkedIn · Instagram |
| Analytics | Universal Analytics `UA-73890747-1` (Google deprecated UA in 2023 — **not collecting current data**) |
| Cookie banner | "GDPR Cookie Compliance" plugin, three-category (Strictly Necessary, 3rd Party / GA, functional) |
| Embedded widgets | Instagram feed (9 posts, mostly stale), Twitter widget (fragile since X rename), no video / booking widgets |
| Partner logos on home | NHS RNOH · Circle · EIOS (English Institute of Sport) · HERC · Lumeon · BEEAS · Coventry University · Innovate UK · Broca Group · University of Manchester · IP100 2017 · IET |
| Broken content | `placeholder.png` used on an Instagram embed with orphaned alt text — visible artefact of a broken plugin |

**Notable finds:**

* "My Portal" in the footer is (or will be) the clinician dashboard login. Confirmed 2026-07-31. Retain the link on the new site; final destination URL to be provided when the clinician-facing dashboard is ready. If it is not yet ready at cutover, either point it at a lightweight "Portal — coming soon" holding page or remove the link until launch. Do not ship a broken link.
* Universal Analytics is dead. No live analytics on the site since mid-2023. This changes the "carry over analytics" decision — there is effectively nothing to carry over.
* Twitter widget will likely need removing regardless of the rebuild — the free widget API is unstable post-2023.

## Disposition Legend

| Code | Meaning |
| --- | --- |
| **KEEP** | Retain as a first-class page, refresh content, likely same or similar URL |
| **MERGE** | Fold content into another page; original URL 301-redirects to the merged page |
| **BLOG** | Move to blog/library, likely with new URL under `/blog/`, `/news/` or `/evidence/` |
| **KILL** | Remove entirely; 301 to closest relevant page (or home if nothing fits) |
| **REVIEW** | Content or purpose unclear from the audit alone — need your input |

## Pages — Top-Level (17)

| ID | URL | Words | Disposition | Target Path | Notes |
| --- | --- | ---: | --- | --- | --- |
| 311 | /home | 1804 | **KEEP** | `/` | Full rewrite. Refocus around Mujo 1.5 clinical release + 2.0 KTP programme. Replace stale partner slider content. |
| 442 | /technology | 705 | **KEEP** | `/technology` | Rewrite. Absorb `/devices` (see below). Drop stale "dashboard and predictive model" claim unless still true. |
| 466 | /evidence | 64 | **MERGE** | `/evidence/` | Currently a stub. Rebuild as the index page for the Evidence blog category (clinical papers, third-party reviews). |
| 75 | /news | 66 | **MERGE** | `/news/` | Currently a stub. Rebuild as the index page for the News blog category. |
| 463 | /blog | 93 | **MERGE** | `/blog/` | Currently a stub. Rebuild as the index page for the Blog category (educational content). |
| 636 | /research | 169 | **KILL** | 301 → `/evidence` | Confirmed 2026-07-31. Both children go (see below). Any residual value in the parent copy folds into `/evidence` or `/technology` at Phase 3. |
| 432 | /treatments | 1133 | **KEEP** | `/treatments` | Rewrite as landing that lists conditions treated with links to per-condition pages (consolidated — see MERGE rows below). |
| 452 | /audience | 354 | **KILL** | 301 → `/` | Weak audience-splitter page. Modern IA handles this via content rather than a page. |
| 929 | /consulting | 200 | **KILL** | 301 → `/` | Confirmed 2026-07-31 — no longer offered. |
| 137 | /faqs | 391 | **KEEP** | `/faqs` | Confirmed 2026-07-31. Rewrite the FAQ content and add clear "contact us" language throughout — every question should nudge unresolved cases to `/contact`. |
| 454 | /about-us | 896 | **KEEP** | `/about` | Rewrite. Reflect current company posture (KTP programme, ISO 13485 direction, current team). |
| 1402 | /why-us | 529 | **MERGE** | `/` (into home) | Marketing copy that belongs in the home page value proposition, not its own page. |
| 126 | /contact | 353 | **KEEP** | `/contact` | Refresh. Point form to gerard@panacea.ws until a dedicated inbox is set up. |
| 691 | /book-free-taster | 499 | **KILL** | 301 → `/contact` | Confirmed 2026-07-31 — the free-taster offer is no longer valid. Any residual CTA on other pages must be removed at Phase 3. |
| 1837 | /booking | 341 | **MERGE** | `/contact` | Duplicate of book-free-taster. Consolidate. |
| 2734 | /privacy-policy | 1247 | **KEEP** | `/privacy` | Legal review required — must reflect current data flows (analytics, form intake, any tablet/backend data). |
| 1496 | /terms-and-conditions | 1496 | **KEEP** | `/terms` | Legal review required. |

## Pages — Treatments (5, all children of /treatments)

Currently duplicated with `/research/conditions/*` — see below. Consolidate to one page per condition.

| ID | URL | Words | Disposition | Target Path | Notes |
| --- | --- | ---: | --- | --- | --- |
| 1263 | /treatments/frozen-shoulder | 2258 | **MERGE** | `/treatments/frozen-shoulder` | Consolidate with `/research/conditions/frozen-shoulder-contracture-syndrome` (3499w). Keep this URL as canonical. |
| 1267 | /treatments/shoulder-impingement | 1700 | **MERGE** | `/treatments/shoulder-impingement` | Consolidate with `/research/conditions/shoulder-impingement-syndrome` (5699w). Keep this URL as canonical. |
| 1964 | /treatments/shoulder-instability | 671 | **KEEP** | `/treatments/shoulder-instability` | No duplicate in `/research/conditions`. Refresh only. |
| 1265 | /treatments/upper-back-and-neck-pain | 742 | **MERGE** | `/treatments/upper-back-and-neck-pain` | Consolidate with `/research/conditions/upper-back-and-neck-pain` (640w, same slug!). |
| 1428 | /treatments/enquire | 166 | **KILL** | 301 → `/contact` | Duplicate contact form. |

## Pages — Technology (2, all children of /technology)

| ID | URL | Words | Disposition | Target Path | Notes |
| --- | --- | ---: | --- | --- | --- |
| 444 | /technology/devices | 344 | **MERGE** | `/technology` | Fold into parent Technology page. Also update to describe Mujo 1.5 hardware baseline and 2.0 direction. |
| 448 | /technology/dashboard-and-predictive-model | 95 | **KEEP** | `/technology/dashboard-and-predictive-model` | Confirmed 2026-07-31 — the dashboard + predictive model will be a future offering. Rewrite required: language must shift from "we have this" to "we are building this" and align with the Mujo 2.0 roadmap. Do not overstate — regulatory review applies. |

## Pages — Audience (3, all children of /audience — parent itself proposed KILL)

| ID | URL | Words | Disposition | Target Path | Notes |
| --- | --- | ---: | --- | --- | --- |
| 766 | /audience/employers | 171 | **KILL** | 301 → `/` | Thin content aimed at a category we don't primarily sell to. |
| 756 | /audience/health-care-providers | 225 | **KILL** | 301 → `/treatments` | Content properly belongs in Treatments-facing copy. |
| 770 | /audience/individuals | 263 | **KILL** | 301 → `/treatments` | Same — patient-facing copy folds into Treatments. |

## Pages — About Us → Team (1 index + 7 bios)

Individual bios are all 150–500 words and sparse. Recommend consolidating to a single Team page with bio cards; do not spend the maintenance overhead on 7 separate URLs.

| ID | URL | Words | Disposition | Target Path | Notes |
| --- | --- | ---: | --- | --- | --- |
| 849 | /about-us/our-team | 524 | **KEEP** | `/about/team` | Rebuild around the current team (see below). Only one of the previous seven bios carries over. |
| 938 | /our-team/jeff-mcbride | 186 | **MERGE** | `/about/team#jeff-mcbride` | Confirmed 2026-07-31 — Jeff McBride is the only carry-over from the previous team. Refresh bio content, keep anchor. |
| 893 | /our-team/douglas-higgins | 172 | **KILL** | 301 → `/about/team` | Confirmed 2026-07-31 — no longer involved. |
| 934 | /our-team/dr-asim-i-bhuta | 206 | **KILL** | 301 → `/about/team` | Confirmed 2026-07-31 — no longer involved. |
| 936 | /our-team/dr-hichem-ben-hamida | 208 | **KILL** | 301 → `/about/team` | Confirmed 2026-07-31 — no longer involved. |
| 912 | /our-team/geri-mcmahon | 207 | **KILL** | 301 → `/about/team` | Confirmed 2026-07-31 — no longer involved. |
| 943 | /our-team/professor-alison-mcgregor | 158 | **KILL** | 301 → `/about/team` | Confirmed 2026-07-31 — no longer involved. |
| 946 | /our-team/susanna-everitt-frcgp | 183 | **KILL** | 301 → `/about/team` | Confirmed 2026-07-31 — no longer involved. |

**Current team to feature on `/about/team`** (confirmed 2026-07-31):

* **Gerard Kool** — CEO
* **Michael Sasserini** — CFO
* **Andre Santos** — Chief Medical Officer
* **Jeff McBride** — (existing role — confirm at Phase 3)

Bios and photos for the three new team members are a Phase 3 content deliverable — Gerard to supply.

## Pages — Research (2 index + 3 condition pages, parent proposed REVIEW)

| ID | URL | Words | Disposition | Target Path | Notes |
| --- | --- | ---: | --- | --- | --- |
| 645 | /research/conditions | 302 | **KILL** | 301 → `/treatments` | Category index whose children merge into Treatments. Confirmed 2026-07-31. |
| 1168 | /research/device-development | 97 | **KILL** | 301 → `/technology` | Ghost page. Confirmed 2026-07-31. |
| 426 | /research/conditions/frozen-shoulder-contracture-syndrome | 3499 | **MERGE** | `/treatments/frozen-shoulder` | Duplicate of `/treatments/frozen-shoulder`. Content depth (3499w) makes this the likely canonical source; port the good bits into the merged page. |
| 428 | /research/conditions/shoulder-impingement-syndrome | 5699 | **MERGE** | `/treatments/shoulder-impingement` | Duplicate of `/treatments/shoulder-impingement`. Longest page on the site (5699w) — depth is here, not on the shorter Treatments version. |
| 430 | /research/conditions/upper-back-and-neck-pain | 640 | **MERGE** | `/treatments/upper-back-and-neck-pain` | Slug clash with `/treatments/upper-back-and-neck-pain` — WP resolves by parent, but confuses users and search engines. Consolidate. |

## Posts (42 total)

Content is heavily dated — **the newest post is 2018-07-10**. Nothing has been published in 8 years. Category distribution:

| Category | Post count |
| --- | ---: |
| News | 25 |
| Blog | 13 |
| Evidence | 3 |
| education (subset of Blog) | 3 |
| Frozen Shoulder / Shoulder Impingement / Shoulder Pain / Tips (topical tags on Blog posts) | 12 overlapping |
| Guest Interviews | 1 |
| Conditions / Device Development / Research | 0 posts |

**Disposition confirmed 2026-07-31:** keep all 42 posts for now. Reshape the site around the sitemap changes above first; a proper cull of dated news and a refresh of the blog will happen after cutover once the new IA is in place.

Practical implications for Phase 3:

* All 42 posts migrate to the new site as blog / news / evidence entries with dates preserved.
* Show original publication dates prominently — the reader can then judge for themselves what is dated. Do not silently backfill 2026 dates onto 2015 content.
* Retire the four zero-post categories (`Conditions`, `Device Development`, `Research`) — they add noise. The remaining categories consolidate down to something like: **News**, **Blog**, **Evidence**, plus the topical tags currently used (Frozen Shoulder, Shoulder Impingement, Shoulder Pain, Tips, Guest Interviews).
* Per-post disposition (`docs/audit/posts-disposition.md`) is not needed for the initial rebuild since we are keeping everything. Deferred as post-launch cleanup.

## Missing / Unknown

Items surfaced by the audit that aren't cleanly resolved by the REST API pull:

* **"My Portal"** footer link — destination and status unknown. Is this a live customer portal, a legacy staff portal, or a dead link?
* **Media library** (162 items) — not yet indexed. Will do this in Phase 3 when we know which pages need which images.
* **Contact form destination** — the current form's mailto / plugin backend is opaque from the outside. Confirm nothing is being missed when we replace it.
* **Google Search Console / sitemap.xml** — do we have access to Search Console for the domain? Determines whether we can see current head-term traffic and 404 rates.
* **Redirect table** — the WP site may already have redirects configured via Redirection or another plugin. Worth checking before we build the new redirect map so we don't lose existing redirects.

## Proposed New Sitemap (Summary)

Based on the dispositions above, the new site collapses to roughly this shape. Final URLs subject to your review.

```
/                                                        (Home — full rewrite)
/technology                                              (Product + hardware overview)
  /technology/dashboard-and-predictive-model             (Future offering, roadmap language)
/treatments                                              (Conditions landing)
  /treatments/frozen-shoulder
  /treatments/shoulder-impingement
  /treatments/shoulder-instability
  /treatments/upper-back-and-neck-pain
/evidence                                                (Clinical evidence library index)
/blog                                                    (Educational content index)
/news                                                    (Press / milestones index)
/faqs                                                    (Refreshed, with contact-us CTAs)
/about                                                   (Company)
  /about/team                                            (All bios on one page, anchored)
/contact                                                 (Single enquiry surface)
/privacy
/terms
```

That is **~11 core pages + 3 content indexes + a growing blog/evidence/news post list**, down from 40 pages currently. Consistent with the "10–15 pages after rationalisation" estimate in [requirements.md](requirements.md).

## Decisions Requested Before Phase 2

Resolved 2026-07-31:

* ~~`/research` → KILL (301 → `/evidence`)~~ ✔
* ~~`/consulting` → KILL~~ ✔ (service no longer offered)
* ~~`/faqs` → KEEP with rewrite + contact-us language~~ ✔
* ~~`/book-free-taster` → KILL~~ ✔ (offer no longer valid; strip residual CTAs elsewhere)
* ~~`/technology/dashboard-and-predictive-model` → KEEP with language change~~ ✔ (future offering; align with 2.0 roadmap; regulatory-safe wording)

Also resolved 2026-07-31:

* ~~Team page — current team is Gerard Kool (CEO), Michael Sasserini (CFO), Andre Santos (CMO), Jeff McBride~~ ✔ (bios + photos to be supplied at Phase 3)
* ~~My Portal — clinician dashboard access, retain link, final destination URL TBD~~ ✔
* ~~Approach to old news — keep everything for the rebuild, revisit post-launch~~ ✔

**Phase 1 audit is closed.** Ready to move to Phase 2 (framework + repo setup) once you're happy with the current state of [requirements.md](requirements.md), [sitemap.md](sitemap.md) and [checklist.md](checklist.md).
