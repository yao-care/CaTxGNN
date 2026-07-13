---
layout: default
title: Flutamide
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Flutamide
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

# Flutamide: From Prostate Cancer to Male Reproductive Organ Cancer

## One-Sentence Summary

Flutamide is a nonsteroidal antiandrogen established in the treatment of prostate cancer, functioning by competitively blocking the androgen receptor (AR) to suppress androgen-dependent tumour growth.
The TxGNN model predicts it may be effective for **Male Reproductive Organ Cancer** — the highest-evidence prediction among all candidates — with **50+ clinical trials** and **20 publications** currently supporting this direction.
The evidence level is **L1**, warranting a **Proceed with Guardrails** recommendation, though Health Canada has no current registration for flutamide.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (known from published pharmacology; Canada regulatory record unavailable — drug not marketed) |
| Predicted New Indication | Male Reproductive Organ Cancer |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on indication selection:** Ten indications were predicted. Ranks 1–5 and 7–10 all carry a **Hold** recommendation (L5 evidence or no clinical basis). Rank 6 — **Male Reproductive Organ Cancer** — is the only prediction with L1 evidence and an actionable recommendation, and is therefore the primary subject of this report.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on extensively published pharmacological literature, flutamide is a pure nonsteroidal antiandrogen: it competitively blocks the androgen receptor (AR), preventing dihydrotestosterone (DHT) and testosterone from binding and activating androgen-responsive gene expression. Unlike steroidal antiandrogens, flutamide does not suppress gonadotropin release, meaning testosterone levels may rise during monotherapy — a distinguishing pharmacological feature.

The vast majority of prostate cancers — the primary malignancy within the "male reproductive organ cancer" category — are hormone-sensitive, especially in early and locally advanced stages. Flutamide's AR antagonism directly targets this molecular dependency. When combined with LHRH agonists (complete androgen blockade, CAB), it suppresses both testicular and adrenal androgen activity simultaneously, achieving more thorough AR silencing than either agent alone. This rationale has been validated across decades of prostate oncology research.

