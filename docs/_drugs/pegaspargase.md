---
layout: default
title: Pegaspargase
parent: High Evidence (L1-L2)
nav_order: 712
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-13
description: "Pegaspargase: predicted new indication Precursor lymphoblastic lymphoma/leukemia (evidence level L1). Approved use: Acute lymphoblastic leukemia (including precursor T-cell ALL)"
monitor_inn: "PEGASPARGASE"
predicted_indications: ["chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "follicular lymphoma", "methylcobalamin deficiency type cblE", "lymphoid neoplasm", "Hodgkins lymphoma", "blast phase chronic myelogenous leukemia, BCR-ABL1 positive"]
---

# Pegaspargase
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

Pegaspargase is a long-acting form of the enzyme L-asparaginase, originally used to treat acute lymphoblastic leukemia (ALL).
The TxGNN model predicts it may be effective for **precursor lymphoblastic lymphoma/leukemia**, with **35 clinical trials** and **20 publications** compiled for this report.
This prediction is largely label-concordant: the predicted disease is essentially the same disease family as the original indication, so it is not true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia (including precursor T-cell ALL) |
| Predicted New Indication | Precursor lymphoblastic lymphoma/leukemia |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

Note: Health Canada's approved indication text was not available in the data compiled for this report, so the original indication above comes from the TxGNN knowledge graph.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available from DrugBank. From the analysis in the compiled data, pegaspargase is a PEGylated L-asparaginase that depletes circulating asparagine. Lymphoblasts have low asparagine synthetase activity and depend on asparagine from the blood, so depleting it selectively kills these cells.

The predicted disease (precursor B/T-cell lymphoblastic leukemia and lymphoblastic lymphoma) is the same disease family as the original ALL indication. Asparaginase-containing regimens are already a standard part of treatment, so the prediction is consistent with established use rather than a new direction.

Other predictions in the ranking are much weaker:
- **Acute lymphoblastic leukemia (rank 5):** also label-concordant, with strong evidence (L1).
- **Lymphoid neoplasm (rank 7):** mostly captures ALL and lymphoblastic lymphoma, plus NK/T-cell lymphoma. It is too heterogeneous for a single recommendation.
- **Hodgkin lymphoma (rank 8):** the linked trials are ALL studies and the literature is about extranodal NK/T-cell lymphoma (ENKTL), a different disease. Pegaspargase is well supported in ENKTL (P-GEMOX, SMILE-type, PEG-L-CHOP, MESA regimens, including phase 2 studies), but this does not transfer to Hodgkin lymphoma. The ontology mapping appears misleading; ENKTL is worth evaluating as a separate question.
- **CLL/SLL variants, follicular lymphoma, cblE deficiency (ranks 2, 3, 4, 6, 9):** prediction only, no trials or literature, no plausible asparagine-depletion rationale. Recommendation: Hold.
- **Blast phase CML (rank 10):** only indirect evidence from an adult ALL trial. Recommendation: Hold.

## Clinical Trial Evidence

Most relevant trials for the top prediction (the compiled data lists 35 in total):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00967057](https://clinicaltrials.gov/study/NCT00967057) | Phase 3 | Completed | 470 | ALLR3: international trial of re-induction chemotherapy in relapsed/refractory ALL |
| [NCT00103285](https://clinicaltrials.gov/study/NCT00103285) | Phase 3 | Completed | 5377 | COG trial of chemotherapy regimens in standard-risk B-precursor ALL |
| [NCT02003222](https://clinicaltrials.gov/study/NCT02003222) | Phase 3 | Active, not recruiting | 488 | Blinatumomab added to chemotherapy (including pegaspargase) in newly diagnosed BCR-ABL-negative B-ALL |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | Active, not recruiting | 440 | Levocarnitine to prevent asparaginase-associated liver toxicity in adolescents and young adults |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Phase 3 | Recruiting | 5000 | AIEOP-BFM ALL 2017 protocol for children and adolescents with ALL |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Phase 3 | Active, not recruiting | 6720 | Blinatumomab plus chemotherapy (including pegaspargase) in standard-risk B-ALL and localized B-lymphoblastic lymphoma |
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | Completed | 37 | MOAD regimen (methotrexate, vincristine, pegylated asparaginase, dexamethasone) in salvage ALL |
| [NCT00890656](https://clinicaltrials.gov/study/NCT00890656) | Phase 2 | Completed | 90 | Augmented hyper-CVAD in salvage ALL or lymphoblastic lymphoma |
| [NCT01005914](https://clinicaltrials.gov/study/NCT01005914) | Phase 2 | Terminated | 11 | Adding PEG-asparaginase to hyper-CVAD in newly diagnosed adult ALL |
| [NCT01403415](https://clinicaltrials.gov/study/NCT01403415) | Phase 1 | Completed | 13 | Temsirolimus with intensive re-induction (including pegaspargase) in relapsed ALL and non-Hodgkin lymphoma; mainly safety |

Most trials test pegaspargase as part of a multi-drug backbone, so they support the regimen rather than isolating the effect of pegaspargase alone.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | COG AALL1231: bortezomib in newly diagnosed T-ALL and T-lymphoblastic lymphoma |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | COG AALL0434: nelarabine in newly diagnosed T-ALL |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | AALL0232: dexamethasone and high-dose methotrexate improved outcome in high-risk B-ALL |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort | Blood Adv | GIMEMA LAL1913: pegaspargase-modified, risk-oriented program in adult ALL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | Expert consensus on preventing and managing asparaginase/pegaspargase adverse events in adults |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | Pegaspargase in ALL: longer circulation time and less frequent dosing than native asparaginase |
| [40858769](https://pubmed.ncbi.nlm.nih.gov/40858769/) | 2025 | Cohort | Ann Hematol | Pegaspargase tolerability in patients aged 55 or older treated with the LAL1913 program |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Other | J Clin Oncol | DFCI 11-001: efficacy and toxicity of pegaspargase vs calaspargase pegol in childhood ALL |
| [27643446](https://pubmed.ncbi.nlm.nih.gov/27643446/) | 2017 | Review | Leuk Lymphoma | Hypersensitivity reactions with IV infusion vs IM injection of pegaspargase |
| [42085640](https://pubmed.ncbi.nlm.nih.gov/42085640/) | 2026 | Other | Blood Adv | COG report on asparaginase toxicity during ALL induction (4925 patients aged 1–30) |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02461900 | ONCASPAR | Not available | Not available |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Enzyme-based antineoplastic (asparagine depletion), used within multi-agent cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function, pancreatic enzymes, triglycerides, glucose, and coagulation parameters, based on the toxicities reported in the literature |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Known toxicities reported in the literature:** hypersensitivity reactions, pancreatitis, thrombosis, hepatotoxicity, hypertriglyceridemia, and hyperglycemia. Tolerability appears lower in adults aged 40–55 and older, and obesity has been linked to more toxicity.
- **Drug interactions:** 100 interactions were found; those listed are all moderate-level. Examples include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), antidiabetic agents (metformin, acarbose, alogliptin, canagliflozin, dapagliflozin, dulaglutide, saxagliptin), antibiotics (doxycycline, tetracycline, clarithromycin), aspirin, and bupropion. The glucose-related interactions are consistent with the hyperglycemia reported with pegaspargase.

Package insert warnings and contraindications were not available, so please refer to the Health Canada package insert for the full safety profile.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials and a large body of literature support asparaginase-containing regimens in lymphoblastic leukemia and lymphoma. The prediction matches the drug's established use, so efficacy is not the main question; managing known toxicities is.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking data gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Health Canada approved indication text, dosage form, and manufacturer for DIN 02461900
- A toxicity monitoring and management plan, especially for adults aged 40 or older, patients with obesity, and patients with prior hypersensitivity
- Separate evaluation of extranodal NK/T-cell lymphoma, rather than the Hodgkin lymphoma prediction, if pursuing lymphoma expansion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

