---
layout: default
title: Lomitapide
parent: Model Prediction Only (L5)
nav_order: 550
evidence_level: L5
indication_count: 10
---

# Lomitapide
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

# Lomitapide: From Homozygous Familial Hypercholesterolemia to Marcothrombocytopenia with Mitral Valve Insufficiency

## One-Sentence Summary

Lomitapide is an oral lipid-lowering drug that inhibits microsomal triglyceride transfer protein (MTP). It is used for homozygous familial hypercholesterolemia (HoFH).
The TxGNN model predicts it may be effective for **marcothrombocytopenia with mitral valve insufficiency**, but **0 clinical trials** and **0 publications** support this prediction, and no plausible mechanism links the two.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Homozygous familial hypercholesterolemia (inferred from trials and literature; the license records contain no indication text) |
| Predicted New Indication | Marcothrombocytopenia with mitral valve insufficiency |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. From the literature, lomitapide inhibits MTP, which blocks the assembly of apoB-containing lipoproteins (VLDL and chylomicrons) in the liver and gut. This lowers LDL-C and apoB.

This mechanism has no known role in platelet production or in heart valve disease. The new indication is a platelet and valve disorder, so it is biologically unrelated to lipoprotein assembly. The high TxGNN score most likely reflects the closeness of nodes in the knowledge graph. Nine of the ten top-ranked predictions are platelet disorders with the same lack of mechanistic support, which points to a graph artifact rather than a true therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2420341 | JUXTAPID |
| 2420376 | JUXTAPID |
| 2420384 | JUXTAPID |

## Safety Considerations

- **Key Warnings**: The evidence pack notes a hepatotoxicity boxed warning and hepatic steatosis warnings for lomitapide. It also notes that the drug has not been studied in neonates, which matters for the neonatal thrombocytopenia predictions.

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature, and no plausible mechanism. Lomitapide also carries a hepatotoxicity boxed warning, so exposing patients to it without supporting evidence is not justified.

**To proceed, the following is needed:**
- Any mechanistic or preclinical evidence linking MTP inhibition to platelet or valve pathology
- Confirmation of the drug's original indication from the current Health Canada product monograph, since the license records contain no indication text
- Package insert warnings and contraindications from Health Canada

**Note on a better-supported prediction:**
Rank 9, **hyperlipoproteinemia** (score 99.74%), has L1 evidence and a "Proceed with Guardrails" recommendation. It is most likely an existing approved use (HoFH) rather than true repurposing. Supporting evidence includes:
- Completed Phase 3 studies: [NCT00730236](https://clinicaltrials.gov/study/NCT00730236) (n=29), [NCT02173158](https://clinicaltrials.gov/study/NCT02173158) (n=9) and [NCT04681170](https://clinicaltrials.gov/study/NCT04681170) (n=46, paediatric)
- Randomized Phase 2 studies: [NCT00559962](https://clinicaltrials.gov/study/NCT00559962) (n=260) and [NCT00690443](https://clinicaltrials.gov/study/NCT00690443) (n=44)
- Pivotal publication: [PMID 23122768](https://pubmed.ncbi.nlm.nih.gov/23122768/) (Lancet, 2013)
- Long-term cardiovascular outcome data are still pending ([NCT06832371](https://clinicaltrials.gov/study/NCT06832371)).
- Guardrails: monitor liver enzymes and hepatic fat, and restrict use to a REMS-type program.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

