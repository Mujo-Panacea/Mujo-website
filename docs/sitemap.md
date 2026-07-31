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

* "My Portal" in the footer implies a customer login area that isn't in the current nav. Needs investigation — is it active, deprecated, or a ghost link? Answer determines whether the new site links to it or not.
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
| 636 | /research | 169 | **REVIEW** | tbd | Sits above `/research/conditions` and `/research/device-development`. Both children look ghostly. Consider merging useful content into `/technology` or `/evidence` and killing the top-level. |
| 432 | /treatments | 1133 | **KEEP** | `/treatments` | Rewrite as landing that lists conditions treated with links to per-condition pages (consolidated — see MERGE rows below). |
| 452 | /audience | 354 | **KILL** | 301 → `/` | Weak audience-splitter page. Modern IA handles this via content rather than a page. |
| 929 | /consulting | 200 | **REVIEW** | tbd | Do you still offer consulting? If yes, KEEP + rewrite. If no, KILL. |
| 137 | /faqs | 391 | **REVIEW** | tbd | Content likely stale (2015-era). KEEP if the answers are still true after edit; KILL if not. |
| 454 | /about-us | 896 | **KEEP** | `/about` | Rewrite. Reflect current company posture (KTP programme, ISO 13485 direction, current team). |
| 1402 | /why-us | 529 | **MERGE** | `/` (into home) | Marketing copy that belongs in the home page value proposition, not its own page. |
| 126 | /contact | 353 | **KEEP** | `/contact` | Refresh. Point form to gerard@panacea.ws until a dedicated inbox is set up. |
| 691 | /book-free-taster | 499 | **REVIEW** | tbd | "Free intro session" — is this still an offer? If yes, KEEP as a CTA on `/contact` or `/treatments`. If no, KILL. |
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
| 448 | /technology/dashboard-and-predictive-model | 95 | **KILL** | 301 → `/technology` | 95-word ghost page. Claim is likely stale (no dashboard shipped). Confirm before final kill. |

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
| 849 | /about-us/our-team | 524 | **KEEP** | `/about/team` | Consolidate the seven bio sub-pages into this page as cards / expandable sections. |
| 893 | /our-team/douglas-higgins | 172 | **MERGE** | `/about/team#douglas-higgins` | Merge as anchor. |
| 934 | /our-team/dr-asim-i-bhuta | 206 | **MERGE** | `/about/team#dr-asim-i-bhuta` | Merge as anchor. |
| 936 | /our-team/dr-hichem-ben-hamida | 208 | **MERGE** | `/about/team#dr-hichem-ben-hamida` | Merge as anchor. |
| 912 | /our-team/geri-mcmahon | 207 | **MERGE** | `/about/team#geri-mcmahon` | Merge as anchor. |
| 938 | /our-team/jeff-mcbride | 186 | **MERGE** | `/about/team#jeff-mcbride` | Merge as anchor. Confirm still a current team member. |
| 943 | /our-team/professor-alison-mcgregor | 158 | **MERGE** | `/about/team#professor-alison-mcgregor` | Merge as anchor. Confirm still a current advisor. |
| 946 | /our-team/susanna-everitt-frcgp | 183 | **MERGE** | `/about/team#susanna-everitt-frcgp` | Merge as anchor. Confirm still a current advisor. |

**Open question:** which of the 7 team members are still involved (Mujo Panacea era vs prior)? Any who have moved on should be dropped, not just re-hosted.

## Pages — Research (2 index + 3 condition pages, parent proposed REVIEW)

