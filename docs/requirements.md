# Mujo Website Rebuild — Requirements Brief

**Version:** 0.1 · **Date:** July 2026 · **Status:** Draft for Review · **Owner:** Mujo Panacea Ltd

**Purpose:** A concise brief capturing what the Mujo website rebuild is, why we are doing it, what it must contain, and what is explicitly out of scope. Sits alongside [sitemap.md](sitemap.md) (Phase 1 audit output) and [checklist.md](checklist.md) (execution tracker) as the three planning documents for this project.

## What This Project Is

The Mujo website rebuild replaces the ageing WordPress site at [mujofitness.com](https://mujofitness.com) — currently hosted on Cloudways — with a modern, statically-generated marketing and content site, deployed on Netlify. The information architecture will be redesigned around the current state of the product (Mujo 1.5 clinical release and Mujo 2.0 KTP programme) rather than the legacy structure inherited from earlier phases of the company.

The old and new sites will run in parallel during the build. The new site is developed on a staging subdomain (e.g. `beta.mujofitness.com`) with search-engine indexing blocked. The live WordPress site is untouched until final DNS cutover, and remains available for rollback for a defined window after cutover.

## Why We Are Doing This

The current site has drifted materially away from being fit for purpose:

* **Stale content.** Pages describe an earlier version of the product and the company that predates the KTP programme, the ISO 13485 / MDR posture, and the 1.5 clinical pilot.
* **Ghost / empty pages.** Menu items and internal links lead to placeholder or empty pages, undermining credibility.
* **Missing information.** Regulatory posture, clinical evidence catalogue, and current company / KTP partner context are either absent or buried.
* **Superfluous information.** Pages exist that no longer serve any audience.
* **Incorrect information.** Product claims, contact details, and partner references are out of date.
* **Poor discoverability.** Clinical papers and third-party reviews are present but hard to find, and the current templates do not present them in a modern reader-friendly form.
* **Legacy platform.** WordPress + a Cloudways VPS carries maintenance overhead, plugin risk, and security surface that a static Astro / Next.js site on Netlify eliminates.

This rebuild is not a redesign for its own sake. It is a correction to bring the public face of the company back in line with what Mujo Panacea now is — a clinically-grounded, regulated musculoskeletal rehabilitation platform mid-way through the 2.0 development programme — and to give investors, clinicians, and prospective customers accurate, current information presented well.

## Scope in One Sentence

A modern statically-generated rebuild of mujofitness.com on Astro or Next.js, deployed via Netlify, that reduces surface area, corrects and refreshes all content, presents the clinical evidence catalogue as a properly indexed blog / library, and cuts over from the WordPress instance without SEO loss.

## Target Audiences

Content and IA decisions should be tested against the following primary audiences, in order:

| Audience | What they need from the site |
| --- | --- |
| Clinicians (NHS, private physio, sports medicine) | What the device does, clinical evidence, how to trial / procure, current regulatory status |
| Investors (Series A track) | Current product state, clinical validation, KTP programme progress, team, contact |
| Prospective partners (sports clubs, research institutions, KTP-style collaborators) | Case studies, published research, how to engage |
| Existing customers of installed fleet (≈12 devices) | Support routes, product updates, contact |
| Press / third parties | Company overview, media pack, contact |

Patients are **not** a primary audience — they interact with the device via the tablet application, not the website.

## Framework / Platform Decisions

The following four decisions are deferred until after the Phase 1 audit produces a real content inventory. Locking them in now would be premature.

| Decision | Chosen | Confirmed |
| --- | --- | --- |
| Site framework | **Astro** | 2026-07-31 |
| Content authoring | **Markdown / MDX in repo** | 2026-07-31 |
| Staging subdomain | **`beta.mujofitness.com`** | 2026-07-31 |
| Hosting | **Netlify** (free tier) | 2026-07-31 |
| Contact form backend | **Netlify Forms** | 2026-07-31 |
| Analytics | Deferred to Phase 4 (UA is dead; nothing to carry over) | — |
| Cookie banner | Deferred to Phase 4 (implementation follows analytics choice) | — |

Rationale: Astro is a better fit than Next.js for a mostly-static marketing / content site — smaller output, better default performance, first-class MDX support, and no runtime overhead where none is needed. Markdown-in-repo removes the need for a CMS account and keeps content versioned alongside code; a headless CMS can be layered in later if non-technical editing becomes a need. Netlify Forms means no third-party service to sign up for, and the free tier (100 submissions / month) comfortably covers expected enquiry volume.

**"Add a CMS later" path.** If browser-based editing becomes a need later, the intended layer is [Decap CMS](https://decapcms.org/) — an open-source admin UI that commits directly to the git repo (i.e. content stays as Markdown-in-repo, editors just get a WYSIWYG). Cost: £0. Auth via GitHub OAuth (free) or Netlify Identity (free up to 5 users). Migrating to a full external CMS such as Sanity or Contentful is a separate, later decision and is not on the near-term roadmap.

## Key Numbers

| Item | Detail |
| --- | --- |
| Current platform | WordPress on Cloudways VPS |
| Target platform | Astro (or Next.js) static site on Netlify |
| Live domain | mujofitness.com |
| Staging domain (proposed) | beta.mujofitness.com |
| Estimated pages after rationalisation | 10–15 pages + growing blog (subject to audit) |
| Estimated dev time | 4–6 weeks part-time from Phase 1 kick-off to cutover, subject to content availability |
| Rollback window post-cutover | 30 days on Cloudways instance before decommission |

These numbers are provisional and will be refined once the Phase 1 audit is complete.

## Content Rationalisation Principles

The rebuild follows five principles when deciding what to carry over, merge, or drop:

1. **Every URL exists for one primary audience.** If a page can't be pinned to a target audience, it goes.
2. **Zero empty pages.** No placeholder, no "coming soon", no orphan menu items.
3. **One canonical page per topic.** If two current pages cover the same ground, they merge.
4. **Blog for time-stamped content, pages for evergreen.** Clinical papers, press mentions, event write-ups, and product updates go in a blog / library section, not as individual top-level pages.
5. **Truthful and current, or absent.** Any claim about clinical status, regulatory posture, or partnerships must be verifiable at time of publish. If it can't be verified now, it doesn't ship.

## Non-Functional Requirements

* **Performance.** Lighthouse scores of ≥90 on Performance, Accessibility, Best Practices, and SEO for every page.
* **Accessibility.** WCAG 2.1 AA target. Semantic HTML, keyboard navigation, alt text on every image, colour contrast within tolerance.
* **SEO parity or better.** No regressions in ranking for the head terms currently driving traffic (`mujo shoulder`, `shoulder rehabilitation device`, brand terms). 301 redirects for every legacy URL that changes path.
* **Analytics.** Cookie-consent-gated, privacy-preserving analytics (GA4 with consent mode, or a Plausible / Fathom equivalent). Decision deferred to audit.
* **Cookie / privacy.** UK GDPR-compliant cookie banner. Privacy policy and cookie policy pages current and correct.
* **Contact intake.** At least one working contact route (form or `mailto:`) reaching a monitored inbox. Zero broken forms.
* **Regulatory disclosures.** Any medical-device claims aligned with UK MHRA and EU MDR guidance for pre-market and installed-base communication — no off-label or unverifiable clinical claims.
* **Responsive.** Mobile, tablet, desktop tested. Sensible breakpoints; no horizontal scroll.
* **Browser support.** Latest two versions of Chrome, Safari, Firefox, Edge. iOS Safari and Chrome Android.

## Phases

Following the Phase 1–5 structure in the original handoff brief:

1. **Phase 1 — Content Audit & Sitemap.** WordPress REST API pull, crawl fallback, produce [sitemap.md](sitemap.md) with keep / merge / kill disposition per URL.
2. **Phase 2 — Framework & Repo Setup.** Lock the four deferred decisions above. Scaffold the chosen framework. Establish folder structure mirroring the rationalised sitemap.
3. **Phase 3 — Content Migration.** Per-page conversion of retained content to Markdown / MDX. Rehost images. Flag plugin-dependent features for manual rebuild.
4. **Phase 4 — Deployment: Netlify + Staging Subdomain.** Netlify site connected to repo. CNAME for staging subdomain. `noindex` enforced.
5. **Phase 5 — QA & Cutover.** URL parity check against sitemap. 301 map. Remove `noindex`. DNS swap. Cloudways instance held for the rollback window.

The execution-level checklist for each phase lives in [checklist.md](checklist.md).

## Out of Scope for This Rebuild

The following are explicitly out of scope for the initial rebuild. Some may become follow-up work; none delay cutover.

* Customer / clinician login area or patient portal
* E-commerce or online purchase / booking of devices
* Multi-language content
* Live product demo, calculator, or interactive simulator
* Migration of the WordPress admin user base
* Backend API changes
* Replatforming of any product-side services (Mujo backend, Android app, KTP hardware programme) — website only
* CMS onboarding for non-technical editors (may be added post-cutover if needed)
* Redesign of brand identity (logo, palette, typography) — the rebuild uses the current brand system unless the audit surfaces a clear need to refresh

## Success Criteria

The rebuild is successful when:

* Every URL in the rationalised sitemap resolves to correct, current content with no placeholders.
* Every legacy URL either resolves at the same path or 301-redirects to its new home.
* Lighthouse targets in the Non-Functional Requirements section are met for every page.
* The contact form and any embedded tools work end-to-end on production.
* SEO head-term rankings hold or improve within 30 days of cutover.
* The Cloudways / WordPress instance can be decommissioned at the end of the rollback window without loss of any published content or capability.

## Related Documents

| Document | Purpose |
| --- | --- |
| [sitemap.md](sitemap.md) | Phase 1 output — inventory of every current URL with disposition and target path |
| [checklist.md](checklist.md) | Execution tracker aligned to Phases 1–5 |
| [MUJO Website Rebuild — Claude Code Handoff Brief](../README.md) | Original handoff brief (to be linked once moved into repo) |

## Confirmed Decisions

Answers captured 2026-07-31 in response to the Phase 1 kick-off questions.

* **Brand assets.** Lift from the current live site as the starting position. A brand kit is being chased from the previous owner and will supersede the lifted assets when it lands. Until then, treat colours / typography / logo extracted from mujofitness.com as the working spec.
* **Analytics.** Attempt to carry over the existing account. **Note from audit:** the live site is running Universal Analytics only (`UA-73890747-1`), which Google shut down mid-2023 — no data has been collected for approximately three years. There is effectively nothing to carry over. Recommend revisiting this decision at Phase 4, options being (a) install GA4 fresh, (b) Plausible / Fathom for a privacy-preserving alternative, or (c) no analytics at launch and decide later. Currently marked as a Phase 4 decision item on the checklist.
* **Partners.** Retain partner logos — several are still relevant (KTP-era partners, 1.5 / 2.0 collaborators). Use in the right locations: home page and / or dedicated partners strip in `/about`, not scattered. Sitemap audit enumerates the current 12 logos in the chrome section.
* **Contact form.** Route to `gerard@panacea.ws` at launch. A dedicated inbox (e.g. `hello@mujofitness.com`) to be set up before go-live so the launch address is not a personal one.

## Open Questions

Captured here so nothing gets lost between sessions. Answered questions move into the Confirmed Decisions section above.

* Is the current WordPress admin still accessible for asset export if the REST API is restricted? (Not needed for Phase 1 — the public REST API returned everything. May matter for Phase 3 image export.)
* What is the "My Portal" link in the current site footer? Live customer portal, legacy staff portal, or dead link? (Surfaced by the Phase 1 audit — see [sitemap.md](sitemap.md#site-chrome-current).)
* Do we have Google Search Console access for the domain, so we can see current head-term traffic and identify high-value URLs before deciding the 301 map?
* Do we have SFTP / admin access on Cloudways for the WordPress instance so the redirect plugin (if any) can be inspected before rebuild?
