---
layout: default
title: Anidulafungin
parent: Model Prediction Only (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
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

# Anidulafungin: From Fungal Infections to Impetigo

## One-Sentence Summary

Anidulafungin is an echinocandin antifungal marketed in Canada as ERAXIS.
The TxGNN model predicts it may be effective for **impetigo** (score 98.9%), but there are **0 clinical trials** and **0 publications** supporting this direction, and no plausible mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antifungal (echinocandin class); approved indication text not provided in the Canadian license data |
| Predicted New Indication | Impetigo |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Anidulafungin is an echinocandin antifungal. It inhibits beta-1,3-D-glucan synthase, an enzyme needed to build the fungal cell wall.

Impetigo is a bacterial skin infection caused by *Staphylococcus aureus* and *Streptococcus pyogenes*. Bacteria do not have beta-1,3-D-glucan synthase, so the drug's target is absent. The high score most likely comes from shared anti-infective neighbours in the knowledge graph rather than a real biological link.

The same problem applies to the other top-ranked predictions:
- **Bacterial or toxin-mediated conditions:** bullous impetigo, staphylococcal scalded skin syndrome, hordeolum (stye), *Clostridium* infection and pleural empyema. The antifungal has no antibacterial activity. Fungal empyema, if it occurred, would already fall under the existing antifungal use rather than repurposing.
- **Pleural malignancies:** malignant pleural mesothelioma, its epithelioid and sarcomatoid subtypes, and malignant visceral pleura tumour. No link between fungal glucan synthase inhibition and mesothelioma biology has been established. Any anticancer rationale would be speculative and would need preclinical data first.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for impetigo.

Among the other predictions, the only retrieved item is a 2008 review, "Update in infectious disease treatment" ([18756840](https://pubmed.ncbi.nlm.nih.gov/18756840/), Cleveland Clinic Journal of Medicine), linked to *Clostridium* infection. It is a broad treatment update that was not shown to address anidulafungin, so it is treated as background rather than supporting evidence.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2330695 | ERAXIS |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or literature, and the drug's antifungal target does not exist in the bacteria that cause impetigo. This is very likely a knowledge-graph artifact, and none of the ten predicted indications has supporting evidence.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that anidulafungin acts on the predicted condition (currently none)
- Health Canada package insert warnings and contraindications, to complete safety screening
- The Canadian approved indication text and dosage form for ERAXIS
- Route compatibility assessment (systemic intravenous drug versus a topically treatable condition such as impetigo)

Unless new evidence emerges, resources are better spent on candidates that have clinical or mechanistic support.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

