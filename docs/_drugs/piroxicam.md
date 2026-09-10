---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 626
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: From Adult Inflammatory Arthritis to Juvenile Idiopathic Arthritis

## One-Sentence Summary

Piroxicam is an oxicam-class NSAID with a long history of use in adult inflammatory arthritis, though the specific Health Canada-approved indication text is not present in this evidence pack. Among the ten TxGNN-predicted indications reviewed, **Juvenile Idiopathic Arthritis (JIA)** is the only one backed by real clinical and literature evidence — **13 publications**, including two historical randomized controlled trials of piroxicam itself in pediatric arthritis — while TxGNN's top four ranked candidates (ultra-rare skeletal dysplasia syndromes) have **zero** supporting evidence and are explicitly flagged in the model output as likely knowledge-graph artifacts.

> **Note on candidate selection**: This report does not follow `predicted_indications[0]` (colobomatous microphthalmia-rhizomelic dysplasia syndrome). That prediction, and ranks 2–8, carry near-identical top-tier TxGNN scores (~99.99%) but zero clinical trials, zero literature, and no plausible mechanistic link to an NSAID — the pack's own `repurposing_rationale` describes these as probable embedding bias from sparse rare-disease nodes. Juvenile Idiopathic Arthritis (rank 10) is the only candidate with converging real-world evidence and biological plausibility, so it is used as the subject of this evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (piroxicam is an oxicam NSAID; no Canada-approved indication text on file — market status is "not marketed") |
| Predicted New Indication | Juvenile Idiopathic Arthritis |
| TxGNN Prediction Score | 99.93% (rank 1992 of full disease list) |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, piroxicam belongs to the oxicam class of nonsteroidal anti-inflammatory drugs (NSAIDs), which act via inhibition of cyclo-oxygenase (COX) enzymes to reduce prostaglandin-mediated inflammation and pain. Its efficacy in adult inflammatory joint disease is well established in the literature, and mechanistically this same anti-inflammatory pathway is directly applicable to pediatric inflammatory joint disease.

Juvenile Idiopathic Arthritis is, pathophysiologically, the pediatric counterpart of the adult inflammatory arthritides piroxicam already treats — both involve synovial inflammation driven by prostaglandin and cytokine pathways. This is not a novel repurposing hypothesis: piroxicam has been studied in children with juvenile (rheumatoid/chronic) arthritis since the 1980s, including head-to-head randomized comparisons against naproxen (PMID 2957205, PMID 3510686) and dedicated pediatric pharmacokinetic characterization (PMID 1782984). Two recent systematic reviews and network meta-analyses (2021, 2024) continue to evaluate piroxicam alongside other NSAIDs specifically for JIA, indicating sustained clinical interest despite the drug's age.

The main caveat is piroxicam's known long half-life (~50 hours in adults) and higher GI/renal toxicity signal relative to newer NSAIDs — a consideration that will need formal safety data (currently a blocking gap) before this candidate can advance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | RCT | British Journal of Rheumatology | Multicentre double-blind cross-over trial (n=47) comparing piroxicam vs. naproxen in juvenile chronic arthritis; no significant difference in efficacy |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | RCT | European Journal of Rheumatology and Inflammation | Randomized trial (n=26) of piroxicam vs. naproxen in juvenile rheumatoid arthritis; significant reduction in painful/swollen joints |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Systematic Review/Network Meta-analysis | World Journal of Clinical Cases | Network meta-analysis comparing NSAIDs (including piroxicam) for JIA to identify optimal treatment |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Systematic Review/Network Meta-analysis | Indian Pediatrics | Comparative efficacy/safety of nine NSAIDs in JIA patients |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | PK Study | European Journal of Clinical Pharmacology | Steady-state pharmacokinetics of piroxicam (0.4 mg/kg once daily) in 10 children with rheumatic disease |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Review | Kinderärztliche Praxis | Reviews drug therapy for juvenile chronic arthritis, discussing piroxicam among newer agents |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Observational/Cohort | Clinical Rheumatology | Long-term toxicity of antirheumatic/anti-inflammatory drugs (incl. NSAIDs) in a pediatric rheumatology cohort |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Case Series | International Ophthalmology | Frequency of chronic iridocyclitis (ocular complication) in ANA-positive pauciarticular JCA patients |
| [15456329](https://pubmed.ncbi.nlm.nih.gov/15456329/) | 2004 | Review | Drugs | Review of nabumetone (comparator NSAID) therapeutic use and safety in arthritis management |
| [6753142](https://pubmed.ncbi.nlm.nih.gov/6753142/) | 1982 | Review | Schweizerische Medizinische Wochenschrift | General review of newer NSAIDs' efficacy/tolerability, prescribing guidance |

---

## Canada Market Information

Piroxicam currently has no marketed products in Canada — 0 DINs on file (`market_status: 未上市` / not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: warnings, contraindications, and drug-drug interaction data for this evidence pack were not retrievable (query status: not found) and are logged as a **Blocking** data gap (DG001), which prevents entry into the Stage 1 safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The literature provides reasonable biological plausibility and decades of historical off-label pediatric use supporting piroxicam in JIA, but the candidate cannot advance because (a) piroxicam has no current Canadian market authorization (0 DINs), and (b) label-level safety data (warnings, contraindications, DDI) is a Blocking gap that prevents any safety pre-assessment.

**To proceed, the following is needed:**
- Health Canada product monograph / TFDA label data — warnings, contraindications, DDI (DG001, Blocking)
- Confirmed mechanism of action and original approved indication from DrugBank (DG002, High)
- Formal classification (RCT/systematic review/case-series tiering) of the 13 JIA literature records, currently unclassified ("pending")
- Modern reassessment of piroxicam's GI/renal/hepatic toxicity profile in a pediatric population, given its long half-life relative to newer NSAIDs used in current JIA guidelines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

