---
layout: default
title: Anagrelide
parent: Moderate Evidence (L3-L4)
nav_order: 58
evidence_level: L4
indication_count: 2
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Anagrelide: From Essential Thrombocythemia to Reactive Thrombocytosis

## One-Sentence Summary

Anagrelide is a platelet-lowering drug used for clonal thrombocytosis such as essential thrombocythemia. The Canadian license record does not state an indication, so this is taken from the literature.
The TxGNN model predicts it may be effective for **reactive thrombocytosis**, but there are **0 clinical trials** and only **10 publications**, none of which show benefit in this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license record. The literature describes use in essential thrombocythemia (clonal thrombocytosis). |
| Predicted New Indication | Reactive thrombocytosis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied record. From general knowledge, anagrelide lowers platelet counts mainly by inhibiting megakaryocyte maturation, and to a lesser extent through PDE3 inhibition. A platelet-lowering effect is therefore plausible whatever the cause of the high platelet count.

The retrieved literature almost entirely concerns essential thrombocythemia, a clonal myeloproliferative neoplasm. It does not show that anagrelide helps in reactive (secondary) thrombocytosis. Reactive thrombocytosis is usually managed by treating the underlying cause. Its thrombotic risk is low, so cytoreductive therapy is rarely needed. The reviews say this directly: reactive thrombocytosis "does not require any therapeutic intervention," while clonal disease may.

The high TxGNN score (0.998) most likely reflects the disease's closeness to essential thrombocythemia in the knowledge graph, not independent evidence. Anagrelide also carries cardiovascular risk, illustrated by a 2024 myocardial infarction case report. That weakens the risk-benefit case in a low-thrombotic-risk population.

The second-ranked prediction, inverse Klippel-Trenaunay syndrome (score 99.59%, L5), has no trials or literature. No mechanistic link to anagrelide could be established, and it is likely a graph-connectivity artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No RCTs were retrieved. Reviews are listed first, then the cohort study and case reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review | Expert Rev Anticancer Ther | Drug profile of anagrelide (mechanisms and therapeutic potential). Notes reactive thrombocytosis needs no treatment, while clonal thrombocytosis may. |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Review | Leuk Lymphoma | Critical review of anagrelide in essential thrombocythemia and related disorders. Hydroxyurea has RCT evidence of reducing thrombosis in high-risk patients. |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Med J Aust | Essential thrombocythemia diagnosis requires excluding other myeloproliferative disorders and reactive thrombocytosis. Platelet counts above 1000 × 10⁹/L warrant platelet-lowering therapy. |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leuk Res | Case-based review of thrombocytapheresis for urgent platelet reduction in myeloproliferative neoplasms. Medical cytoreduction remains the mainstay. |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | Am J Med Sci | Clinical spectrum of thrombocytosis and thrombocythemia, including cytokine regulation of platelet production. |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Rinsho Ketsueki | Diagnosis and treatment of essential thrombocythemia. Differentiates it from reactive thrombocytosis; agents include busulfan, hydroxyurea, interferon-alpha and anagrelide. |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Cohort | Pediatr Blood Cancer | Retrospective analysis of 12 children comparing essential and reactive thrombocythemia. |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case report | Eur J Case Rep Intern Med | Acute myocardial infarction in a patient with essential thrombocythemia treated with anagrelide. |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case report | Srp Arh Celok Lek | Essential thrombocythemia with ankylosing spondylitis treated with anagrelide, DMARDs and etanercept. |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case report | Medicine (Baltimore) | Digit replantation in a patient with thrombocytosis after splenectomy. It does not involve anagrelide. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2274949 | PMS-ANAGRELIDE | Not listed | Not listed |

## Safety Considerations

- **Cardiovascular risk**: A 2024 case report describes acute myocardial infarction in a patient with essential thrombocythemia taking anagrelide.
- **Drug interactions**: No interactions were found in the queried data.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. No trials exist, and the literature covers clonal essential thrombocythemia, not reactive thrombocytosis, where cytoreduction is rarely indicated. Anagrelide's cardiovascular risk further weakens the benefit-risk case.

**To proceed, the following is needed:**
- Health Canada product monograph warnings, contraindications and approved indication text
- Detailed mechanism of action data from DrugBank
- Any direct clinical evidence of anagrelide benefit in reactive thrombocytosis, and a defined patient subgroup with a clear need for platelet reduction
- A cardiovascular risk assessment for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

