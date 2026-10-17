---
layout: default
title: Trametinib
parent: Model Prediction Only (L5)
nav_order: 928
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Trametinib: predicted new indication Choroideremia (evidence level L5). Approved use: Metastatic melanoma"
monitor_inn: "TRAMETINIB"
predicted_indications: ["choroideremia"]
---

# Trametinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Trametinib: From Metastatic Melanoma to Choroideremia

## One-Sentence Summary

Trametinib is a MEK inhibitor originally used to treat metastatic melanoma.
The TxGNN model's top-ranked prediction is **Choroideremia**, but this rests on a computational score alone, with **0 clinical trials** and **0 publications** supporting it.
The better-supported predictions are melanoma subtypes, particularly **non-cutaneous melanoma**, which has **10 related clinical trials** (mostly combination or tumour-agnostic studies).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic melanoma (the Canadian licence records carry no indication text, so this comes from the TxGNN knowledge graph) |
| Predicted New Indication | Choroideremia (rank 1); the highest-evidence alternative is non-cutaneous melanoma (rank 2) |
| TxGNN Prediction Score | 99.31% (choroideremia); 99.30% (non-cutaneous melanoma) |
| Evidence Level | L5 (choroideremia); L2 (non-cutaneous melanoma) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold (choroideremia); the melanoma-subtype predictions are better framed as research questions |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the pharmacology records, trametinib inhibits **MEK1 (MAP2K1)** and **MEK2 (MAP2K2)** in the MAPK pathway. It is used for BRAF V600-mutant melanoma, and in combination with dabrafenib for other BRAF V600E-mutant cancers such as anaplastic thyroid cancer.

**Choroideremia (rank 1):** This is an X-linked retinal degeneration caused by loss of function of the CHM gene, which impairs Rab prenylation. No clear mechanistic link to MEK inhibition is evident. The high score is a model output only, and the prediction should be treated with scepticism.

**Melanoma subtypes (ranks 2–10):** Most of the other predictions are melanoma variants. Here the mechanistic rationale is much stronger:
- **Non-cutaneous melanoma** (mucosal, uveal, acral) often has MAPK pathway activation (BRAF, NRAS, NF1). MEK inhibition is plausible, though uveal melanoma is usually GNAQ/GNA11-driven and less BRAF-dependent.
- **Superficial spreading melanoma** is frequently BRAF V600-mutant, but it overlaps with the approved melanoma indication, so it is largely not true repurposing.
- **Acral lentiginous melanoma** has fewer BRAF V600 mutations, which weakens the rationale.
- **Lentigo maligna melanoma** has more NRAS/NF1/KIT alterations, so trametinib is plausible in NRAS/NF1-mutant disease.
- **CDK4-linked melanoma** acts on the cell cycle, so the link to MAPK inhibition is indirect.

## Clinical Trial Evidence

