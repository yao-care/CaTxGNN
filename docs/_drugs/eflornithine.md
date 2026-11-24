---
layout: default
title: Eflornithine
parent: Model Prediction Only (L5)
nav_order: 316
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Eflornithine: predicted new indication Esotropia (evidence level L5). Approved use: Human African trypanosomiasis"
monitor_inn: "Eflornithine"
predicted_indications: ["esotropia", "neurotrophic keratopathy"]
---

# Eflornithine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Eflornithine: From Human African Trypanosomiasis to Esotropia
{: .text-alpha }

## One-Sentence Summary

Eflornithine was originally used to treat human African trypanosomiasis (sleeping sickness) and is also marketed in Canada as a topical product (VANIQA).
The TxGNN model predicts it may be effective for **esotropia** with a score of 0.9985, but **no clinical trials and no publications** currently support this prediction.
Of the ten predictions generated, only bovine trypanosomiasis has any supporting literature, and that literature is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Human African trypanosomiasis; trypanosomiasis |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for eflornithine: "Eflornithine is an irreversible inhibitor of the enzyme ornithine decarboxylase (ODC), the first and rate-limiting enzyme in the biosynthesis of polyamines and a transcriptional target of MYCN. Polyamines are involved in differentiation and proliferation of mammalian cells and are important for neoplastic transformation." ([DailyMed: Iwilfin (eflornithine hydrochloride) prescribing information, USWM, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6716d8cc-66e6-4cee-935c-ccb85ed984f5), label version 2026-03-26; accessed 2026-11-19.) Based on known pharmacology, eflornithine irreversibly inhibits ornithine decarboxylase (ODC), the first enzyme in polyamine synthesis. This is the basis of its use in late-stage Gambian human African trypanosomiasis.

For esotropia, however, no clear mechanistic link was identified. No known pathway connects polyamine depletion to the pathophysiology of strabismus. The high TxGNN score reflects a network-based prediction, not clinical or literature evidence, and should be read with caution.

**Other predictions reviewed (all with no clinical trials):**

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Neurotrophic keratopathy | 0.9938 | L5 | Polyamines are involved in wound healing, but ODC inhibition would more plausibly impair epithelial repair |

## Clinical Trial Evidence

Currently no related clinical trials registered for esotropia. No clinical trials were found for any of the other nine predicted indications either.

## Literature Evidence

Currently no related literature available for esotropia.

The only literature found relates to the sixth-ranked prediction, bovine trypanosomiasis. It is indirect and preclinical or mechanistic:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32053698](https://pubmed.ncbi.nlm.nih.gov/32053698/) | 2020 | Preclinical/Review | PloS one | Safety and efficacy of hydroxyurea and eflornithine against the blood parasites Babesia and Theileria |
| [23525104](https://pubmed.ncbi.nlm.nih.gov/23525104/) | 2013 | Basic mechanistic study | J Biol Chem | Polyamine biosynthesis is a key drug target in African trypanosomes; eflornithine inhibits the first step of this pathway |

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02243837 | VANIQA | EFLORNITHINE HYDROCHLORIDE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** exanthem and dermatitis are recorded as contraindicated conditions.
- **Drug Interactions:** One pharmacological entry was found. It is the drug's target, ornithine decarboxylase (ODC1, human), which eflornithine inhibits. It is not a drug-drug interaction. Eflornithine is used topically for facial hirsutism and by injection for African sleeping sickness. It has also been authorised in the US as oral maintenance therapy for high-risk neuroblastoma.

Please refer to the package insert for the full warnings and precautions; label-based safety data were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The esotropia prediction rests only on a network score. It has no clinical, literature or mechanistic support, so the evidence level is L5. Package insert safety data are also missing. Among the other predictions, bovine trypanosomiasis is the only one with a plausible mechanism, and it could be pursued as a research question rather than a human repurposing candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A plausible mechanistic hypothesis linking polyamine/ODC inhibition to esotropia, supported by preclinical data
- If pursuing bovine trypanosomiasis, direct veterinary efficacy studies against the relevant Trypanosoma species

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Iwilfin (eflornithine hydrochloride) prescribing information, USWM, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6716d8cc-66e6-4cee-935c-ccb85ed984f5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

