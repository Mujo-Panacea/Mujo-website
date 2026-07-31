# Mujo Website Rebuild — Execution Checklist

**Version:** 0.1 · **Date:** July 2026 · **Status:** Active · **Owner:** Mujo Panacea Ltd

**Purpose:** Ordered execution tracker for the website rebuild, aligned to Phases 1–5 in [requirements.md](requirements.md). Sitemap dispositions live in [sitemap.md](sitemap.md). Tick items as they complete; add new items in the relevant phase as they surface.

## Phase 1 — Content Audit & Sitemap

- [x] Fetch pages via WP REST API (`/wp-json/wp/v2/pages`) — 40 pages retrieved
- [x] Fetch posts via WP REST API (`/wp-json/wp/v2/posts`) — 42 posts retrieved
- [x] Fetch categories and tags (12 categories, 0 tags)
- [x] Capture site chrome (nav, footer, analytics, partner logos, embedded widgets) from live homepage
- [x] Produce `sitemap.md` — per-URL disposition table drafted
- [x] Capture confirmed decisions from open questions into `requirements.md`
- [ ] **Gerard: review `sitemap.md` and answer the 5 Decisions Requested items at the bottom**
- [ ] Confirm which of the 7 currently-listed team members are still involved
- [ ] Confirm status of the "My Portal" footer link (live / legacy / dead)
- [ ] Per-post disposition for the 42 posts (`docs/audit/posts-disposition.md`) — deferred until top-level cuts approved
- [ ] Media library inventory (162 items) — deferred to Phase 3, driven by which pages need which assets

**Exit criteria:** `sitemap.md` approved and the five REVIEW rows resolved to concrete dispositions.

## Phase 2 — Framework & Repo Setup

**Blocked by:** Phase 1 exit criteria.

### Deferred decisions to settle at this phase

- [ ] Framework — Astro (recommended) vs Next.js
- [ ] Content authoring — Markdown-in-repo (recommended) vs headless CMS (Sanity / Contentful)
- [ ] Staging subdomain name — `beta.` / `staging.` / `new.` (recommended `beta.`)
- [ ] Manual-rebuild feature list — Netlify Forms for contact vs a third-party form; cookie banner library; analytics choice (see Phase 4)

### Repo scaffold