| ID | URL | Words | Disposition | Target Path | Notes |
| --- | --- | ---: | --- | --- | --- |
| 645 | /research/conditions | 302 | **KILL** | 301 → `/treatments` | Category index whose children merge into Treatments. |
| 1168 | /research/device-development | 97 | **KILL** | 301 → `/technology` | Ghost page. |
| 426 | /research/conditions/frozen-shoulder-contracture-syndrome | 3499 | **MERGE** | `/treatments/frozen-shoulder` | Duplicate of `/treatments/frozen-shoulder`. Content depth (3499w) makes this the likely canonical source; port the good bits into the merged page. |
| 428 | /research/conditions/shoulder-impingement-syndrome | 5699 | **MERGE** | `/treatments/shoulder-impingement` | Duplicate of `/treatments/shoulder-impingement`. Longest page on the site (5699w) — depth is here, not on the shorter Treatments version. |
| 430 | /research/conditions/upper-back-and-neck-pain | 640 | **MERGE** | `/treatments/upper-back-and-neck-pain` | Slug clash with `/treatments/upper-back-and-neck-pain` — WP resolves by parent, but confuses users and search engines. Consolidate. |

## Posts (42 total)

Content is heavily dated — **the newest post is 2018-07-10**. Nothing has been published in 8 years. Category distribution:

| Category | Post count | Recommendation |
| --- | ---: | --- |
| News | 25 | Keep 5–7 truly notable (Innovate UK, RNOH, MHRA registration, FDA listing, patent grant). KILL the rest — event write-ups from 2013–2015 add nothing to current credibility. |
| Blog | 13 | KEEP the educational posts (anatomy series, home exercises) — evergreen and useful. Refresh dates or mark clearly as archival. |
| Evidence | 3 | KEEP and re-index as clinical evidence. Extend with 2025–2026 material as it becomes available. |
| education | 3 | Same items counted under Blog. |
| Frozen Shoulder / Shoulder Impingement / Shoulder Pain / Tips | 12 overlapping | These are Blog posts with topical tags. Retain the topical categorisation; simplify to 4–5 categories total on the new site. |
| Guest Interviews | 1 | KEEP if the interviewee is still relevant, otherwise KILL. |
| Conditions / Device Development / Research | 0 posts | KILL — unused categories inherited from old IA. |

**Per-post disposition** for the 42 posts is captured in `docs/audit/posts-disposition.md` — a companion file to keep this document readable. Draft that companion after this document is approved so we don't spend the time until we know the top-level cuts are agreed.

Provisional summary:

* **KEEP as blog:** ~10 posts — the anatomy-of-the-shoulder series (3 parts), home exercises for frozen shoulder (2), MUJO exercises for impingement (2), interview with Dr Niels Peek, plus a couple more that hold up.
* **KEEP as news / press milestones:** ~5–7 — FDA listing (2017), MHRA registration (2015), Innovate UK funding (2014), RNOH installation, patent grants.
* **KEEP as evidence:** all 3 in the Evidence category.
* **KILL:** remaining ~22 news items — award shortlists, event appearances, small installations. They date the company badly and don't earn their keep.

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
/                                    (Home — full rewrite)
/technology                          (Product + hardware overview)
/treatments                          (Conditions landing)
  /treatments/frozen-shoulder
  /treatments/shoulder-impingement
  /treatments/shoulder-instability
  /treatments/upper-back-and-neck-pain
/evidence                            (Clinical evidence library index)
/blog                                (Educational content index)
/news                                (Press / milestones index)
/about                               (Company)
  /about/team                        (All bios on one page, anchored)
/consulting                          (only if still active — REVIEW)
/contact                             (Includes any "book a taster" CTA)
/privacy
/terms
```

That is **~12 core pages + 3 content indexes + a growing blog/evidence/news post list**, down from 40 pages currently. Consistent with the "10–15 pages after rationalisation" estimate in [requirements.md](requirements.md).

## Decisions Requested Before Phase 2

1. **REVIEW rows above** — confirm disposition for: `/research`, `/consulting`, `/faqs`, `/book-free-taster`, and `/technology/dashboard-and-predictive-model`.
2. **Team page** — which of the seven listed team members are still involved, and are there additions?
3. **My Portal footer link** — what is it and does it stay?
4. **Consulting service** — still offered?
5. **Approach to old news** — happy to cull the 20+ 2013–2015 items, or want to preserve them all under an "archive" heading?
