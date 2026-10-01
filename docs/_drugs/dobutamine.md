---
layout: default
title: Dobutamine
parent: Model Prediction Only (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine: From Cardiac Inotropic Support to Alopecia

## One-Sentence Summary

Dobutamine is a beta-1 adrenergic inotrope, given intravenously and marketed in Canada.
The TxGNN model predicts it may be effective for **alopecia**, but there are **0 clinical trials** and only **2 publications** (both case reports about other drugs), so no study has tested dobutamine for this use.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

The Health Canada license records in the Evidence Pack contain no approved-indication text, so the original indication is not listed here.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the source database. Dobutamine is generally described as a beta-1 adrenergic agonist that increases heart contractility, and no known role in hair-follicle biology has been identified.

The high TxGNN score (0.9985) is a knowledge-graph prediction only. It most likely reflects graph-neighbour similarity with other hair-related indications, not a biological rationale. The related predictions (hypotrichosis, diffuse alopecia areata, hypertrichosis) also have no mechanistic support and no clinical evidence. Alopecia areata, for example, is autoimmune, and beta-1 agonism has no established immunomodulatory role in it.

I found no credible mechanistic link between dobutamine and alopecia.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case report (veterinary) | J Vet Cardiol | Heart failure from minoxidil intoxication in a cat. Dobutamine was used only to treat hypotension, not hair loss. |
| [17505274](https://pubmed.ncbi.nlm.nih.gov/17505274/) | 2007 | Case report | Pediatr Emerg Care | Acute colchicine poisoning in a child. Hair loss is described as a recovery-phase effect of colchicine, and dobutamine is not tested. |

Neither paper evaluates dobutamine as a treatment for alopecia.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2242010 | DOBUTAMINE INJECTION USP |
| 2462729 | DOBUTAMINE INJECTION USP |

Dosage form and approved indication text are not recorded for these licenses.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone (L5), with no trials and no supporting literature. Dobutamine is a short-acting intravenous inotrope with no plausible mechanism for hair-growth disorders, so it is also impractical for a chronic hair condition.

**To reconsider, the following is needed:**
- Mechanism of action data, to test whether any plausible link to hair-follicle biology exists
- Health Canada package insert warnings and contraindications, which are blocking for safety screening
- Any preclinical or clinical study of dobutamine in alopecia or related hair disorders
- Assessment of route compatibility, since only intravenous dobutamine is marketed and a scalp condition would need a different delivery route
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

