---
layout: default
title: Bromocriptine
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Bromocriptine
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

# Bromocriptine: From Hyperprolactinemia / Parkinson's Disease to Congenital Disorder of Glycosylation with Defective Fucosylation

---

## One-Sentence Summary

Bromocriptine is a dopamine D2/D3 receptor agonist with well-established clinical uses in hyperprolactinemia, Parkinson's disease, acromegaly, and type 2 diabetes, though no formal original indication is recorded in the current dataset for Canada.
The TxGNN model assigns its highest prediction score (99.83%) to **congenital disorder of glycosylation with defective fucosylation**, yet this direction is supported by **no clinical trials** and **no relevant literature** at this time.
All ten top-ranked predictions carry a **Hold** recommendation; the overall evidence base for repurposing bromocriptine into any of these predicted indications remains at exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not formally recorded in dataset (known uses include hyperprolactinemia, Parkinson's disease, acromegaly, type 2 diabetes) |
| Predicted New Indication | Congenital Disorder of Glycosylation with Defective Fucosylation |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on known pharmacology, bromocriptine is a dopamine D2/D3 receptor agonist (and serotonin 5-HT2C agonist) that suppresses prolactin secretion through pituitary dopaminergic pathways, reduces motor deficits in Parkinson's disease via striatal D2 stimulation, and modulates circadian insulin sensitivity in type 2 diabetes via hypothalamic dopaminergic signalling. These well-characterised mechanisms all converge on G-protein-coupled receptor activity in neuronal and neuroendocrine tissues.

Congenital disorder of glycosylation with defective fucosylation (CDG-IIc, also known as Leukocyte Adhesion Deficiency type II) is a rare autosomal recessive metabolic disease caused by loss-of-function mutations in *SLC35C1*, the gene encoding a Golgi GDP-fucose transporter. The result is a global deficiency of fucosylated glycoconjugates, affecting selectin-mediated leukocyte trafficking, Lewis blood group antigens, and multiple glycoprotein functions. There is **no known mechanistic connection** between dopamine D2/D3 receptor agonism and the fucose transport pathway; these biological domains are effectively orthogonal.

The high TxGNN score most likely reflects non-specific topological proximity within the knowledge graph — bromocriptine's nodes are densely connected to neurological and rare-disease nodes, which can inflate scores for mechanistically unrelated rare conditions. This prediction should be regarded as a graph artefact until independent wet-lab or in-silico mechanistic evidence is generated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bromocriptine in congenital disorder of glycosylation with defective fucosylation.

---

## Literature Evidence

Currently no related literature available for bromocriptine in congenital disorder of glycosylation with defective fucosylation.

---

## Canada Market Information

Bromocriptine is not currently marketed in Canada. No Drug Identification Numbers (DINs) are on file in the current dataset. The drug is approved and marketed in numerous other jurisdictions (United States, European Union, Japan) under brand names including Parlodel (hyperprolactinemia / Parkinson's disease) and Cycloset (type 2 diabetes).

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are available in the current dataset.

> **Note:** The absence of safety data is a blocking data gap (severity: Blocking) that prevents formal safety screening (Stage S1). Before any further development work, the full prescribing information should be retrieved from Health Canada or the FDA, with particular attention to cardiovascular warnings (hypotension, valvular disease), psychiatric adverse events (hallucinations, psychosis — especially relevant given dopaminergic mechanism), and fibrotic complications associated with long-term ergot alkaloid use.

---

## Noteworthy Signal from Other Predicted Indications

While the primary report focuses on the top-ranked TxGNN prediction, **schizophrenia** (rank 9, score 99.73%) carries the richest evidence in this pack — **3 clinical trials** and **20 publications** — and merits a brief flag:

| Trial | Phase | Status | Enrollment | Focus |
|-------|-------|--------|------------|-------|
| [NCT03575000](https://clinicaltrials.gov/study/NCT03575000) | Phase 4 | Not Yet Recruiting | 15 | Adjunct bromocriptine for antipsychotic-induced metabolic disturbances in schizophrenia |
| [NCT00315081](https://clinicaltrials.gov/study/NCT00315081) | Phase 3 | Unknown | 20 | Bromocriptine for risperidone-induced hyperprolactinemia in schizophrenia patients |
| [NCT04181385](https://clinicaltrials.gov/study/NCT04181385) | Phase 2/3 | Unknown | 15 | Lipid response to olanzapine (bromocriptine as comparator condition) |

⚠️ **Critical mechanistic conflict:** Bromocriptine is a D2 *agonist*, whereas virtually all effective antipsychotics are D2 *antagonists*. A published case report (PMID [8120934](https://pubmed.ncbi.nlm.nih.gov/8120934/)) documents new-onset schizophrenia *induced* by low-dose bromocriptine. The existing trials address metabolic side-effect management in schizophrenia patients, not direct antipsychotic efficacy. This indication is also rated **Hold** and carries a fundamental safety signal that would need to be resolved before any repurposing programme could proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (congenital disorder of glycosylation with defective fucosylation) rests on model prediction alone (L5 evidence) with no mechanistic, preclinical, or clinical support; all ten top-ranked indications across this evidence pack share a Hold recommendation, reflecting either absent evidence or unresolved safety signals (notably the dopamine agonist / antipsychotic mechanistic conflict for schizophrenia).

**To proceed, the following is needed:**

- **Mechanistic validation:** Establish whether any biological link exists between D2/D3 receptor agonism and SLC35C1-mediated fucose transport (e.g., transcriptomic or proteomic studies in CDG-IIc cell models)
- **MOA data:** Retrieve full mechanism of action from DrugBank API (data gap DG002) to enable rigorous mechanistic mapping across all predicted indications
- **Safety data:** Download and parse the TFDA/Health Canada/FDA package insert to extract warnings, contraindications, and DDI data (blocking data gap DG001)
- **Indication re-prioritisation:** Consider generating a supplementary report focused on the **retinal dystrophy** indication (rank 3, L4), which has one directly relevant pre-clinical repurposing study (PMID [39009597](https://pubmed.ncbi.nlm.nih.gov/39009597/), 2024) describing a GPCR-modulating combination therapy including bromocriptine in retinopathy animal models — this represents the most mechanistically credible signal in the dataset
- **Canada regulatory pathway:** Confirm whether Health Canada holds any historical DIN records for bromocriptine (the dataset may be incomplete) and clarify the regulatory pathway for a new indication filing

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-05.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

