---
layout: default
title: Goserelin
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 3
---

# Goserelin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Goserelin: From Hormone-Sensitive Cancers & Endometriosis to Amenorrhea

## One-Sentence Summary

Goserelin (brand name Zoladex) is a GnRH receptor agonist with EMA/FDA-approved indications for hormone receptor-positive breast cancer, prostate cancer, endometriosis, and uterine fibroids, though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Amenorrhea (disease)** — specifically as a pharmacological amenorrhea inducer — with **7 clinical trials** and **19 publications** currently supporting this direction.
The mechanistic link is exceptionally direct: amenorrhea is goserelin's primary downstream pharmacological effect, and the evidence base is mature.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not approved in Canada; globally EMA/FDA-approved for breast cancer, prostate cancer, endometriosis, and uterine fibroids |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Goserelin is a synthetic analogue of GnRH (Gonadotropin-Releasing Hormone). When administered continuously via subcutaneous depot injection, it initially stimulates GnRH receptors but rapidly causes receptor downregulation at the pituitary. This leads to profound suppression of LH and FSH secretion, which in turn reduces ovarian estrogen synthesis to near-castrate levels — directly inducing reversible pharmacological amenorrhea. This is not an indirect or speculative mechanism: amenorrhea is the intended pharmacodynamic endpoint of goserelin therapy.

The relationship between goserelin's established indications and the predicted new use is unusually tight. In endometriosis and uterine fibroids, goserelin works precisely *because* it induces amenorrhea, allowing estrogen-dependent lesions to regress. In hormone receptor-positive breast cancer, the same ovarian suppression reduces the circulating estrogens that drive tumour growth. Chemotherapy-induced premature ovarian failure is prevented by co-administering goserelin to induce temporary amenorrhea and "shield" the ovaries. Across all these indications, amenorrhea is not a side effect — it is the mechanism.

