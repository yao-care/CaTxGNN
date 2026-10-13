---
layout: default
title: Tenapanor
parent: Model Prediction Only (L5)
nav_order: 890
evidence_level: L5
indication_count: 10
---

# Tenapanor
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

# Tenapanor: From Constipation-Predominant Irritable Bowel Syndrome to Candidiasis

## One-Sentence Summary

Tenapanor is a gut-restricted inhibitor of the intestinal sodium/hydrogen exchanger NHE3. It is marketed for irritable bowel syndrome with constipation (IBS-C) and for lowering serum phosphorus in dialysis patients with chronic kidney disease.
The TxGNN model predicts it may be effective for **candidiasis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data. Clinical-use information indicates IBS-C and hyperphosphatemia in CKD patients on dialysis. |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 97.17% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tenapanor inhibits NHE3 (encoded by *SLC9A3*) in the gut. It is minimally absorbed and its action is confined to the intestinal lumen. This reduces sodium absorption and phosphate uptake through the paracellular pathway. The detailed mechanism-of-action field was not available in the data compiled for this report, so this description relies on the pharmacology information that was provided.

No clear mechanistic path links NHE3 inhibition to antifungal activity or candidiasis. The high TxGNN score reflects proximity in a knowledge graph, not biological or clinical evidence. Because systemic exposure to tenapanor is negligible, a direct antifungal effect is also unlikely. This prediction should be treated as a hypothesis and not as a development lead.

The other nine predictions (adrenocortical insufficiency, familial adrenal hypoplasia, primary cutaneous T-cell lymphoma, Stevens-Johnson syndrome, PAGOD syndrome, aphthous stomatitis, 46,XY disorder of sex development, SJS/TEN overlap syndrome and Crohn's colitis) also have no supporting studies. Crohn's colitis is the most biologically coherent of them, because tenapanor acts in the gut. Even so, its laxative effect could worsen active colitis, so it warrants preclinical investigation only.

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
| 02498049 | IBSRELA | Not specified | Not specified in the licence data |

---

## Safety Considerations

- **Drug Interactions**: The interaction search completed with one pharmacology entry. It describes tenapanor's target, sodium/hydrogen exchanger 3 (NHE3), and not an interaction with another drug. No clinically graded drug-drug interactions were identified.

Please refer to the package insert for key warnings and contraindications. The Health Canada label text was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials or publications, and no plausible mechanism links gut-restricted NHE3 inhibition to candidiasis. The drug has negligible systemic exposure, which further weakens the case.

**To proceed, the following is needed:**
- The Health Canada package insert, to complete the warnings and contraindications review
- Detailed mechanism-of-action data from DrugBank
- A mechanistic rationale and preclinical antifungal data (for example in vitro activity against *Candida*) before any clinical consideration
- If an alternative direction is pursued, preclinical studies in Crohn's colitis, with attention to the risk of worsening diarrhoea
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

