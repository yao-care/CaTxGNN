---
layout: default
title: Bempedoic Acid
parent: Model Prediction Only (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid: From LDL-C Lowering to Hyperthyroidism

## One-Sentence Summary

Bempedoic acid is an ATP-citrate lyase (ACL) inhibitor that lowers LDL cholesterol, and it is marketed in Canada as NILEMDO.
The TxGNN model predicts it may be effective for **hyperthyroidism**, but there are **0 clinical trials** and **1 publication** (a review about a different drug), so this is a **model prediction only**.
The prediction most likely reflects a network artifact rather than real biology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | LDL-C lowering (hypercholesterolemia); the Canadian license record has no indication text |
| Predicted New Indication | Hyperthyroidism |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Based on known information, bempedoic acid inhibits ATP-citrate lyase upstream of HMG-CoA reductase. This reduces cholesterol synthesis in the liver and upregulates LDL receptors, which lowers LDL-C.

**The hyperthyroidism prediction is not mechanistically plausible.** Bempedoic acid has no known antithyroid activity. The high score most likely comes from graph proximity through lipid metabolism and thyroid hormone analogs, which is a network artifact rather than biology. The same pattern appears in other thyroid-related predictions in this list, such as thyroid hormone resistance and hyperthyroxinemia.

**Predictions with more support in this list:**
- **Homozygous familial hypercholesterolemia (HoFH)** (rank 6, score 99.48%, evidence level L3) is the only prediction with real supporting evidence. It is a close extension of the approved LDL-C-lowering use rather than a distant repurposing.
  - Efficacy is expected to be limited, because HoFH patients have little or no LDL receptor function.
  - Preclinical data in LDLR-deficient Yucatan miniature pigs show LDL-C lowering and attenuated atherosclerosis ([PMID 29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/)).
  - A real-world HoFH study ([PMID 41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/), 2026, *Journal of Clinical Lipidology*) is the main direct clinical evidence. Its design and effect size need to be verified.
- **Cytomegalovirus infection** (rank 5) is only speculative. Herpesviruses depend on host lipid synthesis, so ACL inhibition could theoretically affect them, but there is no supporting data.
- **Veterinary diseases (bovine herpesvirus) and osteoporosis-related predictions** have no supported mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40549098](https://pubmed.ncbi.nlm.nih.gov/40549098/) | 2025 | Review | Drugs | Approval review of tiratricol (a thyroid hormone analogue) for MCT8 deficiency. It does not study bempedoic acid and gives no support for this prediction. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2562782 | NILEMDO |

Dosage form, manufacturer and approved indication text are not listed in the license record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hyperthyroidism prediction has no clinical trials, no relevant literature and no plausible mechanism, so it remains at model-prediction level (L5). The only literature hit concerns a different drug. HoFH is the one prediction worth following up, but it is a near-label extension rather than a new-disease repurposing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Confirmation of the approved indication and dosage form for DIN 2562782
- Detailed mechanism of action data from DrugBank
- For HoFH: verification of the study design and effect size of PMID 41274797, and retrieval of the 7 publications not provided (10 of 17 were supplied)
- For hyperthyroidism: no action recommended unless independent preclinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

