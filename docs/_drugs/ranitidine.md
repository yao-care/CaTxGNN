---
layout: default
title: Ranitidine
parent: 僅模型預測 (L5)
nav_order: 667
evidence_level: L5
indication_count: 10
---

# Ranitidine
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

# Ranitidine: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Ranitidine (DrugBank DB00863) is a histamine H2-receptor antagonist with a long, well-established history of use in acid-related gastrointestinal disease. TxGNN's top-ranked prediction, **Active Peptic Ulcer Disease**, is supported by **1 clinical trial** and **19 publications**, but the evidence itself indicates this is largely ranitidine's classic, already-approved use rather than a genuinely novel indication — a caveat that materially affects how this candidate should be interpreted.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the evidence pack (drug.original_indications is empty, no Canadian license text available). Ranitidine is historically an H2-receptor antagonist used for peptic ulcer disease and related acid-secretory conditions — noted directly in the evidence rationale text, not confirmed by a regulatory source. |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002, High severity). Based on the literature captured in this evidence pack, ranitidine is a competitive, selective histamine H2-receptor antagonist that suppresses basal and stimulated gastric acid secretion (PMID 6317325, 6317740). Its efficacy in duodenal and gastric ulcer healing has been established through numerous 1980s–1990s randomized trials (PMID 3909374, 3104657, 2491360).

Mechanistically, "active peptic ulcer disease" is not a distinct pharmacological target from ranitidine's original acid-suppression indication — it is the same disease process at an active stage. The evidence pack's own rationale for this candidate states this explicitly: ranitidine is "a classic approved drug for this indication" with multiple healing trials from the 1980s–90s already establishing efficacy. This means the TxGNN score here largely reflects a **known, approved use** rather than a novel repurposing signal. Reviewers should treat this less as "new indication discovery" and more as a documented efficacy confirmation.

For a more genuine repurposing signal from the same evidence pack, rank 6 (**gastroduodenitis**, L2 evidence, decision stage S1) is notable: multiple controlled studies show ranitidine protects against NSAID- and procedure-induced gastroduodenal mucosal injury — a related but mechanistically distinguishable use from classic ulcer healing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated the effect of various PPIs (not ranitidine directly) and statins on clopidogrel antiplatelet activity in PCI patients; relevance graded C — the drug/disease link to ranitidine and active PUD is indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | RCT | Klinische Wochenschrift | Compared nocturnal rioprostil (prostaglandin E1 analogue) vs ranitidine 300mg for duodenal ulcer healing. |
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | Ranitidine 300mg/day in 151 patients with duodenal, prepyloric, and gastric corporeal ulcers; healing rates 68–91% at 4 weeks; maintenance therapy reduced relapse. |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intelligence & Clinical Pharmacy | Early review establishing ranitidine as 4–10x more potent than cimetidine in inhibiting gastric acid secretion for active duodenal ulcer and hypersecretory states. |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepato-gastroenterology | Reviews acid suppression as central to peptic ulcer healing pathogenesis, contextualizing H2-antagonist efficacy including ranitidine. |
| [2905237](https://pubmed.ncbi.nlm.nih.gov/2905237/) | 1988 | Review | Drugs | Reviews prostaglandins and H2-receptor antagonists (including ranitidine) in peptic ulcer disease pathophysiology and treatment. |
| [9506245](https://pubmed.ncbi.nlm.nih.gov/9506245/) | 1998 | Unclassified | Drugs | Review of rabeprazole (PPI) benchmarked against H2-antagonists including ranitidine in comparative ulcer-healing trials. |
| [8736619](https://pubmed.ncbi.nlm.nih.gov/8736619/) | 1996 | Unclassified | Drugs | Reviews ebrotidine, an H2-antagonist with antisecretory potency described as similar to ranitidine and ~10x cimetidine. |
| [3527658](https://pubmed.ncbi.nlm.nih.gov/3527658/) | 1986 | Unclassified | Drugs | Preliminary review of omeprazole pharmacodynamics/kinetics in peptic ulcer disease, positioning it against H2-antagonist therapy. |
| [1717223](https://pubmed.ncbi.nlm.nih.gov/1717223/) | 1991 | Unclassified | Drugs | Review of roxatidine acetate (H2-antagonist) therapeutic potential in peptic ulcer disease, comparator class to ranitidine. |
| [34986535](https://pubmed.ncbi.nlm.nih.gov/34986535/) | 2021 | Unclassified | J Zhejiang Univ Med Sci | Preclinical study of a plant-derived agent (not ranitidine) against ethanol-induced gastric ulcer; included as topically related mechanism literature. |

---

## Canada Market Information

Ranitidine currently has **no active Health Canada market authorization** (market status: Not Marketed; 0 DINs on file). No license records were returned to populate a product table.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not available in this evidence pack (Data Gap DG001, flagged as Blocking — required before any S1 safety pre-assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the evidence level for active peptic ulcer disease is L1 (multiple completed RCTs), the underlying trials establish ranitidine's efficacy in its *classic, already-recognized* ulcer indication rather than a genuinely novel repurposing target — and the drug is not currently marketed in Canada. Combined with a Blocking data gap on safety labeling, this candidate cannot advance past initial screening as currently framed.

**To proceed, the following is needed:**
- TFDA/Health Canada product labeling (warnings, contraindications) — currently Blocking (DG001)
- DrugBank mechanism of action detail — currently High severity gap (DG002)
- Clarification of whether "active peptic ulcer disease" should be scored as a novel repurposing candidate or reclassified as confirmatory evidence for an existing indication
- If pursuing GI repurposing signals from this drug, prioritize evaluation of the gastroduodenitis candidate (rank 6, L2 evidence), which shows a more mechanistically distinct extension (NSAID/procedural mucosal protection) than the top-ranked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

