---
layout: default
title: Megestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Megestrol Acetate
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

# Megestrol Acetate: From Breast Cancer to Uterine Corpus Endometrial Carcinoma

## One-Sentence Summary

Megestrol Acetate is a synthetic progestogen globally recognized for the treatment of breast cancer and cancer-related anorexia/cachexia, but is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Uterine Corpus Endometrial Carcinoma**, with **3 clinical trials** currently supporting this direction.
Detailed mechanism of action data and Canadian package insert information are not yet available, representing key data gaps that must be resolved before formal development can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Health Canada approvals on record (not marketed in Canada) |
| Predicted New Indication | Uterine Corpus Endometrial Carcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, Megestrol Acetate belongs to the synthetic progestogen class and acts as a progesterone receptor (PR) agonist. It directly binds to PR — which is highly expressed in normal endometrial tissue and in the majority of low-grade endometrial cancers — thereby inhibiting cancer cell proliferation and promoting cellular differentiation. At higher doses, it also suppresses pituitary LH secretion, which in turn reduces ovarian estrogen production, an established driver of endometrial cancer growth.

The predicted indication, uterine corpus endometrial carcinoma, is in fact the most globally studied oncological application of megestrol acetate. Multiple regulatory agencies outside Canada have approved or recognized progestogen therapy for this indication. The mechanistic link is direct and well-characterized: endometrial carcinomas that overexpress PR are biologically susceptible to progestogen-mediated growth suppression, making megestrol a mechanistically rational first-line hormonal option — particularly for patients with Grade 1 endometrioid histology who wish to preserve fertility.

The TxGNN model's 99.94% confidence score therefore reflects both strong biological plausibility and a broad supporting knowledge graph. That the drug is currently not marketed in Canada does not diminish its applicability; rather, it signals a regulatory gap where an internationally validated therapy has yet to be registered locally.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Randomized trial comparing temsirolimus alone versus temsirolimus plus hormonal therapy (megestrol acetate + tamoxifen citrate) in women with advanced, persistent, or recurrent endometrial carcinoma; directly evaluates megestrol-containing combination hormonal therapy in this population |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | Unknown | 60 | Compares PD-1 inhibitor combined with progesterone versus progesterone alone for fertility-sparing treatment of early-stage endometrial cancer; progesterone arm includes agents mechanistically identical to megestrol acetate |
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | Terminated | 9 | Directly evaluated continuous versus sequential megestrol acetate therapy in patients with endometrial intraepithelial neoplasia (EIN) or atypical endometrial hyperplasia wishing to preserve the uterus; mechanistic rationale fully aligned, but terminated early due to insufficient enrollment |

---

## Literature Evidence

Currently no related literature available for uterine corpus endometrial carcinoma in the current evidence pack.

---

## Canada Market Information

Megestrol Acetate (DrugBank ID: DB00351) is not currently approved or marketed in Canada. No Drug Identification Numbers (DINs) are on record with Health Canada. There are no licensed products, dosage forms, or approved indications available for this drug in the Canadian regulatory database.

---

## Cytotoxicity

Megestrol Acetate is used as a hormonal antineoplastic agent for the treatment of hormone receptor-positive cancers. It is **not** a conventional cytotoxic drug; it belongs to the progestogen (hormonal therapy) class.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal / Endocrine therapy (Progestogen class) — not a conventional cytotoxic agent; classified as antineoplastic via hormonal mechanism |
| Myelosuppression Risk | Low — hormonal mechanism of action is not associated with clinically significant myelosuppression |
| Emetogenicity Classification | Minimal — oral progestogens are not associated with significant nausea or vomiting at standard doses |
| Monitoring Items | Body weight and fluid retention (glucocorticoid-like effects at high doses), fasting blood glucose (risk of hyperglycemia), adrenal function tests (secondary adrenal suppression reported with high-dose and prolonged use), coagulation parameters (increased thromboembolic risk) |
| Handling Protection | Standard medication handling precautions; dedicated cytotoxic drug handling facilities are not typically required for oral hormonal agents |

---

## Safety Considerations

Please refer to the package insert for safety information. Note: As megestrol acetate is not currently approved by Health Canada, no Canadian package insert is available. Prescribers and regulators should refer to the US FDA label (NDA 016267 / NDA 019559) or equivalent international monographs for warnings, contraindications, and drug interaction information pending local approval.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case for megestrol acetate in uterine corpus endometrial carcinoma is strong and globally well-validated; a completed Phase 2 randomized trial directly testing megestrol-containing hormonal therapy in this indication provides Level 2 evidence, and the drug has received regulatory recognition for this use outside Canada. The primary barriers are a regulatory gap in Canada, missing safety data, and incomplete MOA documentation — none of which undermine biological plausibility.

**To proceed, the following is needed:**
- Retrieve mechanism of action and pharmacology data from DrugBank API (DB00351) to complete the mechanistic linkage analysis
- Download and parse the TFDA or FDA package insert to complete safety screening (key warnings, contraindications, drug–drug interactions) — currently a blocking data gap
- Document existing international regulatory approvals for endometrial carcinoma (FDA, EMA, PMDA) to support a Health Canada New Drug Submission or evidence-based formulary access request
- Conduct a supplementary literature search specifically targeting completed Phase 2/3 megestrol acetate trials in endometrial carcinoma (the PubMed query for this indication returned zero results, suggesting the search strategy may require expansion)
- Assess PR expression prevalence and patient selection criteria relevant to the Canadian population (e.g., Grade 1–2 endometrioid, PR-positive tumors) to define the target indication precisely
- Note: TxGNN rank 8 (ovarian cancer) carries Level L1 evidence with 6 clinical trials and 20 publications, including multiple high-dose Phase 2 studies — this indication warrants a parallel evaluation as a secondary development candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

