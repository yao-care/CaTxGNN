---
layout: default
title: Etafedrine
parent: Moderate Evidence (L3-L4)
nav_order: 358
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-30
description: "Etafedrine: predicted new indication Bronchitis (evidence level L5). Approved use: Not available"
monitor_inn: "Etafedrine"
predicted_indications: ["bronchitis"]
---

# Etafedrine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Etafedrine: From an Unspecified Original Indication to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Etafedrine is a beta-adrenergic bronchodilator (an ephedrine derivative). The indication listed on its Canadian license is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **bronchitis**, with **0 registered clinical trials** and **2 publications** (both older studies of multi-ingredient combination products) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the Canadian license record contains no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L3 (low-quality; see note below) |
| Canada Market Status | Approved but not marketed (approvals on record: 1) |
| Number of DINs | 1 (valid: 0) |
| Recommended Decision | Hold |

*Evidence level note:* Neither publication tests etafedrine alone. Both evaluated fixed-dose combination products. Strictly under the level rules, this is closer to L5 or L4 for etafedrine itself. The L3 label is retained from the source scoring, and the evidence should be read as weak and indirect.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known drug class information, etafedrine is an ephedrine-derived beta-adrenergic agonist with bronchodilator activity. This mechanism has not been confirmed against a DrugBank annotation.

Bronchitis, especially the chronic form, often involves airway narrowing and bronchospasm. Beta-2 receptor-mediated relaxation of airway smooth muscle could plausibly relieve these symptoms. This is why the prediction is mechanistically reasonable.

The very high TxGNN score (0.9950) supports plausibility, but it is a computational prediction and not clinical evidence. The relationship to the original indication cannot be assessed because no original indication is recorded.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [793781](https://pubmed.ncbi.nlm.nih.gov/793781/) | 1976 | RCT (double-blind, placebo-controlled crossover) | Current Medical Research and Opinion | 48 patients with bronchospastic disease received a long-acting bronchodilator combination ("Nethaprin Dospan": etafedrine, bufylline, doxylamine, phenylephrine) or placebo for one week each. Tests the combination, not etafedrine alone. The abstract is truncated, so the outcome is not available. |
| [326265](https://pubmed.ncbi.nlm.nih.gov/326265/) | 1977 | RCT (double-blind, long-term) | Arzneimittel-Forschung | A combination of tetracycline, theophylline, doxylamine, etafedrine, phenylephrine and guaifenesine in 57 chronic bronchitis patients. Only 12 showed clinical signs of exacerbation during the study. Tests a multi-drug combination that includes an antibiotic, so etafedrine's own contribution cannot be separated. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02230769 | DALMACOL | Not listed | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found for this drug in the data compiled for this report. This does not mean that no interactions exist. As a sympathomimetic, etafedrine may warrant caution with other adrenergic agents and cardiovascular conditions, but this is a general class-level expectation and not drawn from the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is very high and the beta-agonist mechanism is plausible, but there are no registered trials. The only two publications (1976–1977) test multi-ingredient combinations, so they cannot show that etafedrine alone is effective for bronchitis.
- The original indication, mechanism of action, and safety information are all missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indication) for DIN 02230769, to establish the original indication and safety profile
- Confirmed mechanism of action data from DrugBank
- Full text of the two publications to check outcomes and the contribution of etafedrine within each combination
- Evidence from studies of etafedrine as a single agent, or a justified approach for evaluating it within combinations
- A check of whether current bronchitis treatment guidelines leave room for this drug class, given the age of the available evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

