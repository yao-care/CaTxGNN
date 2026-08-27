---
layout: default
title: Potassium Citrate
parent: 僅模型預測 (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
---

# Potassium Citrate
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

# Potassium Citrate: From Unmarketed Status in Canada to Confirmed Use in Nephrolithiasis

> **Note on indication selection:** This Evidence Pack (`TW-DB09125-multi`) contains **10** TxGNN-predicted indications for potassium citrate. The single highest-scoring prediction (rank 1, *familial visceral myopathy*, score 99.95%) has **zero** supporting clinical trials or literature, and the pack's own rationale explicitly flags it as likely knowledge-graph noise rather than a real pharmacological signal. This report therefore focuses on the **rank-4 candidate, nephrolithiasis**, which is the only indication with L1-grade evidence (36 trials, 19 publications) and is in fact potassium citrate's globally established core indication. A summary of the other 9 candidates is provided at the end for completeness.

---

## One-Sentence Summary

Potassium citrate is an oral alkalinizing/electrolyte agent that is currently **not marketed in Canada** (0 DINs on file). Among the 10 indications TxGNN surfaced for this drug, **nephrolithiasis (kidney stone disease)** is the only one backed by substantial real-world evidence, with **36 clinical trials** and **19 publications** — including established use for hypocitraturic calcium oxalate stones, uric acid lithiasis, and renal tubular acidosis-related stone disease. This is best understood as the model correctly recovering a well-established indication rather than a novel repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no Health Canada licences/DINs are captured in this evidence pack (drug is unmarketed) |
| Predicted New Indication | Nephrolithiasis (kidney stone disease) |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails* |

*\*Efficacy evidence alone supports "Proceed with Guardrails," but a Blocking-severity safety data gap (see Conclusion) must be resolved before this can become a final Go decision.*

---

## Why is This Prediction Reasonable?

Currently, a formal DrugBank mechanism-of-action text is not available for potassium citrate in this evidence pack (data gap DG002). Based on the pharmacology captured in the evidence rationale, potassium citrate acts through three well-characterized mechanisms in urinary stone disease: (1) citrate anion forms soluble complexes with urinary calcium, reducing the supersaturation of calcium oxalate and calcium phosphate; (2) citrate is metabolized to bicarbonate, alkalinizing the urine, which promotes uric acid stone dissolution and reduces the solubility requirement for cystine; and (3) it directly corrects hypocitraturia (citrate deficiency), a common metabolic abnormality in stone formers.

Unlike a typical "old drug, new disease" repurposing hypothesis, nephrolithiasis is potassium citrate's **core, already-established indication** worldwide (e.g., marketed as Urocit-K for renal tubular acidosis and hypocitraturic calcium stone disease). The high TxGNN score here reflects the model correctly recovering a real, mechanistically grounded drug–disease relationship rather than surfacing a novel hypothesis — which is itself a useful positive-control signal for the model's reliability on this drug.

Because the drug is not currently marketed in Canada, the practical question for this evaluation is less "is this indication plausible" (it clearly is) and more "what regulatory and safety data are needed to support a Canadian market-entry or off-label-use decision," discussed in Conclusion and Next Steps below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004284](https://clinicaltrials.gov/study/NCT00004284) | Phase 3 | Completed | 300 | Compared potassium phosphate vs. potassium citrate for correcting absorptive hypercalciuria and preventing recurrent stone formation. |
| [NCT02373384](https://clinicaltrials.gov/study/NCT02373384) | Phase 4 | Completed | 182 | Identified predictors of successful oral (citrate-based) dissolution therapy for radiolucent renal stones. |
| [NCT03281928](https://clinicaltrials.gov/study/NCT03281928) | N/A | Terminated | 30 | Evaluated effect of dietary sodium and potassium citrate on renal mineral handling. |
| [NCT06819553](https://clinicaltrials.gov/study/NCT06819553) | Phase 2/3 | Active, not recruiting | 48 | Testing oral potassium citrate to reduce ureteral stent encrustation after ureteroscopy for uric acid stones. |
| [NCT00860093](https://clinicaltrials.gov/study/NCT00860093) | Phase 2 | Terminated | 135 | Multi-site placebo-controlled study of citrate-class adjuvant therapy to facilitate stone passage after shock wave lithotripsy. |
| [NCT06819111](https://clinicaltrials.gov/study/NCT06819111) | Phase 1 | Not yet recruiting | 20 | Comparing pharmacokinetics of different potassium citrate formulations (OTC vs. slow-release) for urinary alkalinization. |
| [NCT01329042](https://clinicaltrials.gov/study/NCT01329042) | Phase 4 | Completed | 80 | Potassium sodium hydrogen citrate reduced stone recurrence/residual fragments after ESWL and PCNL in calcium oxalate urolithiasis. |
| [NCT06966635](https://clinicaltrials.gov/study/NCT06966635) | Phase 4 | Recruiting | 312 | Evaluating potassium citrate sustained-release tablets for lowering uric acid and preventing urinary calculi in gout patients. |
| [NCT04021381](https://clinicaltrials.gov/study/NCT04021381) | Phase 3 | Unknown status | 262 | Randomized placebo-controlled trial of citrate salts for stone-free outcomes after flexible ureterorenoscopy. |
| [NCT03984409](https://clinicaltrials.gov/study/NCT03984409) | N/A | Completed | 22 | Showed dietary citrate (orange juice) can replicate the urinary alkalinization achieved with potassium citrate in hypocitraturic/aciduric stone formers. |

*26 additional lower-relevance or duplicate-mechanism trials were identified but are not shown; see the source evidence pack for the full list.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40978115](https://pubmed.ncbi.nlm.nih.gov/40978115/) | 2025 | Review | Clinical Kidney Journal | Comprehensive update confirming citrate's central role as urinary base equivalent and inhibitor of calcium stone formation. |
| [27915395](https://pubmed.ncbi.nlm.nih.gov/27915395/) | 2017 | Systematic Review/Meta-analysis | Urolithiasis | Meta-analysis confirming potassium citrate supplementation reduces stone recurrence after shockwave lithotripsy. |
| [39206631](https://pubmed.ncbi.nlm.nih.gov/39206631/) | 2024 | RCT (Phase II) | Urologia | Potassium citrate + magnesium + probiotics reduced crystalluria in stone formers. |
| [40583613](https://pubmed.ncbi.nlm.nih.gov/40583613/) | 2025 | Review/Guideline | Archivio Italiano di Urologia e Andrologia | Expert consensus (ESD 2025) on management of urinary stones, including citrate-based alkalinizing therapy. |
| [26582172](https://pubmed.ncbi.nlm.nih.gov/26582172/) | 2016 | Retrospective Cohort | Urolithiasis | Potassium citrate reduced urinary calcium excretion in hypocitraturic calcium oxalate stone formers. |
| [3306318](https://pubmed.ncbi.nlm.nih.gov/3306318/) | 1987 | Review | Mineral and Electrolyte Metabolism | Foundational review establishing potassium citrate's role in RTA-related, hypocitraturic, and uric acid stone disease. |
| [33417997](https://pubmed.ncbi.nlm.nih.gov/33417997/) | 2021 | Preclinical | Kidney International | Chlorthalidone + potassium citrate reduced calcium oxalate stones and improved bone quality in a hypercalciuric rat model. |
| [16443041](https://pubmed.ncbi.nlm.nih.gov/16443041/) | 2006 | Review | The Lancet | General review of kidney stone pathophysiology and medical management, citing citrate therapy. |
| [33459627](https://pubmed.ncbi.nlm.nih.gov/33459627/) | 2021 | Review | Archivos Españoles de Urología | Dietary/lifestyle recommendations for stone formers, including citrate supplementation. |
| [1585829](https://pubmed.ncbi.nlm.nih.gov/1585829/) | 1992 | Clinical Study | Journal of Bone and Mineral Research | Compared physicochemical action of potassium-magnesium citrate vs. potassium citrate on urinary biochemistry in stone formers. |

*9 additional publications (mostly tier-2/3 case reports and cohort studies) were identified but are not shown; see the source evidence pack for the full list.*

---

## Canada Market Information

Potassium citrate is currently **not marketed in Canada** — no Drug Identification Numbers (DINs) or Health Canada product licences are captured in this evidence pack (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack — this is flagged as a **Blocking-severity data gap (DG001)** requiring TFDA/Health Canada label retrieval before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (efficacy) — Hold on final Go/No-Go pending safety data**

**Rationale:**
- Nephrolithiasis is supported by L1-grade evidence (a completed Phase 3 RCT plus a large body of Phase 2–4 trials and a published meta-analysis) and is potassium citrate's already-established core indication elsewhere, giving high confidence in the mechanistic and clinical basis.
- However, a **Blocking** data gap (DG001 — missing TFDA/Health Canada label warnings and contraindications) means this candidate cannot yet pass the safety pre-screen (S1), regardless of the strength of efficacy evidence.

**To proceed, the following is needed:**
- Obtain the official Health Canada / TFDA product monograph (warnings, contraindications, precautions) for potassium citrate — DG001, Blocking.
- Obtain a formal DrugBank mechanism-of-action record to support the mechanistic-relevance analysis — DG002, High.
- Confirm whether Canadian market entry is being pursued via new drug submission or via an existing DIN holder, since none currently exists.
- Independently verify the ambiguous NCT00903201 trial (exocrine pancreatic insufficiency candidate) and the "grade C" trials flagged as possible database co-occurrence noise before citing them as supporting evidence.

---

## Other TxGNN-Predicted Indications (Not Yet Actionable)

For completeness, the remaining candidates in this multi-indication evidence pack are summarized below. Most have no supporting clinical or literature evidence and are assessed by the model's own rationale as likely knowledge-graph artifacts (e.g., shared gene-family or metabolite nodes) rather than real pharmacological signals.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 1 | Familial visceral myopathy | 99.95% | L5 | Hold | No trials/literature; likely electrolyte-node co-occurrence noise |
| 2 | Mitochondrial OXPHOS disorder (nuclear DNA) | 99.92% | L5 | Hold | No trials/literature; no evidence exogenous citrate helps nuclear-gene OXPHOS defects |
| 3 | Pendred syndrome | 99.88% | L5 | Hold | No trials/literature; likely SLC26-family gene-similarity artifact |
| 5 | Cystinosis | 99.73% | L4 | Research Question | 3 case-report-level publications; plausible as supportive therapy for associated Fanconi-syndrome acidosis, not disease-modifying |
| 6 | Hypermanganesemia with dystonia | 99.72% | L5 | Hold | No trials/literature; no mechanistic basis |
| 7 | Nephrolithiasis susceptibility (SLC26A1) | 99.68% | L3 | Research Question | No dedicated trials; reasonable mechanistic extrapolation from main nephrolithiasis evidence base |
| 8 | Autosomal recessive nonsyndromic deafness | 99.67% | L5 | Hold | No trials/literature; likely SLC26A4 gene-family artifact |
| 9 | Exocrine pancreatic insufficiency | 99.66% | L4 | Research Question | 1 trial (relevance unconfirmed) + 1 case report; plausible only for managing secondary oxalate nephropathy, not EPI itself |
| 10 | Leukocyte adhesion deficiency | 99.62% | L5 | Hold | No trials/literature; no mechanistic basis |

These candidates require no immediate action but rank 5, 7, and 9 (cystinosis, SLC26A1-related nephrolithiasis, exocrine pancreatic insufficiency) may warrant a lightweight literature-monitoring flag given their partial mechanistic plausibility as *supportive* (not primary) therapy in electrolyte/acid-base management.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

