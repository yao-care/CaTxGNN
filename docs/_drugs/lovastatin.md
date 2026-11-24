---
layout: default
title: Lovastatin
parent: Model Prediction Only (L5)
nav_order: 563
evidence_level: L5
indication_count: 1
monitor_inn: "LOVASTATIN"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-24
description: "Lovastatin: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hyperlipidemia and related lipid disorders"
---

# Lovastatin
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

## Lovastatin: From Hyperlipidemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Lovastatin is a statin that is used for lipid disorders such as hyperlipidemia, hypertriglyceridemia and atherosclerosis.
The TxGNN model predicts it may be relevant for **cholesterol-ester transfer protein (CETP) deficiency**,
but there are currently **0 clinical trials** and **1 publication** (an unrelated mouse study), so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia and related lipid disorders (relations recorded in the knowledge graph; no approved indication text is available in the licence records) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for lovastatin: "The mechanism of the LDL-lowering effect of lovastatin may involve both reduction of VLDL-C concentration, and induction of the LDL receptor, leading to reduced production and/or increased catabolism of LDL-C. Apolipoprotein B also falls during treatment with lovastatin. Lovastatin is a specific inhibitor of HMG-CoA reductase, the enzyme which catalyzes the conversion of HMG-CoA to mevalonate." ([DailyMed: lovastatin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac86821f-d741-4ab1-bd03-ce8797dd4f34), label version 2026-11-13; accessed 2026-11-19.) Based on general knowledge, lovastatin is an HMG-CoA reductase inhibitor that lowers LDL cholesterol and modestly influences overall lipoprotein metabolism. This is background knowledge, not data from the compiled records.

The link to CETP deficiency is plausible only at the pathway level (cholesterol homeostasis). CETP deficiency is characterised by high HDL cholesterol and altered LDL/HDL particle remodelling, so a statin's lipid-lowering action is only loosely related. The TxGNN score is a model-based prediction with no supporting clinical data.

CETP deficiency is also a genetic trait often associated with elevated HDL cholesterol, and it is not clearly a condition that requires drug treatment. This weakens the clinical rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19965609](https://pubmed.ncbi.nlm.nih.gov/19965609/) | 2010 | Preclinical (mouse knockout model) | Journal of Lipid Research | Disruption of StarD4, a lipid-transfer protein, in mice led to modest weight reduction and minor changes in lipid metabolism. It does not study lovastatin or CETP deficiency. |

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02220172 | LOVASTATIN | LOVASTATIN | Marketed |
| 02220180 | LOVASTATIN | LOVASTATIN | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

The following items come from knowledge-graph relations, not from package insert text.

- **Contraindication relations recorded in the knowledge graph**: liver disease, gallbladder disease, thrombocytopenia, hyperglycemia, peptic ulcer disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, gout, substance abuse/dependence, blood coagulation disease, acute coronary syndrome, rhabdomyolysis, nodular fasciitis, coronary artery disease, myocardial infarction, coronary thrombosis, hemoglobinopathy, injury, hypophosphatemia.
- **Drug Interactions**: 100 interactions were found in total; the 20 listed in the data include:
  - **Major**: clarithromycin
  - **Moderate**: aprepitant, omeprazole, esomeprazole, lansoprazole, pantoprazole, metronidazole, tinidazole, cimetidine, eluxadoline, naltrexone, clotrimazole, miconazole, pectin, rosuvastatin, simvastatin, troglitazone
  - **Minor**: exenatide
  - **Unknown level**: calcitriol, glimepiride

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No clinical trial exists, and the single retrieved publication is a mouse study unrelated to lovastatin or CETP deficiency. The clinical need is also unclear, since CETP deficiency is often a benign genetic trait.

**To proceed, the following is needed:**
- Studies that directly examine lovastatin or statins in CETP deficiency
- Evidence that treating CETP deficiency is clinically needed
- Mechanism of action data
- Health Canada package insert warnings and contraindications for safety screening
- Approved indication text for the two Canadian licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: lovastatin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac86821f-d741-4ab1-bd03-ce8797dd4f34) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

