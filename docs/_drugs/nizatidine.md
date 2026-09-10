---
layout: default
title: Nizatidine
parent: 僅模型預測 (L5)
nav_order: 559
evidence_level: L5
indication_count: 7
---

# Nizatidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Nizatidine: From Peptic Ulcer Disease (H2-Antagonist Class Use) to Active Peptic Ulcer Disease

## One-Sentence Summary

Nizatidine is a histamine H2-receptor antagonist historically used to treat duodenal and gastric ulcer disease. The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**, with **0 clinical trials** and **19 publications** currently supporting this direction — though as detailed below, this largely reflects the drug's already-established original activity rather than a novel repurposing hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Canada license record exists (drug not marketed); historically indicated for duodenal ulcer, benign gastric ulcer, and GERD as an H2-receptor antagonist |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned from the DrugBank query (data gap DG002, high severity). Based on known pharmacological classification, Nizatidine belongs to the H2-receptor antagonist class alongside ranitidine, cimetidine, and famotidine. It competitively inhibits histamine at parietal cell H2 receptors, suppressing basal, nocturnal, and stimulated gastric acid secretion.

Active peptic ulcer disease (duodenal and gastric ulcer) is precisely the therapeutic area this drug class was developed for. The literature evidence below — spanning 1987 to 1997 — consists largely of the original registrational and comparative trials that established nizatidine's efficacy in duodenal and gastric ulcer healing and maintenance.

Importantly, the model's own rationale for this candidate states this explicitly: nizatidine's acid-suppressing action on peptic ulcer disease is an **already-established mechanism**, not a novel repurposing hypothesis — it falls within the drug's original approved indication scope. The primary evidence gap here is not mechanistic plausibility but Canada market presence: the drug currently holds zero DINs and is not marketed, so this evidence pack should be read as validating historical efficacy rather than surfacing a new therapeutic use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2570656](https://pubmed.ncbi.nlm.nih.gov/2570656/) | 1989 | RCT | Clinical Pharmacology and Therapeutics | Two-phase, placebo-controlled, randomized, double-blind trial: 150 mg nizatidine BID vs placebo for active duodenal ulcer healing over 4–8 weeks |
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clinical Pharmacology and Therapeutics | 8-week multicenter RCT comparing 150 mg BID and 300 mg qhs nizatidine vs placebo in active benign gastric ulcer healing and symptom relief |
| [2892259](https://pubmed.ncbi.nlm.nih.gov/2892259/) | 1987 | RCT | Scandinavian Journal of Gastroenterology, Suppl | 1-year randomized maintenance trial (n=513): nizatidine 150 mg qhs vs placebo; recurrence rates 34% vs 64% at 12 months |
| [9198292](https://pubmed.ncbi.nlm.nih.gov/9198292/) | 1997 | RCT | Chinese Medical Journal | Randomized trial of clarithromycin-based H. pylori eradication combination therapy in peptic ulcer disease |
| [1982108](https://pubmed.ncbi.nlm.nih.gov/1982108/) | 1990 | RCT | Hepato-gastroenterology | 8-week randomized, double-blind comparison of nizatidine (150 mg BID or 300 mg qhs) vs ranitidine 150 mg BID in gastric ulcer, similar healing rates |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Early pharmacodynamic/pharmacokinetic review establishing nizatidine as a potent inhibitor of basal, nocturnal, and stimulated gastric acid secretion |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterology Clinics of North America | Overview of peptic ulcer medical therapy positioning nizatidine among H2 antagonists as safe and effective, without novel clinical advantage |
| [8097411](https://pubmed.ncbi.nlm.nih.gov/8097411/) | 1993 | Review | Bailliere's Clinical Gastroenterology | Mechanistic review of neural, hormonal, and paracrine regulation of gastric acid secretion underlying H2-antagonist action |
| [7960687](https://pubmed.ncbi.nlm.nih.gov/7960687/) | 1994 | Cohort | Israel Journal of Medical Sciences | Double-blind RCT (n=55) evaluating nizatidine's effect on duodenal ulcer healing and mucosal inflammatory mediators |
| [1974318](https://pubmed.ncbi.nlm.nih.gov/1974318/) | 1990 | Cohort | Medicina (Florence) | Comparative pharmacodynamic study of nizatidine vs misoprostol on gastric pH, pepsin, and mucus parameters in duodenal ulcer patients |

## Canada Market Information

Nizatidine is not currently marketed in Canada — no DIN records or product authorizations exist in the evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple historical RCTs (L1 evidence) robustly support H2-antagonist efficacy in active peptic ulcer disease, but this reflects nizatidine's original approved mechanism of action rather than a genuinely novel repurposing signal. Combined with zero current Canada market presence, this candidate needs regulatory and safety groundwork before any local development decision.

**To proceed, the following is needed:**
- Health Canada product monograph / label warnings and contraindications (blocking gap DG001 — required before safety pre-assessment can proceed)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Clarification of whether local (Canada) market entry is being considered, since no DIN currently exists
- An assessment of whether this candidate offers incremental value over already-marketed H2 antagonists, given the overlap with nizatidine's known original use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

