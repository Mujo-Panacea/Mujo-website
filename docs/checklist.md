# Mujo Website Rebuild — Execution Checklist

**Version:** 0.2 · **Date:** August 2026 · **Status:** Active · **Owner:** Mujo Panacea Ltd

**Purpose:** Ordered execution tracker for the website rebuild, aligned to Phases 1–5 in [requirements.md](requirements.md). Sitemap dispositions live in [sitemap.md](sitemap.md). Tick items as they complete; add new items in the relevant phase as they surface.

## At a Glance — Current Status (2026-08-06)

| Phase | State |
| --- | --- |
| **Phase 1 — Content Audit & Sitemap** | ✔ Complete (closed 2026-07-31) |
| **Phase 2 — Framework & Repo Setup** | ✔ Complete (scaffold + Netlify deploy done 2026-08-04) |
| **Phase 3 — Content Migration + IA Reshape** | ⧗ Mechanical + IA reshape complete; **editorial content pending** on home, technology, about, athletes, investors, faqs, legal, team bios |
| **Phase 4 — Deployment & Staging** | ⧗ Deployed to auto Netlify URL; waiting on 123-reg DNS credentials to attach `beta.mujofitness.com`; analytics + cookie banner still deferred |
| **Phase 5 — QA & Cutover** | ◯ Not started |

**2026-08-06 IA reshape.** Gerard pushed for a sharper positioning: clinicians and investors first, athletes as a marketing surface, evidence and case studies consolidated. Top nav is now Technology · Evidence · For Athletes · Investors · About · Contact. `/blog` and `/news` retired; `/treatments` landing retired (condition pages kept for SEO). New `/athletes` and `/investors` pages exist as shells. 42 migrated posts became 18 evidence + 6 resources + 18 killed with 301s.

**Live now:** the site builds and deploys on Netlify at the auto-generated `*.netlify.app` URL. 42 pages after reshape, all routes 200, `noindex` still in place. `beta.mujofitness.com` swap happens once 123-reg access lands.

**What's blocking closure of Phase 3:** Gerard's editorial pass on the shell pages (marked in-page with `EDITORIAL REVIEW IN PROGRESS` banners) — home, technology, about, **athletes**, **investors**, faqs, legal, team bios; the brand kit from the previous owner; team bios / photos for the current four-person team; and image alt text for accessibility compliance.

## Phase 1 — Content Audit & Sitemap

- [x] Fetch pages via WP REST API (`/wp-json/wp/v2/pages`) — 40 pages retrieved
- [x] Fetch posts via WP REST API (`/wp-json/wp/v2/posts`) — 42 posts retrieved
- [x] Fetch categories and tags (12 categories, 0 tags)
- [x] Capture site chrome (nav, footer, analytics, partner logos, embedded widgets) from live homepage
- [x] Produce `sitemap.md` — per-URL disposition table drafted
- [x] Capture confirmed decisions from open questions into `requirements.md`
- [x] Gerard: 5 REVIEW-row dispositions resolved (2026-07-31 — `/research` KILL, `/consulting` KILL, `/faqs` KEEP with rewrite, `/book-free-taster` KILL, `/technology/dashboard-and-predictive-model` KEEP with language change)
- [x] Team confirmed 2026-07-31 — current team: Gerard Kool (CEO), Michael Sasserini (CFO), Andre Santos (CMO), Jeff McBride carrying over; other six previous bios KILL
- [x] "My Portal" confirmed 2026-07-31 — clinician dashboard, retain link, final destination URL TBD
- [x] Approach to old news / blog confirmed 2026-07-31 — keep all 42 posts for rebuild; cull is a post-launch task
- [ ] Media library inventory (162 items) — deferred to Phase 3, driven by which pages need which assets

**Exit criteria:** `sitemap.md` approved. All five REVIEW rows + three follow-up decisions resolved. ✔ Achieved 2026-07-31.

## Phase 2 — Framework & Repo Setup

**Blocked by:** Phase 1 exit criteria.

### Deferred decisions to settle at this phase

- [x] Framework — **Astro** (confirmed 2026-07-31)
- [x] Content authoring — **Markdown / MDX in repo** (confirmed 2026-07-31)
- [x] Staging subdomain — **`beta.mujofitness.com`** (confirmed 2026-07-31)
- [x] Contact form backend — **Netlify Forms** (confirmed 2026-07-31)
- [ ] Cookie banner library — deferred to Phase 4 with analytics choice
- [ ] Analytics — deferred to Phase 4 (UA-73890747-1 is dead; effectively starting fresh)

### Repo scaffold

- [x] Astro 7 initialised in this repo (2026-08-04) — `package.json`, `astro.config.mjs`, `tsconfig.json`, `src/`
- [x] Folder structure mirroring the rationalised sitemap
- [x] Base layout (`BaseLayout.astro`, `PageLayout.astro`), Header, Footer, ReviewBanner, PostCard components
- [x] Placeholder brand tokens in `src/styles/tokens.css` — to be replaced when brand kit lands
- [x] Global styles + minimal component set (button, card, section, form fields)
- [x] MDX support wired via `@astrojs/mdx` v7
- [x] Content Collections defined with Zod schemas (posts / team / partners)
- [ ] Image pipeline via Astro `<Image>` component — currently using plain `<img>` for speed; upgrade in Phase 5 QA
- [ ] `CONTRIBUTING.md` describing content authoring conventions

