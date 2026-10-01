---
layout: default
title: Propylene Glycol
parent: Model Prediction Only (L5)
nav_order: 772
evidence_level: L5
indication_count: 10
---

# Propylene Glycol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Propylene Glycol: From Nasal and Eye Lubricant Use to Bronchitis

## One-Sentence Summary

Propylene glycol is a humectant and excipient. In Canada it appears in marketed nasal moisturizing products and lubricant eye drops.
The TxGNN model predicts it may be effective for **bronchitis**, but this rests on a graph-based score alone. The **4 clinical trials** and **3 publications** retrieved do not test propylene glycol as a treatment for bronchitis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the record (marketed as nasal gel/mist and lubricant eye drops/artificial tears) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Propylene glycol is mainly used as a humectant and solvent in nasal and ocular lubricant products. No therapeutic mechanism against bronchitis is established, and no anti-bronchitic action is known.

The high TxGNN score is a graph-based association only. The trials retrieved for this prediction test cyclosporine inhalation solution, in which propylene glycol is likely just the vehicle. The literature points the other way: inhaled propylene glycol, such as e-cigarette aerosol, is discussed as a potential airway irritant, which suggests possible harm rather than benefit.

The other top-ranked predictions are also weak:
- **Diabetic retinopathy:** the only apparent signal is probably a naming artifact. PMID 39006273 studies propylene glycol *mannate sulfate*, a different compound.
- **Cataract subtypes (cortical, nuclear senile, senile, diabetic, immature, mature, craniostenosis):** no clinical trials or supporting literature were found. The one paper retrieved (diabetic cataract) is an ocular insert formulation study in which propylene glycol is only a formulation component.
- **Severe nonproliferative diabetic retinopathy:** no trials or literature were found.

## Clinical Trial Evidence

All four trials were graded low relevance (C): the tested drug is cyclosporine, and the condition is bronchiolitis obliterans in transplant recipients, not bronchitis.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00755781](https://clinicaltrials.gov/study/NCT00755781) | Phase 3 | Completed | 284 | Cyclosporine inhalation solution to prevent bronchiolitis obliterans syndrome in lung transplant recipients |
| [NCT01287078](https://clinicaltrials.gov/study/NCT01287078) | Phase 2 | Completed | 25 | Cyclosporine inhalation solution for bronchiolitis obliterans in lung and stem cell transplant recipients |
| [NCT01273207](https://clinicaltrials.gov/study/NCT01273207) | Phase 2 | Completed | 7 | Extended-access study of cyclosporine inhalation solution |
| [NCT00938236](https://clinicaltrials.gov/study/NCT00938236) | Phase 3 | Terminated | 17 | Open-label extension of cyclosporine inhalation solution in lung transplant recipients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | Whether chronic e-cigarette use may cause lung disease, including chronic bronchitis and COPD |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | E-cigarette constituents as airway irritants and potential links to asthma |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Preclinical (animal) | Respir Res | Quercetin reduced lung inflammation in a mouse COPD model; not related to propylene glycol |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02352699 | RHINARIS NASAL GEL |
| 02354551 | RHINARIS NASAL MIST |
| 02321696 | LUBRICANT EYE DROPS / ARTIFICIAL TEARS |
| 00551805 | SECARIS |
| 02242370 | SOOTHE DRY EYES |

Dosage form and approved indication text are not provided in the record for these licenses.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No retrieved trial tests propylene glycol for bronchitis, and the literature raises an airway irritation concern for inhaled use. The Canadian products are nasal and ocular, so they are not a route match for a bronchial indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data, for example from DrugBank
- Evidence that propylene glycol itself, not a co-administered drug, has a therapeutic effect in bronchitis
- Assessment of route compatibility and the inhalation safety of propylene glycol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