Choroideremia has no registered clinical trials. The table below covers the trials listed for **non-cutaneous melanoma** (rank 2), the most evidence-rich prediction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02296112](https://clinicaltrials.gov/study/NCT02296112) | Phase 2 | Completed | 9 | Trametinib in melanoma with BRAF non-V600 mutations; directly relevant but very small |
| [NCT04439292](https://clinicaltrials.gov/study/NCT04439292) | Phase 2 | Active, not recruiting | 44 | NCI-MATCH Subprotocol H: dabrafenib + trametinib in BRAF V600-mutant tumours, tumour-agnostic |
| [NCT05907304](https://clinicaltrials.gov/study/NCT05907304) | Phase 1 | Active, not recruiting | 86 | Naporafenib + trametinib in RAS Q61X solid tumours |
| [NCT02974725](https://clinicaltrials.gov/study/NCT02974725) | Phase 1 | Terminated | 241 | LXH254 combinations (including trametinib) in KRAS/BRAF-mutant NSCLC or NRAS-mutant melanoma |
| [NCT02872259](https://clinicaltrials.gov/study/NCT02872259) | Phase 1/2 | Completed | 74 | BGB324 with pembrolizumab or dabrafenib/trametinib in advanced melanoma; trametinib is part of the backbone |
| [NCT02410863](https://clinicaltrials.gov/study/NCT02410863) | Phase 2 | Terminated | 10 | Biopsy-driven targeted therapy optimisation in BRAF-mutant melanoma; too small to be informative |
| [NCT03944356](https://clinicaltrials.gov/study/NCT03944356) | N/A | Completed | 232 | Observational study of adjuvant dabrafenib + trametinib in clinical practice |
| [NCT03340506](https://clinicaltrials.gov/study/NCT03340506) | Phase 4 | Recruiting | 100 | Roll-over study for long-term safety of dabrafenib and/or trametinib |
| [NCT07440290](https://clinicaltrials.gov/study/NCT07440290) | Phase 2/3 | Recruiting | 30 | DETERMINE platform trial: dabrafenib + trametinib in BRAF V600-mutant cancers |
| [NCT05275374](https://clinicaltrials.gov/study/NCT05275374) | Phase 1/2 | Not yet recruiting | 221 | XP-102 with trametinib in BRAF V600-mutant solid tumours; no data yet |

Most of these trials test trametinib in combination or across tumour types, so they do not isolate its effect in non-cutaneous melanoma. The expanded access study NCT02416232 is no longer available and provides no efficacy evidence.

## Literature Evidence

No literature was identified for choroideremia. The table below covers the melanoma-subtype predictions, where only indirect evidence exists.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40853557](https://pubmed.ncbi.nlm.nih.gov/40853557/) | 2025 | Review | JAMA | General review of cutaneous melanoma (epidemiology and management); indirect evidence |
| [31361915](https://pubmed.ncbi.nlm.nih.gov/31361915/) | 2020 | Case report/Review | Clin Exp Dermatol | Two BRAF-mutated conjunctival melanomas of epithelioid type, treated with vemurafenib, plus literature review |
| [31747798](https://pubmed.ncbi.nlm.nih.gov/31747798/) | 2019 | Case report/Review | J Investig Med High Impact Case Rep | Lacrimal sac melanoma in 15 Japanese patients (case report and review) |
| [41209431](https://pubmed.ncbi.nlm.nih.gov/41209431/) | 2026 | Case report | Oncol Lett | Combined BRAF/MEK inhibition for BRAF-mutant melanoma brain metastases in pregnancy |
| [37756677](https://pubmed.ncbi.nlm.nih.gov/37756677/) | 2025 | Case report | Retin Cases Brief Rep | Rapid resolution of choroidal metastasis of cutaneous melanoma after combined targeted therapy |
| [42583475](https://pubmed.ncbi.nlm.nih.gov/42583475/) | 2026 | Case report | Ann Med Surg | Early metastatic BRAF V600E-mutant melanoma without a known primary lesion |

All of this is case-level or general review evidence. No RCTs were found.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02409658 | MEKINIST | Not specified | Not specified |
| 02409623 | MEKINIST | Not specified | Not specified |
| 02539993 | MEKINIST | Not specified | Not specified |

All three licences are valid single-ingredient products.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions:** 17 records were retrieved. Fifteen are interactions rated **Moderate**:
  - Fostamatinib
  - Elagolix
  - Apalutamide
  - Brigatinib
  - Dabrafenib
  - Encorafenib
  - Isavuconazonium
  - Lasmiditan
  - Midostaurin
  - Sarecycline
  - Enzalutamide
  - Erdafitinib
  - Gilteritinib
  - Idelalisib
  - Tucatinib

  The other two records are target-pharmacology entries (MEK1 and MEK2), not interactions.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, choroideremia)

**Rationale:**
- Choroideremia is supported only by a model score, with no trials, no literature, and no plausible mechanistic link between MEK inhibition and CHM-related Rab prenylation defects.
- Non-cutaneous melanoma has the strongest evidence among the predictions (L2, with several Phase 1/2 trials). However, these trials are mostly combination or tumour-agnostic, and the indication is close to the already approved melanoma use. It is best treated as a research question rather than a Go.
- The remaining melanoma subtypes are supported only by case reports or general reviews, and several are mostly covered by the existing indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- Trials or studies that isolate trametinib's effect in specific non-cutaneous melanoma subtypes, stratified by mutation (BRAF, NRAS, NF1, GNAQ/GNA11)
- Any preclinical or mechanistic evidence for MEK inhibition in choroideremia, before this prediction is pursued further
- Approved indication text for the Canadian MEKINIST licences, to confirm the label scope
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