**Exit criteria:** the empty scaffold deploys to Netlify at the chosen staging subdomain and shows a working home page skeleton and one blog post skeleton, both with correct fonts, colours, and header/footer chrome. **✔ Achieved 2026-08-04** — deployed to Netlify auto-URL; `beta.mujofitness.com` attaches when DNS credentials arrive.

## Phase 3 — Content Migration

**Blocked by:** Phase 2 exit criteria.

### Pages

Every route below now has a live shell or migrated body on the deploy. Editorial rewrites still needed for items marked ⧗.

- ⧗ `/technology` — shell + banner. Needs editorial rewrite reflecting Mujo 1.5 baseline and 2.0 KTP programme
- ⧗ `/technology/dashboard-and-predictive-model` — shell + banner. Language must shift to "we are building"; regulatory-safe wording required
- ⧗ `/treatments` — landing shell + banner. Needs editorial pass listing conditions and audiences
- [x] `/treatments/frozen-shoulder` — content migrated + merged from both legacy sources. **Accuracy review needed** before Phase 5
- [x] `/treatments/shoulder-impingement` — migrated + merged. **Accuracy review needed**
- [x] `/treatments/shoulder-instability` — migrated. **Accuracy review needed**
- [x] `/treatments/upper-back-and-neck-pain` — migrated + merged. **Accuracy review needed**
- ⧗ `/faqs` — shell + banner. Needs full rewrite with contact-us CTAs on every answer
- ⧗ `/about` — shell + banner. Needs rewrite for current company posture
- ⧗ `/about/team` — shell + banner. Awaiting Gerard for bios + photos of Gerard Kool (CEO), Michael Sasserini (CFO), Andre Santos (CMO), Jeff McBride
- [ ] Confirm the clinician "My Portal" destination URL (or agree on a "coming soon" holding page) before cutover — do not ship a broken link
- [x] `/contact` — Netlify Forms wired, routes to gerard@panacea.ws once notifications configured in Netlify dashboard
- ⧗ `/privacy` — shell + banner. Legal review required before cutover
- ⧗ `/terms` — shell + banner. Legal review required before cutover
- ⧗ `/` (home) — placeholder hero + latest posts. Needs full home-page copy rewrite
- [x] Strip any residual "book a free taster" CTAs — none appear in migrated content

### Content indexes

- [x] `/evidence` — clinical evidence library index driven by posts with `category: evidence`
- [x] `/blog` — educational content index driven by posts with `category: blog`
- [x] `/news` — press / milestones index driven by posts with `category: news`

### Blog / post migration

- [x] Migrate all 42 posts to MDX in `/src/content/posts/` — full carry-over, cull deferred to post-launch
- [x] Assign each migrated post to its content index (evidence / blog / news) — routed via `category` frontmatter into `/blog/`, `/news/`, `/evidence/`
- [x] Show original publication dates prominently — do not silently rebadge 2015 content as 2026
- [x] Auto-mark 2013–2019 posts as `archived: true` so readers see them for what they are
- [x] Consolidate categories: retire the four zero-post categories; retain News, Blog, Evidence

### Assets

- [x] Enumerate images referenced by posts (89 images from 38 posts with heroes + body figures)
- [x] Download images to `/public/images/posts/<slug>/` — 89/89 fetched via `scripts/download_media.sh`
- [ ] Add descriptive `alt` text on every image (WCAG 2.1 AA) — currently blank alts on migrated images, needs a pass
- [ ] Extract partner logos and place in `/public/images/partners/` (deferred until home + about editorial pass)
- [ ] Extract and rehost the MUJO logo, favicon, and any brand-mark variants (deferred until brand kit arrives)

### Manual rebuilds

- [x] Contact form component (Netlify Forms) — `src/components/ContactForm.astro` + `/contact/` + `/contact/thanks/`
- [ ] Configure Netlify → Forms → Notifications to email gerard@panacea.ws (needs Netlify dashboard access)
- [ ] Cookie banner (implementation TBD once analytics decision is made)
- [ ] Any newsletter signup (only if requested — not currently on scope)
- [x] Instagram feed — dropped; no equivalent added
- [x] Twitter widget — dropped; API instability makes it not worth it

**Exit criteria:** every page in the rationalised sitemap is present on staging with reviewed and approved content, images rehosted, and no `TODO` / `LOREM IPSUM` / placeholder markers.

## Phase 4 — Deployment: Netlify + Staging Subdomain

**Blocked by:** Phase 2 exit criteria (but runs alongside Phase 3).