- [ ] Initialise the chosen framework in this repo (or a new repo, TBD at decision time)
- [ ] Establish folder structure mirroring the rationalised sitemap in [sitemap.md](sitemap.md#proposed-new-sitemap-summary)
- [ ] Add base layout, header, footer, and shared components
- [ ] Wire up brand tokens (colour, typography, spacing) from assets lifted from the live site
- [ ] Add global styles + a component library minimal set (button, card, section, callout)
- [ ] Configure image pipeline for the framework's built-in optimisation (Astro `<Image>` / `next/image`)
- [ ] Configure MDX / Markdown support for pages and blog posts
- [ ] Add a `CONTRIBUTING.md` in the repo describing content authoring conventions

**Exit criteria:** the empty scaffold deploys to Netlify at the chosen staging subdomain and shows a working home page skeleton and one blog post skeleton, both with correct fonts, colours, and header/footer chrome.

## Phase 3 — Content Migration

**Blocked by:** Phase 2 exit criteria.

### Pages (in dependency order — home last so it can link to the finished pages)

- [ ] `/technology` (absorbing `/technology/devices`, dropping `/technology/dashboard-and-predictive-model` pending confirmation)
- [ ] `/treatments` (landing page listing conditions)
- [ ] `/treatments/frozen-shoulder` (merged from `/research/conditions/frozen-shoulder-contracture-syndrome`)
- [ ] `/treatments/shoulder-impingement` (merged from `/research/conditions/shoulder-impingement-syndrome`)
- [ ] `/treatments/shoulder-instability`
- [ ] `/treatments/upper-back-and-neck-pain` (merged from `/research/conditions/upper-back-and-neck-pain`)
- [ ] `/about`
- [ ] `/about/team` (consolidated bios from the seven individual team pages)
- [ ] `/consulting` (if REVIEW resolves to KEEP)
- [ ] `/contact` (with form → gerard@panacea.ws, subject to launch-time swap to dedicated inbox)
- [ ] `/privacy` (legal review)
- [ ] `/terms` (legal review)
- [ ] `/` (home page rewrite — depends on all pages above so it can link correctly)

### Content indexes

- [ ] `/evidence` — clinical evidence library index, driven by posts in the Evidence category
- [ ] `/blog` — educational content index
- [ ] `/news` — press / milestones index

### Blog / post migration

- [ ] Draft per-post disposition (`docs/audit/posts-disposition.md`) — every post gets KEEP / KILL / REWRITE
- [ ] Migrate KEEP posts to MDX in `/src/content/posts/` (or framework equivalent)
- [ ] Assign each migrated post to its content index (evidence / blog / news)
- [ ] Add reading-time and updated-date metadata to blog posts that carry old dates
- [ ] Add "Archive" flag on any 2013–2018 post preserved — set expectations for the reader

### Assets

- [ ] Enumerate images used on retained pages (from WP REST media API + per-page content scans)
- [ ] Download those images to `/public/images/` (or framework-equivalent), organised by page
- [ ] Add descriptive `alt` text on every image (WCAG 2.1 AA)
- [ ] Extract partner logos referenced in [sitemap.md](sitemap.md#site-chrome-current) and place in `/public/images/partners/`
- [ ] Extract and rehost the MUJO logo, favicon, and any brand-mark variants

### Manual rebuilds

- [ ] Contact form component (Netlify Forms, or chosen alternative)
- [ ] Cookie banner (implementation TBD once analytics decision is made)
- [ ] Any newsletter signup (only if requested — not currently on scope)
- [ ] Instagram feed — decision: drop entirely, or replace with a curated 3-image static grid so the site is not dependent on a stale Instagram token
- [ ] Twitter widget — drop; API instability makes it not worth it

**Exit criteria:** every page in the rationalised sitemap is present on staging with reviewed and approved content, images rehosted, and no `TODO` / `LOREM IPSUM` / placeholder markers.

## Phase 4 — Deployment: Netlify + Staging Subdomain

**Blocked by:** Phase 2 exit criteria (but runs alongside Phase 3).

- [ ] Connect the repo to Netlify (if not already done in Phase 2 scaffold)
- [ ] Configure production branch, build command, publish directory
- [ ] Set the staging subdomain (CNAME added alongside existing DNS — does not touch the live site)
- [ ] Block indexing on the staging subdomain — `robots.txt` `Disallow: /` **and** meta `noindex,nofollow` on every page (belt + braces)
- [ ] Verify staging is unreachable to Google Search Console (submit staging URL for crawl test → should show "blocked")
- [ ] Set analytics: **decision required** — GA4 fresh, or Plausible / Fathom, or defer to post-launch
- [ ] Set cookie banner: implementation matches analytics choice (no cookies → no banner if Plausible / Fathom)
- [ ] Set custom 404 page with search / navigate-home
- [ ] Set canonical URLs and Open Graph / Twitter card meta on every page
- [ ] Add a `sitemap.xml` and `robots.txt` (real, production-ready — swap the "noindex" versions at cutover)
- [ ] Configure security headers on Netlify (CSP, X-Frame-Options, Referrer-Policy, etc.)
- [ ] Set up Netlify build hook (only if a CMS is chosen)

**Exit criteria:** staging site is reachable at the chosen subdomain, blocked from indexing, and functionally complete.

## Phase 5 — QA & Cutover

**Blocked by:** Phase 3 and Phase 4 exit criteria.

### QA against the sitemap

- [ ] Cross-check every URL in [sitemap.md](sitemap.md) — every KEEP / MERGE row has a live target on staging
- [ ] Cross-check every KILL row has a 301 destination that makes sense (usually home, treatments, or the closest topical page)
- [ ] Build the 301 redirect map file (`_redirects` for Netlify, or `netlify.toml` `[[redirects]]`)
- [ ] Run each Phase 3 page through Lighthouse — target ≥90 on Performance / Accessibility / Best Practices / SEO
- [ ] Fix any regressions from those Lighthouse runs
- [ ] Broken-link check across staging (`lychee` or a similar link checker)
- [ ] Manual review on mobile, tablet, desktop breakpoints
- [ ] Manual test of contact form → confirm email arrives at gerard@panacea.ws
- [ ] Confirm cookie banner (if present) works as intended
- [ ] Legal review of `/privacy` and `/terms` complete
- [ ] Regulatory review of any medical-device claims on `/technology` and `/treatments/*`
- [ ] Gerard: full walkthrough approval

### Cutover

- [ ] Prepare a rollback plan — DNS TTL check, Cloudways instance confirmed live, credentials to hand
- [ ] Confirm dedicated contact inbox is live and reachable (swap gerard@panacea.ws → new inbox)
- [ ] Remove `noindex` meta tag and update `robots.txt` on the production build
- [ ] Verify the production build has no `noindex` in the rendered HTML
- [ ] Perform DNS swap — point `mujofitness.com` (and `www.`) A / CNAME to Netlify
- [ ] Monitor DNS propagation (`dig`, `nslookup` from multiple regions)
- [ ] Submit new `sitemap.xml` to Google Search Console
- [ ] Request re-crawl of the new site in Search Console
- [ ] Announce cutover internally

### Post-cutover monitoring (30-day rollback window)

- [ ] Keep the Cloudways WordPress instance live but unpublished for 30 days
- [ ] Day 1, 7, 14, 30 checks: Search Console for 404 spikes, ranking movements on head terms, analytics working
- [ ] Log any post-cutover fixes as new items in this checklist under a `Post-cutover fixes` heading
- [ ] Day 30: sign-off to decommission the WordPress / Cloudways instance
- [ ] Cancel Cloudways subscription
- [ ] Archive the final WP export (`wp-json` JSON + media) in this repo under `docs/audit/final-export/`

**Exit criteria:** the new site is live at mujofitness.com, the old WP instance is decommissioned, and no unresolved regressions remain from the 30-day monitoring window.

## Ongoing / Post-Launch (out of this rebuild's scope)

Tracked here so nothing gets lost, but not delivered as part of the initial cutover:

- [ ] Adding a headless CMS if non-technical editing becomes needed
- [ ] Multi-language content (deferred per [requirements.md](requirements.md#out-of-scope-for-this-rebuild))
- [ ] Customer / clinician portal (out of scope — separate product)
- [ ] Brand refresh once the new kit arrives from the previous owner

## Notes / Decisions Log

Add dated entries here as decisions are made. Keep the entry short — the reasoning belongs in [requirements.md](requirements.md) or [sitemap.md](sitemap.md).

* **2026-07-31** — Phase 1 kickoff. Confirmed: brand lifts from live site pending kit; analytics — audit found UA is dead so effectively starting fresh, choice deferred to Phase 4; partners retained; contact goes to gerard@panacea.ws until a dedicated inbox is ready.
