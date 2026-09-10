---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 443
evidence_level: L5
indication_count: 2
---

# Lansoprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Lansoprazole: From Acid-Related GI Disorders (PPI Class) to Duodenogastric Reflux

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor (PPI); the evidence pack does not contain a confirmed Taiwan/Canada original indication record, but class-level literature in this pack describes PPIs as first-line therapy for peptic ulcer disease, H. pylori infection, GERD, and NSAID-associated GI lesions. The TxGNN model predicts potential relevance to **Duodenogastric Reflux (DGR)**, but this is currently supported only by **0 clinical trials** and **2 publications** — one of which is a preclinical study suggesting a possible carcinogenesis risk signal rather than efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (original_indications is empty; taiwan_regulatory has no license records). Per PPI-class literature in this pack, typical indications include peptic ulcer, GERD, and H. pylori eradication. |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Lansoprazole in this evidence pack (flagged as a High-severity data gap, DG002). Based on known information, Lansoprazole is a proton pump inhibitor (PPI) that irreversibly inhibits the gastric parietal cell H⁺/K⁺-ATPase to suppress acid secretion — a functional (secretory) mechanism rather than a structural one.

Duodenogastric reflux (DGR) involves reflux of duodenal contents (bile and pancreatic secretions) into the stomach, mixed with variable degrees of acid-related symptoms. PPIs can reduce the acid component of mixed reflux, but they do not neutralize bile or pancreatic enzymes, which are the primary pathogenic agents in DGR. This limits the mechanistic plausibility of the prediction.

More importantly, the literature evidence available in this pack does not support a therapeutic benefit signal: one animal study (PMID 15052437) found that lansoprazole *promoted* gastric carcinogenesis in a rat model of induced duodenogastric reflux, raising a potential safety concern rather than demonstrating efficacy. The second reference (PMID 18679668) is a general PPI review with no direct DGR data. Overall, the mechanistic rationale is weak and is accompanied by a preclinical risk signal, consistent with the model's own "Hold" recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General PPI class review — PPIs are first-line for peptic ulcer, H. pylori infection, GERD, NSAID-induced GI lesions, and Zollinger-Ellison syndrome; no specific DGR data. |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal Study | Gastric Cancer | In a rat model of induced duodenogastric reflux, lansoprazole promoted gastric carcinogenesis — a preclinical safety signal, not evidence of therapeutic benefit. |

---

## Canada Market Information

Lansoprazole currently has **0 active DINs** and is recorded as **Not Marketed** in this dataset — no license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Health Canada label warnings/contraindications are marked as a Blocking data gap (DG001) in this evidence pack — this must be resolved before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 (preclinical/mechanistic only) with zero clinical trials, a mechanistically weak link between PPI action and DGR pathophysiology, and an existing preclinical signal suggesting increased gastric carcinogenesis risk rather than benefit in the DGR context.

**To proceed, the following is needed:**
- Health Canada/TFDA label warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action data from DrugBank (DG002, High)
- Human clinical or observational data specific to duodenogastric reflux
- Follow-up or mechanistic studies to clarify the gastric carcinogenesis signal seen in PMID 15052437 before any further development consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

