---
layout: default
title: Letermovir
parent: Model Prediction Only (L5)
nav_order: 537
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-05
monitor_inn: "LETERMOVIR"
predicted_indications: ["vulvovaginal candidiasis"]
description: "Letermovir: predicted new indication Vulvovaginal candidiasis (evidence level L5). In Canada: 3 DINs (3 marketed)"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Letermovir: Vulvovaginal candidiasis
{: .text-alpha }

## One-Sentence Summary

Letermovir is an antiviral originally used for cytomegalovirus (CMV) infection.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for letermovir: "PREVYMIS is an antiviral drug against CMV. […] Letermovir inhibits the CMV DNA terminase complex (pUL51, pUL56, and pUL89) which is required for viral DNA processing and packaging. Biochemical characterization and electron microscopy demonstrated that letermovir affects the production of proper unit length genomes and interferes with virion maturation." ([DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b), label version 2026-01-14; accessed 2026-11-19.) Letermovir is a CMV-specific antiviral, and its efficacy in CMV infection is the basis for its approval. Its known mechanism is inhibition of the viral terminase complex (pUL56/pUL51/pUL89).

This target is not present in fungi such as *Candida* species, so no plausible link to antifungal activity is supported. The very high TxGNN score (0.9988) is a computational prediction only. It is probably driven by network-level associations, for example letermovir's many drug interactions and its co-prescription with azole antifungals in transplant patients. It should not be read as biological evidence.

Any benefit would be speculative, such as an indirect effect through fewer immunosuppression-related complications, and none is documented. Similarity between the original and predicted indications, and route compatibility, have not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02469367 | PREVYMIS | Not specified | Not specified |
| 02469375 | PREVYMIS | Not specified | Not specified |
| 02469383 | PREVYMIS | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction databases. The first 20 records reviewed include:
  - **Major**: Eliglustat, Naloxegol, Cisapride
  - **Moderate**: Hydrocortisone, Pioglitazone, Aprepitant, Triamcinolone, Omeprazole, Dexamethasone, Betamethasone, Budesonide (including nasal), Chlorpropamide, Clarithromycin, Saxagliptin, Glimepiride, Naldemedine, Lansoprazole, Acetohexamide, Nitisinone

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No clinical trials or publications exist, and letermovir's known target (the CMV terminase complex) is absent from fungi. A biologically plausible link is lacking, and the safety review cannot proceed without the Health Canada label.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Any preclinical evidence of anti-*Candida* activity, such as in vitro susceptibility data
- A literature and trial search for evidence of benefit in vulvovaginal candidiasis
- Assessment of route compatibility and dosage forms for a vulvovaginal indication
- Review of the interaction profile, especially the major interactions, for the likely patient population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

