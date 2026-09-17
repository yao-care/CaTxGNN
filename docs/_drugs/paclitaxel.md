---
layout: default
title: Paclitaxel
parent: High Evidence (L1-L2)
nav_order: 590
evidence_level: L1
indication_count: 10
---

# Paclitaxel
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Paclitaxel: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane chemotherapy agent, historically first approved for refractory ovarian cancer. The TxGNN model's top-ranked prediction for this drug is **Female Breast Carcinoma**, supported by roughly **90 clinical trials** and **20 publications** — however, paclitaxel is already a globally established standard-of-care agent for breast cancer, so this result largely confirms known pharmacology rather than revealing a genuinely novel use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (paclitaxel's first historical approval; no Canada-specific original indication text is present in this evidence pack — data gap) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.995% (rank 184 of all drug-disease pairs scored) |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed (per this evidence pack) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available as a structured field in this evidence pack (flagged as a High-severity data gap, DG002). However, the evidence pack's own repurposing rationale describes paclitaxel's established mechanism: it stabilizes microtubules and blocks mitotic spindle disassembly, inducing M-phase cell-cycle arrest and apoptosis. This is a well-characterized, textbook cytotoxic mechanism rather than a speculative inference.

Breast cancer cells — particularly hormone-receptor-negative and rapidly proliferating subtypes — are highly sensitive to microtubule-targeting agents, which is exactly why taxanes are already a backbone of both neoadjuvant and metastatic breast cancer regimens worldwide. The mechanistic link here is direct and clinically routine, not exploratory.

