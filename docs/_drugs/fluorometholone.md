---
layout: default
title: Fluorometholone
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
---

# Fluorometholone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fluorometholone: From Ophthalmic Inflammation to Postinfectious Vasculitis

## One-Sentence Summary

Fluorometholone (FML) is a topical ophthalmic corticosteroid used for allergic and inflammatory eye conditions, not currently registered in Canada.
The TxGNN model's top prediction is **Postinfectious Vasculitis** (score 99.91%), though this indication has **no clinical trial or literature support**.
Across all 10 predicted indications, the strongest clinical evidence belongs to **Post-bacterial Disorder** (rank 2), backed by **2 clinical trials** totalling 328 patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada; known ophthalmic anti-inflammatory use |
| Predicted New Indication | Postinfectious Vasculitis (rank 1) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only — for rank 1) |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (rank 1) / Proceed with Guardrails (rank 2) |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the dataset. Based on established pharmacology, fluorometholone is a fluorinated glucocorticoid formulated exclusively for ophthalmic topical use. It exerts anti-inflammatory effects primarily by suppressing the NF-κB signalling pathway and reducing pro-inflammatory cytokines (IL-1β, TNF-α), with a well-recognised advantage of lower intraocular pressure (IOP)-elevating potential compared to prednisolone acetate or dexamethasone.

The TxGNN prediction of efficacy in postinfectious vasculitis draws on corticosteroids' general ability to suppress immune-mediated vascular inflammation. However, there is a fundamental pharmacokinetic mismatch: fluorometholone is designed as a topical ophthalmic preparation with negligible systemic bioavailability. It cannot achieve therapeutic plasma concentrations needed to treat systemic vascular conditions, making the rank 1 prediction mechanistically plausible at the class level but pharmacologically non-viable for this specific drug.

The biologically coherent cluster among all 10 predictions centres on **post-infectious ocular inflammatory states** — particularly post-bacterial corneal disorders (rank 2) and punctate epithelial keratoconjunctivitis (rank 6) — where fluorometholone's known ophthalmic mechanism, route of administration, and tissue distribution directly align with the pathology.

---

## Clinical Trial Evidence

> The following trials are drawn from **Post-bacterial Disorder (rank 2)**, the best-evidenced prediction. The top-ranked indication (postinfectious vasculitis) has no registered clinical trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07308938](https://clinicaltrials.gov/study/NCT07308938) | Phase 2 | Not Yet Recruiting | 174 | Fluorometholone 0.1% as adjunctive therapy to topical antibiotics for bacterial corneal ulcers; primary endpoint: best-corrected visual acuity (BCVA) at 3 months. Well-powered, mature design. |
| [NCT01949454](https://clinicaltrials.gov/study/NCT01949454) | N/A | Completed | 154 | Perioperative fluorometholone following trachoma-related trichiasis surgery (Chlamydia trachomatis infection); evaluates whether post-operative anti-inflammatory therapy reduces recurrent trichiasis and scarring. |

---

## Literature Evidence

> The following publications relate to **Punctate Epithelial Keratoconjunctivitis (rank 6)**, the only predicted indication with literature support.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35128186](https://pubmed.ncbi.nlm.nih.gov/35128186/) | 2021 | Observational / Diagnostic | Journal of Current Ophthalmology | AS-OCT imaging characterises epidemic keratoconjunctivitis (EKC) phases and demonstrates measurable impact of topical steroid on disease course |
| [34011737](https://pubmed.ncbi.nlm.nih.gov/34011737/) | 2021 | Case Series / Review | Indian Journal of Ophthalmology | Characterises sequelae of microsporidial keratoconjunctivitis and outlines management including anti-inflammatory approaches |

---

## Canada Market Information

Fluorometholone is **not currently marketed in Canada** — no DINs are on record in the source dataset, and no approved indications are available for review.

> **Note:** Fluorometholone ophthalmic preparations (e.g., FML® 0.1% eye drops) are marketed in multiple international jurisdictions including the United States. A direct query to Health Canada's Drug Product Database (DPD) is recommended to confirm whether any historical or current DIN exists, as this may represent a data gap rather than a true absence from the Canadian market.

---

## Safety Considerations

Complete safety data is not available in the current dataset. The following considerations are based on drug class pharmacology and should be verified against the product monograph:

- **Intraocular pressure elevation**: Steroid-induced ocular hypertension is a class risk for all ophthalmic corticosteroids. Fluorometholone has a lower IOP-elevating profile than prednisolone or dexamethasone, but IOP monitoring remains necessary for courses exceeding 10 days.
- **Risk of masking infection**: Topical corticosteroids may suppress visible signs of ocular infection. Use without adequate antimicrobial coverage in bacterial or viral settings carries risk of infection spread or worsening.
- **Contraindications (class-based)**: Generally contraindicated in active herpes simplex viral keratitis; use with caution in fungal or mycobacterial ocular infections.
- **Safety signal for rank 7 (infection-related HUS) and rank 8 (Chagas cardiomyopathy)**: Corticosteroid use may worsen STEC-mediated toxin injury in HUS, and may promote Trypanosoma cruzi reactivation in Chagas disease. These predictions carry explicit safety concerns and should not be pursued.

---

## Conclusion and Next Steps

**Decision: Hold — Rank 1 (Postinfectious Vasculitis)**

**Rationale:**
Fluorometholone's negligible systemic bioavailability makes it pharmacologically unsuitable for treating systemic vascular inflammation. The rank 1 TxGNN prediction is mechanistically coherent at the corticosteroid class level but non-viable for this specific topical formulation. No clinical or literature evidence exists to support further investigation.

---

**Secondary Decision: Proceed with Guardrails — Rank 2 (Post-bacterial Disorder)**

**Rationale:**
The most actionable repurposing opportunity is bacterial corneal ulcer adjunctive therapy (NCT07308938, Phase 2, n=174), directly aligned with fluorometholone's ophthalmic route and anti-inflammatory mechanism. This is a drug-in-class effect, and the trial design is statistically powered.

**To proceed with rank 2 investigation, the following is needed:**
- Confirm Health Canada DPD status (whether FML ophthalmic is registered under any DIN not captured in this dataset)
- Retrieve full MOA data from DrugBank (data gap DG002)
- Obtain TFDA package insert warnings and contraindications (data gap DG001)
- Establish IOP monitoring guardrails for any protocol using fluorometholone beyond standard duration
- Monitor NCT07308938 results (expected completion December 2030)
- Review NCT01949454 full results for lessons on perioperative anti-inflammatory dosing in infectious disease contexts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

