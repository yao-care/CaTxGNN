---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 563
evidence_level: L5
indication_count: 10
---

# Norfloxacin
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

# Norfloxacin: From Urinary Tract Infection to Septicemic Plague

## One-Sentence Summary

Norfloxacin (DrugBank DB01059) is a fluoroquinolone antibacterial, classically used to treat urinary tract and other bacterial infections. Among 10 TxGNN-predicted candidate indications reviewed for this drug, only one — **Septicemic Plague** (*Yersinia pestis* infection) — carries a biologically plausible mechanism and any literature support; the other nine candidates (hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, etc.) are score-only predictions explicitly flagged by the reviewer as having no known mechanistic link. Evidence for the plague indication is currently limited to **2 animal/in-vitro publications**, with no norfloxacin-specific human trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (fluoroquinolone antibacterial class; no Taiwan/Canada license record available in this evidence pack) |
| Predicted New Indication | Septicemic Plague |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L3 |
| Canada Market Status | 未上市 (Not Marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for norfloxacin is not available in this evidence pack. Based on known pharmacological information, norfloxacin is a second-generation fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV, and its efficacy against gram-negative bacterial infections (notably urinary tract infections) is well established.

*Yersinia pestis*, the causative organism of plague, is a gram-negative bacillus within the antibacterial spectrum typically covered by fluoroquinolones. Class-mates ciprofloxacin and levofloxacin are already approved for plague treatment and post-exposure prophylaxis, which lends indirect, class-level plausibility to norfloxacin's TxGNN prediction.

However, the only norfloxacin-specific data located (PMID 10987101) indicates norfloxacin's protective effect on post-vaccination immunity in an animal plague model was **weaker** than ciprofloxacin, ofloxacin, or pefloxacin — meaning the class-level rationale does not translate into a norfloxacin-specific advantage. This tempers the reasonableness of the prediction relative to other fluoroquinolones already approved for this use.

**Note on the other 9 TxGNN candidates:** Hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant hematological system disease, diffuse scleroderma, monoclonal gammopathy, and hematological disease with acquired peripheral neuropathy were all reviewed and explicitly assessed as having **no plausible mechanistic link** to norfloxacin's antibacterial action, with zero supporting clinical trials or literature. Punctate epithelial keratoconjunctivitis had 2 literature hits, but both describe a *microsporidial* (fungal-parasitic, not bacterial) pathogen for which norfloxacin has no recognized activity. These nine are not carried forward in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Animal study | Antibiotiki i khimioterapiia | Combined emergency fluoroquinolone + specific (EV Nalr vaccine) prophylaxis outperformed sequential use in plague-infected mice; norfloxacin's interference with post-vaccine immunity was lower than ciprofloxacin/ofloxacin/pefloxacin, but the study did not establish norfloxacin as an effective standalone treatment |
| [11057367](https://pubmed.ncbi.nlm.nih.gov/11057367/) | 2000 | In vitro resistance study | Antibiotiki i khimioterapiia | Examined fluoroquinolone resistance mutants of *Vibrio cholerae* (cholera pathogen, not *Yersinia pestis*); relevance to the plague indication is limited |

---

## Canada Market Information

Norfloxacin is currently **not marketed** in this jurisdiction (未上市); no license/DIN records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications for norfloxacin are flagged in this evidence pack as a **Blocking** data gap — see Next Steps. As a class, fluoroquinolones carry known risks including peripheral neuropathy, tendinopathy, and QT prolongation; these should be assumed applicable pending confirmation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for norfloxacin in septicemic plague is limited to two animal/in-vitro studies with no norfloxacin-specific human data, and the drug is not currently marketed in this jurisdiction. A blocking data gap on TFDA safety labeling prevents this candidate from entering formal safety review (S1).

**To proceed, the following is needed:**
- TFDA/product label warnings and contraindications (Blocking gap — required before any S1 safety assessment)
- Detailed mechanism of action (MOA) documentation from DrugBank
- Norfloxacin-specific efficacy data in plague (current evidence is class-level, drawn from other fluoroquinolones)
- Confirmation of regulatory/market status and licensing pathway
- No further investigation recommended for the other 9 TxGNN-predicted candidates unless new mechanistic or literature evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

