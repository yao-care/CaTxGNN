---
layout: default
title: Clobetasol Propionate
parent: Model Prediction Only (L5)
nav_order: 209
evidence_level: L5
indication_count: 7
---

# Clobetasol Propionate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Clobetasol Propionate: From Atopic Eczema and Dermatitis to Exanthem (Disease)

## One-Sentence Summary

Clobetasol propionate is a super-potent topical corticosteroid, originally used for inflammatory skin conditions such as atopic eczema, contact dermatitis, seborrheic dermatitis and scalp dermatosis.
The TxGNN model's top-ranked prediction is vulvar inverted follicular keratosis, but it has no supporting studies. The best-supported prediction is **Exanthem (disease)**, with **7 clinical trials** and **no publications**. These trials mainly concern oral lichen planus and lichen sclerosus, not exanthem itself, so the support is indirect.

> Note: The rank 1 prediction (vulvar inverted follicular keratosis) has no clinical trials or literature. This report focuses on rank 3 (exanthem), the first prediction with trial evidence, and mentions the others briefly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic eczema, dermatitis (contact, occupational, seborrheic), scalp dermatosis (the Canadian licence records contain no indication text) |
| Predicted New Indication | Rank 1: Vulvar inverted follicular keratosis (no evidence). Best-supported: Exanthem (disease), rank 3 |
| TxGNN Prediction Score | Rank 1: 99.46%. Exanthem: 99.26% |
| Evidence Level | Rank 1: L5. Exanthem: L1 as graded, but only indirectly relevant, so a more cautious reading is L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold (rank 1). Exanthem: Proceed with Guardrails, as a research question only |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Clobetasol propionate is a synthetic glucocorticoid that acts on the glucocorticoid receptor (NR3C1). Its anti-inflammatory and immunosuppressive effects are well established in inflammatory skin disease.

Exanthem is a broad term for inflammatory skin eruptions. The glucocorticoid mechanism fits this kind of inflammation, and this is the rationale behind the prediction. However, the trials listed under this term mostly concern **oral lichen planus** and **vulvar lichen sclerosus**. These are inflammatory mucocutaneous diseases, not true exanthems. The mapping to the predicted indication is therefore only partial.

For the other predictions, the rationale is weaker:
- **Vulvar inverted follicular keratosis** is a benign keratinocytic lesion related to seborrheic keratosis. A potent steroid is not expected to resolve it.
- **Acrodermatitis chronica atrophicans** is an infectious condition (Borrelia) treated with antibiotics. Steroids could worsen atrophy.
- **Acne keloidalis** has some plausibility, with one small open-label study (see below).
- **Neonatal dermatomyositis**: topical super-potent steroids in neonates raise serious safety concerns.
- **Interstitial lung disease in childhood connective tissue disease**: there is no plausible route for a topical drug to act on the lung.
- **Amyopathic dermatomyositis**: topical steroids are sometimes used as adjuncts for skin lesions, which gives some plausibility, but there is no evidence.

---

## Clinical Trial Evidence

