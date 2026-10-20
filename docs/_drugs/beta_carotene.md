---
layout: default
title: Beta Carotene
parent: Moderate Evidence (L3-L4)
nav_order: 109
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Beta Carotene: predicted new indication Acne (disease) (evidence level L4). Approved use: Not available"
monitor_inn: "Beta carotene"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "cortical cataract", "nuclear senile cataract", "diabetes mellitus type 2 associated cataract", "mature cataract", "tetanic cataract", "immature cataract"]
---

# Beta Carotene
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Beta Carotene: From an Unspecified Original Indication to Acne

## One-Sentence Summary

Beta carotene is a provitamin A carotenoid with antioxidant activity. It is currently marketed in Canada only as a component of pregnancy multivitamin products, and no formal approved indication text is available.
The TxGNN model predicts it may be effective for **acne (disease)**, but there are **no registered clinical trials** and only **7 publications**, none of which tested beta carotene as an acne treatment.
The evidence is therefore weak, and the prediction is best treated as a research hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the Canadian licence records) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, beta carotene is a provitamin A carotenoid with antioxidant properties, and it is marketed in Canada within multivitamin products. Mechanistically, it may be relevant to acne.

Acne vulgaris has been linked to oxidative stress and altered vitamin A and antioxidant status. This gives a plausible but indirect link between an antioxidant and vitamin A precursor and acne.

The available literature consists mainly of observational antioxidant and serum-level studies, studies of plant extracts, and a study of isotretinoin-induced oxidative toxicity. No study has tested beta carotene as an acne treatment. The very high TxGNN score (0.99999) is a model output and is not supported by clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20049267](https://pubmed.ncbi.nlm.nih.gov/20049267/) | 2009 | Cross-sectional | Indian J Dermatol | Oxidant/antioxidant status was assessed in obese adolescent females with acne vulgaris. |
| [22517509](https://pubmed.ncbi.nlm.nih.gov/22517509/) | 2012 | Cohort | Cell Biochem Funct | Pilot study of plasma antioxidant vitamins and oxidative markers in acne patients before and after isotretinoin; the treatment induced oxidative toxicity. |
| [7618499](https://pubmed.ncbi.nlm.nih.gov/7618499/) | 1995 | Review | J Am Board Fam Pract | General review of vitamins and their derivatives used as therapy. |
| [2073211](https://pubmed.ncbi.nlm.nih.gov/2073211/) | 1990 | Review | Australas J Dermatol | Skin abnormalities in 14 anorexia nervosa patients, including elevated beta-carotene levels and acne in a small subset. |
| [4230169](https://pubmed.ncbi.nlm.nih.gov/4230169/) | 1967 | Cross-sectional | Dermatol Wochenschr | Serum vitamin A and beta-carotene levels in people with and without skin diseases. |
| [39459015](https://pubmed.ncbi.nlm.nih.gov/39459015/) | 2024 | In vitro | Pharmaceuticals (Basel) | Antioxidant and antibacterial properties of ylang-ylang essential oil with potential dermatological use (not beta carotene). |
| [23625436](https://pubmed.ncbi.nlm.nih.gov/23625436/) | 2013 | In vitro | Pak J Pharm Sci | Antioxidant and antibacterial activity of Helichrysum oligocephalum extracts (not beta carotene). |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02535718 | PREGNANCY MULTIVITAMIN | Not specified | Not specified |
| 02552620 | PREGVIT | Not specified | Not specified |
| 02537478 | PREGNANCY MULTIVITAMIN FOLIC 5 | Not specified | Not specified |
| 02552639 | PREGVIT FOLIC 5 | Not specified | Not specified |

---

## Safety Considerations

- **Disease associations flagged by the knowledge graph (not label text)**: The TxGNN knowledge graph lists contraindication links with blood coagulation disease, sickle cell anemia, hereditary persistence of fetal hemoglobin, primary hyperoxaluria, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, and Wilson disease. These come from a model knowledge graph and should be verified against the official product labelling.
- **Drug Interactions**: Two interactions were identified.
  - Verteporfin: Moderate
  - Lutein: Minor

Please refer to the package insert for warnings and contraindications from the label, as these were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a very high model score and an indirect antioxidant rationale. There are no clinical trials, and no study has tested beta carotene as an acne treatment. The evidence is graded L4, and the label safety information needed for safety screening is missing.

**To proceed, the following is needed:**
- The Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Interventional studies of beta carotene in acne, or at least controlled data comparing acne patients with healthy controls
- Clarification of the original approved indication and dosage forms for the Canadian products
- Review of the knowledge-graph disease associations (such as iron metabolism disorders and Wilson disease) against labelling

---

### Note on Other Predicted Indications

The data compiled for this report also include other predictions with the same or lower evidence strength:

- **Diabetic retinopathy (L4)**: Evidence is preclinical (diabetic rodent models) and observational, with no clinical trials. It is classed as a research question.
- **Cortical cataract (L3)**: Interventional data exist, including the ATBC trial substudy (PMID 9527321). They did not show a clear benefit from beta carotene, and this is classed as a research question.
- **Diabetic cataract and type 2 diabetes-associated cataract (L4)**: Only observational or general literature is available.
- **Severe nonproliferative diabetic retinopathy, nuclear senile, mature, tetanic and immature cataract (L5)**: Model prediction only, with no supporting studies. For mature and tetanic cataract, the antioxidant rationale is also unlikely to be relevant.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

