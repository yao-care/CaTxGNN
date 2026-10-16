---
layout: default
title: Desmopressin
parent: Model Prediction Only (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Desmopressin: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Hereditary von Willebrand disease"
monitor_inn: "Desmopressin"
predicted_indications: ["congenital prothrombin deficiency", "inherited thrombophilia", "Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Scott syndrome", "flood factor deficiency", "thrombocytopenic purpura", "bleeding diathesis due to a collagen receptor defect", "hereditary thrombocytosis with transverse limb defect"]
---

# Desmopressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Desmopressin: From Von Willebrand Disease to Congenital Prothrombin Deficiency

## One-Sentence Summary

Desmopressin is a synthetic vasopressin analogue, originally used for hereditary von Willebrand disease, haemophilia (including symptomatic female carriers) and nocturnal enuresis.
The TxGNN model's top-ranked prediction is **congenital prothrombin deficiency**, but it has **0 clinical trials** and only **1 publication** (a 1993 general review), so the evidence is very weak.
Among the 10 predicted indications, **primary release disorder of platelets** has the most credible support and is discussed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary von Willebrand disease; haemophilia; nocturnal enuresis (the Canadian licence records contain no indication text) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on published knowledge, desmopressin triggers V2 receptor-mediated release of von Willebrand factor (vWF) and factor VIII from endothelial stores. This is why it works in mild haemophilia A and in some subtypes of von Willebrand disease.

For the top-ranked prediction, **congenital prothrombin deficiency**, this mechanism does not fit. Desmopressin does not raise prothrombin (factor II) levels. The high TxGNN score most likely reflects the disease's proximity to other coagulation disorders in the knowledge graph rather than a true therapeutic link.

Looking across all 10 predictions, they fall into three groups:

- **Plausible:** *Primary release disorder of platelets*. Desmopressin may shorten bleeding time by raising vWF and improving platelet-vessel wall interaction. A paediatric study in aspirin-like defect (PMID 21509710) and a 2023 review (PMID 36656570) support this, though there is no randomised trial. This is the strongest candidate.
- **Weak or indirect:** Glanzmann thrombasthenia (the aggregation defect cannot be corrected by desmopressin), Scott syndrome, bleeding diathesis due to a collagen receptor defect, and the entry "flood factor deficiency" (which appears to be a data artefact).
- **Safety signal rather than opportunity:** Inherited thrombophilia, thrombocytopenic purpura and pseudo-von Willebrand disease (platelet-type). Desmopressin-induced vWF release can worsen thrombotic thrombocytopenic purpura and platelet clumping. Several case reports document this.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

Literature for the top-ranked prediction (congenital prothrombin deficiency):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | General review of treatment options for inherited bleeding disorders; no specific evidence for desmopressin in prothrombin deficiency |

Selected literature for the most relevant prediction (primary release disorder of platelets):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36656570](https://pubmed.ncbi.nlm.nih.gov/36656570/) | 2023 | Review | Eur J Haematol | Desmopressin releases vWF and FVIII, enhances platelet adhesion and shortens bleeding time; effective in mild haemophilia A, some von Willebrand disease subtypes, and uraemic or liver-disease bleeding; hyponatraemia and rare arterial thrombosis are risks |
| [21509710](https://pubmed.ncbi.nlm.nih.gov/21509710/) | 2011 | Cohort | Klin Padiatr | Evaluated desmopressin effect on primary haemostasis in children with aspirin-like defect |
| [23051555](https://pubmed.ncbi.nlm.nih.gov/23051555/) | 2013 | Mechanistic study | Haemophilia | More vWF is bound to microparticles after desmopressin infusion, which may explain effects in platelet disorders |
| [22057877](https://pubmed.ncbi.nlm.nih.gov/22057877/) | 2011 | Case report | Hamostaseologie | Refractory menorrhagia as first manifestation of Hermansky-Pudlak syndrome |
| [22726100](https://pubmed.ncbi.nlm.nih.gov/22726100/) | 2012 | Review | Haemophilia | Overview of inherited platelet disorders |

Safety-relevant literature (thrombotic thrombocytopenic purpura):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15499705](https://pubmed.ncbi.nlm.nih.gov/15499705/) | 2004 | Case report | Thromb Haemost | Worsening of TTP symptoms after desmopressin |
| [21921792](https://pubmed.ncbi.nlm.nih.gov/21921792/) | 2011 | Case report | Blood Coagul Fibrinolysis | Moschcowitz-like syndrome after desmopressin for postpartum haemorrhage |
| [16460464](https://pubmed.ncbi.nlm.nih.gov/16460464/) | 2006 | Case report | J Thromb Haemost | Link between desmopressin use for enuresis and inherited TTP (Upshaw-Schulman syndrome) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02513579 | BIPAZEN | Not listed | Not listed |
| 00873993 | DDAVP INJ 4MCG/ML | Not listed | Not listed |
| 02284030 | APO-DESMOPRESSIN | Not listed | Not listed |
| 02024179 | OCTOSTIM LIQ INJ. 15MCG/ML | Not listed | Not listed |
| 02242465 | DESMOPRESSIN SPRAY | Not listed | Not listed |

Ten valid single-ingredient authorisations are recorded in total; none is cancelled. The product names suggest injection, nasal spray and oral melt formulations.

---

## Safety Considerations

- **Contraindications and conditions flagged in the drug-disease knowledge graph:** hypertension, coronary artery disease, impaired renal function, cystic fibrosis, allergic or vasomotor rhinitis, pharyngitis, common cold, respiratory tract infection, von Willebrand disease (certain subtypes), dipsogenic diabetes insipidus, polydipsia and water intoxication. These come from the knowledge graph, not from label text, and should be verified against the product monograph.
- **Drug interactions:** The interaction check returned 100 entries. Major-level interactions include corticosteroids (hydrocortisone, dexamethasone, prednisone, prednisolone, triamcinolone, betamethasone, budesonide, beclomethasone). Moderate-level interactions include epinephrine, loperamide, morphine, opium and chlorpropamide. Acetylsalicylic acid is minor.
- **Literature safety signals:** Hyponatraemia, rare arterial thrombotic events, and worsening of TTP or platelet-type von Willebrand disease (type 2B-like thrombocytopenia).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, congenital prothrombin deficiency, has no mechanistic rationale, no trials and only one general review, so it is probably a graph-based false positive. Several other predictions (thrombophilia, thrombocytopenic purpura, platelet-type von Willebrand disease) represent safety concerns rather than opportunities. Only primary release disorder of platelets (evidence level L3) merits follow-up as a structured research question.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A focused clinical question and systematic literature review for primary platelet release disorders, ideally leading to a controlled study
- Clinical review of the knowledge-graph contraindications and TTP-related safety signals
- Dosage form and approved indication details for each Canadian DIN
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

