---
layout: default
title: Pibrentasvir
parent: Model Prediction Only (L5)
nav_order: 734
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pibrentasvir: predicted new indication Hepatitis B virus infection (evidence level L5). Approved use: Chronic hepatitis C virus infection"
monitor_inn: "PIBRENTASVIR"
predicted_indications: ["hepatitis B virus infection", "HIV infectious disease", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Pibrentasvir
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

## Pibrentasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection
{: .text-alpha }

## One-Sentence Summary

Pibrentasvir is an NS5A inhibitor, originally used to treat chronic hepatitis C virus (HCV) infection, and it is marketed in Canada as part of MAVIRET (glecaprevir/pibrentasvir).
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, but there are **no clinical trials** and **no HBV-specific publications** supporting this prediction. All retrieved literature concerns HCV, so this is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, pibrentasvir is an HCV NS5A inhibitor used in combination with the protease inhibitor glecaprevir, and its efficacy in HCV has been well established.

The mechanistic link to hepatitis B is weak. NS5A is a protein specific to HCV (a Flaviviridae virus) and has no homolog in HBV. HBV is a DNA virus that replicates through reverse transcription, so it is structurally and functionally unrelated to HCV. The high TxGNN score most likely reflects the shared "viral hepatitis" context in the knowledge graph rather than a true drug-target relationship.

The other top-ranked predictions show the same pattern. These include HIV infection, hepatitis E, hepatitis A, tick-borne flaviviruses (Omsk hemorrhagic fever, Kyasanur forest disease), animal retroviruses, and a rare neurodevelopmental disorder. None has a supported mechanistic basis. The HIV and hepatitis A trials found are HCV studies (in HIV/HCV-coinfected patients or with matching artifacts), not studies of those diseases as treatment targets.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for hepatitis B virus infection.

---

## Literature Evidence

The publications retrieved for this prediction are listed below. None provides HBV-specific efficacy data for pibrentasvir.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort | J Viral Hepat | Real-world glecaprevir/pibrentasvir in HCV patients with severe renal impairment in Taiwan (108 patients); HCV, not HBV |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review | Lancet Gastroenterol Hepatol | HCV infection in children and adolescents; direct-acting antivirals have transformed treatment |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | Diagnosis and treatment of chronic hepatitis C in primary care |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Management of pediatric viral hepatitis; HBV treatment remains far from curative |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Review | AIDS Rev | Conference report on viral hepatitis treatment, covering both HBV and HCV |
| [42127258](https://pubmed.ncbi.nlm.nih.gov/42127258/) | 2026 | Review | Top Antivir Med | CROI 2026 viral hepatitis overview; no pibrentasvir-specific HBV data |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Preclinical/Virology | Hepatology | HCV protease inhibitor resistance variants; HCV only |
| [31129632](https://pubmed.ncbi.nlm.nih.gov/31129632/) | 2019 | Case report | BMJ Case Rep | Glecaprevir/pibrentasvir-associated acute liver injury in HCV patient without HBV co-infection |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02522470 | MAVIRET | Not specified | Not specified |
| 02467550 | MAVIRET | Not specified | Not specified |

---

## Cytotoxicity

Not applicable. Pibrentasvir is an antiviral, not an antineoplastic drug.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report, and the available literature includes a case report of glecaprevir/pibrentasvir-associated acute liver injury in an HCV patient.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (evidence level L5). It has no registered trials or HBV-specific literature, and pibrentasvir's NS5A target has no counterpart in HBV. The score most likely reflects knowledge-graph association between viral hepatitis diseases.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) for pibrentasvir
- In vitro evidence of anti-HBV activity (for example, HBV replication assays)
- Health Canada package insert warnings and contraindications
- Product details for the Canadian licenses (dosage form and approved indication text)
- Any HBV-specific preclinical or clinical studies, since all current literature concerns HCV
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

