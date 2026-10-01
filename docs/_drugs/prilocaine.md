---
layout: default
title: Prilocaine
parent: Model Prediction Only (L5)
nav_order: 762
evidence_level: L5
indication_count: 10
---

# Prilocaine
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

# Prilocaine: From Local Anesthesia to Papillary Conjunctivitis

## One-Sentence Summary

Prilocaine is an amide local anesthetic, marketed in Canada in dental injections, a topical cream and an oral gel.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **0 clinical trials** and **0 publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (inferred from product types; approved indication text is not available in the Canadian records) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, prilocaine is a local anesthetic that is used in dental injections and in the lidocaine/prilocaine (EMLA) cream. It is generally understood to block voltage-gated sodium channels and so dampen nerve firing.

The only plausible link to papillary conjunctivitis is symptom relief. A topical anesthetic might ease discomfort on the ocular surface. This would not treat the underlying inflammatory or allergic process, so it is not a disease-modifying mechanism. No trials or publications were found to test the idea. The prediction is therefore a model output with no supporting evidence.

For context, other predictions for prilocaine are better supported than this top-ranked one. **Neuralgia** (score 99.34%, L3) has small, older reports of lidocaine/prilocaine cream in postherpetic neuralgia from 1989–1999. That evidence is for the combination product, not prilocaine alone. **Migraine** (L4) has nerve-block trials, but none clearly identifies prilocaine as the agent. Neuralgia is the more promising direction for follow-up.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage form and approved indication text are not available for these authorizations.

| DIN | Product Name |
|---------|------|
| 2435276 | 4% Citanest Plain Dental |
| 2325993 | Oraqix |
| 2347695 | 4% Citanest Forte Dental with Epinephrine 1:200,000 |
| 886858 | EMLA Cream |
| 393746 | Prilocaine HCl 4% Epinephrine 1:200000 Injection |

One further DIN is not listed above (6 in total).

## Safety Considerations

Please refer to the package insert for safety information.

Literature retrieved for other predicted indications reports serious events after topical EMLA (lidocaine/prilocaine) use on barrier-compromised skin. These include methemoglobinemia and seizures in a young child with atopic dermatitis, and purpura. Local anesthetic contact allergy, including to prilocaine, has also been reported. Any ocular or mucosal use would need separate safety assessment, because no ophthalmic product is among the Canadian authorizations.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no trials or publications for papillary conjunctivitis, and the only plausible mechanism is symptomatic relief rather than treatment of the disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence for prilocaine in papillary conjunctivitis
- Route compatibility assessment, since no ophthalmic formulation is currently authorized
- Consideration of redirecting effort to neuralgia, which has the strongest supporting evidence among the predictions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

