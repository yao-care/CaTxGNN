---
layout: default
title: Sacituzumab Govitecan
parent: Model Prediction Only (L5)
nav_order: 823
evidence_level: L5
indication_count: 10
---

# Sacituzumab Govitecan
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

# Sacituzumab Govitecan: From Its Current Oncology Use to Drug-Induced Osteoporosis

## One-Sentence Summary

Sacituzumab govitecan (Canadian brand TRODELVY) is a Trop-2-directed antibody-drug conjugate carrying a cytotoxic SN-38 payload.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but **0 clinical trials** and **0 publications** support this prediction.
It is a model prediction only and should be treated as a hypothesis, not a finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

The approved indication text is not recorded in the Evidence Pack, so the original indication is not listed here.

---

## Why is This Prediction Reasonable?

On the available evidence, it is not well supported. Sacituzumab govitecan combines a Trop-2-targeting antibody with SN-38, a topoisomerase I inhibitor. Detailed mechanism data and the recorded original indications are not available in the Evidence Pack.

Cytotoxic therapy is generally a bone-health concern rather than a treatment for bone loss. No mechanistic link to osteoporosis was identified. The high score (0.998) comes from the TxGNN knowledge-graph model alone, and without original-indication and mechanism data it is hard to interpret.

The other nine predictions point the same way:
- They are all ocular conditions: diabetic retinopathy, severe nonproliferative diabetic retinopathy, diabetic cataract, and several cataract subtypes. All are L5 with no trials or literature.
- Several have identical scores, such as cortical and nuclear senile cataract at 98.55%. Many are parent and child terms of one another. This points to disease-ontology proximity in the graph rather than drug-specific biology.
- These predictions are not independent evidence for one another.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2520788 | TRODELVY |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic topoisomerase I inhibitor (SN-38) payload |
| Myelosuppression Risk | Expected to be significant; the prediction rationale notes myelosuppressive and other systemic toxicities. Please refer to the package insert for quantified rates. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high TxGNN score with no clinical trials, no literature and no plausible mechanism. A cytotoxic drug with systemic toxicity is an unlikely treatment for drug-induced osteoporosis, and the ocular predictions look like ontology artifacts.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action and original indication data (e.g., from DrugBank)
- Any preclinical or clinical signal linking the drug or its SN-38 payload to bone metabolism or ocular disease
- Route-compatibility and similarity-to-original-indication assessments, both still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

