---
layout: default
title: Bicalutamide
parent: Model Prediction Only (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

The evidence pack lists the top prediction as hypertrichosis, but the only meaningful clinical evidence supports female breast carcinoma (rank 9). Both are covered below, with hypertrichosis as the headline per the rank-1 prediction.

---

## One-Sentence Summary

Bicalutamide is a nonsteroidal androgen receptor (AR) antagonist, marketed in Canada as a single-ingredient product. The TxGNN model's top prediction is **hypertrichosis**, but it is supported by only **1 comment letter and no clinical trials**. The best-supported prediction in the list is **female breast carcinoma**, with **1 Phase 2 trial** and **20 publications**, mostly preclinical studies and reviews.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the Canadian licence records carry no indication text) |
| Predicted New Indication | Hypertrichosis (rank 1); the best-evidenced alternative is female breast carcinoma (rank 9) |
| TxGNN Prediction Score | 99.69% (hypertrichosis); 99.11% (female breast carcinoma) |
| Evidence Level | L4 (hypertrichosis); L2 (female breast carcinoma) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold (hypertrichosis); Proceed with Guardrails (female breast carcinoma) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known pharmacology, bicalutamide is a nonsteroidal AR antagonist. It blocks androgen signalling and is widely used in hormone-driven prostate cancer.

**Hypertrichosis:** Some hair growth, particularly minoxidil-induced hypertrichosis in women, has an androgen-signalling component, so AR blockade is biologically plausible. The only supporting item is a 2022 comment on a retrospective review of bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss. A comment letter is not primary clinical evidence, and no trial data were supplied.

**Female breast carcinoma:** AR is expressed in a substantial fraction of triple-negative breast cancers (the luminal androgen receptor subtype) and in apocrine carcinoma. AR blockade is therefore a rational targeted strategy. Preclinical work and multiple reviews support this, but clinical results have been modest. A Phase 2 study of bicalutamide plus an aromatase inhibitor in ER+/AR+ advanced breast cancer showed a 6-month clinical benefit rate of 16.7% and no objective responses, and it was terminated.

The other top-ranked predictions (for example, malformation syndromes, leprosy and nephrogenic syndrome of inappropriate antidiuresis) have no plausible AR-antagonist mechanism and no supporting evidence. They appear to be graph-based artefacts.

---

## Clinical Trial Evidence

**Hypertrichosis:** Currently no related clinical trials registered.

**Female breast carcinoma:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03650894](https://clinicaltrials.gov/study/NCT03650894) | Phase 2 | Active, not recruiting | 30 | Nivolumab + bicalutamide + ipilimumab in metastatic HER2-negative breast cancer; combines AR blockade with immune checkpoint therapy while omitting or delaying chemotherapy. No results reported in the data. |

**Multiple endocrine neoplasia (rank 7, weakly relevant only):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | SMMART PRIME personalised oncology platform trial; not specific to MEN. |
| [NCT02615223](https://clinicaltrials.gov/study/NCT02615223) | Not applicable | Unknown | 120 | Endocrine therapy with or without cryoablation in stage IV prostate cancer; no direct evidence for MEN. |

---

## Literature Evidence

**Hypertrichosis:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Comment/Letter | J Am Acad Dermatol | Comment on a retrospective review of 35 patients on bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss. No abstract available. |

**Female breast carcinoma (selected from 20 publications):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31434793](https://pubmed.ncbi.nlm.nih.gov/31434793/) | 2020 | Phase 2 single-arm study | The Oncologist | Bicalutamide plus aromatase inhibitor in ER+/AR+ advanced breast cancer: no synergy, 6-month clinical benefit rate 16.7%, objective response rate 0%; terminated early. |
| [40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/) | 2025 | Review | Curr Med Sci | Anti-androgen therapy for TNBC, covering bicalutamide, enzalutamide and combination strategies. |
| [29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/) | 2018 | Review | Cancer Treat Rev | AR as a potential target in the LAR subtype of TNBC. |
| [35027319](https://pubmed.ncbi.nlm.nih.gov/35027319/) | 2022 | Review | Clin Breast Cancer | Molecular and clinical features of apocrine carcinoma (ER-negative, AR-positive). |
| [40974527](https://pubmed.ncbi.nlm.nih.gov/40974527/) | 2026 | Preclinical | Sci China Life Sci | AR/ERK co-targeting (bicalutamide plus GDC-0994) triggers ferroptosis via FOXC2 in TNBC. |
| [31917699](https://pubmed.ncbi.nlm.nih.gov/31917699/) | 2020 | Preclinical | Anti-Cancer Drugs | Bicalutamide plus curcumin showed a strong effect in AR-positive TNBC models. |
| [32332626](https://pubmed.ncbi.nlm.nih.gov/32332626/) | 2020 | Preclinical | Medicine | Bicalutamide inhibited proliferation and invasion of MDA-MB-231 TNBC cells. |
| [39063165](https://pubmed.ncbi.nlm.nih.gov/39063165/) | 2024 | Preclinical | Int J Mol Sci | Bicalutamide enhanced doxorubicin and docetaxel activity in human and canine inflammatory mammary cancer cell lines. |
| [21633166](https://pubmed.ncbi.nlm.nih.gov/21633166/) | 2011 | Preclinical/Molecular classification | J Clin Invest | Identified six TNBC subtypes, including the LAR subtype. |
| [24740738](https://pubmed.ncbi.nlm.nih.gov/24740738/) | 2014 | Review | J Mol Endocrinol | Revisits the role of AR in breast cancer. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02270226 | TEVA-BICALUTAMIDE | Not specified | Not specified |
| 02519178 | BICALUTAMIDE | Not specified | Not specified |
| 02357216 | JAMP-BICALUTAMIDE | Not specified | Not specified |
| 02325985 | ACH-BICALUTAMIDE | Not specified | Not specified |
| 02275589 | PMS-BICALUTAMIDE | Not specified | Not specified |

Six valid single-ingredient licences are held in total; the sixth is PRO-BICALUTAMIDE - 50 (DIN 02311038).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (nonsteroidal AR antagonist); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low; anaemia is listed among the knowledge-graph contraindication signals, so monitor blood counts |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function, blood glucose, haemoglobin/CBC |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Label-based warnings and contraindications were not available in the compiled data. The following signals come from a drug-disease contraindication knowledge graph, not from label text:

- **Knowledge-graph contraindication signals:** liver disease, drug-induced liver injury, gallbladder disease, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, anaemia, macrocytic anaemia and interstitial lung disease.
- **Drug interactions:** 100 interactions were identified. The two **Major** interactions in the listed results are **cisapride** and **dolasetron** (both QT-related concerns). Moderate interactions include famotidine, loperamide, aprepitant, clarithromycin, levofloxacin, granisetron, budesonide, eliglustat and several laxatives (bisacodyl, lactulose, lactitol, magnesium citrate, magnesium hydroxide, glycerin, castor oil, mineral oil). Metronidazole is a Minor interaction.

Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold (hypertrichosis, the rank-1 prediction); Proceed with Guardrails (female breast carcinoma, the best-supported prediction)**

**Rationale:**
- Hypertrichosis has a plausible AR-related mechanism but only a comment letter as evidence, so it remains a research question.
- Female breast carcinoma has a Phase 2 trial, extensive preclinical data and reviews. However, the one completed clinical signal (bicalutamide plus an aromatase inhibitor) was negative, and the active trial is a combination regimen without results, so the bicalutamide contribution cannot be isolated.
- Use should be limited to AR-positive, biomarker-selected patients, ideally within a trial.
- The remaining predictions (ranks 2-8 and 10) lack mechanistic or clinical support and should be held.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Detailed mechanism of action data
- The primary retrospective study of bicalutamide for minoxidil-induced hypertrichosis, with efficacy and safety data
- Results from NCT03650894, and AR-positivity selection criteria for breast cancer
- Hepatic, glycaemic and haematological monitoring plans, plus a QT-risk review of co-medications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

