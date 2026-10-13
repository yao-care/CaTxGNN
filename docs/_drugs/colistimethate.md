---
layout: default
title: Colistimethate
parent: Model Prediction Only (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Colistimethate
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

# Colistimethate: From Gram-Negative Bacterial Infection to Osteoarthritis

## One-Sentence Summary

Colistimethate is a polymyxin antibiotic that disrupts the outer membrane of Gram-negative bacteria. The TxGNN model predicts it may be effective for **osteoarthritis**, but no clinical trials or publications currently support this direction, so the prediction rests on the model alone. Note that the original indication is not stated in the Canadian licence data compiled for this report; the antibacterial use is inferred from the drug class.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (polymyxin antibiotic, used against Gram-negative infections) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 97.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge of the drug class, colistimethate is a polymyxin antibiotic that disrupts the outer membrane of Gram-negative bacteria.

Osteoarthritis is a degenerative, non-infectious joint disease, so no mechanistic link to the original antibacterial use has been identified. The 97.8% score is a graph-based computational prediction, and the other top-ranked predictions show the same pattern:

- **Rheumatoid arthritis** (97.5%): no known immunomodulatory activity relevant to autoimmune synovitis.
- **Osteoarthritis susceptibility** (97.4%): a genetic susceptibility phenotype that overlaps with the osteoarthritis prediction, probably a graph-propagation artifact.
- **Gout** (96.8%): no link to urate metabolism or inflammasome activity. Renal toxicity could also worsen urate handling.
- **Rare skeletal and hepatic conditions** (pseudoachondroplasia, brachyolmia, hepatic porphyria, portal vein thrombosis, hepatoportal sclerosis, idiopathic copper-associated cirrhosis): no plausible mechanism. Several share identical scores, which points to a shared graph neighbourhood rather than a biological signal.

Systemic colistimethate also carries nephrotoxicity and neurotoxicity risks, which weigh against use in a chronic non-infectious condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02546639 | COLISTIMETHATE FOR INJECTION USP | Not specified | Not specified |

---

## Safety Considerations

**Drug Interactions** (33 interactions found in total; the 20 below were available for review):

- **Major (aminoglycosides):** kanamycin, neomycin, streptomycin
- **Major (other):** deferasirox
- **Major (iodinated contrast agents):** diatrizoate, iodipamide, iodixanol, iohexol, iopamidol, iopromide, iothalamic acid, ioversol, ioxilan
- **Moderate:** mesalazine, balsalazide, olsalazine, sulfasalazine, picosulfuric acid, exenatide, vancomycin

Systemic use carries nephrotoxicity and neurotoxicity risks. Many of the major interactions involve other nephrotoxic or ototoxic agents, so combined use needs close monitoring.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature, and no plausible mechanism. The known nephrotoxicity and neurotoxicity make a chronic non-infectious indication unattractive.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Mechanism of action data, to test whether any biologically plausible link to osteoarthritis exists
- Approved indication and dosage form details for the Canadian licence
- Any preclinical or clinical evidence for osteoarthritis, together with an assessment of whether a route of administration compatible with the condition exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

