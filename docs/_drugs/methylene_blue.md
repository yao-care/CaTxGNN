---
layout: default
title: Methylene Blue
parent: Model Prediction Only (L5)
nav_order: 604
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Methylene Blue: predicted new indication Bronchitis (evidence level L5). Approved use: Methemoglobinemia, sulfhemoglobinemia"
monitor_inn: "METHYLENE BLUE"
predicted_indications: ["bronchitis", "methemoglobinemia, alpha type", "methemoglobinemia due to deficiency of methemoglobin reductase"]
---

# Methylene Blue
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Methylene Blue: From Methemoglobinemia to Bronchitis

## One-Sentence Summary

Methylene blue is an established treatment for methemoglobinemia and sulfhemoglobinemia.
The TxGNN model predicts it may be effective for **Bronchitis**, but this is a model-only prediction with **0 clinical trials** and **no publications that actually support therapeutic use** in this setting.
The data compiled for this report also list two other predictions (congenital methemoglobinemia forms) that largely overlap with the drug's existing use and are better supported mechanistically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Methemoglobinemia, sulfhemoglobinemia (the Canadian licence records contain no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, methylene blue is a redox-active dye. It is reduced to leucomethylene blue, which converts methemoglobin back to functional haemoglobin. This explains its original use. It is also known to affect nitric oxide signalling and to have antimicrobial and photosensitizing properties, but none of this is documented in the data compiled for this report.

No plausible mechanistic link to bronchitis is supported by the available data. The retrieved literature mentions methylene blue only as a diagnostic stain (for example, in bronchoscopy) or is unrelated (plant essential oils, biosensors, beta-blockers, an endocarditis case). The very high score therefore looks like an artifact of the knowledge graph rather than clinical evidence.

By contrast, the two other predictions, **methemoglobinemia, alpha type** (score 99.36%) and **methemoglobinemia due to methemoglobin reductase deficiency** (score 99.36%), are mechanistically sound. They fall within the drug's original indication, so they are extensions of existing use rather than true repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the retrieved papers shows therapeutic efficacy of methylene blue in bronchitis. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | Diagnostic study | Zhonghua Wai Ke Za Zhi | Methylene blue staining during bronchoscopy: 97.14% of central malignant bronchial tumours stained versus 8.33% of bronchitis cases. Diagnostic use only. |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | Diagnostic study | Terapevticheskii Arkhiv | Chromoendoscopy with methylene blue to distinguish benign from malignant gastrointestinal and bronchial neoplasms. |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | Methodological study | Am Rev Respir Dis | Methylene blue used as a marker to quantify intraalveolar fluid in bronchoalveolar lavage. Not an efficacy study. |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | Clinical pharmacology | Int J Clin Pharmacol Ther Toxicol | Methylene blue used as an indicator-dilution tracer in a beta-blocker study. Unrelated. |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | Preclinical | J Ethnopharmacol | Plant essential oil relaxes guinea-pig trachea. Does not involve methylene blue therapy. |

The remaining retrieved papers (an electrochemical aptasensor, an Aloysia gratissima antidepressant study, a Moraxella endocarditis case report) are unrelated and not listed.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02487993 | Methylene Blue Injection | Not specified | Not specified |
| 02230770 | Methylene Blue Injection USP | Not specified | Not specified |
| 00050466 | Methylene Bleu Liq 1% | Not specified | Not specified |
| 00674354 | Collyre Bleu Laiter | Not specified | Not specified |

All four licences are valid single-ingredient products.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** The TxGNN knowledge graph links methylene blue to contraindications in G6PD deficiency, hypertension, liver failure and liver disease, kidney disease, congestive heart failure, coronary artery disease, anaemia, diabetes mellitus and diabetic ketoacidosis, blood coagulation disorders and haemophilia, myasthenia gravis, and heart conduction disease, among others. These need verification against the product monograph.
- **Drug Interactions:** 100 interactions are recorded. Many are rated Major, notably with serotonergic or sympathomimetic agents: bupropion, ondansetron, granisetron, dolasetron, palonosetron, morphine, opium, phentermine, fenfluramine, dexfenfluramine, lorcaserin, mazindol, diethylpropion, ephedrine and isometheptene. Epinephrine products are rated Moderate. Serotonin syndrome risk is the main concern.
- **Other considerations:** Haemolysis in G6PD deficiency and paradoxical methaemoglobin formation at high doses are known concerns. The Canadian package insert warnings and contraindications have not been retrieved, so a full safety screen cannot be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on a model score alone. There are no clinical trials, and the literature shows methylene blue only as a diagnostic stain or in unrelated contexts. The safety profile is also substantial, with many major interactions and several knowledge-graph contraindications.

**To proceed, the following is needed:**
- A plausible mechanistic rationale for bronchitis, supported by preclinical data (anti-inflammatory, antimicrobial or nitric oxide pathway effects in airways)
- Mechanism of action data for the drug
- Canadian package insert warnings and contraindications, including approved indications and dosage forms
- Route feasibility assessment (inhaled or systemic delivery has not been evaluated)
- Consideration of the congenital methemoglobinemia predictions as a separate, better-supported line of work. Evidence there is limited to human case reports and veterinary studies of oral long-term use, and it is essentially an extension of existing use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