Given this background, the TxGNN prediction that goserelin is effective for amenorrhea as a discrete indication is strongly biologically grounded. The model score of 99.99% reflects a well-established pharmacological truth rather than a novel inference. The clinical question is therefore less "is this plausible?" and more "in which specific patient populations and amenorrhea subtypes does formal evidence exist?"

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | Completed | 400 | OPTION trial: Goserelin vs no goserelin during chemotherapy for Stage I–III breast cancer; primary endpoint was prevention of early menopause (amenorrhea rate) |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | LHRH agonist (goserelin) + chemotherapy vs chemotherapy alone; primary endpoint was ovarian failure (amenorrhea) after treatment in hormone receptor-negative early breast cancer |
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | Completed | 98 | Goserelin added to standard chemotherapy in premenopausal breast cancer; ovarian function recovery and amenorrhea rate were key secondary endpoints |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | Completed | 32 | Head-to-head RCT comparing GnRH agonist vs aromatase inhibitor for uterine adenomyosis in fertility-preserving patients; amenorrhea induction was the primary therapeutic target |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene ± goserelin in premenopausal HR+ breast cancer; chemotherapy-induced amenorrhea was a stratification variable and secondary endpoint |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | Unknown | 100 | Goserelin for ovarian protection during cyclophosphamide-containing chemotherapy; menstruation outcome (amenorrhea rates at 1 and 3 years) was the primary endpoint |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | N/A | Unknown | N/A | Single-arm study of Zoladex + CEF chemotherapy as neoadjuvant therapy in premenopausal breast cancer; noted that Zoladex "can induce reversible amenorrhea" comparable to ovarian ablation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Meta-analysis / RCT pooling | Annals of Oncology | OPTION trial results: GnRH agonist during chemotherapy significantly reduced premature ovarian insufficiency (amenorrhea-based endpoint) in early breast cancer |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT secondary analysis | J Clin Oncology | IBCSG Trial VIII: Compared amenorrhea and hot flash rates across chemotherapy, goserelin, and combination arms; goserelin arm showed highest sustained amenorrhea rates with better QOL profile |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J National Cancer Institute | IBCSG Trial VIII: Sequential CMF followed by goserelin vs either alone for premenopausal node-negative breast cancer; amenorrhea documented as major treatment-related outcome |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncology | ZEBRA study: Goserelin vs CMF in node-positive premenopausal breast cancer; goserelin produced consistent amenorrhea and survival outcomes comparable to chemotherapy |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertility and Sterility | GnRH agonist (goserelin) vs low-dose OCP for endometriosis-associated pelvic pain; goserelin-induced amenorrhea was central to its efficacy |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Research and Treatment | Goserelin ovarian ablation improved survival in Stage II/III HR+ breast cancer patients *without* chemotherapy-induced amenorrhea, underscoring amenorrhea as a therapeutic mechanism |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treatment | Comprehensive review of LHRH agonists in early breast cancer; confirms goserelin induces "reversible ovarian ablation" (amenorrhea) and is the most extensively studied agent in this class |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J Royal Army Medical Corps | Therapeutic induction of amenorrhea overview; identifies goserelin as "extremely effective" at amenorrhea induction with reversible effect — one of the earliest dedicated amenorrhea-indication reviews |
| [10730389](https://pubmed.ncbi.nlm.nih.gov/10730389/) | 1999 | Case series | Akusherstvo i Ginekologiia | GnRH agonist (Zoladex) used to induce amenorrhea for controlling severe uterine hemorrhage in adolescents with aplastic/hypoplastic anaemia; bleeding stopped within 2–4 days |
| [17006733](https://pubmed.ncbi.nlm.nih.gov/17006733/) | 2007 | Case report | Int Urology and Nephrology | Vesicouterine fistula treated via cystoscopic fulguration plus hormonal amenorrhea with goserelin; authors advocate this approach as a primary minimally invasive option |

---

## Canada Market Information

Goserelin is **not currently approved or marketed in Canada** (0 DINs). It holds EMA and FDA approval for hormone receptor-positive breast cancer, prostate cancer, endometriosis, and uterine fibroids in international markets. No Canadian product licence table is available.

---

## Cytotoxicity

Goserelin is classified as an antineoplastic hormonal agent (GnRH agonist), with established use in breast cancer and prostate cancer.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormonal / Endocrine therapy (GnRH agonist) — NOT a conventional cytotoxic drug |
| Myelosuppression Risk | Low — GnRH agonists do not cause bone marrow suppression |
| Emetogenicity Classification | Minimal — subcutaneous depot injection; emesis not a recognized class effect |
| Monitoring Items | Bone mineral density (with long-term use >6 months), serum estradiol/testosterone for suppression confirmation, hot flashes and mood assessment |
| Handling Protection | Standard subcutaneous injection handling; no cytotoxic spill precautions required (non-cytotoxic mechanism) |

---

## Safety Considerations

Safety data from the Canadian regulatory file is unavailable (goserelin is not marketed in Canada). Please refer to the package insert of the originator product (Zoladex, AstraZeneca) for complete warnings, contraindications, and precautions. Key clinical considerations known from the literature include:

- **Tumour flare**: Initial GnRH agonist administration transiently raises testosterone/estrogen before suppression; antiandrogen/antiestrogen co-administration may be required in the first 2–4 weeks
- **Bone density loss**: Prolonged use (>6 months) is associated with decreased bone mineral density; consider add-back therapy or DEXA monitoring
- **Hot flashes and menopausal symptoms**: Common class effect during ovarian suppression
- **Contraindication in pregnancy**: Goserelin can cause fetal harm and is contraindicated in pregnant women

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The pharmacological mechanism linking goserelin to amenorrhea is not a predictive inference — it is the drug's primary mode of action. Multiple completed Phase 3 RCTs with large sample sizes (NCT00427245 n=400; NCT00068601 n=257) directly evaluate goserelin-induced amenorrhea as a primary or key secondary endpoint, placing this at Evidence Level L1. The OPTION trial meta-analysis (PMID 28472240) further consolidates the evidence base.

**To proceed, the following is needed:**

- **Canada market entry pathway**: Identify whether a New Drug Submission (NDS) or Abbreviated NDS pathway applies, given the drug is not currently DIN-listed
- **Canadian prescribing information**: Obtain the Health Canada-approved monograph (if any prior submission exists) or rely on the PMDA/EMA/FDA-approved label as the primary safety reference
- **Targeted indication scoping**: Clarify the specific amenorrhea subtype intended (e.g., therapeutic amenorrhea for endometriosis, ovarian protection during chemotherapy, or military/operational amenorrhea as in PMID 1533675) — each may require a distinct regulatory pathway
- **Bone density risk management plan**: Protocol for DEXA monitoring and add-back HRT for any amenorrhea indication exceeding 6 months of therapy
- **Mechanism of action documentation**: Retrieve full MOA data from DrugBank API (DG002) to complete the drug profile for regulatory dossiers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

