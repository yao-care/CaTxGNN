---
layout: default
title: Ivermectin
parent: Model Prediction Only (L5)
nav_order: 508
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
monitor_inn: "Ivermectin"
predicted_indications: ["vulvovaginal candidiasis", "esophageal candidiasis", "anogenital human papillomavirus infection", "vulvovaginitis", "congenital candidiasis", "candida glabrata", "neonatal candidiasis", "postmenopausal atrophic vaginitis", "candidiasis, invasive"]
description: "Ivermectin: predicted new indication Vulvovaginal candidiasis (evidence level L5). In Canada: 2 DINs (2 marketed)"
---

# Ivermectin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ivermectin: Vulvovaginal candidiasis
{: .text-alpha }

## One-Sentence Summary

Ivermectin is an antiparasitic originally used to treat strongyloidiasis and onchocerciasis.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but **no clinical trials and no relevant publications** currently support this direction. The prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for ivermectin: "In vitro studies using human liver microsomes and recombinant CYP450 enzymes have shown that ivermectin is primarily metabolized by CYP3A4." ([DailyMed: Stromectol (ivermectin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=681888c9-af79-4b7d-ae80-c3f4f6f1effd), label version 2024-09-20; accessed 2026-11-19.) Ivermectin is known as an antiparasitic that acts on glutamate-gated chloride channels in invertebrates. These channels are not a recognised target in *Candida*, so no mechanistic link to vulvovaginal candidiasis is established.

The original indications (strongyloidiasis, onchocerciasis) are parasitic infections, while the predicted indication is a fungal infection. The high score (0.9995) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The other top predictions are also mostly Candida-related or vulvovaginal conditions (for example esophageal candidiasis, vulvovaginitis, congenital candidiasis, invasive candidiasis), and none has supporting clinical data. This pattern suggests a model-level association rather than a real pharmacological signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for vulvovaginal candidiasis.

For other predicted Candida-related indications, two papers were retrieved. Both appear to be retrieval mismatches rather than evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) | 2022 | Case report | BMJ Case Reports | Disseminated strongyloidiasis after prolonged corticosteroid treatment. This concerns the original indication, not esophageal candidiasis. |
| [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) | 1999 | Case report | Australasian Journal of Dermatology | Oral ivermectin cleared crusted scabies in two immunocompromised children, one of whom had chronic mucocutaneous candidiasis. It does not support a candidiasis indication. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02480557 | STROMECTOL | Not specified | Not specified |
| 02440342 | ROSIVER | Not specified | Not specified |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: Loiasis and filariasis are listed as disease contraindications in the TxGNN knowledge graph.
- **Drug Interactions**: 100 potential interactions were identified. Moderate-level examples include aprepitant, clarithromycin, ethanol, cobicistat, deferasirox, warfarin, dicoumarol, fostamatinib, radioactive iodide (I-123 and I-131), and topical abametapir. Other listed interactions are of unknown severity, including omeprazole, lansoprazole, prednisone, prednisolone, dexamethasone, ranitidine, famotidine, ursodeoxycholic acid, and heparin.
- **Population note**: For the neonatal candidiasis prediction, ivermectin safety data in very young or low-weight infants are limited.

Please refer to the package insert for warnings and other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no clinical trials, no relevant publications, and no plausible mechanism in the data. Effective approved antifungal therapies already exist for candidiasis.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for ivermectin
- Evidence of in vitro or preclinical antifungal activity against *Candida* species
- Clarification of the target indication, including formulation and route, since route compatibility has not been assessed
- A re-run of the literature search with relevant queries to exclude retrieval mismatches

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data for ivermectin is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Stromectol (ivermectin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=681888c9-af79-4b7d-ae80-c3f4f6f1effd) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

