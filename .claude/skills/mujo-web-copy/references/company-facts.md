# MUJO fact register

The single source of truth for facts used in website copy. Compiled August 2026 from the MUJO Panacea Confluence, Google Drive, the 2015 brand guidelines, and the current `Mujo-website` repo.

**How to use this.** Every factual statement in MUJO web copy should trace to a row here, to a document you have personally read, or to something the user told you in the conversation. The confidence column matters: `Verified` means it was read in a primary MUJO document; `Site-stated` means it appears in the current draft site but has not been checked against a primary record; `Contradicted` means two internal sources disagree and copy must not use it until Gerard settles it.

Nothing in this file is a substitute for asking. When a page needs a fact that isn't here, ask for it.

## Contents

1. [Company and corporate](#1-company-and-corporate)
2. [People](#2-people)
3. [Product](#3-product)
4. [Regulatory status](#4-regulatory-status)
5. [Evidence and clinical history](#5-evidence-and-clinical-history)
6. [Deployment and traction](#6-deployment-and-traction)
7. [Intellectual property](#7-intellectual-property)
8. [The KTP programme](#8-the-ktp-programme)
9. [Market and financial](#9-market-and-financial)
10. [Open contradictions — do not use until resolved](#10-open-contradictions--do-not-use-until-resolved)

---

## 1. Company and corporate

| Fact | Detail | Confidence |
| --- | --- | --- |
| Operating company | MuJo Panacea Limited, registered in England & Wales, company number **17165284** | Site-stated (`investors.mdx`) — worth a Companies House check before publish |
| Predecessor | MuJo Mechanics Limited, registered in England number **7506410**, registered office 1 St Andrew's Hill, London EC4V 5BY | Verified (2014 Innovate UK Collaboration Agreement) |
| Relationship | MUJO Panacea acquired the company and assets of MuJo Mechanics under an Asset Purchase Agreement, and is relaunching | Verified (Gerard; the APA is referenced in the Mujo 1.5 Project Brief re: the emulator dispute) |
| Origin of the technology | Mechanical engineer **Douglas Higgins** invented the fully-moving multi-axial cam in **2006**, originally to train the complex muscles of the spine. **MuJo** was founded in **2011** to apply the system to other commonly injured, high-cost areas of the body. | Verified (2015 Brand & Identity Guideline) |
| Contact | gerard@panacea.ws; contact form routes via Netlify Forms | Verified (repo) |

**Naming.** The 2015 brand mark is "MuJo™ Multiple Joint Fitness Systems". The current site uses "MUJO" and "MuJo Panacea" inconsistently. Match whatever the page you are editing already uses and stay consistent within that page; raise the sitewide inconsistency rather than silently changing it.

## 2. People

| Name | Role | Confidence |
| --- | --- | --- |
| Gerard Kool | Chief Executive Officer | Verified (Confluence, repo) |
| Michael Sasserini | Chief Financial Officer | Verified (repo); note the KTP page spells it "Sassarini" — **confirm the correct spelling before publishing a bio** |
| André Santos | Listed as **Chief Clinical Officer** on the site and **CMO** throughout Confluence. Physiotherapist, movement and strength specialist, founder of DreSports. Candidate PRRC for Mujo 2.0 subject to MDR Art 15 qualification check. | Contradicted title — settle CCO vs CMO sitewide |
| Jeff McBride | Chief Operating Officer | Verified (KTP On a Page, `investors.mdx`); the website programme-control page still says "role TBC" — COO is the later and better-supported source |
| Clinical champions | Two, not yet confirmed | Verified (Gerard, this conversation) — **do not name or imply until confirmed** |
| KTP academic lead | Not appointed; university partner not selected | Verified (REG-002 lists it as TBC) |

## 3. Product

**MUJO (the installed platform, "1.0").** A multi-axial mechanical resistance system built around the patented fully-moving cam. Trains a joint across its full envelope of motion rather than in a single plane. Passive mass-stack resistance. Paired with a tablet display application that guides prescribed exercises, shows real-time visual feedback of joint movement, captures session data and uploads to an AWS backend.

**MUJO 1.5** — the current software programme. Verified from the Mujo 1.5 Android Project Brief (June 2026):

- An Android rewrite of the original iOS shoulder rehabilitation display software, which is no longer maintained. Without it the existing machines cannot function.
- Bluetooth replaces the previous wired USB/Lightning serial connection (RS232-to-Bluetooth Classic adapter, ~£30–60 per unit).
- 26 screens, mapped from the iOS app. 107 numbered requirements. 103 implementation tasks across 10 phases.
- Estimated 8–12 weeks for one experienced Android developer.
- Existing AWS backend; no backend changes required.
- Purpose, in the company's own words: re-enable the ~12 existing machines, run a structured pilot with NHS and sports club partners to gather clinical evidence, and provide working evidence of the product to support the fundraise and the 2.0 programme.
- Explicitly **a bridge product**. Target pilot start was July 2026 — **check current status before writing anything in the present tense.**

**MUJO 2.0** — in development, not on the market. Verified from KTP On a Page and REG-002:

- A motorised, **admittance-control** robotic actuation system replacing the passive weight stack with high-torque motors, enabling active assistance, variable resistance and real-time biomechanical analytics.
- Distinct from the simpler impedance-control (spring-like) approach used in other robotic therapy. Measures the patient's force input via high-frequency sensor fusion, calculates real-time intent against a digital model of the patented cam, and instructs the motor to deliver reactive resistance.
- Enables **process** measurement — how the patient moves during a session — not just outcome measurement. This is the most genuinely novel thing the company can say, and it is a capability claim about the technology rather than a clinical claim, so it is safe to make.
- 24-month development programme. Commercial-ready prototype is the KTP output.
- Stated business rationale: the current mechanical system cannot adapt to patient fatigue, limits throughput to one patient per practitioner, and cannot harvest real-time biometric data.

**Beyond the shoulder.** Lower-limb adaptation is described as a possible KTP extension, "TBD". `investors.mdx` extends this to hip, knee and spine. Treat as roadmap ambition, always in explicitly future/conditional language.

## 4. Regulatory status

This section governs what the site may claim. Read it with `claims-guardrails.md`.

| Item | Status | Source |
| --- | --- | --- |
| MUJO 2.0 EU MDR classification | **Class IIb** under Annex VIII **Rule 9** (active therapeutic device exchanging energy). Software portions inherit Class IIb. | REG-002 §3, July 2026 — the authoritative internal position |
| MUJO 1.5 baseline classification | Class IIa under Rule 11, IEC 62304 Class B, described as "a range-of-motion measurement and reporting aid" | REG-002 §1 and §6.1 |
| Existing device registrations | FDA listing under product code **IKK** (Class II, 510(k)-exempt); UK MHRA registration **CA015151** (Class I) | Site-stated (`investors.mdx`) — **not independently verified; confirm against the MHRA public register and FDA listing before publish** |
| MUJO 2.0 conformity | **Not CE or UKCA marked.** Notified Body not yet selected. ISO 13485 certification not yet held. CE certificate targeted at KTP Month 27–30. | REG-002 §5, §10 |
| MUJO 2.0 clinical investigation | Required under MDR Art 62. Not yet run. Two-phase design planned (feasibility ~15–20 patients; RCT ~80–120 patients, 2–3 sites). Primary endpoint: shoulder ROM recovery at 12 weeks, co-primary with a PROM (Oxford Shoulder Score or DASH). | REG-002 §6.2 |
| Cloud analytics / AI | Internal recommendation is to **exclude clinician-decision-supporting AI from V1** and ship analytics as non-medical descriptive reporting. | REG-002 §9.2 |
| Intended use at V1 | Professional / clinical setting only. Home use is explicitly out of scope. | REG-002 §2 |

**The most consequential line in this whole file:** MUJO 2.0 has an *active therapeutic claim* in its regulatory plan, but does not yet have the conformity marking or the clinical investigation that would license that claim in public advertising. Until it does, 2.0 copy describes what the system *is being developed to do*, in the future tense, and never what it *does* for a patient.

The legacy WordPress site describes the devices as **Class I** and sells assessments and treatments at a London clinic. That framing predates the current regulatory position. Do not carry it forward.

## 5. Evidence and clinical history

| Item | Detail | Confidence |
| --- | --- | --- |
| RNOH feasibility study | Clinical feasibility study at the Royal National Orthopaedic Hospital (2016), published as **Gilbert, Hauptmannova & Jaggi, *BMC Musculoskeletal Disorders* 19:133 (2018)** | Site-stated — the citation is specific enough to be checkable; **verify the DOI and author list before putting it on an evidence page** |
| Innovate UK collaboration | Project *"Connected orthopaedic rehabilitation devices for remote patient monitoring during post-surgery care"*. Parties: MuJo Mechanics, Qinec Ltd, Royal National Orthopaedic Hospital NHS Trust, University of Manchester. Effective date 1 April 2015. Funded by Innovate UK (formerly Technology Strategy Board). | Verified (Collaboration Agreement, Lambert Model C) |
| Named RNOH personnel on that project | Iva Hauptmannova, Anju Jaggi, Susan Alexander | Verified (same) — **do not use as endorsements**; they were project personnel |
| University of Manchester personnel | Niels Peek, John Ainsworth | Verified (same) |
| Coventry University | Evaluation work (2015); prior engagement on upper-quadrant motor control, range-of-motion muscle activation and EMG benchmarking | Verified (KTP On a Page) + site-stated for the 2015 date |
| English Institute of Sport | Structured use (2017); the athletes page references EIOS Lilleshall | Site-stated |
| Sports users | Wasps Rugby, GB Weightlifting, European Tour Health & Performance Institute | Site-stated / Verified (the European Tour deployment is in KTP On a Page) — **get written permission before naming any of these as a customer in new copy** |
| Partner logos currently on the home page | RNOH · EIOS · University of Manchester · Coventry University · Innovate UK · Circle · HERC · IET | Verified (repo) |
| Testimonials | Three practitioner testimonials exist on the legacy site (an occupational therapist, a rugby physiotherapy head, a private physiotherapist), all concerning shoulder rehabilitation | Verified they exist; **they are old, the individuals may have moved roles, and consent may have lapsed — re-confirm before reuse** |

## 6. Deployment and traction

| Fact | Detail | Confidence |
| --- | --- | --- |
| Installed fleet | ~12 devices in the field across NHS trusts, orthopaedic hospitals, elite sport institutes and private MSK clinics | Verified (Mujo 1.5 Project Brief: "~12 existing Mujo shoulder devices") |
| Practitioner sites | "an established deployment footprint across six practitioner sites" | Verified (KTP On a Page) |
| Stored fleet | A further 20 devices — 3 built and ready to ship, 17 awaiting assembly | Site-stated (`investors.mdx`) |
| Current operating state | The installed units currently operate as mechanical machines; the 1.5 Android release reactivates their connected screen and data-capture layer | Verified |

Note the "12 devices" and "six sites" figures are not in conflict — they measure different things — but copy should not blur them into "12 sites" or "six devices".

## 7. Intellectual property

**Treat this section as unverified and check it before it goes near an investor page.** Two different US patent numbers appear across MUJO's own materials:

| Where | Number claimed |
| --- | --- |
| `investors.mdx` | **US 9,776,034**, *Exercise apparatus*, granted 2017 |
| `technology.mdx` (per programme-control summary) | **US 8,821,357** |

Also stated in `investors.mdx`: corresponding protection in the UK/Europe (**EP 2683451**) and China (**ZL2012800227917**); patent family filed 2012, granted from 2017; all software developed and owned in-house.

`technology.mdx` additionally attributes an "Imperial origin" to the mechanism, which sits oddly against the brand guideline's account of Douglas Higgins inventing the cam in 2006. **Resolve both before publishing IP copy.** Patent numbers are the single easiest thing for a diligent investor to check and the most damaging thing to get wrong.

## 8. The KTP programme

Innovate UK Knowledge Transfer Partnership, "Mujo 2.0 Motorisation". Verified from KTP On a Page and the KTP Project Brief.

- 24 months. Innovate UK funds 67%, MUJO Panacea funds 33%.
- Three work packages: WP1 control theory and force-feedback loop optimisation (admittance paradigm); WP2 real-time biomechanical sensor fusion and cloud dashboard integration; WP3 kinematic and EMG laboratory validation.
- A full-time KTP Associate embedded in the business, with ≥3.5 hrs/week academic supervision, ≥2 hrs/week CEO mentoring, bimonthly clinical workshops with the CMO.
- IP and software copyrights (including admittance-control parameters) transfer to Panacea **during** the project, under a Lambert Model C Collaboration Agreement.
- Target academic partners identified but **not selected**: UCL Mechanical Engineering (Prof. Richard Bucknall); University of Sussex (Prof. Luis Ponce Cuspinera); Coventry University (Life Sciences / Biomechanics).

**Do not name a university partner on the website until one is contracted.** Do not describe the KTP as awarded unless it is — check with Gerard. "In development under a Knowledge Transfer Partnership route" is the safe framing if the status is ambiguous.

## 9. Market and financial

Everything in this section is contested or unverified. Read section 10 before using any of it.

| Figure | As stated | Source |
| --- | --- | --- |
| Global MSK market | "$100bn+ total global MSK market" | KTP On a Page / KTP Fact Find Form |
| Serviceable addressable market | "approximately $16bn" global Orthopaedic/MSK segment — but the same Confluence page also writes it as "**£**16 billion" | KTP documents, internally inconsistent on currency |
| ARR target | "c.£10m by year 3 for the shoulder device" | KTP On a Page — a **forecast**, and forward-looking figures do not belong on a public page |
| NHS saving per avoided shoulder surgery | "estimated ~£5,000 taxpayer saving per avoided shoulder surgery cited in the Exploitation Plan" | KTP On a Page, citing an internal document — **an internal estimate, not a published finding. Do not present it as research.** |
| Break-even | "financial break-even by month 22"; "initial market return with upgraded devices within 14 months" | KTP On a Page — forward-looking; keep off public pages |

## 10. Open contradictions — do not use until resolved

Raise these with Gerard rather than picking a side.

1. **Seed vs Series A.** `investors.mdx` says a **£1,000,000 seed round, 20% at a £4,000,000 post-money valuation**. Confluence consistently calls it the **Series A**. These are different stories to an investor. *(Separately — and more urgently — see the FSMA section of `claims-guardrails.md` on whether the amount and valuation can be on a public page at all.)*
2. **US physical therapy market size.** `investors.mdx` says "~$50bn market (2024), forecast to grow at roughly 5% annually". The website programme-control page says "US PT ~$30bn, ~7% CAGR". Neither carries a source. A published market figure needs a named research house, a publication year and a link, or it should be cut.
3. **Patent numbers.** US 9,776,034 vs US 8,821,357. See section 7.
4. **André Santos's title.** Chief Clinical Officer (site) vs CMO (all regulatory documents). The regulatory pack matters here — if he is the designated PRRC candidate, the title on the website should match the title in the technical file.
5. **Michael Sasserini vs Sassarini.**
6. **Regulatory class in public-facing copy.** The site states MHRA Class I and FDA Class II (IKK) for the installed device; REG-002 describes the 1.5 baseline as MDR Class IIa. These may all be simultaneously true across three different regimes and two product configurations — but the site currently does not explain which applies to what, which reads as either confusion or overstatement. Needs one clear sentence per market, signed off by Andre.
7. **"Imperial origin"** on the technology page vs the Douglas Higgins account in the brand guidelines.
