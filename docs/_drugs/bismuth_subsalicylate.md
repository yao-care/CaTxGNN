---
layout: default
title: Bismuth Subsalicylate
parent: Model Prediction Only (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Bismuth Subsalicylate
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

# Bismuth Subsalicylate: From Digestive Upset and Diarrhea to Paratyphoid Fever

## One-Sentence Summary

Bismuth subsalicylate is a long-marketed gastrointestinal remedy (best known as Pepto-Bismol) used for digestive upset and diarrhea. The TxGNN model predicts it may be effective for **paratyphoid fever**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The prediction rests on model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records provided; the drug is widely used for digestive upset and diarrhea |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 99.98% (model rank 836) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Bismuth subsalicylate is known to have antibacterial and anti-secretory activity in the gut, and it is established for gastrointestinal complaints such as traveler's diarrhea. Mechanistically, it may be applicable to enteric Salmonella infections by extension.

Paratyphoid fever is a systemic enteric infection caused by Salmonella. The link to the original use is plausible only at a general level, through activity against enteric bacteria. Bismuth is minimally absorbed, so its action stays largely in the gut lumen. That is unlikely to be enough to treat a systemic infection with tissue invasion. The high score (~0.9998) is a graph-based prediction, not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Fourteen authorizations are on record. The five main ones are listed below. Dosage form and approved-indication text were not available in the records provided.

| DIN | Product Name |
|---------|------|
| 2313162 | Bismuth Subsalicylate Suspension |
| 2468646 | Regular Strength Bismuth |
| 2097079 | Pepto-Bismol |
| 2534436 | Gastrovol Liquid Gels |
| 2177994 | Pepto Bismol Caplet, 262 mg/caplet |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5). The oral, minimally absorbed product is mechanistically poorly suited to a systemic infection such as paratyphoid fever.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Any clinical or observational evidence specific to paratyphoid fever

**Note:** In the same prediction list, **salmonellosis** (score 99.95%) has more support and is rated L4, a research question. That support consists of in vitro bacterial binding and killing data and reviews on diarrheal disease, with no Salmonella-specific human trials. It would be a more practical starting point than paratyphoid fever, as a symptomatic or adjunctive role only, not a replacement for antimicrobial therapy.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

