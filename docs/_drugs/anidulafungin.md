---
layout: default
title: Anidulafungin
parent: Model Prediction Only (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Anidulafungin: predicted new indication Impetigo (evidence level L5). Approved use: Esophageal candidiasis, candidemia"
---

# Anidulafungin
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

# Anidulafungin: From Esophageal Candidiasis and Candidemia to Impetigo

## One-Sentence Summary

Anidulafungin is an echinocandin antifungal, originally used to treat esophageal candidiasis and candidemia.
The TxGNN model predicts it may be effective for **impetigo** (top-ranked prediction), but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction with no mechanistic or clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis, candidemia (the Health Canada licence record has no indication text) |
| Predicted New Indication | Impetigo |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, anidulafungin is an echinocandin that inhibits fungal 1,3-beta-D-glucan synthase, an enzyme needed to build the fungal cell wall. Its efficacy in invasive *Candida* infections is established.

Impetigo is a superficial bacterial skin infection, mainly caused by *Staphylococcus aureus* and *Streptococcus pyogenes*. Bacteria have no glucan synthase and no fungal cell wall, so **no plausible mechanistic link** exists between anidulafungin and impetigo. The same applies to the other bacterial predictions on the list (bullous impetigo, staphylococcal scalded skin syndrome, hordeolum, Clostridium infection).

The high score (0.989) most likely reflects relationships within the knowledge graph rather than true pharmacological activity. The score should not be read as evidence of efficacy.

**Other predictions reviewed:**
- **Mesothelioma-related tumours** (malignant pleural mesothelioma, epithelioid, sarcomatoid, malignant visceral pleura tumour): no mechanism, trials or publications support them.
- **Pleural empyema:** one 2018 pharmacokinetic study shows the drug reaches pleural effusion. This is not efficacy data, and it is relevant at most to fungal empyema, which would extend the existing antifungal use rather than being true repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for impetigo.

For context, the only literature retrieved for the other top predictions was:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29439960](https://pubmed.ncbi.nlm.nih.gov/29439960/) | 2018 | Pharmacokinetic study | Antimicrob Agents Chemother | Anidulafungin reached pleural effusion (0.32–2.02 μg/ml) and ascites fluid (0.12–0.99 μg/ml) in 10 critically ill patients, at levels below those in plasma. This is relevant to pleural empyema, not impetigo. |
| [18756840](https://pubmed.ncbi.nlm.nih.gov/18756840/) | 2008 | Review | Cleve Clin J Med | General infectious disease treatment update. It gives no evidence of anidulafungin use for Clostridium infection. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02330695 | ERAXIS | Not recorded | Not recorded |

---

## Safety Considerations

- **Knowledge-graph contraindication signals:** liver disease and gallbladder disease. These come from drug-disease relationships in the knowledge graph, not from product label text, and should be checked against the package insert.
- **Drug Interactions:** one minor interaction was identified, with cyclosporine.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications for impetigo, and the drug has no antibacterial mechanism, so there is no biological basis for the prediction. Anidulafungin is also given intravenously, which is poorly suited to a superficial skin infection.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic assessment
- Health Canada package insert warnings and contraindications, needed for safety screening
- Preclinical evidence (for example, in vitro activity against *S. aureus* and *S. pyogenes*) before any further consideration
- A review of whether the model's bacterial and mesothelioma predictions are artefacts of the knowledge graph
- If any lead is pursued, the pleural empyema direction (fungal pleural infection) is the only one with indirect data, and it would need efficacy evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

