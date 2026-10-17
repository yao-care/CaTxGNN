---
layout: default
title: Sodium Citrate
parent: Model Prediction Only (L5)
nav_order: 855
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Sodium Citrate: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease, esophagitis…"
monitor_inn: "SODIUM CITRATE"
predicted_indications: ["papillary conjunctivitis", "postgastrectomy syndrome", "gastroduodenitis", "familial visceral myopathy", "rosacea conjunctivitis", "allergic urticaria"]
---

# Sodium Citrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Sodium Citrate: From Acid-Related Upper GI and Upper Respiratory Conditions to Papillary Conjunctivitis

## One-Sentence Summary

Sodium citrate is a buffering (antacid) agent, originally associated with peptic ulcer disease, gastroesophageal reflux disease, dyspepsia and upper respiratory conditions such as rhinitis and the common cold.
The TxGNN model predicts it may be effective for **Papillary Conjunctivitis** (top-ranked prediction), but **no clinical trials and no publications** currently support this direction.
The prediction is a computational signal only, and the evidence is at the model-prediction level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, esophagitis, dyspepsia, pharyngitis, common cold, rhinitis, nasopharyngitis (from the knowledge graph; no approved-indication text is available for the Canadian licences) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sodium citrate acts as a buffer and antacid and as a calcium chelator. Its role in acid-related gastric conditions is plausible, but a mechanistic connection to papillary conjunctivitis (an allergic or contact-lens-related ocular inflammation) is not supported by the data compiled for this report.

The high TxGNN score (99.95%) is a computational prediction only. It may reflect how the knowledge graph links sodium citrate to inflammatory conditions of the upper airway and mucosa (rhinitis, nasopharyngitis, common cold), rather than any independent evidence of efficacy in the eye.

Other predictions in the same list are also at low evidence levels:

| Rank | Predicted Indication | Score | Evidence Level | Note |
|---|---|---|---|---|
| 2 | Nasal cavity disease | 99.95% | L5 | Likely reflects proximity to existing rhinitis/cold indications |
| 3 | Acute laryngopharyngitis | 99.94% | L5 | Largely an extension of existing pharyngitis indications |
| 4 | Stomach disease | 99.89% | L4 | Only indirect preclinical and mixed-quality literature |
| 6 | Gastroduodenitis | 99.62% | L4 | Two indirect papers only |

The stomach-related predictions (ranks 4 and 6) are the most mechanistically plausible, because of gastric acid buffering. They are still not supported by direct trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for papillary conjunctivitis.

---

## Literature Evidence

Currently no related literature available for papillary conjunctivitis.

For reference, the literature retrieved for the related prediction "stomach disease" is indirect, and several records look off-topic:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27163639](https://pubmed.ncbi.nlm.nih.gov/27163639/) | 2016 | In vitro | Biochem Biophys Res Commun | 3-Bromopyruvate plus sodium citrate induced apoptosis in a gastric cancer cell line by inhibiting glycolysis |
| [26708213](https://pubmed.ncbi.nlm.nih.gov/26708213/) | 2016 | In vitro / animal | Oncol Rep | The same combination suppressed survivin and inhibited orthotopic gastric tumour growth |
| [29115645](https://pubmed.ncbi.nlm.nih.gov/29115645/) | 2018 | Animal xenograft | Oncol Rep | FDG PET/CT used to evaluate glycolysis-targeted therapy in a gastric xenograft model |
| [25316860](https://pubmed.ncbi.nlm.nih.gov/25316860/) | 2014 | Community RCT | J Infect Dis | Effect of a buffer solution on the immune response to oral poliovirus vaccine |
| [1777551](https://pubmed.ncbi.nlm.nih.gov/1777551/) | 1991 | Clinical/formulation | Aliment Pharmacol Ther | A glucose–sodium citrate formulation reduced gastric mucosal damage from azapropazone in rats, with a trend toward less blood loss in volunteers |
| [7086102](https://pubmed.ncbi.nlm.nih.gov/7086102/) | 1982 | Clinical physiology | J Clin Gastroenterol | Gastroduodenal acidification did not provoke ulcer-type pain in most patients with active duodenal ulcer |
| [1959368](https://pubmed.ncbi.nlm.nih.gov/1959368/) | 1991 | Clinical comparison | Crit Care Med | Sucralfate vs ranitidine for stress ulceration and secondary pneumonia in ICU patients |

These papers do not directly test sodium citrate as a treatment for the predicted conditions.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02529637 | Anticoagulant Sodium Citrate Solution, USP | Not specified | Not specified |
| 00060313 | Anticoagulant Sod Citrate Soltn 4 g/100 mL | Not specified | Not specified |
| 02377411 | Anticoagulant Sodium Citrate 4% w/v Solution, USP | Not specified | Not specified |
| 02496755 | Regiocit | Not specified | Not specified |
| 02469731 | Anticoagulant Citrate Dextrose Solution USP (ACD) Formula A | Not specified | Not specified |

A total of 12 valid single-ingredient licences are on the Canadian market (none cancelled). The product names indicate that the marketed products are mainly anticoagulant, blood-processing and irrigating solutions rather than oral antacids.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** The knowledge graph links sodium citrate to several conditions where caution may be warranted, including:
  - Cardiovascular: hypertension, coronary artery disease, myocardial infarction
  - Renal and metabolic: impaired renal function, anuria, metabolic acidosis, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease
  - Adrenal: adrenal insufficiency, Addison disease, congenital adrenal hyperplasia
  - Other: pancreatitis, benign prostatic hyperplasia, angle-closure glaucoma, ocular hypertension, rhabdomyolysis, hemoglobinopathy
- **Drug Interactions:** 100 interactions were identified; the 20 shown here include:
  - **Major:** aluminum hydroxide
  - **Moderate:** doxycycline, minocycline, tetracycline, levofloxacin, aspirin, iron, rosuvastatin, acalabrutinib, ephedrine (including nasal), pseudoephedrine
  - **Minor:** sulfonylureas (acetohexamide, chlorpropamide, glipizide, glyburide, tolazamide, tolbutamide), lactulose, misoprostol

Label-based warnings and contraindications from Health Canada were not available, so the list above should be confirmed against the product monograph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The papillary conjunctivitis prediction has a high model score but no supporting trials, literature or plausible mechanism, so it is an L5 (prediction-only) signal. Marketed Canadian products are mainly non-oral solutions, which also leaves route compatibility with an ocular indication unresolved.

**To proceed, the following is needed:**
- Mechanism of action data for sodium citrate, to assess any biological link to ocular inflammation
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening)
- Preclinical or clinical evidence in papillary conjunctivitis, or a re-prioritisation toward better-supported gastric predictions (stomach disease, gastroduodenitis)
- A route and formulation assessment (ocular vs. oral or systemic) for the chosen indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

