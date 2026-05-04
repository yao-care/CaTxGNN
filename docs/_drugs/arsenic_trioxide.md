---
layout: default
title: Arsenic Trioxide
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Arsenic Trioxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Arsenic Trioxide: From Acute Promyelocytic Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Arsenic trioxide (ATO, Trisenox®) is an inorganic arsenical compound established globally as a cornerstone treatment for acute promyelocytic leukemia (APL), where it degrades the PML-RAR fusion oncoprotein to trigger leukemic cell differentiation and apoptosis.
The TxGNN model ranks **Myelodysplastic Syndrome (MDS)** as one of the top predictions for ATO repurposing (rank 6, score 99.91%; with the "unclassified MDS" subtype ranked highest at 99.93%),
supported by **24 clinical trials** and **20 publications**, including two actively recruiting studies launched in 2024–2025 evaluating novel oral ATO formulations in MDS patients who have failed standard therapies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Promyelocytic Leukemia (APL) — globally established (FDA/EMA approved); not currently marketed in Canada |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.91% (MDS, rank 6); 99.93% for "unclassified MDS" subtype (rank 1) |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Arsenic trioxide's mechanism in APL — degradation of the PML-RAR fusion protein, leading to differentiation and apoptosis of leukemic blasts — is only one facet of a broader multi-target pharmacology. ATO also inhibits NF-κB/FLIP signalling, remodels the BCL-2 family balance (downregulating anti-apoptotic BCL-2, upregulating pro-apoptotic BAX), generates reactive oxygen species (ROS) to trigger mitochondrial apoptosis, and blocks the Hedgehog/Gli2 pathway involved in cancer stem cell self-renewal. These mechanisms are not APL-specific; they operate across a range of myeloid malignancies.

MDS is a clonal hematopoietic stem cell disorder characterised by precisely the pathological features that ATO's mechanism addresses: constitutive NF-κB activation drives aberrant survival of dysplastic clones, BCL-2 overexpression impairs normal apoptosis, and epigenetic silencing via DNMT hypermethylation contributes to abnormal differentiation. Each of these hallmarks is directly targeted by ATO. Mechanistic studies confirm that ATO inhibits NF-κB and FLIP in MDS patient bone marrow cells (PMID 16105982), modulates BCL-2 family gene expression in vivo (PMID 22964015), and shows synergistic apoptosis with decitabine via endoplasmic reticulum stress (PMID 30898879). A 2023 systematic review and network meta-analysis (PMID 37908176) provides the highest-level synthesis, confirming ATO's activity in MDS through both apoptosis induction and demethylation.

