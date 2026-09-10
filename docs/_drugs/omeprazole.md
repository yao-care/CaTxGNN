---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 581
evidence_level: L5
indication_count: 2
---

# Omeprazole
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

# Omeprazole: From Acid-Related Gastrointestinal Disorders to Duodenogastric Reflux

## One-Sentence Summary

Omeprazole is a proton pump inhibitor (PPI) established for acid-related gastrointestinal conditions such as GERD, peptic ulcer disease, and Barrett's esophagus. The TxGNN model predicts a possible new application in **Duodenogastric Reflux (DGR)**, but this signal is currently supported by only **1 indirectly-related clinical trial** and **20 publications**, several of which show conflicting effects (some protective, some raising a carcinogenesis-promotion concern).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack — omeprazole is not currently marketed in Canada under this record, so no approved indication text is available |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Omeprazole is a PPI that irreversibly inhibits the H⁺/K⁺-ATPase (proton pump) in gastric parietal cells, reducing gastric acid secretion. Its mechanistic link to Duodenogastric Reflux (DGR) is indirect: DGR is primarily driven by retrograde bile flow from the duodenum into the stomach, not by acid secretion itself, so omeprazole does not directly target the underlying valve/motility dysfunction that causes DGR.

The supporting literature is mixed in direction. Several small clinical studies in Barrett's esophagus populations (e.g., PMIDs 10994616, 9824338) report that omeprazole reduces DGR-related reflux parameters, suggesting a plausible symptomatic benefit through indirect pH-mediated effects on the refluxate. However, other animal studies (PMIDs 33027361, 10389684) suggest that acid blockade with omeprazole may *potentiate* DGR-induced gastric carcinogenesis by altering gastric pH and mucosal growth signaling — a directionally opposite and clinically important safety signal.

Given this, the prediction is mechanistically plausible only as a secondary/adjunctive effect of acid suppression rather than a primary treatment mechanism for DGR, and the evidence base is preclinical/small-cohort in nature with an unresolved safety question. This is consistent with the model's own evidence-level classification of L4 (preclinical/mechanism-level evidence) and a mid-range TxGNN rank (7,327), indicating this indication is not among the model's most specific or confident predictions despite the high raw score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | NA | Completed | 157 | Diagnostic imaging study (endoscopic tri-modal imaging) to distinguish functional dyspepsia from reflux disease (acid or bile). Not an omeprazole interventional trial — only indirectly relevant (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | RCT | Scandinavian Journal of Gastroenterology | Omeprazole reduced antral duodenogastric reflux in Barrett's esophagus patients |
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | RCT | Gut | Omeprazole 20mg twice daily assessed for effect on duodenogastric and duodenogastro-oesophageal bile reflux in Barrett's esophagus |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Cohort | European Journal of Pediatrics | Primary DGR documented in children/adolescents via 24h gastric bilimetry, unresponsive to classical antacid therapy |
| [11552908](https://pubmed.ncbi.nlm.nih.gov/11552908/) | 2001 | Cohort | Alimentary Pharmacology & Therapeutics | PPI therapy (pantoprazole) decreases acid reflux but effect on biliary reflux and motility remains unclear |
| [21916229](https://pubmed.ncbi.nlm.nih.gov/21916229/) | 2011 | Cohort | Experimental & Clinical Gastroenterology | DGR characteristics in duodenal ulcer patients and dynamics after H. pylori eradication |
| [9841990](https://pubmed.ncbi.nlm.nih.gov/9841990/) | 1998 | Cohort | Journal of Gastrointestinal Surgery | Bile reflux implicated in malignant degeneration of Barrett's esophagus; effect of acid suppression and fundoplication studied |
| [8076761](https://pubmed.ncbi.nlm.nih.gov/8076761/) | 1994 | Cohort | Gastroenterology | Duodenogastroesophageal reflux relationship to pH and role in Barrett's esophagus pathogenesis |
| [11232672](https://pubmed.ncbi.nlm.nih.gov/11232672/) | 2001 | Cohort | American Journal of Gastroenterology | Increased acid and bile reflux found in Barrett's esophagus vs. reflux esophagitis; PPI therapy effect assessed |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Animal study | Acta Cirúrgica Brasileira | Investigated whether omeprazole is protective against gastric adenocarcinoma in rats with induced DGR |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Animal study | Digestive Diseases and Sciences | Gastric acid blockade with omeprazole found to **promote** gastric carcinogenesis induced by DGR in rats — a safety-relevant conflicting signal |

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note on evidence-derived safety signal:** Beyond the formal safety dataset (which contains no populated warnings, contraindications, or DDI data), two animal studies in the literature evidence above (PMIDs 33027361, 10389684) raise an unresolved question about whether long-term acid suppression with omeprazole could promote — rather than prevent — DGR-related gastric carcinogenesis. This should be explicitly evaluated before any further development.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 (preclinical/mechanism-level), decision stage is S1, and there is a **Blocking** data gap (DG001: TFDA/label warnings and contraindications) that prevents even an initial safety screen (S1). The clinical literature is also directionally inconsistent — some studies suggest benefit, while others suggest omeprazole may promote DGR-associated gastric carcinogenesis — so the signal cannot currently support progression.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications before any S1 safety screening
- Resolve DG002 (High): confirm mechanism of action detail specific to DGR applicability, not just general PPI pharmacology
- A dedicated interventional trial (not diagnostic-imaging studies) evaluating omeprazole specifically for DGR as a primary endpoint
- Clarification of the conflicting carcinogenesis-promotion signal from animal studies (PMIDs 33027361, 10389684) before any clinical advancement
- Canada market/regulatory pathway assessment, since the drug currently has no active Canadian licenses (0 DINs) under this record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

