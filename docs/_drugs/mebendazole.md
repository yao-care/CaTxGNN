---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 569
evidence_level: L5
indication_count: 10
---

# Mebendazole
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

# Mebendazole: From Antiparasitic Use to Acne

## One-Sentence Summary

Mebendazole is a benzimidazole anthelmintic (antiparasitic) marketed in Canada as VERMOX.
The TxGNN model predicts it may be effective for **acne**, but there are **0 clinical trials** and only **1 unrelated case report** behind this prediction, so it is currently a model output without clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied licence data (mebendazole is an anthelmintic) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Mebendazole belongs to the benzimidazole class, which binds parasite beta-tubulin and blocks microtubule polymerization. Its efficacy against parasitic infections is established, but this mechanism has no recognized link to acne.

Acne is a chronic inflammatory condition of the skin's oil glands and is not a parasitic disease. The only publication linked to this prediction (PMID 7072899) is a 1982 case report of proliferative sparganosis, a tapeworm larval infection, in which the patient happened to have acne-like skin lesions. It says nothing about treating acne. The very high model score (99.20%) is most likely a knowledge-graph artifact rather than a real therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case report | Am J Trop Med Hyg | Proliferative sparganosis in Venezuela; the patient had acne-like skin lesions, but the report does not address acne treatment or mebendazole efficacy |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 556734 | VERMOX |

Dosage form and approved indication text were not supplied for this licence.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the supplied data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction rests on the model score alone. There are no trials, and the single linked publication is an unrelated case report. No plausible mechanism connects mebendazole to acne.

**To proceed, the following is needed:**
- Mechanistic evidence, or preclinical data, showing a plausible link between mebendazole and acne pathology
- Health Canada package insert warnings and contraindications for VERMOX, which are required before any safety screening
- The approved indication text and dosage form for the Canadian licence
- Any prospective clinical evidence, since none currently exists for acne

**Other predictions in this run:** Only **alveolar echinococcosis** (score 94.2%, evidence level L3) has real support. It has 1 completed non-interventional study and multiple reviews showing that benzimidazoles (albendazole, mebendazole) are established chemotherapy. This is closer to a recognized antiparasitic use than novel repurposing, and albendazole is generally preferred. It is a "Proceed with Guardrails" candidate. **Cystic echinococcosis** (*Echinococcus granulosus*) is a research question with only indirect support. The remaining predictions (leishmaniasis, hordeolum, botulism, impetigo, Sorsby's fundus dystrophy, demodicidosis) are model-only and should stay on Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

