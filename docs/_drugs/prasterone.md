---
layout: default
title: Prasterone
parent: 僅模型預測 (L5)
nav_order: 443
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone: From an Undocumented Original Indication to Systemic Sclerosis (Scleroderma)

> **Note on candidate selection:** TxGNN's raw top-ranked predictions for this drug (heparin cofactor 2 deficiency, factor V excess, antithrombin deficiency type 2, severe diabetic retinopathy, protein S deficiency thrombophilia, complement C4a deficiency, pseudo-von Willebrand disease, primary platelet release disorder) all carry **zero clinical trials and zero literature** — pure knowledge-graph signal with no way to judge direction or plausibility. One of them (rank 4, general thrombophilia) does have literature, but that literature points toward androgens **increasing** thrombotic risk rather than treating it. The only candidate in this Evidence Pack with genuine, direction-consistent mechanistic support is **rank 7 — Systemic Sclerosis (Scleroderma)**, which is why it is used as the lead candidate in this report rather than the top-scored rank-1 item. All ten candidates are listed for completeness under "Other TxGNN Signals" near the end.

## One-Sentence Summary

Prasterone (DHEA, DB01708) has no documented original indication and no market authorization in this Evidence Pack — it is currently **not marketed in Canada** and its mechanism of action is a recorded data gap. The TxGNN model's highest-scoring predictions are unsupported by any evidence, but among the ranked candidates, **Systemic Sclerosis (Scleroderma)** stands out with **6 supporting publications** (all observational/correlational) showing reduced DHEA-S levels in affected patients — **no interventional clinical trials exist for this indication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no original indication or MOA data on file) |
| Predicted New Indication | Systemic Sclerosis (Scleroderma) |
| TxGNN Prediction Score | 99.11% (score 0.9911; rank 14,749 by raw score) |
| Evidence Level | L4 (observational/mechanistic studies only, no interventional trials) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for prasterone is currently unavailable (recorded as a High-severity data gap, DG002, requiring a DrugBank API lookup). Prasterone is the pharmaceutical form of dehydroepiandrosterone (DHEA), an adrenal androgen precursor — this is inferred structurally from the compound name and evidence-pack rationale text, not from a confirmed MOA record, and should be treated as provisional until DG002 is resolved.

The rationale for a link to systemic sclerosis comes entirely from endocrine correlation studies rather than mechanistic or interventional data. Multiple independent cohort studies found that patients with systemic sclerosis — particularly postmenopausal women and those with more severe disease — have significantly **lower** circulating DHEA-S levels than matched controls, alongside blunted adrenocortical (HPA axis) responsiveness. This pattern is analogous to the "hormone replacement" rationale that has supported DHEA use in other autoimmune conditions such as systemic lupus erythematosus: if adrenal androgen output is relatively deficient in a disease state, exogenous replacement is biologically plausible as a way to modulate the associated immune/inflammatory process (DHEA has documented immunosuppressive effects on IL-6 production in the broader literature cited).

This remains a **correlational-to-mechanistic hypothesis, not a treatment mechanism**: no study in this Evidence Pack tested whether administering DHEA to SSc patients improves outcomes. It should be read as biologically plausible grounds for a research question, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12073659](https://pubmed.ncbi.nlm.nih.gov/12073659/) | 2002 | Review | Orvosi hetilap | Reviews adrenal/gonadal hormone role in autoimmune polyarthritis; notes DHEA/DHEA-S immunosuppressive effects (IL-6 inhibition) and consistently decreased DHEA-S in most autoimmune diseases |
| [16855152](https://pubmed.ncbi.nlm.nih.gov/16855152/) | 2006 | Cohort | Annals of the New York Academy of Sciences | Androgen and prolactin levels measured in 39 SSc patients vs. controls; altered androgen/DHEA-S status related to disease duration and severity |
| [9159534](https://pubmed.ncbi.nlm.nih.gov/9159534/) | 1997 | Cohort | British Journal of Rheumatology | High prolactin and low DHEA-S serum levels found in patients with severe systemic sclerosis; linked to soluble immune mediators |
| [11247320](https://pubmed.ncbi.nlm.nih.gov/11247320/) | 2001 | Cohort | Clinical and Experimental Rheumatology | DHEA-S serum levels evaluated in a cohort of women with SSc; examined relationship with disease severity |
| [17086608](https://pubmed.ncbi.nlm.nih.gov/17086608/) | 2006 | Cohort | The Journal of Rheumatology | Lower adrenocortical and adrenomedullary responses to hypoglycemia in premenopausal women with SSc, indicating blunted HPA axis function |
| [25524921](https://pubmed.ncbi.nlm.nih.gov/25524921/) | 2015 | Cohort | Rheumatology (Oxford) | Androgen levels examined in post-menopausal patients with systemic sclerosis (abstract not available) |

---

## Canada Market Information

Prasterone currently holds **no market authorizations in Canada** — 0 DINs on file, market status "Not Marketed" as of the data cutoff (2026-07-14). No product name, dosage form, or approved-indication text is available to report.

---

## Safety Considerations

No formal safety data (key warnings, contraindications, or drug interactions) is available for this compound — all fields are recorded as data gaps, including a **Blocking**-severity gap (DG001: Health Canada label warnings/contraindications not yet retrieved).

**Additional safety signal identified during evidence review (not from formal DDI/warning data):** Literature surfaced for other TxGNN-predicted indications suggests hyperandrogenic states are associated with *increased* thrombotic risk (e.g., PCOS-related thrombophilia, androgen-secreting Leydig cell tumors causing recurrent pulmonary embolism). While this is not a confirmed interaction for prasterone specifically, it flags a plausible risk direction that should be evaluated before any interventional study, particularly given DHEA's androgenic activity.

> Please refer to the official package insert / Health Canada label (once available) for authoritative safety information.

---

## Other TxGNN Signals (For Transparency)

| Disease | TxGNN Score | Evidence | Note |
|---|---|---|---|
| Heparin cofactor 2 deficiency | 99.99% | None | Top-scored, but no evidence and unclear direction |
| Factor V excess w/ spontaneous thrombosis | 99.98% | None | No evidence; androgens generally associated with thrombosis risk, not benefit |
| Antithrombin deficiency type 2 | 99.98% | None | No evidence; possible relative contraindication rather than benefit |
| Thrombophilia | 99.91% | 4 papers (correlational) | Literature shows androgen excess as a *risk factor* for thrombosis — direction opposes a treatment hypothesis |
| Severe nonproliferative diabetic retinopathy | 99.25% | None | No evidence |
| Thrombophilia (protein S deficiency, AR) | 99.13% | None | No evidence |
| Complement component 4a deficiency | 99.05% | None | No evidence |
| Pseudo-von Willebrand disease | 99.01% | None | No evidence |
| Primary platelet release disorder | 99.01% | None | No evidence |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the lead candidate (Systemic Sclerosis) is limited to L4 observational/mechanistic correlation — no interventional trial has tested DHEA supplementation in SSc, and both the drug's MOA and its Canadian regulatory/safety profile are currently unresolved data gaps (one of them Blocking-severity). The nominally higher-scored TxGNN predictions are unsupported by any evidence and should not drive prioritization.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve Health Canada product label warnings/contraindications before any safety assessment can proceed
- Resolve DG002 (High): confirm prasterone's mechanism of action via DrugBank
- Establish the drug's actual original/approved indication(s), since none are currently on file
- Design or identify a pilot/exploratory interventional study of DHEA supplementation in systemic sclerosis, since current support is correlational only
- Evaluate thrombotic-risk signal (from the thrombophilia-related predictions) as a safety consideration before any clinical protocol is drafted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

