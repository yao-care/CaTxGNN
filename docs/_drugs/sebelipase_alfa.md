---
layout: default
title: Sebelipase Alfa
parent: 僅模型預測 (L5)
nav_order: 706
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

# Sebelipase Alfa: From Lysosomal Acid Lipase Deficiency to Scheie Syndrome

## One-Sentence Summary

> Sebelipase alfa (Kanuma) is a recombinant human lysosomal acid lipase (LAL) enzyme replacement therapy, well established for treating **Lysosomal Acid Lipase Deficiency** (LAL-D, covering both Wolman disease and Cholesteryl Ester Storage Disease).
> The TxGNN model's top-ranked new prediction is **Scheie syndrome**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the underlying enzyme defect is unrelated to LAL — this prediction should be treated as unvalidated model output rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lysosomal Acid Lipase Deficiency (LAL-D; Wolman disease / Cholesteryl Ester Storage Disease) — derived from literature, not from Canadian regulatory filings (drug is not marketed in Canada) |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| Canada Market Status | 未上市 (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for sebelipase alfa is not available in this evidence pack (Data Gap). Based on literature evidence collected under other candidate indications in this pack, sebelipase alfa is a recombinant human lysosomal acid lipase that replaces deficient LAL enzyme activity, reducing lysosomal accumulation of cholesteryl esters and triglycerides in patients with LAL-D.

Scheie syndrome is a mild form of Mucopolysaccharidosis type I (MPS I), caused by deficiency of **alpha-L-iduronidase**, an enzyme involved in glycosaminoglycan degradation — a completely different substrate and metabolic pathway from the cholesteryl ester/triglyceride pathway acted on by LAL. There is no shared molecular target, no shared pathway, and no cross-reactivity mechanism that would support sebelipase alfa having activity in Scheie syndrome.

The evidence pack's own annotation for this candidate states directly: *"MPS I 輕型，缺陷酵素同 Hurler syndrome（alpha-L-iduronidase），與 LAL 無關。無任何臨床或文獻證據，純屬 TxGNN 預測分數"* — i.e., the high TxGNN score likely reflects a knowledge-graph feature confound (e.g., both diseases being categorized as "lysosomal storage disorders") rather than a real pharmacological relationship. This is a case of model score without mechanistic or empirical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Sebelipase alfa is **not currently marketed in Canada** (0 licenses/DINs on file). No Canadian product listing or approved-indication text is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Health Canada label warnings and contraindications are flagged as a Blocking data gap (DG001) in this evidence pack — this must be resolved before any safety-stage evaluation (S1) can proceed.)*

---

## Additional Note: Other Candidates in This Evidence Pack

For transparency, the strongest clinical/literature evidence in this evidence pack (multiple completed Phase 2/3 RCTs, an FDA-approval-supporting literature base of ~15–20 publications) attaches to **Cholesteryl Ester Storage Disease (rank 4)** and **Wolman disease (rank 5)** — but these are not novel repurposing candidates: they are the drug's **already-approved indications** (sebelipase alfa/Kanuma is globally approved for LAL-D, which includes both phenotypes). The model is correctly re-identifying known efficacy rather than surfacing a new therapeutic direction.

The remaining candidates (Hurler syndrome, Gaucher disease, Tay-Sachs disease, adrenal adenoma, etc.) are annotated in the evidence pack itself as mechanistically unrelated to LAL (different deficient enzymes/pathways) and are considered TxGNN prediction noise, likely arising from shared "lysosomal storage disease" category features in the knowledge graph rather than true drug-disease relationships.

**Conclusion: no genuine, evidence-supported new repurposing indication for sebelipase alfa is present in this evidence pack.**

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Scheie syndrome) has zero clinical or literature support and a mechanistically implausible rationale (different deficient enzyme/pathway than LAL). None of the 10 ranked candidates in this pack represent a credible novel repurposing opportunity — the only candidates with strong evidence (CESD, Wolman disease) are the drug's existing approved indications, not new ones.

**To proceed, the following is needed:**
- TFDA/Health Canada product label (warnings, contraindications) — currently a Blocking data gap (DG001)
- Verified mechanism-of-action data from DrugBank (DG002)
- If repurposing evaluation is to continue for this drug, re-run/re-rank TxGNN predictions with mechanistic filtering to exclude "lysosomal storage disease" category confounds, or manually screen lower-ranked candidates for genuine LAL-pathway overlap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

