---
layout: default
title: Idelalisib
parent: Model Prediction Only (L5)
nav_order: 464
evidence_level: L5
indication_count: 10
---

# Idelalisib
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

# Idelalisib: From CLL / Follicular Lymphoma to Mantle Cell Lymphoma

## One-Sentence Summary

Idelalisib (Zydelig) is an oral PI3Kδ inhibitor, described in published reviews as approved for relapsed chronic lymphocytic leukemia (CLL), follicular lymphoma and small lymphocytic lymphoma (SLL).
The TxGNN model predicts it may be effective for **mantle cell lymphoma (MCL)**, with **9 clinical trials** and **20 publications** retrieved. Only one small Phase 1 study (40 patients) is MCL-specific, and the rest is indirect or preclinical.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CLL and relapsed follicular lymphoma/SLL (from published reviews; the Canadian license text is blank in the record) |
| Predicted New Indication | Mantle cell lymphoma |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 (borderline L2/L3, see below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in DrugBank for this record. Idelalisib is a selective inhibitor of PI3Kδ, an enzyme central to B-cell receptor signaling. PI3Kδ is expressed mainly in blood cells, so its inhibition reduces the survival and microenvironment homing of malignant B cells.

MCL is a B-cell lymphoma that depends on B-cell receptor and PI3K/AKT survival signaling. CLL and follicular lymphoma rely on the same pathway, and idelalisib's activity there gives the prediction a plausible basis. Preclinical papers show that idelalisib slows MCL cell growth and inhibits translation, and a Phase 1 study reported activity in heavily pretreated MCL patients.

Two cautions apply. MCL cells show intrinsic resistance to idelalisib in some studies. Recent work (P300/CBP inhibition, CBX5 loss) is still characterizing how that resistance arises and whether it can be overcome.

The evidence level of L2 is borderline. The strongest disease-directed trial (NCT01838434) is registered as Phase 1 with a randomized Phase 2 portion, and I could not confirm from the pack that it completed a Phase 2/3 RCT.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1 (with randomized Phase 2) | Completed | 106 | Lenalidomide with or without idelalisib in relapsed/refractory MCL. This is the strongest disease-directed dataset; MCL-specific enrollment should be confirmed. |
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Completed | 241 | Idelalisib combined with chemotherapy, immunomodulators or anti-CD20 antibody in indolent NHL, MCL or CLL. Likely includes MCL cohorts. |
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Terminated | 66 | Entospletinib plus idelalisib in relapsed/refractory hematologic malignancies, including MCL. Terminated early, so its MCL contribution is limited. |
| [NCT02457598](https://clinicaltrials.gov/study/NCT02457598) | Phase 1 | Terminated | 203 | Tirabrutinib combined with idelalisib and other targeted agents in B-cell malignancies. Informative for combination safety only. |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1 | Completed | 20 | BCL201 plus idelalisib in follicular lymphoma and MCL. MCL relevance is indirect. |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Terminated | 16 | Idelalisib maintenance after allogeneic transplant in B-cell malignancies. Not MCL-specific. |
| [NCT02824159](https://clinicaltrials.gov/study/NCT02824159) | N/A (observational) | Completed | 121 | Side effects versus plasma concentrations of ibrutinib and idelalisib. Gives PK and safety context but no efficacy data. |
| [NCT03740529](https://clinicaltrials.gov/study/NCT03740529) | Phase 1/2 | Completed | 803 | Pirtobrutinib in CLL/SLL and NHL. Idelalisib is not the investigational agent. |
| [NCT04985214](https://clinicaltrials.gov/study/NCT04985214) | N/A (observational) | Unknown | 464 | Quality of life with oral lymphoma therapies. No efficacy evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24615778](https://pubmed.ncbi.nlm.nih.gov/24615778/) | 2014 | Phase 1 trial | Blood | 48-week study in 40 relapsed/refractory MCL patients (50–350 mg daily or twice daily). Primary outcomes were safety and dose-limiting toxicity; response rate, PFS and duration of response were secondary. |
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | Commentary | Cancer Discovery | Reports that idelalisib was effective in heavily pretreated MCL (based on the Phase 1 data). |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Preclinical | Clin Cancer Res | Idelalisib inhibits cell growth in MCL by disrupting translation-regulatory mechanisms. |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Preclinical | Acta Pharmacol Sin | Idelalisib shows intrinsic resistance in MCL. The p300/CBP inhibitor A-485 overcame this in vitro and in vivo. |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Preclinical | Cancer Letters | Idelalisib enhances the antitumor effect of the CDK4/6 inhibitor palbociclib via PLK1 in B-cell lymphoma, including MCL. |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Preclinical | Phytomedicine | CBX5 loss drives PI3Kδ inhibitor resistance in MCL. Propolis restores sensitivity by inducing ferroptosis. |
| [28775119](https://pubmed.ncbi.nlm.nih.gov/28775119/) | 2017 | Review | Haematologica | Practical guide to the incidence and management of toxicity with ibrutinib and idelalisib. |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Review | Br J Haematol | Current regimens and novel agents for MCL. |
| [26360791](https://pubmed.ncbi.nlm.nih.gov/26360791/) | 2015 | Review | Expert Opin Pharmacother | Standard and novel treatment options for MCL. |
| [26841011](https://pubmed.ncbi.nlm.nih.gov/26841011/) | 2016 | Review | Cancer J | Idelalisib and the PI3K pathway in non-Hodgkin lymphoma. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2438801 | ZYDELIG |
| 2438798 | ZYDELIG |

Dosage form, manufacturer and approved indication text are not available in the supplied record.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kδ kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Not quantified in the pack (cytopenias are monitored in the Phase 1 post-transplant study). Please refer to the package insert warnings and precautions. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function tests, and symptom monitoring for diarrhea/colitis, pneumonitis and infection |
| Handling Protection | Follow institutional hazardous-drug handling rules for oral anticancer agents; confirm against the package insert |

---

## Safety Considerations

- **Key Warnings** (from the pack's mechanistic rationale, not a verified label): boxed-warning toxicities are hepatotoxicity, severe diarrhea/colitis, pneumonitis, serious infections and intestinal perforation. Published reviews also note that postmarketing safety signals led to termination of registry trials and to Gilead's voluntary withdrawal of the accelerated-approval indication in 2022 (PMID 36939665).
- **Drug Interactions**: The interaction query returned no results, which is probably a data gap. Idelalisib is a known CYP3A4 inhibitor, so interactions should be checked against the label.

The Health Canada package insert has not been reviewed, so please refer to it for the authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
MCL-specific clinical evidence is limited to one small Phase 1 study and a Phase 1/2 combination trial, with no confirmed efficacy from a completed Phase 2/3 RCT. Idelalisib also carries serious boxed-warning toxicities and has been displaced by BTK inhibitors in practice. Safety screening cannot proceed until the Health Canada package insert has been obtained.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Confirmed MCL cohort data and outcomes from NCT01838434 and NCT01088048
- DrugBank mechanism-of-action data and a proper drug-interaction check (CYP3A4)
- Comparison against current MCL standards of care, given the resistance signals

Among the other predictions, the B-cell neoplasm result (L1) reflects idelalisib's own established CLL/indolent-lymphoma use and is not a true repurposing signal. It is not considered further here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