Multiple Phase 3 RCTs enrolling hundreds to over 2,000 patients each have confirmed flutamide as an effective component of ADT regimens in locally advanced, intermediate-risk, and metastatic prostate cancer settings. The TxGNN model's high confidence score (99.98%) for this prediction reflects mechanistic alignment and strong clinical precedent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002597](https://clinicaltrials.gov/study/NCT00002597) | Phase 3 | Completed | 2,028 | RT with or without antiandrogen therapy (flutamide, goserelin, or leuprolide) for good-prognosis localized prostate cancer; evaluates RT enhancement by hormonal therapy |
| [NCT00005044](https://clinicaltrials.gov/study/NCT00005044) | Phase 3 | Completed | 1,579 | Short-term (4 months) vs longer-term (28 months) total androgen suppression combined with RT for intermediate-risk prostate cancer |
| [NCT00936390](https://clinicaltrials.gov/study/NCT00936390) | Phase 3 | Completed | 1,538 | Dose-escalated RT with or without short-term ADT (including flutamide) for intermediate-risk prostate cancer; assesses whether ADT adds benefit to dose-escalated RT |
| [NCT00769548](https://clinicaltrials.gov/study/NCT00769548) | Phase 3 | Completed | 1,322 | Compares whole-pelvic vs boost-only irradiation and neoadjuvant vs adjuvant total androgen suppression for prostate cancer |
| [NCT00003653](https://clinicaltrials.gov/study/NCT00003653) | Phase 3 | Completed | 1,386 | Intermittent vs continuous androgen suppression for PSA progression after RT; monitors time to castration resistance and survival |
| [NCT00003026](https://clinicaltrials.gov/study/NCT00003026) | Phase 3 | Completed | 966 | Long-term LHRH analogue adjuvant therapy vs no further treatment in locally advanced prostate cancer previously treated with RT + 6-month CAB |
| [NCT00767286](https://clinicaltrials.gov/study/NCT00767286) | Phase 3 | Completed | N/A | Long-term total androgen suppression following neoadjuvant hormonal cytoreduction and RT in locally advanced prostate carcinoma |
| [NCT00817739](https://clinicaltrials.gov/study/NCT00817739) | Phase 2 | Completed | 341 | Intermittent leuprorelin (3.75 mg SR) + flutamide for stage D2/metastatic prostate cancer; evaluates PSA response, hormonal recovery, and survival |
| [NCT00450463](https://clinicaltrials.gov/study/NCT00450463) | Phase 2 | Completed | 64 | PROSTVAC/TRICOM vaccine + flutamide vs flutamide alone in androgen-insensitive non-metastatic prostate cancer; directly tests flutamide as comparator arm |
| [NCT06601205](https://clinicaltrials.gov/study/NCT06601205) | Phase 2/3 | Completed | 125 | Pre-surgical window-of-opportunity trial comparing finasteride vs low-dose flutamide vs placebo in localized prostate cancer; tissue biomarker endpoints |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [21751904](https://pubmed.ncbi.nlm.nih.gov/21751904/) | 2011 | RCT | N Engl J Med | Short-term ADT before and during RT improves cancer control and reduces disease progression in early localized prostate adenocarcinoma; landmark trial supporting hormonal therapy integration |
| [24950779](https://pubmed.ncbi.nlm.nih.gov/24950779/) | 2014 | Preclinical/Clinical Biomarker | Cancer Prev Res | Flutamide (125 mg/day × 6 weeks) identified meaningful androgen-action biomarkers in high-risk women; androgen ablation reduced serous ovarian tumour burden 24-fold in mice |
| [8252497](https://pubmed.ncbi.nlm.nih.gov/8252497/) | 1993 | Mechanistic Review | Cancer | Establishes flutamide as a pure antiandrogen; maximal prostate growth inhibition achieved by combining flutamide with LHRH agonist, providing mechanistic rationale for CAB |
| [8650871](https://pubmed.ncbi.nlm.nih.gov/8650871/) | 1996 | Clinical Study | Urology | TRUS-measured prostate volume reduction with flutamide ± castration in untreated prostate cancer; objective assessment of treatment response |
| [37919464](https://pubmed.ncbi.nlm.nih.gov/37919464/) | 2023 | Preclinical | Sci Rep | Ganoderma lucidum polysaccharide potentiates flutamide + docetaxel cytotoxicity in prostate cancer cells; explores drug sensitization strategies |
| [30400755](https://pubmed.ncbi.nlm.nih.gov/30400755/) | 2018 | Preclinical | Tumour Biol | miR-23b + miR-27b combined with flutamide enhances apoptosis and decreases CCNG1 expression in castration-resistant prostate cancer cells |
| [3157927](https://pubmed.ncbi.nlm.nih.gov/3157927/) | 1985 | Clinical Trial | The Prostate | LH-RH agonist (D-Trp-6-LH-RH) + flutamide combination in Dunning R-3327H prostate cancer model; early preclinical support for CAB approach |
| [3071951](https://pubmed.ncbi.nlm.nih.gov/3071951/) | 1988 | Review | Am J Clin Oncol | Mechanistic rationale for combining nonsteroidal antiandrogen with LHRH analogue in prostate cancer; addresses residual adrenal androgen suppression |
| [29958919](https://pubmed.ncbi.nlm.nih.gov/29958919/) | 2018 | Mechanistic | Reprod Toxicol | Flutamide alters cell-cell junction protein expression in testis, epididymis, and prostate; relevant to understanding off-target reproductive tissue effects |
| [65117](https://pubmed.ncbi.nlm.nih.gov/65117/) | 1976 | Review | Adv Sex Horm Res | Early comprehensive review of antiandrogen mechanisms including flutamide; molecular basis of AR blockade and biological assay characterization |

---

## Canada Market Information

Flutamide is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) are registered with Health Canada. There are no approved product records to display.

---

## Cytotoxicity

Flutamide is used in the treatment of cancer; this section applies as an antineoplastic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Non-cytotoxic antineoplastic — Hormonal therapy (nonsteroidal androgen receptor antagonist) |
| Myelosuppression Risk | Low — antiandrogens do not target haematopoietic cells; myelosuppression is not a primary toxicity concern |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (LFTs) — hepatotoxicity is a documented concern; PSA monitoring for therapeutic response; baseline CBC |
| Handling Protection | Standard medication handling procedures; not classified as hazardous cytotoxic under conventional chemotherapy handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data including warnings, contraindications, and drug interactions were not captured in this Evidence Pack. Published literature documents a hepatotoxicity risk with flutamide (including rare fatal liver failure). A thorough review of the product monograph and current safety labelling is strongly recommended before any clinical application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Flutamide has robust Phase 3 RCT evidence supporting its efficacy as a component of complete androgen blockade in prostate cancer — the dominant male reproductive organ cancer — with trials enrolling up to 2,028 patients. The mechanistic basis (AR antagonism in androgen-dependent tumours) is well established, and the TxGNN L1 prediction reflects this existing clinical validation rather than a speculative leap.

**To proceed, the following is needed:**
- Determine the regulatory pathway for Health Canada market authorization (New Drug Submission or abbreviated route), given current unregistered status in Canada
- Obtain the full product monograph and review hepatotoxicity warnings, contraindications, and prescribing conditions
- Assess competitive positioning against newer-generation AR antagonists (enzalutamide, apalutamide, darolutamide) that are already registered in Canada and have more favourable safety profiles
- Define the precise clinical indication and patient population within "male reproductive organ cancer" where flutamide adds differentiated value
- Establish mandatory liver function monitoring protocol (pre-treatment LFTs and periodic monitoring) as a patient safety guardrail
- Review drug-drug interactions with LHRH agonists, warfarin, and other agents common in this patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

