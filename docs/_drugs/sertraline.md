---
layout: default
title: Sertraline
parent: 僅模型預測 (L5)
nav_order: 714
evidence_level: L5
indication_count: 8
---

# Sertraline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sertraline: From Depression to Histrionic Personality Disorder

## One-Sentence Summary

> Sertraline (DrugBank DB01104) is a selective serotonin reuptake inhibitor (SSRI), internationally established for treating major depressive disorder and related mood/anxiety conditions; no Canada-specific indication is on file in this evidence pack because the product is currently **not marketed in Canada**.
> The TxGNN model predicts it may be effective for **Histrionic Personality Disorder**,
> with a score of **99.93%**, but this is supported by **0 clinical trials** and only **1 tangentially related publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Canada regulatory data (drug not marketed); internationally known as an SSRI for major depressive disorder and anxiety-spectrum conditions |
| Predicted New Indication | Histrionic Personality Disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✗ 未上市 (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known information, sertraline is an SSRI, a drug class whose serotonergic mechanism is well established in mood and anxiety disorders. It is plausible that serotonergic modulation could influence affective instability and impulsivity traits seen across personality disorders, which is the likely conceptual basis for this prediction.

However, the evidence pack does not contain any study that directly tests sertraline in histrionic personality disorder. The single retrieved publication (PMID 22075735) examines MMPI-2 neurotic-triad scores in depressed patients after pharmacological treatment — it is about depression symptom clusters, not histrionic personality disorder treatment outcomes, and its relevance classification is still "pending."

It is also worth noting that **six of the eight predicted indications in this pack are personality disorders (ranks 1–4, 7–8), all sharing an almost identical TxGNN score (~0.9993)**. This pattern suggests the model may be predicting sertraline's relevance to a broad "personality disorder" cluster rather than generating a specific, differentiated signal for histrionic personality disorder. By contrast, **agoraphobia (rank 6)** in this same pack is backed by multiple completed Phase 4 RCTs and dozens of publications — a substantially stronger evidence base that may deserve separate evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22075735](https://pubmed.ncbi.nlm.nih.gov/22075735/) | 2011 | Clinical study | Psychiatria Danubina | Examined MMPI-2 neurotic triad (hypochondria, depression, hysteria) subscale scores before/after pharmacological treatment in depressed inpatients; not specific to sertraline or to histrionic personality disorder as a treatment target |

---

## Canada Market Information

Currently no Health Canada authorizations (DINs) on file — the drug is not marketed in Canada (未上市, 0 total licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all listed as data gaps in this evidence pack; DG001 — missing TFDA/Health Canada label warnings and contraindications — is flagged as **Blocking**.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trials and only one weakly related publication support sertraline for histrionic personality disorder specifically; the near-identical TxGNN scores across six personality-disorder predictions suggest a low-specificity model signal rather than a differentiated hypothesis. Combined with the drug's non-marketed status in Canada and missing MOA/safety data, evidence is insufficient to advance.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain product label warnings/contraindications, e.g. via Health Canada or a comparable regulatory source, before any S1 safety screening
- Resolve DG002 (High): retrieve confirmed mechanism of action data from DrugBank
- Targeted literature/trial search specifically on sertraline in histrionic (or Cluster B/C) personality disorder, rather than depression-comorbidity studies
- Consider re-scoping toward **agoraphobia (rank 6)**, where this same evidence pack already shows multiple completed Phase 4 RCTs and a substantial published literature base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

