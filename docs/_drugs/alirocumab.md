---
layout: default
title: Alirocumab
parent: Model Prediction Only (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: From Lipid Lowering to X-linked Ichthyosis (Without Steroid Sulfatase Deficiency)

## One-Sentence Summary

Alirocumab is a PCSK9-inhibiting monoclonal antibody that lowers LDL cholesterol, and it is marketed in Canada as PRALUENT.
The TxGNN model predicts it may be effective for **X-linked ichthyosis without steroid sulfatase deficiency**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | LDL-C lowering (lipid-lowering use; licence indication text was not supplied) |
| Predicted New Indication | Ichthyosis, X-linked, without steroid sulfatase deficiency |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Alirocumab is known to be a PCSK9 monoclonal antibody. By blocking PCSK9, it increases the availability of hepatic LDL receptors and lowers circulating LDL-C.

The predicted disease is a skin keratinization disorder. PCSK9 inhibition has no known effect on the pathways involved, and the review found no credible mechanistic link. The high score (0.994) reflects graph-based similarity in the knowledge graph, not biological or clinical support. The prediction ranks 10,308th overall in TxGNN's scoring, and no trials or literature back it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2453835 | PRALUENT |
| 2547732 | PRALUENT |
| 2453819 | PRALUENT |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical or literature support and no plausible mechanistic link to PCSK9 inhibition, so it does not justify further investment. Among the other nine top-10 predictions, none has a credible mechanism plus supporting evidence:
- Xanthomatosis (rank 3) is biologically plausible but overlaps with the drug's existing lipid-lowering action, so it is not a distinct repurposing signal.
- Cholesterol catabolic process disease (rank 5) has one completed Phase 3 trial (NCT03207945, n=118, PCSK9 inhibition in treated HIV). That trial studies cardiovascular risk, not a defined cholesterol catabolism disorder. The Evidence Pack does not confirm that alirocumab was the study drug.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which currently block safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking PCSK9 inhibition to keratinization disorders
- Verification of the intervention arm and primary endpoint of NCT03207945 if rank 5 is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

