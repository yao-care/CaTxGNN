---
layout: default
title: Levonorgestrel
parent: Moderate Evidence (L3-L4)
nav_order: 464
evidence_level: L3
indication_count: 6
---

# Levonorgestrel
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **6** 
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

# Levonorgestrel: From Contraception to Acne

## One-Sentence Summary

Levonorgestrel is a second-generation progestin best known as a component of combined oral contraceptives, emergency contraception, and intrauterine systems. The TxGNN model predicts it may be effective for **Acne (disease)**, but the supporting evidence is mixed and mechanistically contested: **5 clinical trials** and **20 publications** were retrieved, yet only a handful directly address acne, and levonorgestrel's known androgenic activity runs counter to how progestin-based acne therapies are believed to work.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (well-established use; no Canada-specific regulatory filing available — see Market Status) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available in the evidence pack (DrugBank MOA field returned a data gap). Based on known pharmacology, levonorgestrel is a second-generation progestin with comparatively **high androgenic activity** relative to other progestins used in oral contraceptives. This is a double-edged feature for the acne indication: androgen-driven sebum production is a core driver of acne pathogenesis, and the oral contraceptives with proven acne benefit (e.g., those containing chlormadinone, drospirenone, or cyproterone) work specifically because their progestin component is **anti-androgenic** — the opposite pharmacological direction from levonorgestrel.

The evidence pack's own repurposing rationale flags this directly: TxGNN's high score likely reflects a generalized "oral contraceptives treat acne" association learned across the knowledge graph, rather than a levonorgestrel-specific mechanistic fit. Some literature does show benefit for low-dose ethinylestradiol/levonorgestrel combinations in moderate acne (see PMID 12196750 below), which keeps the hypothesis from being dismissed outright, but competing literature (e.g., PMID 15025547) reports that an anti-androgenic comparator outperformed the EE/levonorgestrel combination for the same indication. This directional uncertainty is the central reason the evidence level remains moderate (L3) despite the very high model score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Completed | 101,498 | Large safety cohort comparing nomegestrol acetate/estradiol vs. levonorgestrel-containing combined oral contraceptives; general safety endpoints, not acne-specific. |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Phase 2 | Unknown | 60 | Fertility-conservative treatment of atypical endometrial hyperplasia (Mirena vs. megestrol); unrelated to acne. |
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completed | 131 | Continuous oral contraceptive + doxycycline (a common acne drug) to reduce breakthrough bleeding; acne link is incidental via doxycycline, not levonorgestrel confirmed. |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Phase 2 | Completed | 100 | Subdermal gestrinone implant for endometriosis-related pelvic pain; unrelated to acne. |
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Terminated | 44 | Levonorgestrel IUS for endometrial cancer prevention in obese women; acne mentioned only as a known side effect of oral progestins, not a treatment target. |

**Note:** None of the retrieved trials directly and confidently test levonorgestrel for acne; relevance grading in the source data rates all but one as low-to-moderate ("B"/"C").

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | RCT | J Am Acad Dermatol | Randomized, placebo-controlled trial: low-dose ethinylestradiol (20mcg)/levonorgestrel (100mcg) improved moderate acne, attributed to reduced bioavailable androgens. |
| [6084924](https://pubmed.ncbi.nlm.nih.gov/6084924/) | 1984 | Clinical study | Acta Derm Venereol | Serum testosterone/SHBG measured in acne patients on two OCPs (one containing levonorgestrel); abnormal pretreatment androgen values were common. |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Review | Drugs | Ethinylestradiol/chlormadinone (anti-androgenic) was significantly more effective than ethinylestradiol/levonorgestrel for mild-to-moderate papulopustular acne. |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Review | Am J Clin Dermatol | Reviews dermatological (acne, hirsutism) benefits of anti-androgenic progestins, framing excess androgen at the pilosebaceous unit as the causal driver. |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | Am J Med | Reviews androgenicity of progestins; levonorgestrel is derived from testosterone (19-carbon series) and retains meaningful androgenic activity. |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Review | J Womens Health | Compares drospirenone to levonorgestrel and others; notes levonorgestrel's association with acne vulgaris and hirsutism as side effects, not benefits. |

**Note:** 14 additional publications retrieved (general contraception/IUD reviews, VTE risk, lipid effects) were excluded from this table as not substantively related to the acne indication.

---

## Canada Market Information

Levonorgestrel-containing products have no active Canadian market authorization recorded in this evidence pack (0 DINs, market status: Not Marketed). No license-level indication data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack — notably, the TFDA/product-insert warning and contraindication data is flagged as a **Blocking** data gap (DG001), which by itself prevents this candidate from clearing initial safety screening (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is undercut by a plausible mechanism mismatch — levonorgestrel's androgenic activity is directionally opposite to the anti-androgenic mechanism that makes other progestin-containing contraceptives effective for acne, and the strongest comparative literature (PMID 15025547) shows an anti-androgenic alternative outperforming it. Combined with a Blocking safety data gap and no current Canadian market presence, there is not yet a sound basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/product-insert warnings and contraindications (resolves Blocking gap DG001)
- Confirmed original mechanism of action from DrugBank (resolves gap DG002)
- A pharmacology review specifically resolving the direction of levonorgestrel's androgenic effect on acne (risk vs. benefit)
- A levonorgestrel-specific (not generic EE/progestin-class) controlled trial for the acne indication
- Route/formulation and market-entry assessment, given the drug is not currently marketed in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

