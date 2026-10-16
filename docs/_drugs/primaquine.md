---
layout: default
title: Primaquine
parent: Model Prediction Only (L5)
nav_order: 770
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Primaquine: predicted new indication Myiasis (evidence level L5). Approved use: Plasmodium vivax malaria"
---

# Primaquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Primaquine: From Plasmodium vivax Malaria to Myiasis

## One-Sentence Summary

Primaquine is an 8-aminoquinoline antimalarial, originally used for radical cure of *Plasmodium vivax* malaria.
The TxGNN model predicts it may be effective for **myiasis** (infestation by fly larvae) with a very high score, but **0 clinical trials** and **0 publications** support this direction.
The prediction is purely computational and no plausible biological rationale has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasmodium vivax malaria |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, primaquine is an 8-aminoquinoline antiprotozoal. Its efficacy against liver-stage parasites (hypnozoites) and gametocytes in malaria is well established.

Myiasis is a different kind of disease. It is an infestation by dipteran fly larvae, not a protozoal infection. Standard management is larval removal (occlusion or surgical extraction), wound debridement, and occasionally ivermectin or albendazole. Primaquine has no known larvicidal activity.

The high TxGNN score most likely reflects knowledge-graph proximity to antiparasitic drugs rather than a biological rationale. The related subtypes (furuncular, wound and creeping myiasis) carry nearly identical scores (about 99.73%). This suggests the prediction is inherited from the parent disease node and is not independent evidence.

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
| 02017776 | PRIMAQUINE | — | — |

Primaquine has one valid single-ingredient authorization in Canada. Dosage form and approved indication text were not available in the data compiled for this report.

---

## Safety Considerations

- **Contraindication-related conditions (from the TxGNN knowledge graph, not label text):** neutropenia, agranulocytosis, G6PD deficiency, hemolytic anemia, glycogen storage disease, cystinuria, galactosemia, pyruvate dehydrogenase E3 deficiency, and methemoglobinemia due to methemoglobin reductase deficiency.
- **Drug Interactions:** 100 interactions were recorded, and 20 are listed in the compiled data. The one rated **Major** is dolasetron. Most others are rated Moderate, including:
  - antiemetics and gastrointestinal agents: ondansetron, granisetron, palonosetron, famotidine, alosetron, loperamide
  - antibiotics: clarithromycin, levofloxacin
  - laxatives and bowel-preparation agents: bisacodyl, picosulfuric acid, polyethylene glycol, lactulose, lactitol, magnesium citrate, sodium sulfate, glycerin, castor oil

  Metronidazole is rated Minor.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by a model score only (evidence level L5). There are no clinical trials or publications, and no mechanistic link between primaquine and fly-larva infestation. Established, effective treatments already exist for myiasis.

For context, the other predictions in the same analysis are better supported. Primaquine plus clindamycin as a second-line regimen for *Pneumocystis* pneumonia has Phase 3 evidence and is rated Proceed with Guardrails. The malaria prediction is simply the drug's existing core indication.

**To proceed, the following is needed:**
- Any in vitro or in vivo evidence of larvicidal activity against myiasis-causing flies
- Mechanism of action data for primaquine, to support a mechanistic-link analysis
- Package insert warnings and contraindications from Health Canada
- A review of the knowledge-graph connection driving the score, to check whether it is a parent-node artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