- [x] Connect the repo to Netlify (done by Gerard, auto-URL live)
- [x] Configure production branch, build command, publish directory (Netlify auto-detected Astro)
- [ ] Attach `beta.mujofitness.com` subdomain — **blocked on 123-reg credentials** from previous owner handover
- [x] Block indexing — `robots.txt` `Disallow: /` **and** meta `noindex,nofollow` on every page (both live)
- [ ] Verify staging is blocked from indexing via Google Search Console URL inspection (Phase 5 QA)
- [ ] Configure Netlify → Forms → Notifications to email gerard@panacea.ws
- [ ] Set analytics — **decision still deferred**: GA4 fresh, Plausible, Fathom, or defer to post-launch
- [ ] Set cookie banner — implementation follows the analytics decision (Plausible / Fathom → no banner needed)
- [ ] Set custom 404 page with search / navigate-home
- [x] Canonical URLs and Open Graph / Twitter card meta on every page (in `BaseLayout.astro`)
- [x] `sitemap.xml` generated via `@astrojs/sitemap` integration on every build
- [ ] Swap production `robots.txt` to allow crawling at cutover (currently blocking everything)
- [ ] Configure security headers on Netlify (CSP, X-Frame-Options, Referrer-Policy, etc.) — Phase 5 QA
- [ ] Set up Netlify build hook (only if a CMS is chosen — not applicable now)

**Exit criteria:** staging site is reachable at the chosen subdomain, blocked from indexing, and functionally complete.

## Phase 5 — QA & Cutover

**Blocked by:** Phase 3 and Phase 4 exit criteria.

### QA against the sitemap

- [ ] Cross-check every URL in [sitemap.md](sitemap.md) — every KEEP / MERGE row has a live target on staging
- [ ] Cross-check every KILL row has a 301 destination that makes sense (usually home, treatments, or the closest topical page)
- [x] Build the 301 redirect map file (`public/_redirects` — done 2026-08-05)
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
* **2026-07-31** — Five sitemap REVIEW rows resolved. `/research` → KILL (301 to `/evidence`). `/consulting` → KILL (service no longer offered). `/faqs` → KEEP, rewrite with contact-us language throughout. `/book-free-taster` → KILL (offer retired — also strip residual CTAs from other pages). `/technology/dashboard-and-predictive-model` → KEEP, but language shifts from "we have" to "we are building"; a future offering aligned with the Mujo 2.0 roadmap, regulatory review required to avoid overstatement.
* **2026-07-31** — Team confirmed. Current team is Gerard Kool (CEO), Michael Sasserini (CFO), Andre Santos (CMO), and Jeff McBride carrying over from the previous seven bios. The other six bios are KILL with 301 to `/about/team`. Bios and photos to be supplied by Gerard at Phase 3.
* **2026-07-31** — "My Portal" clarified: clinician dashboard access, either live or planned. Retain the link on the new site; final destination URL to be confirmed at Phase 3 / 4, with a placeholder acceptable if the dashboard is not yet ready by cutover. Do not ship a broken link.
* **2026-07-31** — Posts approach confirmed: keep all 42 posts for the rebuild. Reshape the site around the sitemap first, then cull dated news and refresh the blog post-launch. Per-post disposition file deferred as post-launch cleanup.
* **2026-07-31** — Phase 1 audit closed. Ready to begin Phase 2 (framework + repo setup) on Gerard's go.
* **2026-07-31** — Phase 2 stack locked in: Astro + Markdown/MDX in-repo + Netlify hosting + Netlify Forms for contact + `beta.mujofitness.com` staging. No new accounts required beyond the Netlify account already opened. Cookie banner + analytics choices remain deferred to Phase 4.
* **2026-08-04** — Astro 7 scaffold committed, dev server working end-to-end. Node 26 LTS installed via Homebrew as a prerequisite.
* **2026-08-05** — Phase 3 mechanical migration complete. 42 WordPress posts → MDX (blog / news / evidence) with 89 hero + body images rehosted. 13 retained pages have shells or migrated bodies with `ReviewBanner` markers for editorial pass. Contact form wired to Netlify Forms. 301 redirect map covers every KILL / MERGE row in the sitemap. Production build clean — 60 pages built in ~5s. Awaiting Gerard's editorial pass on home, technology, about, faqs, and legal pages; awaiting brand kit and team bios/photos.
* **2026-08-05** — Deployed to Netlify auto-URL. `beta.mujofitness.com` subdomain attachment paused pending 123-reg credentials from the previous-owner handover.
* **2026-08-06** — **IA reshape.** New nav: Technology · Evidence · For Athletes · Investors · About · Contact. Retired `/blog`, `/news`, `/treatments` landing; condition pages under `/treatments/` retained for SEO. New `/athletes`, `/investors`, `/resources` pages as shells. 42 migrated posts → 18 evidence + 6 resources + 18 killed. `_redirects` rewritten to cover every URL move: surviving news → `/evidence/`, surviving educational blog → `/resources/`, sports-derivative → `/athletes/`, others to nearest section landing. Production build clean at 42 pages in ~3s.
