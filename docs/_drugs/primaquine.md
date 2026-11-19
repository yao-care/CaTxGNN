---
layout: default
title: Primaquine
parent: Model Prediction Only (L5)
nav_order: 770
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-05
monitor_inn: "Primaquine"
predicted_indications: ["myiasis", "furuncular myiasis", "wound myiasis", "creeping myiasis", "toxoplasmosis", "nocardiosis", "pneumocystosis"]
description: "Primaquine: predicted new indication Myiasis (evidence level L5). In Canada: 1 DIN (1 marketed)"
---

# Primaquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Primaquine: Myiasis
{: .text-alpha }

## One-Sentence Summary

Primaquine is an 8-aminoquinoline antimalarial, originally used for radical cure of *Plasmodium vivax* malaria.
The TxGNN model predicts it may be effective for **myiasis** (infestation by fly larvae) with a very high score, but **0 clinical trials** and **0 publications** support this direction.
The prediction is purely computational and no plausible biological rationale has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for primaquine: "Primaquine phosphate is an 8-aminoquinoline antimalarial drug. The mechanism of action has not been fully established. The major assumptions are an inhibition of the mitochondrial system of dormant parasites, and an oxidative stress generated through reactive metabolites in infected cells." ([DailyMed: primaquine phosphate prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1bfbf4ae-81b8-4160-a00d-6322aadd4b59), label version 2026-02-11; accessed 2026-11-19.) Based on known information, primaquine is an 8-aminoquinoline antiprotozoal. Its efficacy against liver-stage parasites (hypnozoites) and gametocytes in malaria is well established.

Myiasis is a different kind of disease. It is an infestation by dipteran fly larvae, not a protozoal infection. Standard management is larval removal (occlusion or surgical extraction), wound debridement, and occasionally ivermectin or albendazole. Primaquine has no known larvicidal activity.

The high TxGNN score comes from the TxGNN model (deep learning) and most likely reflects similarities the model learned between related diseases, not biological evidence. The related subtypes (furuncular, wound and creeping myiasis) carry nearly identical scores (about 0.9973). This suggests the prediction is inherited from the parent disease and is not independent evidence.

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

For context, the other predictions in the same analysis are better supported. Primaquine plus clindamycin as a second-line regimen for *Pneumocystis* pneumonia has Phase 3 evidence and is rated Proceed with Guardrails.

**To proceed, the following is needed:**
- Any in vitro or in vivo evidence of larvicidal activity against myiasis-causing flies
- Mechanism of action data for primaquine, to support a mechanistic-link analysis
- Package insert warnings and contraindications from Health Canada
- A review of the similarities the TxGNN model (deep learning) learned between related diseases that drive the score, to check whether the score is simply inherited from the parent disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: primaquine phosphate prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1bfbf4ae-81b8-4160-a00d-6322aadd4b59) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

