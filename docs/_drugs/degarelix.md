---
layout: default
title: Degarelix
parent: Model Prediction Only (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Degarelix: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "DEGARELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "allergic urticaria", "cold urticaria", "familial male-limited precocious puberty", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Degarelix
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Degarelix: From Its Approved Use to Hypertrichosis (Prediction Only)

## One-Sentence Summary

Degarelix is a GnRH receptor antagonist marketed in Canada as FIRMAGON. The approved indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no publications** currently support this prediction, so it rests on a graph-based model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Degarelix is a GnRH receptor antagonist. It suppresses LH and FSH, which lowers gonadal androgen and estrogen levels. Detailed mechanism-of-action data were not available in the compiled data, so this description is based on the drug's known class.

In theory, suppressing androgens could reduce androgen-dependent hair growth, such as hirsutism-type hypertrichosis. However, most forms of hypertrichosis are not androgen-dependent: they are congenital, drug-induced, or part of a syndrome. The mechanistic link is therefore weak. The very high TxGNN score reflects network proximity in a knowledge graph and is not backed by clinical or literature evidence.

**Other predicted indications (all L5, no trials or literature):**

| Rank | Predicted Indication | Score | Assessment |
|---|---|---|---|
| 2 | Ambras type hypertrichosis universalis congenita | 99.98% | Not driven by gonadal androgens (TRPS1 regulation); no clear rationale |
| 3 | Syndrome with Dandy-Walker malformation | 99.98% | Structural developmental disorder; no plausible mechanism |
| 4 | Malformation syndrome with odontal/periodontal component | 99.98% | Likely a graph artifact |
| 5 | Isolated genetic hair shaft abnormality | 99.98% | Structural, not hormonally mediated |
| 6 | Allergic urticaria | 99.97% | Urticaria is a known adverse event of the drug, so this is more likely a safety signal |
| 7 | Cold urticaria | 99.86% | No mechanistic pathway; histamine-releasing potential argues against use |
| 8 | Familial male-limited precocious puberty | 99.84% | Driven by activating LHCGR mutations downstream of the pituitary, so GnRH antagonism is not expected to help |
| 9 | Central precocious puberty 1 | 99.67% | Most biologically plausible, since GnRH-axis suppression is the established principle; remains a research question only |
| 10 | Familial isolated trichomegaly | 99.65% | Not known to be androgen-driven |

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
| 02337029 | FIRMAGON | Not available | Not available |
| 02337037 | FIRMAGON | Not available | Not available |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (GnRH antagonist), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these come from drug-disease graph edges, not from label text): long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease, potassium deficiency disease.
- **Drug Interactions** (100 interactions found; examples shown):
  - **Major:** cisapride, dolasetron
  - **Moderate:** clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, famotidine, loperamide, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, lactulose, magnesium citrate, magnesium hydroxide)
  - **Minor:** metronidazole
  - Many of these interactions are likely related to QT prolongation and electrolyte disturbance.
- **Adverse-event signal:** urticaria and injection-site reactions have been associated with degarelix, which argues against the urticaria predictions.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials or literature (Evidence Level L5), and its mechanistic link is weak because most hypertrichosis is not androgen-driven. Of all the predictions, only central precocious puberty is mechanistically coherent, and it is already treated with established GnRH agonists. It should be handled as a research question, not a development candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage form for the two DINs
- Mechanism of action data from DrugBank
- A literature and trial search focused on central precocious puberty and androgen-dependent hirsutism
- Pediatric safety data, plus a QT and electrolyte risk assessment, before any new-population use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

