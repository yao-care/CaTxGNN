---
layout: default
title: Anagrelide
parent: Moderate Evidence (L3-L4)
nav_order: 58
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-13
description: "Anagrelide: predicted new indication Reactive thrombocytosis (evidence level L4). Approved use: Thrombocythemia"
monitor_inn: "ANAGRELIDE"
predicted_indications: ["reactive thrombocytosis", "inverse Klippel-Trenaunay syndrome"]
---

# Anagrelide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

## Anagrelide: From Thrombocythemia to Reactive Thrombocytosis
{: .text-alpha }

## One-Sentence Summary

Anagrelide is a platelet-lowering drug, originally used for thrombocythemia and familial thrombocytosis.
The TxGNN model predicts it may be effective for **reactive thrombocytosis**,
but there are currently **0 registered clinical trials** and **10 publications** (almost all reviews or case reports, none directly testing this use).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thrombocythemia; familial thrombocytosis |
| Predicted New Indication | Reactive thrombocytosis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general literature knowledge, anagrelide lowers platelet counts by inhibiting megakaryocyte maturation and differentiation. This is plausibly relevant to any condition with elevated platelets.

The original indications (thrombocythemia and familial thrombocytosis) and reactive thrombocytosis are all conditions with high platelet counts. This similarity probably explains the very high TxGNN score. However, the score should not be read as independent clinical support.

There is an important caveat. Reactive (secondary) thrombocytosis is driven by an underlying cause such as inflammation, iron deficiency, infection, malignancy or splenectomy. Management normally targets that cause, and platelet-lowering therapy is generally not indicated. The thrombotic risk is also lower than in clonal disorders such as essential thrombocythemia. The mechanistic fit is therefore weak in clinical terms.

A second predicted indication, inverse Klippel-Trenaunay syndrome (score 99.59%), has no supporting trials or publications. No mechanistic link to anagrelide is apparent, so it is not pursued here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review (mechanism) | Expert Rev Anticancer Ther | Update on anagrelide's mechanisms and use; notes reactive thrombocytosis needs no therapy, while clonal thrombocytosis may |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Review | Leuk Lymphoma | Critical review of anagrelide in essential thrombocythemia and related disorders; reactive thrombocytosis often inconsequential |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospective case series | Pediatr Blood Cancer | Compares essential vs reactive thrombocythemia in 12 children |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Med J Aust | Essential thrombocythaemia must be distinguished from reactive thrombocytosis; platelet-lowering therapy advised for platelets above 1000 x 10⁹/L |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | Am J Med Sci | Clinical spectrum of thrombocytosis and thrombocythemia |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Rinsho Ketsueki | Diagnosis and treatment of essential thrombocythemia, including anagrelide; differentiation from reactive thrombocytosis |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leuk Res | Thrombocytapheresis for hyperthrombocytosis in myeloproliferative neoplasms |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case report | Eur J Case Rep Intern Med | Acute myocardial infarction in a patient with essential thrombocythaemia treated with anagrelide |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case report | Srp Arh Celok Lek | Essential thrombocythemia with ankylosing spondylitis treated with anagrelide and other agents |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case report | Medicine | Digit replantation in a patient with post-splenectomy thrombocytosis |

None of these publications tests anagrelide in reactive thrombocytosis. Most concern essential thrombocythemia.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02274949 | PMS-ANAGRELIDE | Not specified | Not specified |

## Cytotoxicity

Anagrelide is not a conventional cytotoxic chemotherapy. It is used for clonal thrombocytosis in myeloproliferative disorders, and the data compiled for this report do not classify it as antineoplastic, so no cytotoxic handling classification is provided. Please refer to the package insert warnings and precautions.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure, liver disease, kidney disease, gallbladder disease, thrombocytopenia, blood coagulation disease, heart disease, cardiovascular disease, anemia, macrocytic anemia, interstitial lung disease, eosinophilic pneumonia, pulmonary eosinophilia, high output heart failure, pyoureter.
- **Drug Interactions**: 100 interactions were identified; the 20 listed in the data include these.
  - **Major**: cisapride, clarithromycin, dolasetron, granisetron, levofloxacin. These are largely drugs associated with QT prolongation.
  - **Moderate**: famotidine, cimetidine, alosetron, aprepitant, acetylsalicylic acid, bisacodyl, castor oil, dexfenfluramine, fenfluramine, glycerin, lactitol, lactulose, loperamide, magnesium citrate, magnesium hydroxide.
- A case report in the literature describes acute myocardial infarction during anagrelide treatment, which is consistent with the cardiovascular concerns above.

Health Canada package insert warnings and contraindications were not available. Please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model similarity to the approved indications. There are no clinical trials and no literature directly supporting anagrelide in reactive thrombocytosis. Clinically, treatment targets the underlying cause and platelet-lowering therapy is generally not indicated. Cardiovascular and other safety signals add further caution.

**To proceed, the following is needed:**
- Clear clinical rationale identifying a reactive thrombocytosis subgroup with high thrombotic risk and no treatable underlying cause
- Mechanism of action data (DrugBank)
- Health Canada package insert warnings, contraindications and approved indication text
- Cardiovascular and QT-related safety assessment, given the interactions and contraindication signals
- Any controlled or observational data on anagrelide in secondary thrombocytosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

