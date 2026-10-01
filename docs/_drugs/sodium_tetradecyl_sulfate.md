---
layout: default
title: Sodium Tetradecyl Sulfate
parent: High Evidence (L1-L2)
nav_order: 851
evidence_level: L2
indication_count: 10
---

# Sodium Tetradecyl Sulfate
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Sodium Tetradecyl Sulfate: From Varicose Veins to Esophageal Varices with Bleeding

## One-Sentence Summary

Sodium tetradecyl sulfate (STS) is a sclerosing agent marketed for varicose veins. The TxGNN model predicts it may be effective for **esophageal varices with bleeding**, with **1 registered clinical trial (indirect relevance)** and **20 publications** supporting this direction, including 4 randomized trials of STS as a variceal sclerosant. Most of this evidence dates from the 1980s and 1990s.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Varicose veins (sclerosant use; the licence text was not provided in the data) |
| Predicted New Indication | Esophageal varices with bleeding |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not currently available. Based on known information, STS is a detergent sclerosant. It damages the venous endothelium, which causes thrombosis and fibrosis and obliterates the vessel.

The same mechanism applies to esophageal and gastric varices, so the link between the original and new indication is direct and biologically plausible. The prediction is closer to a site or route extension than to true repurposing, because the drug is already used as a sclerosant.

The published record supports this use. Randomized comparisons of STS against polidocanol, sodium morrhuate and ethanolamine oleate exist. However, they are older and mostly predate band ligation. Current guidelines favor band ligation over sclerotherapy for esophageal varices, so any proposal should be framed as an alternative or rescue option. The evidence is graded L2 rather than L1 because the input data do not state a trial phase, and the older randomized trials are not labeled Phase 3.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05500625](https://clinicaltrials.gov/study/NCT05500625) | NA | Unknown | 70 | EUS-guided coil with cyanoacrylate vs balloon-occluded retrograde transvenous obliteration (BRTO) in gastric varices. STS is not shown as an arm, and the focus is gastric rather than esophageal varices. This is indirect support only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8287811](https://pubmed.ncbi.nlm.nih.gov/8287811/) | 1993 | RCT (double-blind) | Endoscopy | 3% STS vs 5% ethanolamine oleate in 95 patients with variceal bleeding. |
| [1734694](https://pubmed.ncbi.nlm.nih.gov/1734694/) | 1992 | RCT | Am J Gastroenterol | STS vs polidocanol in 52 patients with esophageal variceal bleeding. Eradication was achieved in 88% in each group. |
| [2279644](https://pubmed.ncbi.nlm.nih.gov/2279644/) | 1990 | RCT | Gastrointest Endosc | STS vs sodium morrhuate in 41 patients with acute variceal bleeding. Mortality was 38% vs 25% (not significant). |
| [8886633](https://pubmed.ncbi.nlm.nih.gov/8886633/) | 1996 | RCT | Endoscopy | Hypertonic glucose water vs STS for gastric variceal bleeding in advanced cirrhosis. |
| [30170340](https://pubmed.ncbi.nlm.nih.gov/30170340/) | 2019 | Review | J Gastroenterol Hepatol | Recent development of BRTO, including the shift to STS foam as a sclerosant. |
| [3443730](https://pubmed.ncbi.nlm.nih.gov/3443730/) | 1987 | Prospective cohort | J Clin Gastroenterol | Clinical and histopathologic effects of STS endoscopic sclerotherapy on the esophagus in 24 patients. |
| [9540875](https://pubmed.ncbi.nlm.nih.gov/9540875/) | 1998 | Comparative study | Gastrointest Endosc | Cyanoacrylate vs STS for variceal bleeding in patients with hepatocellular carcinoma. |
| [28180928](https://pubmed.ncbi.nlm.nih.gov/28180928/) | 2017 | Cohort | Cardiovasc Intervent Radiol | Safety and efficacy of STS and lipiodol foam in BRTO for large porto-systemic shunts and gastric fundal varices. |
| [21353984](https://pubmed.ncbi.nlm.nih.gov/21353984/) | 2011 | Cohort | J Vasc Interv Radiol | Initial experience with BRTO using STS foam for bleeding gastric varices. |
| [37745308](https://pubmed.ncbi.nlm.nih.gov/37745308/) | 2023 | Cohort | Diagn Interv Radiol | Antegrade foam sclerotherapy for portal hypertensive variceal bleeding. |

---

## Canada Market Information

| DIN / Licence No. | Product Name |
|---------|------|
| 511234 | TROMBOJECT 1% |
| 511226 | TROMBOJECT 3% |

---

## Safety Considerations

- **Key risks from the literature**: esophageal ulceration and stricture are the main complications of variceal sclerotherapy. They are examined in the prospective esophageal-effects study (PMID 3443730) and in the sclerotherapy vs band ligation comparison (PMID 11232687).

For other safety information, including warnings, contraindications and drug interactions, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
STS has a direct, plausible mechanism and several randomized comparisons in esophageal variceal bleeding. However, these trials are old, and band ligation is now the guideline-preferred approach. The only registered trial is indirect. This indication should therefore be considered only as an alternative or rescue option.

Other predictions for this drug are weaker:
- **Esophageal varices without bleeding:** this remains a research question, because prophylactic sclerotherapy is not recommended.
- **Ranks 3–10** (for example Steel syndrome and hypophosphatasia): these have no mechanistic link and no evidence beyond the model score. They are on Hold.

**To proceed, the following is needed:**
- The Health Canada package insert warnings and contraindications, which are currently missing and block safety screening.
- Detailed mechanism-of-action data from DrugBank.
- A comparison against band ligation or current standard care.
- Confirmation of route and formulation compatibility, since the marketed products are intravenous sclerosants and variceal use requires endoscopic or interventional administration.
- A safety plan for esophageal ulcer and stricture.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

