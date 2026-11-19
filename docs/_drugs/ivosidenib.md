---
layout: default
title: Ivosidenib
parent: Model Prediction Only (L5)
nav_order: 509
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-05
description: "Ivosidenib: predicted new indication Bulbar polio (evidence level L5). Approved use: Myeloid leukemia (including acute myeloid leukemia and related subtyp…"
monitor_inn: "IVOSIDENIB"
predicted_indications: ["bulbar polio"]
---

# Ivosidenib
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

## Ivosidenib: From Myeloid Leukemia to Bulbar Polio
{: .text-alpha }

## One-Sentence Summary

Ivosidenib is a targeted inhibitor of mutant IDH1, originally used to treat acute myeloid leukemia (AML) and related myeloid disorders.
The TxGNN model predicts it may be effective for **bulbar polio**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone and has no identified biological support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myeloid leukemia (including acute myeloid leukemia and related subtypes) |
| Predicted New Indication | Bulbar polio |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ivosidenib: "Ivosidenib is a small molecule inhibitor that targets the mutant isocitrate dehydrogenase 1 (IDH1) enzyme. In patients with AML, susceptible IDH1 mutations are defined as those leading to increased levels of 2-hydroxyglutarate (2-HG) in the leukemia cells and where efficacy is predicted by 1) clinically meaningful remissions with the recommended dose of ivosidenib and/or 2) inhibition of mutant IDH1 enzymatic activity at concentrations of ivosidenib sustainable at the recommended dosage according to validated methods." ([DailyMed: Tibsovo (ivosidenib) prescribing information, Servier Pharmaceutical LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=65d254c0-67ad-42c4-b972-ad463b755b2d), label version 2025-12-22; accessed 2026-11-19.) From general knowledge, ivosidenib inhibits the mutant IDH1 enzyme and lowers 2-hydroxyglutarate in IDH1-mutated tumours. Its efficacy in IDH1-mutated AML is the basis for its original indication.

Bulbar polio is a viral infection of motor neurons caused by poliovirus. It is not a tumour and has no known link to IDH1 mutation or 2-hydroxyglutarate metabolism. No plausible mechanistic link between ivosidenib and this disease could be identified. The very high TxGNN score (0.9931) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and no trials or literature corroborate it.

**Other predictions of note:** Two other high-scoring predictions are closely related to the approved indications:

Both are secondary myeloid neoplasms. They are essentially an extension of the existing AML label, since therapy-related AML is already among the original indications. A benefit is biologically plausible only if the disease carries an IDH1 mutation. No subtype-specific trials or literature are available, so the evidence is indirect. These two are better framed as research questions that need IDH1 mutation stratification than as true repurposing candidates.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02549980 | TIBSOVO | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mutant IDH1 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (haematological parameters, liver and renal function are generally monitored) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

**Drug Interactions:** The interaction screening returned 100 interacting drugs in total. The first 20 returned include the following.

- **Major:** aprepitant, clarithromycin, dolasetron, palonosetron, cisapride, granisetron, levofloxacin
- **Moderate:** famotidine, loperamide, bisacodyl, picosulfuric acid, polyethylene glycol (3350 with electrolytes), saxagliptin, eliglustat, linagliptin, sodium sulfate, castor oil, glycerin, lactitol, lactulose

Several of the major interactions involve antiemetics and QT-prolonging agents, so co-prescribing deserves particular care.

For other safety information, such as warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for bulbar polio has no clinical trials, no literature, and no plausible mechanistic link. The high score appears to be a TxGNN model (deep learning) artifact. Ivosidenib's mechanism targets IDH1-mutated tumours, not a viral infection of motor neurons.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Any biological or preclinical evidence linking mutant IDH1 inhibition to poliovirus infection (none currently identified)
- For the therapy-related AML/MDS subtypes (alkylating agent- and radiation-related): subtype-specific clinical data and IDH1 mutation stratification, as a separate research question

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tibsovo (ivosidenib) prescribing information, Servier Pharmaceutical LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=65d254c0-67ad-42c4-b972-ad463b755b2d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

