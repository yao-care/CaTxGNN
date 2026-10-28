---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 557
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "Loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "serous conjunctivitis except viral", "parasitic conjunctivitis", "chronic follicular conjunctivitis", "conjunctival folliculosis", "Angelucci syndrome"]
description: "Loperamide: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Loperamide
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

## Loperamide: Acute contagious conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Loperamide is an anti-diarrhoeal medicine, originally used for diarrheal disease and dysentery symptoms.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
The high score appears to be a TxGNN model (deep learning) artifact rather than a biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 14 of 14) |
| Number of DINs | 14 (valid: 14) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, loperamide is a peripheral mu-opioid receptor agonist that acts on the myenteric neurons of the gut to slow motility. This is how it reduces diarrhoea.

That mechanism has no plausible connection to an infectious condition of the ocular surface. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as diarrhea- and infection-related conditions, not biological evidence. Opioid receptors exist in ocular tissue, but nothing shows a therapeutic effect in conjunctival disease.

The other top-ranked predictions follow the same pattern. Seven of the top ten are conjunctival conditions (conjunctivitis, pseudomembranous, serous, parasitic and chronic follicular conjunctivitis, conjunctival folliculosis, Angelucci syndrome). None has any clinical evidence. The two gastrointestinal predictions (amebic dysentery and gastroduodenitis) have only literature that points to harm.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No publications are available for acute contagious conjunctivitis.

Literature exists only for two other predicted indications, and both raise safety concerns rather than efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Case report | J Travel Med | Fulminant amoebic colitis and toxic megacolon in a patient with heavy loperamide use (amebic dysentery prediction) |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | Am J Med | Non-fluid therapy for acute diarrhoea, including antimotility agents and bismuth subsalicylate (amebic dysentery prediction) |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Case report | Cureus | Loperamide-induced respiratory depression in severe chemotherapy-related gastrointestinal inflammation (gastroduodenitis prediction) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02238211 | RIVA-LOPERAMIDE | Not available | Not available |
| 02544989 | JAMP LOPERAMIDE | Not available | Not available |
| 02291800 | IMODIUM CALMING LIQUID | Not available | Not available |
| 02499517 | DIARRHEA RELIEF FAST DISSOLVE | Not available | Not available |
| 02552337 | DIARRHEA RELIEF LIQUID GELS | Not available | Not available |

There are 14 valid single-ingredient licences in total. None is cancelled, and none is a combination product.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: liver disease, gallbladder disease, paralytic ileus, intestinal obstruction, familial visceral myopathy, dysentery, diarrheal disease, infectious diarrheal disease, intestinal infectious disease.
- **Drug Interactions**: 100 interactions were found. Examples of **Major** interactions are abiraterone, ranitidine, fosamprenavir and gemfibrozil. **Moderate** interactions include codeine, dihydrocodeine, tramadol, ethanol, chlorpheniramine, cetirizine, salbutamol, galantamine and gemifloxacin.
- **Related safety signals in the literature**: toxic megacolon in invasive amoebic colitis, and respiratory depression when the gut is severely inflamed and absorption increases.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. It has no mechanistic link, no clinical trials and no literature (Evidence Level L5). The other predictions with literature show safety signals, not therapeutic benefit.

**To proceed, the following is needed:**
- Documented mechanistic evidence that loperamide acts on conjunctival disease, plus preclinical data in an ocular model
- Package insert warnings and contraindications from Health Canada, and mechanism of action data from DrugBank
- A route and formulation assessment, since all current products are oral and an ocular use would need a new formulation
- A review of whether the TxGNN model (deep learning) score reflects similarities the model learned between related diseases (for example, shared infection-related conditions), not biological evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

