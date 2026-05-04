---
layout: default
title: Difluprednate
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
---

# Difluprednate
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

# Difluprednate: From Anterior Uveitis to Iris Disease

## One-Sentence Summary

Difluprednate (Durezol®) is a high-potency fluorinated corticosteroid ophthalmic emulsion approved in the United States and Japan for anterior uveitis and post-surgical ocular inflammation, but currently not marketed in Canada.
The TxGNN model predicts it may be effective for **Iris Disease** — a broad category encompassing anterior uveitis, iritis, and intraocular inflammation — which aligns directly with the drug's known mechanism of action.
This prediction is supported by **3 completed Phase 3 clinical trials** and **2 publications**, placing it at evidence level **L1** and making it the only actionable finding among all 10 ranked predictions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anterior uveitis; post-surgical ocular inflammation (US FDA approved; no Canadian approval on record) |
| Predicted New Indication | Iris Disease |
| TxGNN Prediction Score | 99.16% (TxGNN rank #10; highest evidence-ranked among all predictions) |
| Evidence Level | L1 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Difluprednate (6α,9α-difluoroprednisolone 21-acetate 17-butyrate) is a synthetic fluorinated corticosteroid that acts as a glucocorticoid receptor agonist. Upon binding its receptor, it suppresses the NF-κB signalling pathway, reducing the production of key inflammatory mediators — including IL-1β, TNF-α, and prostaglandin E2 (PGE2). Critically, its 0.05% ophthalmic emulsion formulation is engineered to penetrate the corneal epithelium and reach therapeutic concentrations in the anterior chamber of the eye, the precise compartment where iris inflammation originates.

Iris disease — including anterior uveitis, iritis, and post-surgical intraocular inflammation — is pathologically driven by the same inflammatory cascade that difluprednate is designed to interrupt. This is not an extrapolation across disease categories; it is a direct mechanistic match. The drug's US FDA approval for endogenous anterior uveitis and post-cataract surgery inflammation validates this biological rationale, and the pharmacokinetic literature confirms that the ophthalmic emulsion achieves superior anterior chamber penetration compared to other corticosteroid formulations.

Although difluprednate ranks #10 in TxGNN score, it ranks first in clinical utility among all 10 predictions. The nine higher-ranked indications — including familial adrenal hypoplasia, seborrheic keratosis, PAGOD syndrome, and nephrotic syndrome — are either structurally incompatible with an ophthalmic-only formulation, lack biological plausibility, or represent noise from knowledge graph generalisation. Iris disease is the only indication where mechanism, formulation, and clinical evidence converge.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00407056](https://clinicaltrials.gov/study/NCT00407056) | Phase 3 | Completed | 20 | Open-label Phase 3 study directly evaluating difluprednate 0.05% ophthalmic emulsion for severe anterior uveitis (including panuveitis); the core pivotal study establishing efficacy for the iris disease indication |
| [NCT01124045](https://clinicaltrials.gov/study/NCT01124045) | Phase 3 | Completed | 80 | Multicentre, randomised, double-blind active-controlled study comparing difluprednate (Durezol™) vs. prednisolone acetate 1% (Pred Forte™) for post-cataract surgery inflammation in children aged 0–3 years; a key trial contributing to FDA approval |
| [NCT03693989](https://clinicaltrials.gov/study/NCT03693989) | Phase 3 | Completed | 178 | Double-blind, multicentre Phase 3 RCT comparing PRO-145 (a difluprednate-based ophthalmic emulsion) vs. prednisolone acetate 1% for anterior chamber inflammation and pain following phacoemulsification; indirectly supports difluprednate's efficacy and tolerability profile |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [27594198](https://pubmed.ncbi.nlm.nih.gov/27594198/) | 2016 | Case Report | *Ophthalmology* | Long-term management of panuveitis and iris heterochromia in an Ebola survivor; demonstrates real-world clinical application of difluprednate in complex, refractory iris and uveal inflammation |
| [21182429](https://pubmed.ncbi.nlm.nih.gov/21182429/) | 2011 | Preclinical PK Study | *J Ocular Pharmacol Ther* | Characterises the pharmacokinetic and pharmacodynamic profile of difluprednate ophthalmic emulsion via glucocorticoid receptor-binding bioassay in rabbits; confirms superior anterior chamber penetration and receptor-binding activity compared to other ophthalmic corticosteroids, providing mechanistic underpinning |

---

## Canada Market Information

Difluprednate currently has **no Drug Identification Numbers (DINs)** issued in Canada and is not marketed in any dosage form. No Health Canada approved product information is available.

For reference, the US FDA-approved formulation is:

| Product Name | Dosage Form | Approved Indication (US) |
|---------|------------|--------------------------|
| Durezol® (difluprednate 0.05%) | Ophthalmic emulsion | Inflammation and pain associated with ocular surgery; endogenous anterior uveitis |

A Health Canada New Drug Submission (NDS) would be required before Canadian clinical use.

---

## Safety Considerations

Formal warning and contraindication data for difluprednate are not available in this evidence pack. Please refer to the full product prescribing information (US FDA label for Durezol® or equivalent) for complete safety details.

As a high-potency fluorinated corticosteroid, the following class-effect risks are clinically relevant and should be confirmed against the product monograph prior to any regulatory or clinical planning:

- **Intraocular pressure (IOP) elevation**: Corticosteroid-induced ocular hypertension and steroid-response glaucoma; IOP monitoring is mandatory
- **Posterior subcapsular cataract formation**: Risk increases with duration of use
- **Delayed ocular wound healing**: Relevant in post-surgical settings
- **Susceptibility to ocular infection**: Masking of signs; contraindicated in active viral, bacterial, or fungal ocular infections

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 clinical trials directly support difluprednate's efficacy in anterior uveitis and post-surgical intraocular inflammation. The drug is already approved for these indications in the US and Japan, and its mechanism of action provides a direct, high-confidence match to iris disease pathophysiology. The absence of Canadian approval is the primary barrier, not a lack of clinical evidence.

**To proceed, the following is needed:**

- Retrieve the Health Canada product monograph or US FDA full prescribing information (Durezol®) to complete the safety assessment, particularly IOP monitoring requirements and contraindications
- Confirm mechanism of action details via DrugBank API query (DB06781) to close the identified data gap
- Assess Health Canada NDS pathway requirements and whether existing US/Japanese approval data can serve as bridging evidence
- Evaluate unmet clinical need in Canada relative to currently available alternatives (e.g., prednisolone acetate 1% generics, loteprednol etabonate)
- Consult Canadian ophthalmology and uveitis specialists to confirm clinical positioning and identify target patient populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

