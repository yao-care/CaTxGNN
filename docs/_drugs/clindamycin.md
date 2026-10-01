---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 204
evidence_level: L5
indication_count: 6
---

# Clindamycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Clindamycin: From Bacterial Infection to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic, so its original use is bacterial infection. The licence records in the Evidence Pack contain no indication text, so this is inferred from the drug class.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, with a very high score. However, there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infection (inferred from drug class; no licence indication text available) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Clindamycin belongs to the lincosamide class of antibacterials, which inhibit the bacterial 50S ribosomal subunit and block protein synthesis.

That mechanism does not fit this prediction well. Punctate epithelial keratoconjunctivitis is often viral, toxic or immune-mediated, so an antibacterial has little direct rationale. The high TxGNN score is a graph-based prediction with no trials or literature behind it, and it should not be read as evidence of benefit.

Other predictions for this drug are somewhat better supported:
- **Exposure keratitis** (score 99.80%, evidence level L4) is the most plausible lead. It can become secondarily infected by bacteria such as *S. aureus*, and four indirect papers were retrieved on bacterial keratitis and ocular infections. None of them evaluates clindamycin for exposure keratitis. Ocular penetration and the choice of topical versus systemic route are unresolved.
- **Neurotrophic keratopathy** and **postmenopausal atrophic vaginitis** have no supported mechanistic link.
- **Epidemic keratoconjunctivitis** is typically adenoviral. Its two papers concern bovine Moraxella infection and look like name-matching artefacts.
- **Non-human animal disease** is a non-specific veterinary category and likely a knowledge-graph artefact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Health Canada lists 20 DINs for clindamycin. The record includes dosage form and approved indication fields for none of the five main authorizations shown below.

| DIN | Product Name |
|---------|------|
| 2408511 | CLINDAMYCIN IV INFUSION |
| 2400529 | CLINDAMYCIN |
| 2230535 | CLINDAMYCIN INJECTION USP |
| 2266938 | TARO-CLINDAMYCIN |
| 2436914 | AURO-CLINDAMYCIN |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.
- **Other**: Clindamycin is a recognised risk factor for *Clostridioides difficile* infection. This is a general safety concern and was not assessed for this specific use.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials, no literature and a weak mechanistic link, since an antibacterial is unlikely to help a largely viral or immune-mediated condition. Package insert safety data is also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data for clindamycin (e.g., from DrugBank)
- Any clinical or preclinical evidence for clindamycin in punctate epithelial keratoconjunctivitis
- Reassessment of exposure keratitis as a research question. This would need evidence that clindamycin is active against the causative bacteria, ocular penetration data and a decision on the route of administration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

