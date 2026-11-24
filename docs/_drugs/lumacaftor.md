---
layout: default
title: Lumacaftor
parent: Model Prediction Only (L5)
nav_order: 565
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Lumacaftor"
predicted_indications: ["leprosy"]
description: "Lumacaftor: predicted new indication Leprosy (evidence level L5). In Canada: 5 DINs (5 marketed)"
---

# Lumacaftor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Lumacaftor: Leprosy
{: .text-alpha }

## One-Sentence Summary

Lumacaftor is a CFTR corrector originally used to treat cystic fibrosis (marketed in Canada as ORKAMBI).
The TxGNN model predicts it may be effective for **leprosy**,
but **no clinical trials and no publications** currently support this prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 5 of 5) |
| Number of DINs | 5 (marketed: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lumacaftor and ivacaftor (a combination product containing lumacaftor): "Lumacaftor improves the conformational stability of F508del-CFTR, resulting in increased processing and trafficking of mature protein to the cell surface. In vitro studies have demonstrated that both lumacaftor and ivacaftor act directly on the CFTR protein in primary human bronchial epithelial cultures and other cell lines harboring the F508del-CFTR mutation to increase the quantity, stability, and function of F508del-CFTR at the cell surface, resulting in increased chloride ion transport." ([DailyMed: Orkambi (lumacaftor and ivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3fc1c40e-cfac-47a1-9e1a-61ead3570600), label version 2026-03-24; accessed 2026-11-19.) Based on general knowledge, lumacaftor is a CFTR corrector that improves the folding and trafficking of F508del-CFTR protein, and its use in cystic fibrosis is established.

Leprosy is a chronic infection caused by *Mycobacterium leprae*, and no plausible CFTR-related pathway is evident. The high TxGNN score (0.9944) is a computational prediction from the TxGNN model (deep learning) only. It may reflect similarities the model learned between related diseases, not biological evidence, and the prediction is not supported by any trial or publication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02451379 | ORKAMBI | IVACAFTOR; LUMACAFTOR | Marketed |
| 02463040 | ORKAMBI | IVACAFTOR; LUMACAFTOR | Marketed |
| 02483831 | ORKAMBI | IVACAFTOR; LUMACAFTOR | Marketed |
| 02483858 | ORKAMBI | IVACAFTOR; LUMACAFTOR | Marketed |
| 02537087 | ORKAMBI | IVACAFTOR; LUMACAFTOR | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. The first 20 returned are summarized below.
  - **Major**: Eliglustat, Naldemedine, Naloxegol, Rolapitant
  - **Moderate**: Acetohexamide, Betamethasone, Bupropion, Dexlansoprazole, Esomeprazole, Glimepiride, Lansoprazole, Linagliptin, Nitisinone, Omeprazole, Pantoprazole, Pioglitazone, Prednisone, Rabeprazole, Ranitidine, Repaglinide

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN score, with no clinical trials, no publications, and no plausible mechanistic link between CFTR correction and *M. leprae* infection. Lumacaftor also carries a substantial interaction burden, so there is no basis to advance.

**To proceed, the following is needed:**
- Mechanism of action data and a testable biological hypothesis linking CFTR correction to leprosy
- Preclinical or in vitro evidence (e.g., activity against *M. leprae* or relevant host pathways)
- Health Canada package insert warnings and contraindications, to enable safety screening
- A review of the interaction profile in the context of standard leprosy regimens

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Orkambi (lumacaftor and ivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3fc1c40e-cfac-47a1-9e1a-61ead3570600) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