**Important caveat:** because paclitaxel is already an approved, guideline-recommended treatment for breast cancer in most jurisdictions, this "predicted new indication" should be read as the model correctly recovering a known drug-disease relationship (a positive validation signal for the TxGNN methodology) rather than as a novel repurposing opportunity. The practical question for this jurisdiction is less "does it work" and more "is it licensed and labeled here" — see Canada Market Information below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005581](https://clinicaltrials.gov/study/NCT00005581) | Phase 3 | Unknown | 1000 | Epirubicin + paclitaxel vs. CEF as adjuvant therapy in node-positive breast cancer; large randomized comparison directly involving paclitaxel |
| [NCT01426880](https://clinicaltrials.gov/study/NCT01426880) | Phase 2/3 | Completed | 595 | Addition of carboplatin to neoadjuvant anthracycline/taxane + trastuzumab in triple-negative and HER2+ early breast cancer |
| [NCT00005649](https://clinicaltrials.gov/study/NCT00005649) | Phase 2 | Completed | N/A | Capecitabine + standard paclitaxel as first/second-line therapy in metastatic breast carcinoma |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: compares two dose-dense/dose-intensified neoadjuvant strategies, one paclitaxel/liposomal-doxorubicin based, in high-risk early breast cancer |
| [NCT05296798](https://clinicaltrials.gov/study/NCT05296798) | Phase 3 | Active, not recruiting | 922 | Giredestrant + Phesgo vs. Phesgo after taxane induction in HER2+/ER+ advanced breast cancer |
| [NCT01848197](https://clinicaltrials.gov/study/NCT01848197) | N/A (RCT) | Unknown | 1000 | Paclitaxel every 2 weeks vs. weekly as adjuvant treatment of breast cancer |
| [NCT00003440](https://clinicaltrials.gov/study/NCT00003440) | Phase 3 | Completed | 580 | Weekly 1-hour vs. standard 3-hour paclitaxel infusion ± trastuzumab in HER2 metastatic breast cancer |
| [NCT03799679](https://clinicaltrials.gov/study/NCT03799679) | Phase 4 | Unknown | 60 | Nab-paclitaxel followed by dose-intensive epirubicin + cyclophosphamide as neoadjuvant therapy in triple-negative breast cancer |
| [NCT05092373](https://clinicaltrials.gov/study/NCT05092373) | Phase 1 | Recruiting | 43 | Tumor treating fields + nab-paclitaxel/atezolizumab in advanced solid tumors involving abdomen/thorax |
| [NCT00019019](https://clinicaltrials.gov/study/NCT00019019) | Phase 1 | Completed | 70 | CAI + paclitaxel in refractory cancers or lymphoma |

*(Full underlying evidence pack lists ~90 trials tagged to this indication; the above 10 were prioritized by phase, completion status, and enrollment size.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Comprehensive review of paclitaxel's mechanistic and clinical effects in breast cancer, including resistance mechanisms |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early review establishing paclitaxel's extension from ovarian cancer into metastatic breast carcinoma treatment |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Cohort | Cancer | Phase II multicenter trial of doxorubicin + paclitaxel in advanced breast carcinoma, noting impact of prior anthracycline exposure |
| [9164198](https://pubmed.ncbi.nlm.nih.gov/9164198/) | 1997 | Phase 2 clinical | J Clin Oncol | ECOG Phase II trial of biweekly paclitaxel + cisplatin in advanced breast carcinoma |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Preclinical/translational | Chemical Biology & Drug Design | Patient-derived xenograft study of paclitaxel combination therapy in breast carcinoma with biomarker identification |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Real-world study | BioMed Research International | Real-world efficacy of epirubicin/cyclophosphamide + weekly paclitaxel + trastuzumab in HER2+ breast carcinoma |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Mechanistic | J Immunother Cancer | Paclitaxel's role in modulating tumor-associated macrophages to enhance PD-1 blockade in triple-negative breast cancer |
| [14508823](https://pubmed.ncbi.nlm.nih.gov/14508823/) | 2003 | Mechanistic | Cancer | Combined trastuzumab + paclitaxel more effectively inhibits ErbB-2-mediated angiogenesis than either agent alone |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Cohort | Cancer | Paclitaxel's role in multimodality treatment of inflammatory breast carcinoma |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Genomic study | Nature Communications | TEKT4 germline variation enrichment associated with breast cancer resistance to paclitaxel |

---

## Canada Market Information

No Health Canada licenses are on file for this drug in the current evidence pack (market status: **Not Marketed**, 0 DINs recorded). This does not necessarily mean paclitaxel is unavailable in Canada in practice — it indicates that this specific dataset did not capture an active license record, which itself is a data gap that should be verified directly against Health Canada's Drug Product Database before any regulatory decision is finalized.

---

## Cytotoxicity

Paclitaxel is a conventional cytotoxic chemotherapy agent (taxane class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule-stabilizing agent) |
| Myelosuppression Risk | High — neutropenia is a well-documented, dose-limiting toxicity of paclitaxel; jurisdiction-specific label details are pending (see DG001 below) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function, peripheral neuropathy assessment, infusion-related hypersensitivity monitoring |
| Handling Protection | Yes — requires handling under standard cytotoxic/hazardous drug precautions |

Note: this classification reflects paclitaxel's well-established general pharmacology. The evidence pack itself contains no structured toxicity or label data (see Safety Considerations), so jurisdiction-specific warnings should still be confirmed against the official product monograph.

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack does not contain structured warnings, contraindications, or drug-interaction data for paclitaxel — retrieval of the official Canadian product monograph is flagged as a **Blocking** data gap (DG001) that must be resolved before any formal safety screening can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical and mechanistic evidence for paclitaxel in breast cancer is exceptionally strong (multiple completed Phase 2/3 trials, extensive literature, and a mechanism that is already standard clinical practice) — this is not a speculative repurposing hypothesis but a case of the model correctly recovering an established drug-disease relationship. However, a **Blocking** data gap (DG001: no product-label warnings/contraindications retrieved) currently prevents this candidate from formally clearing the S1 safety screening stage, regardless of how strong the efficacy evidence is.

**To proceed, the following is needed:**
- Retrieve and review the official Health Canada product monograph for paclitaxel (resolves DG001, Blocking)
- Confirm current Health Canada licensing/DIN status directly, since this evidence pack shows 0 active licenses on file
- Obtain formal mechanism-of-action documentation from DrugBank or the monograph (resolves DG002)
- Clarify that this is a confirmatory/market-access question rather than a novel-efficacy question, given paclitaxel's existing global approval for breast cancer

---

## Note: Other Predicted Indications in This Evidence Pack

This evidence pack scored paclitaxel against multiple candidate indications, not just breast carcinoma. For context, here is how the other nine ranked:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 2 | Estrogen-receptor negative breast cancer | 99.91% | L1 | Proceed with Guardrails |
| 3 | Ehrlich tumor carcinoma | 99.91% | L4 | Hold (animal tumor model, not a human disease entity) |
| 4 | Hormone-resistant breast carcinoma | 99.91% | L2 | Research Question |
| 5 | Estrogen-receptor positive breast cancer | 99.91% | L1 | Proceed with Guardrails |
| 6 | Bilateral breast carcinoma | 99.89% | L3 | Hold (not a distinct biological entity) |
| 7 | Breast carcinoma by gene expression profile | 99.89% | L2 | Research Question |
| 8 | Nipple carcinoma | 99.89% | L4 | Hold (no dedicated trial/literature evidence) |
| 9 | Parameningeal embryonal rhabdomyosarcoma | 99.73% | L5 | Hold (model score only, no supporting evidence) |
| 10 | Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.73% | L5 | Hold (model score only, no supporting evidence) |

Ranks 2–7 are essentially variants of the same breast cancer signal (different molecular/anatomic subtypes) and share the same underlying rationale as the primary indication above. Ranks 9–10 (rhabdomyosarcoma subtypes) have no clinical trial or literature support in this pack and should be treated as unvalidated model output only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

