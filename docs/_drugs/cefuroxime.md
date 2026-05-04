---
layout: default
title: Cefuroxime
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Cefuroxime
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

# Cefuroxime: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic used globally to treat a broad spectrum of bacterial infections, including respiratory tract infections, urinary tract infections, skin and soft tissue infections, and as perioperative surgical prophylaxis.
The TxGNN model predicts it may be effective for **Hyperamylasemia**, yet there are currently **0 clinical trials** and **0 publications** directly supporting this direction.
The prediction score is high (99.76%), but is most likely an artifact of knowledge graph proximity effects rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record (not marketed in Canada) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, cefuroxime belongs to the second-generation cephalosporin class of β-lactam antibiotics. It acts by binding to penicillin-binding proteins (PBPs) and inhibiting bacterial cell wall peptidoglycan synthesis, leading to cell lysis. It is active against a wide range of gram-positive cocci and gram-negative rods (including *Haemophilus influenzae*, *E. coli*, *Klebsiella pneumoniae*, and *Proteus mirabilis*) and is resistant to many common β-lactamases. It is available in parenteral (cefuroxime sodium) and oral (cefuroxime axetil) formulations.

Hyperamylasemia — elevated serum amylase — is a laboratory finding rather than a discrete disease entity. It is most commonly a marker of acute pancreatitis, chronic pancreatitis, salivary gland disorders, or extrapancreatic abdominal pathology. There is no direct pharmacological mechanism by which inhibiting bacterial cell wall synthesis would reduce serum amylase levels.

The most plausible explanation for this TxGNN prediction is a **knowledge graph proximity effect**: cefuroxime is associated with the antibiotic management of infected necrotizing pancreatitis (a well-recognised complication of acute pancreatitis), and acute pancreatitis is the canonical cause of hyperamylasemia. The knowledge graph likely traverses the path *cefuroxime → infectious pancreatitis → pancreatitis → hyperamylasemia*, inflating the prediction score without reflecting a true drug–indication relationship. No mechanistic basis for cefuroxime as a direct therapy for hyperamylasemia has been identified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Cefuroxime is not currently marketed in Canada. No Drug Identification Numbers (DINs) were found in the Health Canada regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is rated L5 — model prediction only — with no supporting clinical trials or published literature. The mechanistic link between cefuroxime (an antibiotic) and hyperamylasemia (a marker of pancreatic or salivary gland disease) is implausible as a direct treatment relationship; the high TxGNN score almost certainly reflects a knowledge graph artefact via the infectious pancreatitis pathway rather than a genuine drug repurposing opportunity.

**To proceed, the following is needed:**
- Subgraph path analysis to confirm or refute the knowledge graph proximity hypothesis (cefuroxime → infectious pancreatitis → hyperamylasemia)
- Mechanism of action data from DrugBank (currently unavailable) to formally assess mechanistic plausibility
- Consideration of redirecting evaluation resources toward higher-value predictions in this evidence pack — notably, **urinary tract infection** (rank 6) which carries Evidence Level L2 with 17 clinical trials and 20 publications, a clear mechanistic basis, and a "Proceed with Guardrails" recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

