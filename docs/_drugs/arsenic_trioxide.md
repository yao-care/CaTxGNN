---
layout: default
title: Arsenic Trioxide
parent: Model Prediction Only (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
monitor_inn: "ARSENIC TRIOXIDE"
predicted_indications: ["unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "severe congenital hypochromic anemia with ringed sideroblasts", "aregenerative anemia", "partial deletion of the long arm of chromosome 5", "myelodysplastic syndrome", "Ewing sarcoma", "dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
last_modified_at: 2026-11-20
description: "Arsenic Trioxide: predicted new indication unclassified myelodysplastic syndrome (evidence level L5). In Canada: 4 DINs (4 marketed)"
---

# Arsenic Trioxide
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

## Arsenic Trioxide: arsenic-based antineoplastic agent → unclassified myelodysplastic syndrome
{: .text-alpha }

## One-Sentence Summary

Arsenic trioxide is an intravenous arsenic-based anticancer drug that is currently marketed in Canada.
The TxGNN model predicts it may be useful for **unclassified myelodysplastic syndrome**.
At present, **no clinical trials and no publications** in the compiled data address this specific condition, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | unclassified myelodysplastic syndrome |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 4 of 4) |
| Number of DINs | 4 (marketed: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for arsenic trioxide: "The mechanism of action of TRISENOX is not completely understood. Arsenic trioxide causes morphological changes and DNA fragmentation characteristic of apoptosis in NB4 human promyelocytic leukemia cells in vitro. Arsenic trioxide also causes damage or degradation of the fusion protein promyelocytic leukemia (PML)-retinoic acid receptor (RAR)-alpha." ([DailyMed: Trisenox (arsenic trioxide) prescribing information, Cephalon, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=101fc347-d0ad-4aee-8b06-9feb187fd741), label version 2022-06-30; accessed 2026-11-19.) Arsenic trioxide is generally described as an agent that induces cancer-cell death and affects cell differentiation. Whether this applies to this particular subtype is not established.

The predicted condition is a subtype within the broader family of myelodysplastic syndromes, which are disorders of blood-cell production in the bone marrow. Any argument for benefit is therefore indirect and works only through that broader category. No trial or publication in the compiled data is linked to this specific term. The high model score is a computational signal, not evidence of clinical benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Health Canada records show the drug is marketed, with 4 valid licences. All are single-ingredient products for injection, and none is cancelled. The local records do not include approved-indication text, dosage form or manufacturer details for these licences.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antineoplastic, arsenic-based agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood counts, liver and kidney function, electrolytes (potassium, magnesium) and cardiac rhythm (ECG/QT), subject to the package insert |
| Handling Protection | Follow institutional cytotoxic drug handling procedures |

## Safety Considerations

- **Conditions flagged as concerns:** The compiled data flags the following conditions as potential concerns. This comes from a drug-disease relationship source, not from label text.
  - long QT syndrome (including the familial form)
  - torsades de pointes
  - atrioventricular block
  - kidney disease
  - liver disease
  - gallbladder disease
  - potassium deficiency
  - pyoureter
- **Drug interactions:** 100 interactions are recorded. Examples:
  - **Major:**
    - hydrocortisone
    - amphotericin B (conventional, lipid complex, cholesteryl sulfate and liposomal forms)
    - cisapride
    - clarithromycin
    - dolasetron
    - granisetron
    - levofloxacin
  - **Moderate:**
    - famotidine
    - loperamide
    - bisacodyl
    - castor oil
    - glycerin
    - lactitol
    - lactulose
    - magnesium citrate
    - magnesium hydroxide
  - **Minor:** metronidazole

Many of the major interactions involve drugs that prolong the QT interval or disturb electrolytes. Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high (0.9993), but no clinical trial or publication in the compiled data directly studies this specific condition. The evidence level is therefore L5. The drug's known cardiac and electrolyte-related safety concerns also call for caution.

**To proceed, the following is needed:**
- Studies or case series that directly address this specific condition, or a clear justification for extrapolating from the broader myelodysplastic syndrome category
- Mechanism-of-action data to support the biological link
- Package insert warnings and contraindications from Health Canada
- A cardiac and electrolyte monitoring plan, including review of QT-prolonging co-medications

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for this drug is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Trisenox (arsenic trioxide) prescribing information, Cephalon, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=101fc347-d0ad-4aee-8b06-9feb187fd741) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

