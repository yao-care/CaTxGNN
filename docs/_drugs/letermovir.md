---
layout: default
title: Letermovir
parent: Model Prediction Only (L5)
nav_order: 532
evidence_level: L5
indication_count: 1
---

# Letermovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Letermovir: From Cytomegalovirus Infection to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is an antiviral that inhibits the cytomegalovirus (CMV) DNA terminase complex. The Canadian licence records in the Evidence Pack do not include indication text, so its original use is inferred from its mechanism.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, a fungal infection, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is model output only and is not supported by a known biological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (CMV infection inferred from the drug's mechanism) |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record. From the pack's mechanistic analysis, letermovir is a CMV DNA terminase complex (pUL56) inhibitor. This mechanism is specific to the virus.

Vulvovaginal candidiasis is a fungal infection, mainly caused by *Candida albicans*. Letermovir has no known antifungal activity, and the pack found no supported mechanistic link between the drug and this disease. The original indication and the new indication also lack a documented relationship, and similarity to the original indication is still pending.

The very high TxGNN score (99.88%, rank 2971) most likely reflects knowledge-graph topology. Anti-infective drugs and infection-related disease nodes share many neighbours in the graph, and this does not necessarily reflect biology. The score is a computational prediction and should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2469367 | PREVYMIS |
| 2469375 | PREVYMIS |
| 2469383 | PREVYMIS |

Dosage form, manufacturer and approved indication text are not populated in the current records.

---

## Safety Considerations

Please refer to the package insert for safety information. The Evidence Pack contains no warnings or contraindications, and its drug-interaction query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanism. Letermovir is a virus-specific antiviral with no known antifungal activity, so the score cannot be justified biologically at this stage.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indications), which is currently a blocking gap for safety screening
- Mechanism of action data from DrugBank, to enable a proper mechanistic-link analysis
- Any in vitro or preclinical evidence of activity against *Candida* species
- A route compatibility assessment (vulvovaginal candidiasis is typically treated locally, and the available and required routes are still pending)
- A similarity assessment against the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