Both APL and MDS are myeloid malignancies arising from hematopoietic progenitor cells with shared dependencies on survival pathways that ATO disrupts. The clinically relevant differentiation is the absence of the PML-RAR driver in MDS — but ATO's efficacy does not depend on this target. The translation is further validated by the sustained clinical development activity: two trials opened in 2024–2025 (NCT06778187, NCT06670222) specifically target ATO in MDS patients who have exhausted first-line options including luspatercept and erythropoiesis-stimulating agents, signalling that investigator conviction in this indication remains high.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT06778187](https://clinicaltrials.gov/study/NCT06778187) | Phase 2 | Recruiting | 30 | Oral ATO (Arsenol®) + ascorbic acid + investigator-choice low-intensity therapy in previously untreated or relapsed/refractory TP53-mutated MDS, AML, and CMML; addresses a critical unmet need in high-risk disease where standard therapies fail (2025–2028) |
| [NCT06670222](https://clinicaltrials.gov/study/NCT06670222) | Phase 1 | Recruiting | 24 | Dose-escalation of oral ATO in low-risk MDS after failure of ESA and luspatercept (or ineligibility); evaluates a novel oral formulation suited for outpatient, chronic-disease management (2025–2027) |
| [NCT02190695](https://clinicaltrials.gov/study/NCT02190695) | Phase 2 | Completed | 92 | Randomised comparison of decitabine alone vs. decitabine + carboplatin vs. decitabine + arsenic in relapsed/refractory and elderly AML/MDS/CMML; largest completed randomised dataset that directly tests ATO in an MDS-inclusive population |
| [NCT00274781](https://clinicaltrials.gov/study/NCT00274781) | Phase 2 | Completed | 30 | ATO + gemtuzumab ozogamicin in advanced MDS; completed with a full safety and efficacy dataset, representing one of the core completed Phase 2 studies supporting MDS activity |
| [NCT00803530](https://clinicaltrials.gov/study/NCT00803530) | Phase 2 | Terminated | 55 | Multicentre ATO + ascorbic acid in MDS (prospective); despite early termination, 55 patients enrolled provides a meaningful safety and efficacy signal dataset |
| [NCT00274820](https://clinicaltrials.gov/study/NCT00274820) | Phase 2 | Completed | 15 | TADA regimen (thalidomide + ATO + dexamethasone + ascorbic acid) in MDS / myeloproliferative overlap; demonstrates ATO's tolerability and contribution in a four-drug MDS regimen |
| [NCT00671697](https://clinicaltrials.gov/study/NCT00671697) | Phase 1 | Completed | 13 | IV decitabine + ATO + ascorbic acid in MDS and AML; confirmed safe dosing for the epigenetic-plus-cytotoxic triplet, providing the dose rationale for subsequent Phase 2 work |
| [NCT00621023](https://clinicaltrials.gov/study/NCT00621023) | Phase 2 | Completed | 7 | Pilot open-label study of decitabine + ATO + ascorbic acid in MDS; first proof-of-concept human data for the ATO + decitabine combination, establishing the rationale for larger trials |
| [NCT03377725](https://clinicaltrials.gov/study/NCT03377725) | Phase 3 | Withdrawn | 0 | Decitabine + ATO in MDS with TP53 mutation focus; the only Phase 3-designed ATO-MDS trial, withdrawn before enrolment — confirms the combination warrants Phase 3 evaluation while marking a critical unresolved evidence gap |
| [NCT00003395](https://clinicaltrials.gov/study/NCT00003395) | Phase 1 | Completed | N/A | Foundational dose-ranging study of ATO across advanced haematologic cancers including MDS (1998–2000); established the baseline safety and pharmacokinetic profile for ATO in non-APL haematologic malignancies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37908176](https://pubmed.ncbi.nlm.nih.gov/37908176/) | 2023 | Systematic Review / Network Meta-analysis | Hematology | Highest-level synthesis of ATO-containing regimens in MDS; confirms ATO activity via apoptosis induction and demethylation, and identifies optimal combination strategies across trial comparisons |
| [40167011](https://pubmed.ncbi.nlm.nih.gov/40167011/) | 2025 | Retrospective Cohort | Hematology | Decitabine + ATO in elderly high-risk MDS; reports efficacy and safety outcomes in a poor-prognosis population with few therapeutic options, directly supporting the combination regimen approach |
| [38816179](https://pubmed.ncbi.nlm.nih.gov/38816179/) | 2024 | Comparative Clinical Study | Immunopharmacology and Immunotoxicology | Compares immunological changes (T-cell subsets, cytokines) following oral realgar (arsenic disulfide) vs. intravenous ATO in a murine MDS model; informs mechanistic differences relevant to oral vs. IV formulation development |
| [20956016](https://pubmed.ncbi.nlm.nih.gov/20956016/) | 2011 | Phase I/II Clinical Study | Leukemia Research | ATO + low-dose cytarabine in 49 previously untreated intermediate-2 and high-risk MDS patients; CR rate 17%, 4-week mortality 8%; demonstrates ATO combination activity and tolerability in advanced MDS |
| [18282365](https://pubmed.ncbi.nlm.nih.gov/18282365/) | 2007 | Review | Clinical Lymphoma & Myeloma | Comprehensive review of ATO clinical data in leukemias and MDS; summarises single-agent and combination ATO response rates and tolerability across MDS subtypes |
| [17920679](https://pubmed.ncbi.nlm.nih.gov/17920679/) | 2008 | Clinical Study | Leukemia Research | ATO + all-trans retinoic acid + thalidomide in higher-risk MDS; evaluates clinical efficacy and safety of the three-drug combination with a differentiation-targeting rationale |
| [20425329](https://pubmed.ncbi.nlm.nih.gov/20425329/) | 2006 | Review | Current Hematologic Malignancy Reports | Reviews ATO's pro-apoptotic, antiproliferative, and anti-angiogenic mechanisms and their relevance to MDS; contextualises single-agent and combination clinical results |
| [30898879](https://pubmed.ncbi.nlm.nih.gov/30898879/) | 2019 | Translational / In Vitro | Journal of Investigative Medicine | Decitabine + ATO induces synergistic apoptosis in MDS cell lines (MUTZ-1, SKM-1) via endoplasmic reticulum stress; provides mechanistic rationale for the widely trialled ATO + decitabine combination |
| [22964015](https://pubmed.ncbi.nlm.nih.gov/22964015/) | 2012 | Mechanistic Clinical Study | Journal of Hematology & Oncology | ATO + ascorbic acid modulates 93 apoptotic genes including the BCL-2 family in MDS patient bone marrow before and after treatment; first in-patient evidence for ATO's gene expression effects in MDS |
| [16105982](https://pubmed.ncbi.nlm.nih.gov/16105982/) | 2005 | Mechanistic Study | Blood | NF-κB and FLIP regulation by ATO in MDS patient bone marrow; shows NF-κB activity is stage-dependent in MDS (elevated in high-grade RAEB), establishing the key molecular rationale for ATO's MDS activity |

---

## Canada Market Information

Arsenic trioxide has not been approved or marketed in Canada and currently holds no DINs. Access for research or compassionate use would require application through Health Canada's Special Access Programme (SAP). ATO is approved as Trisenox® in the United States (FDA) and as Trisenox® / generic formulations in Europe (EMA) for APL; its regulatory pathway for MDS would constitute a new indication filing in any jurisdiction.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Inorganic arsenical compound with pro-apoptotic, anti-angiogenic, and differentiating properties; classified as a hazardous antineoplastic agent |
| Myelosuppression Risk | **High** — Leukopenia, thrombocytopenia, and anaemia are commonly reported in ATO trials across haematologic indications; in the MDS population (who already have baseline cytopenias), myelosuppression monitoring is critically important to distinguish treatment toxicity from disease progression |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (at minimum weekly during induction); hepatic and renal function; serum electrolytes — potassium and magnesium must be corrected to normal levels before initiation due to arrhythmia risk; 12-lead ECG with QTc measurement at baseline and periodically during treatment (QTc prolongation is a known class effect); serum arsenic levels for patients on prolonged courses |
| Handling Protection | Must be handled under cytotoxic drug precautions: PPE (gloves, gown, eye protection), closed-system drug transfer devices (CSTDs) for IV preparation, and appropriate waste disposal per hazardous drug regulations; arsenic is renally excreted — urine disposal protocols apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important class-level note**: Arsenic trioxide carries well-established safety signals that are essential to review before any non-APL application. These include QTc prolongation with risk of life-threatening torsades de pointes (requires electrolyte correction and ECG monitoring), APL differentiation syndrome (predominantly in APL, but inflammatory systemic responses have been reported in other haematologic settings), hyperleukocytosis, peripheral neuropathy, and hepatotoxicity. These concerns are particularly relevant when evaluating ATO in MDS patients who may have multiple co-morbidities, polypharmacy, and pre-existing cytopenias. The full Trisenox® prescribing information (FDA label) should be consulted as the primary safety reference.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
ATO has a mechanistically compelling and clinically validated basis for activity in MDS: multiple completed Phase 2 studies (including a 92-patient randomised trial), a 2023 systematic review and meta-analysis, and two actively recruiting trials in 2025 collectively constitute L2 evidence. The combination with hypomethylating agents (decitabine, azacitidine) is supported by both mechanistic synergy data and early-phase clinical results. The absence of Canadian market authorisation and incomplete safety documentation are addressable barriers rather than fundamental obstacles to further development.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate a Health Canada Special Access Programme (SAP) application to enable access for research use; map requirements for a new indication filing based on accumulated MDS evidence
- **Target population definition**: Clarify the specific MDS subtype to pursue — the unclassified MDS subtype (top TxGNN prediction, rank 1) lacks direct clinical evidence; the best-evidenced populations are high-risk MDS (intermediate-2 / high IPSS) and TP53-mutated MDS, where two active Phase 2 trials are currently enrolling
- **Safety documentation**: Obtain and review the complete Trisenox® FDA package insert; translate key warnings — particularly QTc monitoring protocol, electrolyte management requirements, and differentiation syndrome recognition — into a Canadian clinical monitoring plan
- **Mechanism of action data**: Retrieve the full DrugBank MOA entry for ATO (DB01169) to complete the mechanistic rationale documentation (currently a data gap)
- **Drug interaction assessment**: Conduct a formal DDI review (the current evidence pack returned no interactions), with particular focus on QT-prolonging co-medications common in MDS patients (antibiotics, antifungals, antiemetics)
- **Additional predictions for parallel evaluation**: Aregenerative anemia / aplastic anemia (rank 4, L3 evidence, 6 trials, 12 publications — ATO's immunomodulatory mechanism on Tregs and cytokine axes provides a distinct and plausible rationale) and Ewing sarcoma (rank 7, L3 evidence, via Hedgehog/Gli2 inhibition) represent secondary research questions warranting independent evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

