---
layout: default
title: Vasopressin
parent: Moderate Evidence (L3-L4)
nav_order: 822
evidence_level: L4
indication_count: 10
---

# Vasopressin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

Using the drug-repurposing-report skill implied by the task prompt (v5 template) to produce the report directly from the evidence pack.

# Vasopressin: From Diabetes Insipidus/Vasodilatory Shock to Congenital Prothrombin Deficiency

## One-Sentence Summary

> Vasopressin (DB00067) is an antidiuretic hormone historically associated with diabetes insipidus and vasodilatory shock, though this evidence pack does not itself record an approved original indication.
> The TxGNN model's top-ranked prediction is **Congenital Prothrombin Deficiency**, with a **99.63% prediction score**,
> but only **3 case-level publications** support it — and none of them actually studies vasopressin or this exact disease, making the mechanistic case weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this evidence pack (drug not marketed in Canada; general pharmacology suggests diabetes insipidus / vasodilatory shock — unconfirmed here) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for vasopressin is not available in this evidence pack (Data Gap DG002, severity: High). Based on general pharmacological knowledge, vasopressin acts on V1 (vascular smooth muscle) and V2 (renal collecting duct) receptors, driving vasoconstriction and antidiuresis — a mechanism unrelated to coagulation factor synthesis.

Critically, the supporting literature identified for this prediction does **not** actually support the drug–disease link. The three cited papers discuss DDAVP (desmopressin, a vasopressin *analogue*) used to raise Factor VIII/von Willebrand Factor levels in **Factor V/VIII deficiency** — a different drug and a different disease entity from **congenital prothrombin (Factor II) deficiency**. This is flagged directly in the evidence pack as a mechanistic mismatch, not a validated repurposing rationale.

Given the absence of MOA data, the lack of any clinical trial evidence, and a literature base that is topically adjacent but not actually on-target, this prediction should be treated as a TxGNN scoring artifact rather than a biologically grounded hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity reviews | Reviews acquired hemophilia A (Factor VIII autoantibodies) — does not discuss vasopressin or prothrombin deficiency |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | Rinsho Ketsueki | DDAVP (desmopressin) used in combined Factor V/VIII deficiency — not vasopressin, not prothrombin deficiency |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | Rinsho Ketsueki | Factor VIII concentrate replacement during cesarean section in combined Factor V/VIII deficiency — same mismatch as above |

**Note:** None of these three publications directly studies vasopressin or congenital prothrombin (Factor II) deficiency. They were likely retrieved due to topical overlap with "congenital factor deficiency" and coagulation hormone therapy (DDAVP), not a genuine match.

---

## Canada Market Information

Vasopressin is currently **not marketed in Canada** (0 DINs on file), so no Health Canada product authorization or approved-indication text is available for cross-reference.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack — DG001, severity: Blocking, required before any S1 safety screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (congenital prothrombin deficiency) carries an evidence level of only L4, driven entirely by case reports/review literature that, on inspection, discuss a different drug (DDAVP) and a different disease (Factor V/VIII deficiency) rather than vasopressin and prothrombin deficiency directly. No clinical trials exist, no MOA data is available, and the drug is not marketed in Canada. The remaining nine candidates in this pipeline are similarly weak-to-unsupported: eight are pure TxGNN predictions with zero literature or trial evidence (L5), and the tenth (cystic neoplasm) is supported only by Tolvaptan trials — a V2 **antagonist**, mechanistically opposite to vasopressin's agonist action. All ten candidates carry a "Hold" recommendation.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for vasopressin (DrugBank query, currently missing — DG002)
- Health Canada / TFDA product monograph warnings and contraindications (currently blocking — DG001)
- Re-run literature search with corrected disease-specific terms to rule out retrieval false positives (e.g., separate "prothrombin deficiency" from generic "coagulation factor deficiency")
- If pursuing rank-10 (cystic neoplasm) instead, clarify whether the intended hypothesis is agonism or antagonism at V2 receptors, since current evidence (Tolvaptan) points the opposite direction from vasopressin's known pharmacology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

