---
layout: default
title: Mesalazine
parent: Model Prediction Only (L5)
nav_order: 589
evidence_level: L5
indication_count: 7
---

# Mesalazine
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

# Mesalazine: From Ulcerative Colitis to Congenital Hypotrichosis with Juvenile Macular Dystrophy

## One-Sentence Summary

Mesalazine (5-aminosalicylic acid) is an anti-inflammatory aminosalicylate used mainly for inflammatory bowel disease such as ulcerative colitis.
The TxGNN model ranks **congenital hypotrichosis with juvenile macular dystrophy** as its top prediction, but there are **0 clinical trials** and **0 publications** supporting it, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis (inferred from the literature in the evidence pack; the Canadian licence records list no indication text) |
| Predicted New Indication | Congenital hypotrichosis with juvenile macular dystrophy |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 18 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, mesalazine is an aminosalicylate whose efficacy in ulcerative colitis is well established. Its anti-inflammatory effects are linked to prostaglandin and leukotriene inhibition and, in preclinical work, to PPAR-gamma signalling.

**This prediction is not mechanistically plausible.** Congenital hypotrichosis with juvenile macular dystrophy is a rare monogenic disorder caused by loss of function of the CDH3 gene. It has no inflammatory or PPAR-gamma component that mesalazine would address. The very high score (0.996) most likely reflects graph proximity in the knowledge graph rather than a real pharmacological link, and no trials or literature back it.

For context, two other TxGNN predictions for this drug have more supporting evidence and would be better places to focus:

- **Osteoarthritis (evidence level L4):** A 2024 preclinical study (PMID 38310093, *Nature Communications*) reports that 5-ASA suppresses osteoarthritis through the OSCAR-PPARγ axis. No human trials exist, and delivery to joint tissue is uncertain because mesalazine is formulated for local action in the gut.
- **Rheumatoid arthritis (evidence level L4):** The clinical evidence concerns sulfasalazine, not mesalazine alone. Several studies point to sulfapyridine, not 5-ASA, as the main active component in RA.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

The first five of 18 authorizations are shown. Dosage form and approved indication text are not listed in the licence records.

| DIN | Product Name |
|---------|------|
| 2529610 | OCTASA |
| 2465752 | OCTASA |
| 2545012 | MEZERA |
| 2112809 | SALOFALK |
| 2524481 | MEZERA |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature and no plausible mechanism for a CDH3-related disorder. It does not justify further investment.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking mesalazine to CDH3 loss-of-function pathology, and any supporting preclinical data
- Mechanism of action data for mesalazine from DrugBank
- Health Canada package insert warnings and contraindications, to complete safety screening
- Consider redirecting effort to the osteoarthritis prediction, which has preclinical support, and to the RA prediction, only if the question of whether 5-ASA contributes beyond sulfapyridine is of interest

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

