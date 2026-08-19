# Evidence library

The MSK research corpus MUJO holds, what each document can actually support, and the trap in each. Compiled by reading the source documents in August 2026.

**The rule this file exists to enforce:** quote the source, the year the *data* refers to, and the figure's actual scope. Most of the traps below are scope traps — a real number about a slightly different thing. Those are the ones that get caught, because a clinician or a diligence analyst checks them.

Source folder: Google Drive → **UK Shoulder & MSK Data & Studies / Data**.

## Contents

1. [Usable figures](#1-usable-figures)
2. [Document-by-document notes](#2-document-by-document-notes)
3. [Figures MUJO does not have](#3-figures-mujo-does-not-have)
4. [Filenames that are wrong](#4-filenames-that-are-wrong)

---

## 1. Usable figures

Each of these was read in the source document. Each still needs its caveat carried into the copy.

**Frozen shoulder — cost of care pathways.** From the UK FROST trial economic evaluation (Corbacho et al., *Bone & Joint Open* 2021;2-8:685–695, DOI 10.1302/2633-1462.28.BJO-2021-0075.R1), at **2018 prices**:

| Intervention | Mean cost |
| --- | --- |
| Early structured physiotherapy | £260 |
| Manipulation under anaesthetic | £425 |
| Arthroscopic capsular release | £2,170 |

Differences: capsular release was £1,734 more costly than physiotherapy (95% CI £1,529–£1,938) and £1,457 more than manipulation; manipulation was £276 more than physiotherapy (95% CI £66–£487). At a £20,000/QALY threshold, manipulation had the highest probability of being cost-effective (0.8632), then physiotherapy (0.1366), then capsular release (0.0002).

*Carry these caveats:* 2018 prices, seven years old — label the price year. And the parent trial (Rangan et al., *The Lancet* 2020;396:977–89, DOI 10.1016/S0140-6736(20)31965-6) found **none of the three interventions clinically superior** on the Oxford Shoulder Score at 12 months. Any copy implying physiotherapy beat surgery, or vice versa, contradicts the paper. The Lancet and BJO papers are the *same trial* — citing both as corroborating evidence overstates the evidence base.

**Shoulder replacement in England.** From the National Joint Registry (identified in the document as the **22nd Annual Report 2025**, reporting 2024 activity):

- 78,603 patients have undergone shoulder replacement and been entered into the registry, ~10% bilateral, giving **86,882 primary cases** available for analysis over a 13-year period.
- Of cases performed in **2024, 70.4% were reverse shoulder replacements**.
- Shoulder replacement volume is **~10% of hip replacement volume**; ~85% of 2024 cases were performed by a surgeon doing more than one per month.

*Carry these caveats:* 78,603 is **cumulative registry entries, not an annual figure** — easy to misread and the most likely misuse. The document was captured from a **UAT/staging server**, so verify against the live published report before use. The summary explicitly warns of intrinsic selection bias in the dataset.

**Reverse vs anatomical total shoulder replacement.** Valsamis et al., *BMJ* 2024;385:e077939, DOI 10.1136/bmj-2023-077939 — NJR + Hospital Episode Statistics for England, 12,986 elective primary procedures in 11,961 patients, 1 April 2012 – 31 December 2020. Population restricted to adults aged 60+, osteoarthritis, intact rotator cuff, England only. Revisions: 126 (1.8%) in the matched cohort, 294 (2.3%) weighted.

*Carry this caveat:* the authors state that a statistically significant reoperation difference of around 1 in 200 "is likely to be of no clinical importance". Quoting the odds ratio without that sentence misrepresents the paper. Also: 61% of preoperative Oxford Shoulder Scores were missing, which precluded a cost-effectiveness analysis — so **there is no usable lifetime-cost figure in this paper**, despite the cost chart.

**Return on investment in physiotherapy — MSK outpatient service.** Russell & Innes, *Musculoskeletal Care* 2024;22:e70008, DOI 10.1002/msc.70008. A single-provider service evaluation at Allied Health Professionals Suffolk CIC:

- Mean **social return on investment of £4.13 for every £1 invested** (237 respondents, 35.6% response rate).
- Range **£3.76 to £6.32** by condition type: £3.76 upper limb, £6.32 spinal.
- Based on an average episode-of-care cost of **£294.24** (NHS National Cost Collection, 2021/22).

*Carry these caveats, all of them:* **SROI is not a cash return.** The authors write explicitly that it "should not be confused with an economic evaluation as there is no material return on investment for the service provider or commissioner". Presenting £4.13 as money returned to a payer misrepresents the study. It is one provider, single-arm, retrospective, self-selected, 35.6% response. **£3.76 is "upper limb", not shoulder** — the study has no shoulder breakdown. And **do not describe this as a Welsh or NHS Wales study**; the file is misnamed, the work was done in Suffolk, England.

**Return on investment in physiotherapy — national.** The CSP published a Treasury-approved analysis on **21 November 2025** reporting **nearly £4 returned for every £1 invested**, **£145m** annual net NHS savings and **£1.88bn** net yearly benefit to the UK economy, with a value calculator and business-case guidance. Source: <https://www.csp.org.uk/publications/return-investment-physiotherapy-uk>. *This is from web research, not from the Drive corpus — read the publication itself before quoting any of these three figures.* If it holds up, it is a stronger and more citable commercial-case anchor than the Suffolk study, and it comes with a calculator MUJO could build a clinic ROI tool against.

**MSK commissioning gaps.** ARMA, *ICB approach to musculoskeletal services within their area*, **August 2024** (all 42 ICBs responded to the FOI): twelve ICBs had no MSK lead; fourteen could not provide MSK priorities; over one in three had neither a lead nor priorities.

*Carry this caveat:* this is a governance survey. It supports an argument about MSK being under-prioritised in commissioning. It contains **no shoulder data, no waiting-list numbers, no costs**.

**NHS England MSK waiting-time policy.** *An improvement framework to reduce community musculoskeletal waits*, published 10 January 2023, last updated 8 December 2025. Thresholds: two weeks for priority patients, 12 weeks for non-priority; objectives of no patients waiting over 52 weeks, and none over 18 weeks by Q1 25/26.

*Carry this caveat:* these are **targets and thresholds, not measured waits**. The document contains no waiting-list size. Cite as "NHS England, 2023 (updated December 2025)".

## 2. Document-by-document notes

| File in Drive | What it actually is | Use it for | Do not use it for |
| --- | --- | --- | --- |
| `ARMA-FOI-Report-Sep2024-Final.pdf` | ARMA ICB FOI survey, **August** 2024 | Commissioning gaps in MSK | Any shoulder, cost or waiting figure |
| `Chartered Soc Physio - Invest in physiotherapy.pdf` | A CSP **news article**, 10 July 2018, reporting on an NIHR review | Signposting to the NIHR *Moving Forward* review | Anything financial — despite the headline it contains **no monetary figure at all**. The "65,000" is a 2026 site-footer membership count covering physiotherapists, students **and** support workers — not a workforce statistic |
| `NHS England » An improvement framework…` | NHS England policy framework | Waiting-time targets | Actual waiting-list volumes |
| `NJR 2024 Shoulder Summary.pdf` | NJR **22nd Annual Report 2025** (2024 data), captured from a staging server | Registry volumes, reverse/anatomical split, specialisation | Annual procedure volumes — not stated numerically anywhere in the summary |
| `NHS Wales SROI MSK physio Russell.pdf` | Russell & Innes 2024, **Suffolk, England** | Physiotherapy SROI, with heavy caveats | Anything framed as Welsh, national, shoulder-specific, or a cash return |
| `bmj-2023-077939.full.pdf` | Valsamis et al., *BMJ* 2024 | RTSR vs TSR revision and reoperation rates | Lifetime cost of shoulder replacement |
| `PIIS0140673620319656.pdf` | **UK FROST**, Rangan et al., *The Lancet* 2020 | Frozen shoulder pathway comparison, trial-level costs | Any claim that one intervention beat another |
| `BJO-2-685.pdf` | **UK FROST economic evaluation**, Corbacho et al., *BJO* 2021 | Intervention costs at 2018 prices | Treating it as a second, independent source alongside the Lancet paper |
| `jcm-14-04765.pdf`, `12916_2023_Article_3112.pdf`, `3035217.pdf`, `MSK Science & Practice.pdf`, `u211254.w4531.full.pdf` | Not individually catalogued here | — | Read before citing |

## 3. Figures MUJO does not have

Worth knowing so they are not invented. None of these are in the corpus:

- Any **UK shoulder pain or shoulder disorder prevalence** figure. The only prevalence figures present are for frozen shoulder specifically — 8.2% of men and 10.1% of women of working age (Walker-Bone et al., *Arthritis & Rheumatism* 2004, UK) and a cumulative incidence of 2.4 per 1,000 population per year (van der Windt et al., *Annals of the Rheumatic Diseases* 1995, **Netherlands**). Both reach MUJO's corpus only as secondary citations inside the FROST papers. **Cite the 2004 and 1995 originals or do not use them. The 2.4 per 1,000 figure is not UK data at all.**
- Any absolute annual volume of shoulder replacements in the UK.
- Any absolute NHS MSK waiting-list size.
- Any total cost of MSK care to the NHS or the UK economy.
- Any physiotherapy workforce headcount or vacancy figure.
- Any shoulder-specific ROI figure.
- Any numeric lifetime cost of shoulder replacement.
- **Any published validity or reliability data for MUJO's own measurement** — accuracy against a gold-standard goniometer or motion-capture system, and inter-rater repeatability. This is the third thing on the trust hierarchy in `sector-craft.md` and the first thing a clinic buyer asks about a measurement device. It is not in the corpus and no MUJO document reviewed states that it exists. **Ask Gerard whether the Coventry EMG benchmarking work or the RNOH feasibility study contains any of it before writing a page that implies MUJO's measurement is validated.** If it does not exist, that is a gap in the evidence base worth naming internally, not papering over on the site.

If a page needs one of these, source it fresh from a named primary publication and add it here — do not reach for a plausible number.

Also note: the "~£5,000 taxpayer saving per avoided shoulder surgery" that appears in MUJO's KTP documents is cited to the company's own Exploitation Plan. It is an internal estimate, not a published finding, and must not be presented as research.

## 4. Filenames that are wrong

Three files in the Drive folder are actively misleading. Anyone reading the folder listing rather than the documents will get these wrong:

- `NHS Wales SROI MSK physio Russell.pdf` — **not Wales.** Suffolk, England.
- `ARMA-FOI-Report-Sep2024-Final.pdf` — the document says **August** 2024.
- `NJR 2024 Shoulder Summary.pdf` — is the **22nd Annual Report 2025**, covering 2024 data, and was captured from a **test server**.

Worth renaming them in Drive.
