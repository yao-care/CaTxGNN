---
layout: default
title: Dichlorobenzyl Alcohol
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 2
---

# Dichlorobenzyl Alcohol
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

# Dichlorobenzyl Alcohol: From Oral Antiseptic to Bronchitis

## One-Sentence Summary

Dichlorobenzyl alcohol (DCBA) is a broad-spectrum antimicrobial antiseptic, best recognized as an active ingredient in over-the-counter throat lozenges, with no formally registered pharmaceutical indication in Canada.
The TxGNN model predicts it may be effective for **Bronchitis**, but the current evidence base consists of **0 clinical trials** and **1 peripherally related publication** that concerns a structurally analogous compound rather than DCBA itself.
Given the complete absence of MOA data, regulatory registration, and direct clinical evidence, this prediction currently warrants a **Hold** decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication (used as antiseptic ingredient in OTC lozenges) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for dichlorobenzyl alcohol (DCBA). Based on known pharmacological properties reported in the general literature, DCBA is an aryl alcohol with broad-spectrum antimicrobial and antiseptic activity, believed to act primarily through disruption of bacterial cell membranes. It is most recognized as one of two active ingredients in widely available throat lozenge formulations (such as Strepsils), where it provides localized antiseptic action in the oropharynx.

Bronchitis — particularly acute bronchitis — is frequently triggered or complicated by bacterial or viral infection of the respiratory mucosa. There is a superficial mechanistic rationale that an antimicrobial agent with activity against common respiratory pathogens could reduce microbial burden at the airway surface. However, this is critically undermined by a key pharmacological barrier: DCBA is formulated exclusively for topical, localized oropharyngeal use, and there is no evidence that it achieves pharmacologically meaningful drug concentrations at the bronchial epithelium following any known route of administration.

The TxGNN prediction score of 99.21% reflects high-confidence inference based on knowledge graph topology — specifically, the network proximity of DCBA to bronchitis-associated nodes. This should not be interpreted as biological plausibility or clinical evidence. Without any published MOA data directly linking DCBA to bronchitis pathophysiology (e.g., airway inflammation, mucociliary clearance, pathogen inhibition in the lower respiratory tract), this prediction remains speculative and does not yet meet the threshold for advancing to a repurposing programme.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1036939](https://pubmed.ncbi.nlm.nih.gov/1036939/) | 1976 | Observational / Adverse Event Report | Arzneimittel-Forschung | In 25 patients with **chronic bronchitis**, oral clenbuterol (NAB 365) — a beta-2 agonist bronchodilator whose chemical name contains "dichlorobenzyl alcohol" as a structural descriptor — was associated with elevated serum creatine kinase (MM isoenzyme), without other clinical signs |

> **⚠️ Critical Caveat:** This publication concerns **clenbuterol** (4-amino-α-\[(tert-butylamino)methyl\]-3,5-dichlorobenzyl alcohol hydrochloride), a beta-2 adrenergic agonist broncholytic drug. Its retrieval appears to be the result of a string-match on "dichlorobenzyl alcohol" within the chemical name. Clenbuterol and DCBA are pharmacologically distinct compounds with entirely different mechanisms of action. This publication provides **no direct evidence** for DCBA in bronchitis and should not be counted as supporting literature.

---

## Canada Market Information

Dichlorobenzyl alcohol currently has **no registered Drug Identification Numbers (DINs)** in Canada and is not marketed as a standalone pharmaceutical product. It may appear as an unlisted excipient or active ingredient in certain OTC formulations, but no formal Health Canada drug licence exists for this compound.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction sits at Evidence Level L5 — model inference only — with zero applicable clinical trials, no directly relevant literature, and a complete absence of MOA data linking DCBA to bronchitis. The sole retrieved publication addresses a pharmacologically unrelated compound (clenbuterol) whose chemical name incidentally contains the search string; it contributes no meaningful evidence for this repurposing hypothesis.

**To proceed, the following is needed:**

- **Establish MOA**: Query DrugBank API and primary literature to document DCBA's mechanism of action and any known antimicrobial spectrum relevant to respiratory pathogens
- **Pharmacokinetic/pharmacodynamic assessment**: Determine whether any route of administration (e.g., inhalation, oral) could achieve therapeutic DCBA concentrations at the bronchial mucosa
- **Preclinical evidence search**: Conduct a targeted search for in vitro or in vivo studies testing DCBA against bronchitis-relevant pathogens (e.g., *Haemophilus influenzae*, *Streptococcus pneumoniae*) or airway inflammation models
- **Safety documentation**: Download and parse the TFDA product monograph or equivalent Health Canada documents to identify warnings, contraindications, and known adverse effects before any Stage 1 safety review can proceed
- **Regulatory pathway clarification**: Assess whether DCBA would require a new NDS submission or could be repositioned within an existing OTC monograph framework in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

