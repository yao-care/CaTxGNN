---
layout: default
title: Fluorescein
parent: Model Prediction Only (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Fluorescein: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the available licence data"
monitor_inn: "Fluorescein"
predicted_indications: ["Prinzmetal angina", "antithrombin deficiency type 2", "rheumatoid arthritis", "factor 5 excess with spontaneous thrombosis", "hemoglobinopathy", "heparin cofactor 2 deficiency", "thrombophilia", "hyperthyroidism", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations"]
---

# Fluorescein
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

## Fluorescein: From a Diagnostic Dye to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Fluorescein is a diagnostic fluorescent dye used for angiography and ocular surface staining, and it is marketed in Canada under 3 licences.
The TxGNN model (deep learning) predicts it may be effective for **Prinzmetal angina** with a very high score, which may reflect similarities the model learned between related diseases, not biological evidence, and **no clinical trials and no supporting publications** currently back this prediction.
The literature retrieved for other top predictions describes fluorescein only as a diagnostic tool, not as a treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data (known use: diagnostic angiography and ocular surface staining) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for fluorescein: "Fluorescein sodium responds to electromagnetic radiation and light between the wavelengths of 465 to 490 nm and fluoresces, i.e., emits light at wavelengths of 520 to 530 nm. Thus, the hydrocarbon is excited by blue light and emits light that appears yellowish green." ([DailyMed: Ak-Fluor (fluorescein) prescribing information, Long Grove Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=73511e79-c050-4dc0-aa2f-a79ed320b5b0), label version 2026-02-26; accessed 2026-11-19.) Fluorescein is a diagnostic fluorescent dye used in retinal angiography and for staining the ocular surface. It has no known vasodilatory or anti-vasospastic activity.

No plausible mechanistic link to Prinzmetal angina has been identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; it is not backed by clinical or literature evidence. Other top-ranked predictions (antithrombin deficiency type 2, factor 5 excess, heparin cofactor 2 deficiency, partial deletion of chromosome 16p, beta-thalassemia) likewise have no identified mechanism.

For the predictions where literature was retrieved (rheumatoid arthritis, hemoglobinopathy, thrombophilia, hyperthyroidism), the papers describe fluorescein angiography or staining as a way to **detect or monitor** eye complications. These are diagnostic uses, not disease-modifying treatment, so they do not support a repurposing claim.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

For context, the literature retrieved for lower-ranked predictions is diagnostic or descriptive only (for example, sickle cell retinopathy imaging reviews and ocular findings in rheumatoid arthritis and thyroid eye disease). It does not show a therapeutic effect of fluorescein.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00505005 | FLUORESCITE | FLUORESCEIN (FLUORESCEIN SODIUM) | Marketed |
| 02148390 | MINIMS FLUORESCEIN SODIUM | FLUORESCEIN SODIUM | Marketed |
| 02160773 | DIOFLUOR STRIPS | FLUORESCEIN SODIUM | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction rests on a model score alone (L5), with no trials, no literature and no plausible mechanism. Fluorescein's established role is diagnostic, so none of the top 10 predictions currently justifies a therapeutic repurposing effort.

**To proceed, the following is needed:**
- A plausible pharmacological mechanism linking fluorescein to coronary vasospasm (and mechanism of action data in general)
- Package insert warnings and contraindications from Health Canada, plus approved indication text and dosage forms for each DIN
- Any preclinical or clinical evidence of therapeutic (not diagnostic) activity
- Confirmation that a diagnostic dye can be developed for systemic therapeutic use, including route and dose compatibility

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ak-Fluor (fluorescein) prescribing information, Long Grove Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=73511e79-c050-4dc0-aa2f-a79ed320b5b0) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

