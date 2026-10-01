---
layout: default
title: Remdesivir
parent: Model Prediction Only (L5)
nav_order: 794
evidence_level: L5
indication_count: 10
---

# Remdesivir
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

# Remdesivir: From COVID-19 to Multiple Endocrine Neoplasia

## One-Sentence Summary

Remdesivir is an antiviral drug, and the evidence pack's own trials and literature describe its use for COVID-19. The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, a hereditary endocrine tumour syndrome. There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | COVID-19 (taken from the trial and literature context; the Health Canada licence record has no indication text) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Remdesivir is a nucleotide analog prodrug that inhibits viral RNA-dependent RNA polymerase. Detailed mechanism-of-action data from DrugBank are not currently available, so this description comes from the evidence pack's mechanistic notes.

Multiple endocrine neoplasia is a hereditary tumour syndrome driven by host genetic mutations, not by a virus. No plausible link exists between inhibiting a viral polymerase and treating this disease. The high TxGNN score (0.995) reflects a pattern in the knowledge graph, not a biological rationale.

The mechanistic review of the other top-ranked predictions reached the same conclusion:
- **HIV, feline AIDS and simian immunodeficiency virus infection:** these are retroviral infections that depend on reverse transcriptase, not on the RdRp that remdesivir targets.
- **HIV trials and papers:** every retrieved item concerns COVID-19, not HIV, so the raw counts (23 trials, 20 papers) are retrieval artifacts and not evidence.
- **Cytomegalovirus:** CMV is a DNA virus, and the literature only describes co-infection with COVID-19.
- **Leprosy:** the retrieved papers show clofazimine, a leprosy drug, acting against coronaviruses. That is the reverse direction.

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
| 2502143 | VEKLURY | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no mechanistic link to remdesivir's antiviral action. The high TxGNN score alone is not enough to justify further investment. The other top-ranked predictions are also unsupported or based on mismatched COVID-19 evidence.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings and contraindications) and the licensed indication text
- Detailed mechanism-of-action data from DrugBank
- A disease-specific biological rationale linking remdesivir to multiple endocrine neoplasia
- A disease-specific search for trials and literature that is not confounded by drug-name matches

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

