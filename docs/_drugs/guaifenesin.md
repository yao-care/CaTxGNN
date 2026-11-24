---
layout: default
title: Guaifenesin
parent: Model Prediction Only (L5)
nav_order: 444
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "GUAIFENESIN"
predicted_indications: ["nasal cavity disease", "faucial diphtheria", "cervical disc degenerative disorder", "papillary conjunctivitis"]
description: "Guaifenesin: predicted new indication Nasal cavity disease (evidence level L5). In Canada: at least 20 DINs"
---

# Guaifenesin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Guaifenesin: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Guaifenesin is an expectorant that thins and loosens airway mucus. It has been used for upper-airway conditions such as allergic rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**.
Evidence is very limited: **no registered clinical trials** and **1 publication** (a 2002 review), so this remains a research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 (model prediction with no clinical studies; only one indirect review) |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of guaifenesin as: Unknown ([ChEMBL CHEMBL980 (guaifenesin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL980), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, guaifenesin is an expectorant that thins and loosens airway mucus. Its use in rhinitis and nasopharyngitis has been established, and mechanistically it may help with mucus-related nasal symptoms.

Nasal cavity disease is a broad category that includes the rhinitis conditions already listed as original indications. The very high TxGNN score (0.9998) probably reflects this overlap and is not an independent repurposing signal. In other words, the prediction is largely a restatement of existing uses rather than a new therapeutic discovery.

The only supporting publication is a 2002 article on respiratory allergies in voice users. It mentions that decongestants containing guaifenesin may be useful, which is indirect support only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | Treatment strategies for hidden respiratory allergies in voice users. Antihistamines are generally avoided, while decongestants containing guaifenesin may be useful. Steroids are helpful in perennial allergic symptoms. |

## Canada Market Information

All 20 licences are valid single-ingredient products. The data compiled for this report does not include dosage forms or approved indication text.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00476374 | CHOLEDYL EXPECTORANT | GUAIFENESIN; OXTRIPHYLLINE | Marketed |
| 00609951 | BALMINIL EXPECTORANT (SUCROSE FREE) | GUAIFENESIN | Marketed |
| 01931024 | ROBITUSSIN COUGH CONTROL | DEXTROMETHORPHAN HYDROBROMIDE; GUAIFENESIN | Marketed |
| 01944762 | BENYLIN REGULAR STRENGTH COUGH PLUS CHEST CONGESTION RELIEF | DEXTROMETHORPHAN HYDROBROMIDE; GUAIFENESIN | Marketed |
| 02121999 | BRONCHOPHAN EXPECTORANT (SANS SUCROSE) | GUAIFENESIN | Marketed |
| 02142775 | ROBITUSSIN EXTRA STRENGTH COUGH CONTROL | DEXTROMETHORPHAN HYDROBROMIDE; GUAIFENESIN | Marketed |
| 02142783 | ROBITUSSIN EXTRA STRENGTH MUCUS AND PHLEGM | GUAIFENESIN | Marketed |
| 02248568 | ROBITUSSIN SUGAR FREE COUGH CONTROL | DEXTROMETHORPHAN HYDROBROMIDE; GUAIFENESIN | Marketed |
| 02265427 | BENYLIN EXTRA STRENGTH CHEST CONGESTION & COLD | GUAIFENESIN; MENTHOL | Marketed |
| 02289164 | BUCKLEY'S CHEST CONGESTION | GUAIFENESIN; MENTHOL | Marketed |
| 02320940 | BENYLIN EXTRA STRENGTH MUCUS & PHLEGM | GUAIFENESIN; MENTHOL | Marketed |
| 02346451 | BUCKLEY'S MUCUS & PHLEGM | GUAIFENESIN; MENTHOL | Marketed |
| 02434725 | MUCINEX CHEST CONGESTION | GUAIFENESIN | Marketed |
| 02479869 | BENYLIN EXTRA STRENGTH SORE THROAT & COUGH | GUAIFENESIN; MENTHOL | Marketed |
| 02485524 | ROBITUSSIN EXTRA STRENGTH HONEY COUGH & CONGESTION | DEXTROMETHORPHAN HYDROBROMIDE; GUAIFENESIN | Marketed |
| 02522950 | JACK & JILL HONEY COUGH & COLD | DEXTROMETHORPHAN HYDROBROMIDE; GUAIFENESIN | Marketed |
| 02534762 | MUCUS & PHLEGM RELIEF EXTRA STRENGTH | GUAIFENESIN | Marketed |
| 02540908 | MUCUS & PHLEGM RELIEF WITH COUGH CONTROL EXTRA STRENGTH | DEXTROMETHORPHAN HYDROBROMIDE; GUAIFENESIN | Marketed |
| 02541882 | COUGH & CHEST CONGESTION REGULAR STRENGTH | DEXTROMETHORPHAN HYDROBROMIDE; GUAIFENESIN | Marketed |
| 02541890 | COUGH & CHEST CONGESTION EXTRA STRENGTH | DEXTROMETHORPHAN HYDROBROMIDE; GUAIFENESIN | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

Package insert warnings, contraindications and drug interaction data were not available for this report. Please refer to the package insert for safety information.

The knowledge graph links guaifenesin to a list of contraindicated conditions. This is graph-derived and not label text, so it should be verified against the official label. The conditions include:
- Cardiovascular: hypertension
- Hepatic and gastrointestinal: liver failure, liver disease, cirrhosis, gastric ulcer, peptic ulcer disease, pancreatitis, gallbladder disease, inflammatory bowel disease
- Respiratory: chronic obstructive pulmonary disease
- Neuropsychiatric: epilepsy, insomnia, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder
- Metabolic and endocrine: porphyria, hypothyroidism, myxedema, adrenocortical insufficiency (Addison disease)
- Renal and haematological: kidney disease, thrombocytopenia

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication largely overlaps with guaifenesin's existing rhinitis-related uses. There are no clinical trials, and the single publication is an indirect, low-tier review. The package insert safety review is also incomplete, so the candidate cannot move beyond the research-question stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Clarification of which specific nasal cavity conditions are meant, beyond those already covered by existing indications
- Controlled clinical evidence, or a targeted literature search, for the predicted indication
- Dosage form, route and approved indication details for the Canadian products

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL980 (guaifenesin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL980) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

