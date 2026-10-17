---
layout: default
title: Rifaximin
parent: Moderate Evidence (L3-L4)
nav_order: 807
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-13
description: "Rifaximin: predicted new indication Oral candidiasis (evidence level L4). Approved use: Hepatic encephalopathy, hepatic coma"
monitor_inn: "RIFAXIMIN"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Rifaximin: From Hepatic Encephalopathy to Oral Candidiasis

## One-Sentence Summary

Rifaximin is a gut-targeted oral antibiotic, originally used for hepatic encephalopathy and hepatic coma.
The TxGNN model predicts it may be effective for **Oral Candidiasis**,
but there are **0 clinical trials** and only **1 publication**, and that publication points to increased Candida infection risk rather than benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic encephalopathy, hepatic coma (the Canadian licence has no indication text on file, so these come from the knowledge-graph indication data) |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rifaximin is a minimally absorbed, gut-targeted antibiotic. Its efficacy in hepatic encephalopathy is established, and it acts by reducing bacteria in the gut.

A mechanistic link to oral candidiasis is weak. Candidiasis is a fungal infection, and rifaximin has no known antifungal activity. The one available publication (PMID 34180023) suggests the opposite of a therapeutic effect: rifaximin use was associated with micafungin-resistant Candida infections in patients receiving allogeneic stem cell transplants. This may reflect selection pressure or disruption of the microbiome. The high TxGNN score is therefore not supported by a plausible mechanism or by clinical evidence of benefit.

The other top predictions (commissural lip fistula, osteoradionecrosis of the mandible, oral leukoedema, burning mouth syndrome) have no clinical trials or literature at all, and no plausible rationale for rifaximin. The broader candidiasis prediction (score 99.15%) is likewise supported only by studies showing increased Candida risk.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | Rifaximin was proposed as prophylaxis against gut bacterial infection and acute graft-versus-host disease in stem cell transplant recipients. Its use favoured micafungin-resistant Candida infections. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02410702 | ZAXINE | Not listed | Not listed |

## Safety Considerations

- **Knowledge-graph contraindications (not label text)**: Clostridium difficile colitis; perinatal necrotizing enterocolitis.
- **Drug Interactions**: 69 interactions were identified. Examples:
  - **Major**: Vibrio cholerae CVD 103-HgR live vaccine
  - **Moderate**: warfarin, cyclosporine, tolvaptan, apalutamide, darolutamide, cabozantinib, brigatinib, encorafenib, alpelisib, bempedoic acid, daclatasvir, ledipasvir, elagolix, eliglustat, enasidenib, istradefylline, picosulfuric acid
- **Candida signal**: The available literature links rifaximin use to resistant Candida infections in transplant patients, which is a safety consideration for this proposed use.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the evidence is thin and points the wrong way. Rifaximin has no known antifungal activity, there are no clinical trials, and the only study links it to increased risk of resistant Candida infection. The other top predictions have no evidence at all.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism of action data
- In vitro or preclinical data showing any antifungal or anti-candidal effect
- Prospective or controlled studies, which should include monitoring of Candida colonisation and resistance
- Route and formulation compatibility assessment, since rifaximin is minimally absorbed and oral candidiasis is a local mucosal infection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

