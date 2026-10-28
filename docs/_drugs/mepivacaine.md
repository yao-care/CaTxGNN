---
layout: default
title: Mepivacaine
parent: Model Prediction Only (L5)
nav_order: 589
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Mepivacaine: predicted new indication Gastroduodenitis (evidence level L5). Approved use: Not stated in the licence data compiled for this report (the product…"
monitor_inn: "Mepivacaine"
predicted_indications: ["gastroduodenitis", "peptic ulcer disease"]
---

# Mepivacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Mepivacaine: From Local Anaesthesia to Gastroduodenitis
{: .text-alpha }

## One-Sentence Summary

Mepivacaine is an amide-type local anaesthetic, marketed in Canada mainly in dental and local anaesthetic injection products.
The TxGNN model predicts it may be effective for **gastroduodenitis**,
but **no clinical trials and no relevant publications** currently support this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report (the product names suggest local and dental anaesthesia) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 7 of 7) |
| Number of DINs | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, mepivacaine is an amide-type local anaesthetic that blocks voltage-gated sodium channels and thereby reduces nerve signal conduction.

A theoretical link to gastroduodenitis, such as reduced visceral pain signalling or local mucosal anaesthesia, is possible but speculative. Blocking sodium channels does not address the underlying causes of gastroduodenal inflammation, such as acid injury, *H. pylori* infection or impaired mucosal defence. No gastrointestinal indication has been established for this injected anaesthetic.

The high TxGNN score is a computational prediction only. No clinical or literature evidence supports it.

A second predicted indication, **peptic ulcer disease** (score 0.9941), has the same limitations. Its only retrieved publication is an animal safety pharmacology study of lofexidine, a different drug, and it was treated as an irrelevant retrieval.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for gastroduodenitis.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00479934 | SCANDONEST 3% PLAIN INJ | Not listed | Not listed |
| 02474174 | CARBOCAINE 3% | Not listed | Not listed |
| 02241999 | CARBOCAINE 1% | Not listed | Not listed |
| 02330733 | 3% POLOCAINE DENTAL | Not listed | Not listed |
| 00364304 | ISOCAINE HCL INJ 3% | Not listed | Not listed |

Two further single-ingredient licences (CARBOCAINE 1% and CARBOCAINE 2%) are also valid, for 7 in total.

## Safety Considerations

- **Disease associations in the knowledge graph** (not taken from label text): the TxGNN knowledge graph links mepivacaine to contraindications in kidney disease, liver disease, gallbladder disease, pyoureter, myasthenia gravis (including adult-onset), neuromuscular junction disease, butyrylcholinesterase deficiency, cardiovascular disease and heart disease. These should be verified against the official labelling.
- **Drug Interactions**: 11 interactions were identified, 10 rated Moderate and 1 Minor.
  - Moderate: other local anaesthetics and related agents, including topical and ophthalmic lidocaine, topical benzocaine, topical and nasal cocaine, ophthalmic and topical tetracaine, ophthalmic oxybuprocaine and topical cinchocaine. Liposomal morphine is also rated Moderate.
  - Minor: hyaluronidase.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (evidence level L5). There are no clinical trials, no relevant literature and no established mechanistic link to gastroduodenitis. Mepivacaine is also an injected local anaesthetic, so its route of administration may not suit a gastroduodenal condition.

**To proceed, the following is needed:**
- Mechanism of action data for mepivacaine
- Package insert warnings and contraindications from Health Canada, which is required before any safety screening
- Approved indication text and dosage forms for each Canadian licence
- A targeted literature search for local anaesthetics in gastroduodenal inflammation or pain
- An assessment of route compatibility, since no required or available routes have been defined
- Preclinical or early exploratory evidence before any clinical development is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

