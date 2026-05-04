---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Bicalutamide is a non-steroidal antiandrogen that competitively blocks the androgen receptor (AR), originally used to treat prostate cancer.
The TxGNN model predicts it may be effective for **Hypertrichosis** (pathological excessive hair growth, including drug-induced forms),
with **0 clinical trials** and **1 publication** (a letter commenting on a retrospective review of 35 patients) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, bicalutamide is a non-steroidal androgen receptor antagonist primarily used in prostate cancer. Its efficacy in androgen-sensitive disease is well-established, and mechanistically it may be applicable to hypertrichosis driven by androgen-induced follicular activation.

Androgens promote hair follicle growth in androgen-sensitive regions via AR signaling. Minoxidil, a widely used treatment for hair loss, can paradoxically cause systemic hypertrichosis (excessive hair growth in non-target areas) as a dose-dependent side effect. By blocking AR, bicalutamide may reduce androgen-driven follicular hypersensitivity and attenuate this unwanted response — a plausible secondary pharmacological application.

Critically, this predicted use represents a **secondary indication** — managing a side effect of another drug rather than treating primary disease. Furthermore, the mechanistic rationale applies only to androgen-mediated hypertrichosis; genetic forms (such as Ambras syndrome or isolated hair shaft abnormalities, also appearing in this prediction list) have distinct, non-androgen-dependent pathways where AR blockade would not be expected to help.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Letter/Comment | Journal of the American Academy of Dermatology | Commentary on a retrospective review of 35 patients with female pattern hair loss, discussing bicalutamide's potential role in reducing minoxidil-induced hypertrichosis; not an original clinical study |

---

## Cytotoxicity

Bicalutamide meets the antineoplastic criteria: it is a first-line hormonal treatment for prostate cancer (androgen-sensitive malignancy) and belongs to the antiandrogen class of hormone therapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted hormonal therapy — Non-steroidal androgen receptor antagonist (not a conventional cytotoxic) |
| Myelosuppression Risk | Low — bicalutamide does not directly suppress bone marrow; hematological toxicity is not a primary concern |
| Emetogenicity Classification | Minimal — not associated with significant nausea or vomiting |
| Monitoring Items | Liver function tests (ALT/AST — hepatotoxicity risk), PSA (disease monitoring), blood glucose, complete blood count |
| Handling Protection | Standard oral medication precautions apply; bicalutamide is not classified as a hazardous cytotoxic agent requiring specialized chemotherapy handling |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The entire supporting evidence base consists of a single letter/commentary referencing a retrospective case series of 35 patients; no prospective or interventional studies exist for bicalutamide in hypertrichosis. This level of evidence (L4) is insufficient to advance the indication, particularly given that the proposed use is a secondary application — managing a side effect of another drug — rather than treating a primary pathological condition.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and full safety profile from DrugBank or published sources
- Package insert warnings and contraindications (currently a data gap; flagged as blocking for safety pre-screening)
- A prospective observational or small pilot study formally assessing bicalutamide for minoxidil-induced hypertrichosis in a defined population
- Risk-benefit assessment specific to the target population (typically women without prostate cancer), accounting for the systemic antiandrogen effects of bicalutamide in a non-oncology context
- Regulatory consultation on whether this constitutes an off-label use requiring a new indication filing or can be managed under compassionate/special access provisions

> **Note:** While hypertrichosis ranks first in the TxGNN prediction list, the Evidence Pack also contains a significantly higher-evidence prediction for **female breast carcinoma** (Rank 9, Evidence Level L2, 1 active Phase 2 trial + 20 publications, recommendation: *Proceed with Guardrails*). If the research objective is to identify the most actionable repurposing candidate from this dataset, breast cancer — specifically AR-positive triple-negative breast cancer (LAR subtype) — represents the far stronger and more clinically mature opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

