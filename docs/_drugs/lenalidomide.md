---
layout: default
title: Lenalidomide
parent: High Evidence (L1-L2)
nav_order: 535
evidence_level: L2
indication_count: 4
last_modified_at: 2026-10-13
monitor_inn: "LENALIDOMIDE"
predicted_indications: ["myeloid leukemia", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts"]
description: "Lenalidomide: predicted new indication Myeloid leukemia (evidence level L2). Approved use: Not recorded in the local data"
---

# Lenalidomide
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **4** 
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

## Lenalidomide: Myeloid leukemia
{: .text-alpha }

## One-Sentence Summary

Lenalidomide is an oral immunomodulatory drug originally used for plasma cell myeloma, mantle cell lymphoma and myelodysplastic syndrome (MDS).
The TxGNN model predicts it may be effective for **myeloid leukemia**,
with **48 clinical trials** and **20 publications** currently supporting this direction. Most trials are early-phase (Phase 1/2), and no completed Phase 3 trial is available for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L2 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails (as a research question) |

---

## Why is This Prediction Reasonable?

Lenalidomide is a cereblon E3 ligase modulator. It binds cereblon and promotes degradation of the transcription factors IKZF1 and IKZF3, as well as CK1α. It also activates NK and T cells. The CK1α mechanism is well established in MDS with del(5q), a disease closely related to acute myeloid leukemia (AML). A 2025 laboratory study also showed that cereblon levels influence how sensitive AML cells are to lenalidomide.

Lenalidomide is already used in MDS and plasma cell myeloma. MDS is a myeloid neoplasm that often progresses to AML, so the biology is shared. Early trials in AML and high-risk MDS include relapsed/refractory disease, post-remission maintenance, and combinations with azacitidine or standard chemotherapy.

Detailed mechanism-of-action data were not available in the data compiled for this report, so the above reflects established pharmacology. The link is plausible, but clinical proof in AML is still limited.

---

## Clinical Trial Evidence

48 trials were identified. The table lists the 10 most relevant, prioritising trials with a relevance grade of A or B, then larger completed Phase 2/3 studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Phase 1/2 | Completed | 37 | Lenalidomide plus azacitidine in advanced MDS/myeloid malignancies |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | Completed | 29 | Lenalidomide maintenance in high-risk AML in remission |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | Completed | 27 | Single-agent lenalidomide in relapsed/refractory AML or high-risk MDS with chromosome 5 abnormalities |
| [NCT00831766](https://clinicaltrials.gov/study/NCT00831766) | Phase 1/2 | Completed | 51 | Idarubicin and cytarabine followed by lenalidomide in MDS (RAEB-2) or untreated AML |
| [NCT01681537](https://clinicaltrials.gov/study/NCT01681537) | Phase 1 | Completed | 36 | Lenalidomide plus mitoxantrone, etoposide, cytarabine (MEC) for AML reinduction; dose-finding and safety |
| [NCT01578954](https://clinicaltrials.gov/study/NCT01578954) | Phase 1 | Completed | 20 | Dose-finding of lenalidomide as consolidation and maintenance in AML patients 60 or older |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Phase 2 | Completed | 120 | Alternating lenalidomide and azacitidine maintenance after induction in elderly AML |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | Completed | 88 | Randomised comparison of lenalidomide, sequential azacitidine plus lenalidomide, and azacitidine alone in older newly diagnosed AML |
| [NCT01038635](https://clinicaltrials.gov/study/NCT01038635) | Phase 1/2 | Completed | 94 | Azacitidine plus lenalidomide in high-risk MDS and AML |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Phase 3 | Unknown | 60 | Azacitidine plus lenalidomide maintenance guided by MRD monitoring in elderly or unfit AML; status unverified |

Note: the only Phase 3 trials found are NCT04490707 (status unknown, 60 patients) and NCT00843882 (MDS with anemia, still active). Neither is a completed Phase 3 RCT in AML.

---

## Literature Evidence

Most of the retrieved papers are MDS reviews rather than AML-specific trials.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | Lenalidomide as a novel AML treatment; approved for del(5q) MDS and myeloma, with trials in higher-risk MDS and AML |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | Laboratory study | Cell Mol Biol Lett | KDM5C stabilises cereblon and increases AML cell sensitivity to lenalidomide |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | Am J Hematol | MDS diagnosis, risk stratification and management update |
| [42400116](https://pubmed.ncbi.nlm.nih.gov/42400116/) | 2026 | Review | Am J Hematol | 2026 update on MDS diagnosis and management |
| [41348013](https://pubmed.ncbi.nlm.nih.gov/41348013/) | 2025 | Review | Hematology ASH Educ Program | Updates in low- and intermediate-risk MDS |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | Clinical decision-making in MDS |
| [29795386](https://pubmed.ncbi.nlm.nih.gov/29795386/) | 2018 | Review | Blood Cancer J | Current MDS treatment algorithm |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | Myelodysplastic syndromes overview; progression to AML in about a third of patients |
| [22483153](https://pubmed.ncbi.nlm.nih.gov/22483153/) | 2012 | Review | Curr Cancer Drug Targets | Novel and emerging drugs for AML |
| [17488990](https://pubmed.ncbi.nlm.nih.gov/17488990/) | 2007 | Review | J Clin Oncol | AML and MDS in older patients |

---

## Canada Market Information

20 licences are valid, all single-ingredient products. Dosage form, manufacturer and approved-indication text were not available for these licences. The table lists 5 of them.

| DIN | Product Name |
|---------|------|
| 02304899 | REVLIMID |
| 02304902 | REVLIMID |
| 02459418 | REVLIMID |
| 02507900 | TARO-LENALIDOMIDE |
| 02518597 | SANDOZ LENALIDOMIDE |

Other products include generics from Reddy, Apotex (APO), Nat, and JAMP.

---

## Cytotoxicity

Lenalidomide is an immunomodulatory antineoplastic agent, not a conventional cytotoxic. It is used for haematological malignancies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunomodulatory / targeted (cereblon E3 ligase modulator) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, renal function |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Contraindications / risk conditions (from the knowledge graph, not label text):** thrombocytopenia, neutropenia, agranulocytosis, pulmonary embolism, impaired renal function, cancer, embryoma. The knowledge graph also flags embryo-related risk, consistent with lenalidomide's thalidomide-derived pregnancy risk, so confirm this against the label.

**Drug Interactions:** 100 interactions were found. Major-level interactions include:
- Rosuvastatin (Major)
- Simvastatin (Major)

Moderate-level interactions include eliglustat and naltrexone. The remaining interactions listed have no severity classification.

Package-insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The mechanism is well characterised (cereblon-mediated degradation) and early-phase evidence in AML is substantial, with many completed Phase 1/2 and Phase 2 trials. However, there is no completed Phase 3 RCT and the retrieved literature is mostly MDS reviews. Lenalidomide is already marketed in Canada, so access is not a barrier.

**To proceed, the following is needed:**
- Phase 3 or randomised evidence in AML, and published results from the completed Phase 2 trials
- Package insert warnings and contraindications from Health Canada
- Detailed mechanism-of-action data
- A haematological monitoring and risk-management plan, given the myelosuppression and thromboembolism signals
- Biomarker-defined populations (for example del(5q)) to identify patients most likely to benefit

**Other predicted indications (briefly):**
- Unclassified MDS (L3): benefit is likely limited to del(5q) subsets. Evidence is a Czech cohort experience and case reports.
- Partial deletion of chromosome 5q (L4): the biological basis of the approved MDS use, but it is a biomarker rather than a distinct disease. Best treated as a defined subgroup of MDS and related myeloid neoplasms.
- Aregenerative anemia (L3): indirect evidence only; the retrieved literature is mostly myeloma and lymphoma.
- Refractory cytopenia of childhood (L3, Hold): only a pediatric Phase 1 study in solid tumors/MDS, which offers dosing and safety data but no efficacy data.
- Severe congenital hypochromic anemia with ringed sideroblasts (L5, Hold): no trials or literature and no established mechanistic link.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

