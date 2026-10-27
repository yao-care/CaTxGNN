---
layout: default
title: Naphazoline
parent: Model Prediction Only (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Naphazoline: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Temporary relief of eye redness (vasoconstrictor). The Canadian licen…"
monitor_inn: "Naphazoline"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "primary hereditary glaucoma", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "open-angle glaucoma", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Naphazoline
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

## Naphazoline: From Ocular Redness Relief to Hypotrichosis Simplex of the Scalp
{: .text-alpha }

## One-Sentence Summary

Naphazoline is a topical alpha-adrenergic vasoconstrictor, marketed in Canada mainly in eye drops that temporarily relieve eye redness.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but **no clinical trials and no publications** currently support this direction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Temporary relief of eye redness (vasoconstrictor). The Canadian licence records did not include indication text, so this comes from pharmacology reference data. |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. From pharmacology reference data, naphazoline acts on alpha-1A, alpha-2A and alpha-2C adrenoceptors. By narrowing swollen blood vessels in the eye, it temporarily reduces redness.

The link to the predicted indication is weak. Hypotrichosis simplex of the scalp is a hereditary disorder of hair follicle development, and no mechanism connects alpha-adrenergic vasoconstriction to it. The high score most likely reflects the model's network proximity to other hair-related disease nodes rather than a biological rationale. If anything, vasoconstriction would be expected to reduce scalp blood flow. By comparison, hair-loss treatments such as minoxidil are vasodilators, so the pharmacology points in the opposite direction.

The other top predictions (congenital hypotrichosis milia, alopecia areata, alopecia, hypertrichosis, and several rare malformation syndromes) also lack mechanistic support and have no trials or publications. Two eye-related predictions, primary hereditary glaucoma and open-angle glaucoma, have some class-level plausibility, because other alpha-agonists such as brimonidine and apraclonidine lower intraocular pressure. Naphazoline itself is not an established IOP-lowering drug, and it may carry risk in eyes prone to angle closure.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top predicted indication, currently no related literature is available.

For the open-angle glaucoma prediction (rank 8), one paper was retrieved, but it does not study naphazoline:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1295525](https://pubmed.ncbi.nlm.nih.gov/1295525/) | 1992 | Other | Australian and New Zealand Journal of Ophthalmology | Effect of topical corticosteroids on laser-induced peripheral anterior synechiae after argon laser trabeculoplasty. It does not evaluate naphazoline, so it provides no direct evidence. |

## Canada Market Information

All 8 authorizations are valid single-ingredient products. The compiled records do not include dosage form or approved indication text.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02248060 | CLEAR EYES | Not available | Not available |
| 00001147 | ALBALON | Not available | Not available |
| 02242764 | VISINE FOR ALLERGY WITH ANTIHISTAMINE | Not available | Not available |
| 00674354 | COLLYRE BLEU LAITER | Not available | Not available |
| 02360837 | CLEAR EYES EXTRA STRENGTH REDNESS RELIEF | Not available | Not available |

Three more valid licences are held: SOOTHE ALLERGY (00750794), NAPHCON A (00481408) and CLEAR EYES ALLERGY (02248059).

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

Supplementary information from the knowledge graph (disease-level contraindication links, not label text):
- **Contraindication-related conditions**: hypertension and hypertensive disorders, cardiovascular and heart disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, angle-closure (closed-angle) glaucoma, hyperthyroidism (Graves disease, thyrotoxicosis), eye infections, and conjunctivitis.
- **Pharmacological targets**: alpha-1A, alpha-2A and alpha-2C adrenoceptors (human). A mouse TAAR4P/Taar4 target is also listed. No specific drug-drug interactions were identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials or relevant publications, and the pharmacology (vasoconstriction) does not support a benefit in hair-growth disorders. The knowledge-graph contraindication signals add further caution.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) to allow a proper mechanistic analysis
- Health Canada package insert warnings, contraindications, dosage forms and approved indications
- Preclinical or mechanistic evidence that links alpha-adrenergic agonism to hair follicle biology
- A review of whether the glaucoma-related predictions merit separate evaluation, given the angle-closure risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