Trials listed under the exanthem prediction:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02573883](https://clinicaltrials.gov/study/NCT02573883) | Phase 3 | Completed | 52 | Clobetasol 0.05% ointment vs fractionated CO2 laser in vulvar lichen sclerosus |
| [NCT04364555](https://clinicaltrials.gov/study/NCT04364555) | Phase 2/3 | Active, not recruiting | 90 | Placebo-controlled multicentre trial of topical clobetasol in symptomatic oral lichen planus |
| [NCT03026478](https://clinicaltrials.gov/study/NCT03026478) | Phase 2 | Unknown | 30 | Clobetasol vs betamethasone in Orabase with clotrimazole in oral lichen planus |
| [NCT03592342](https://clinicaltrials.gov/study/NCT03592342) | Phase 2 | Completed | 140 | Randomised placebo-controlled study of Rivelin®-CLO patches (0, 1, 5, 20 μg) in oral lichen planus, applied up to 6 times twice daily for 4 weeks |
| [NCT03386643](https://clinicaltrials.gov/study/NCT03386643) | Phase 2 | Completed | 22 | Probiotic B. lactis HN019 in oral lichen planus; clobetasol is likely background therapy, not the tested drug |
| [NCT07536737](https://clinicaltrials.gov/study/NCT07536737) | N/A | Completed | 65 | Photodynamic therapy vs topical corticosteroids on taste perception and salivary oxidative stress in oral lichen planus |
| [NCT07278999](https://clinicaltrials.gov/study/NCT07278999) | N/A | Recruiting | 60 | Photobiomodulation vs photodynamic therapy vs clobetasol (standard of care) in erosive oral lichen planus |

None of these trials tests exanthem directly. Ranks 1, 2 and 5 to 7 have no registered clinical trials.

---

## Literature Evidence

No publications were found for the exanthem prediction. The only literature in the data is for **acne keloidalis** (rank 4):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16047868](https://pubmed.ncbi.nlm.nih.gov/16047868/) | 2005 | Open-label study | Cutis | Clobetasol propionate 0.05% foam and betamethasone valerate 0.12% foam in 20 African American patients with mild to moderate acne keloidalis, treated for 8 to 12 weeks with a pulsed-dose regimen. It is small, uncontrolled and non-randomised. |

---

## Canada Market Information

Twenty valid single-ingredient licences are held; the first five are shown. Dosage form and approved indication text are not available in the data compiled for this report. The product names indicate topical formulations (solution, spray, ointment, cream, shampoo, scalp application).

| DIN | Product Name | Formulation (from product name) |
|---------|------|------|
| 02245522 | TARO-CLOBETASOL Topical Solution USP, 0.05% | Topical solution |
| 02489619 | TARO-CLOBETASOL Spray | Spray |
| 02026767 | MYLAN-CLOBETASOL Ointment | Ointment |
| 02024187 | MYLAN-CLOBETASOL Cream | Cream |
| 02490706 | ODAN CLOBETASOL Spray | Spray |

---

## Safety Considerations

**Contraindication-related disease associations (from the knowledge graph, not label text):** hyperglycaemia, adrenocortical insufficiency, Addison disease, diabetes mellitus, diabetic ketoacidosis, folliculitis, seborrheic dermatitis, glaucoma, skin atrophy, peripheral vascular disease, intermittent claudication, and peripheral arterial disease.

**Pharmacological interaction:** clobetasol acts on the glucocorticoid receptor (NR3C1). No drug-drug interactions were listed.

**Specific concerns for the predicted uses:**
- Skin atrophy is a listed association, which is relevant to acrodermatitis chronica atrophicans and long-term use.
- Systemic absorption and HPA axis suppression are a particular concern in neonates (neonatal dermatomyositis).

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold for the rank 1 prediction. Proceed with Guardrails for exanthem, as a research question only.**

**Rationale:**
- The top prediction (vulvar inverted follicular keratosis) rests on model score alone, with no trials or literature, and its mechanistic plausibility is low. Ranks 2, 5 and 6 are also prediction-only and either implausible or unsafe for topical use.
- The exanthem prediction carries an L1 grade because of a Phase 3 trial and a Phase 2/3 trial. These study lichen sclerosus and oral lichen planus, so the evidence supports related inflammatory conditions rather than exanthem itself. Clobetasol is already marketed in Canada in 20 products.

**To proceed, the following is needed:**
- Clarify whether "exanthem" in the model maps to any real clinical target, or whether lichen planus and lichen sclerosus should be assessed as separate indications.
- Review the trial populations and results, especially NCT02573883 and NCT04364555.
- Obtain the Canadian package insert warnings, contraindications and approved indications.
- Obtain detailed mechanism of action data.
- Verify the acne keloidalis study mapping and look for controlled evidence.
- Assess the route and formulation fit (oral mucosal patches, rinses, and topical forms) for any new indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

