---
layout: default
title: Chloroprocaine
parent: Moderate Evidence (L3-L4)
nav_order: 183
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-13
description: "Chloroprocaine: predicted new indication Cauda equina syndrome (evidence level L4). Approved use: Not specified in the Canadian license record (local anesthesia by dru…"
monitor_inn: "Chloroprocaine"
predicted_indications: ["cauda equina syndrome"]
---

# Chloroprocaine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Chloroprocaine: From Local Anesthesia to Cauda Equina Syndrome (Prediction Likely Reflects an Adverse-Event Association)

## One-Sentence Summary

Chloroprocaine is a short-acting ester-type local anesthetic. The TxGNN model predicts a link to **cauda equina syndrome (CES)**, but the data compiled for this report suggest this link most likely reflects a known **adverse event** of intrathecal or epidural local anesthetics rather than a therapeutic effect. There are **0 clinical trials** and **4 publications** (none showing a treatment benefit), so the evidence supports a safety signal, not a new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian license record (local anesthesia by drug class) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on its drug class, chloroprocaine is an ester-type local anesthetic that blocks voltage-gated sodium channels and thereby prevents nerve conduction.

The high prediction score most plausibly reflects a graph-level association between the drug and the disease, not therapeutic potential. Intrathecal or epidural local anesthetics, including chloroprocaine, have been implicated in causing CES. Proposed causes include direct neurotoxicity to nerve roots from high local concentrations, poor distribution in the sacral thecal sac, and preservative or antioxidant effects (such as sodium bisulfite in older formulations).

No therapeutic mechanism supports use in CES. CES is typically managed by urgent surgical decompression. The prediction should therefore not be read as a repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22236346](https://pubmed.ncbi.nlm.nih.gov/22236346/) | 2012 | RCT | Acta Anaesthesiol Scand | Compared chloroprocaine with lidocaine for selective spinal anesthesia in outpatient transurethral prostatectomy. This is an anesthesia study, not CES treatment. |
| [23320599](https://pubmed.ncbi.nlm.nih.gov/23320599/) | 2013 | Review | Acta Anaesthesiol Scand | Reviews chloroprocaine for spinal anesthesia as an alternative to lidocaine, which is linked to transient neurologic symptoms. Neurologic sequelae were described after large doses of preservative-containing chloroprocaine. |
| [11368250](https://pubmed.ncbi.nlm.nih.gov/11368250/) | 2001 | Review | Drug Safety | Describes the incidence and prevention of regional anesthesia complications, including neural injury and local anesthetic toxicity. |
| [9338907](https://pubmed.ncbi.nlm.nih.gov/9338907/) | 1997 | Case report | Regional Anesthesia | Two cases of CES after spinal-epidural anesthesia. Earlier reports implicated lidocaine, chloroprocaine and procaine. |

All four publications concern anesthesia use or complications. None shows that chloroprocaine treats CES.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02551063 | CLOROTEKAL | Not specified | Not specified |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships in the TxGNN knowledge graph, not label text): kidney disease, pyoureter, liver disease, gallbladder disease, myasthenia gravis (including adult-onset), neuromuscular junction disease, butyrylcholinesterase deficiency, cardiovascular disease, and heart disease.
- **Drug interactions:** 12 interactions were identified.
  - **Major (1):** Nitrous acid.
  - **Moderate (10):** Sulfasalazine; other local anesthetics, including topical lidocaine, benzocaine, ophthalmic lidocaine, ophthalmic tetracaine, ophthalmic oxybuprocaine, topical cinchocaine and topical tetracaine; and cocaine (nasal and topical).
  - **Minor (1):** Hyaluronidase.
- **Neurotoxicity:** The literature indicates that intrathecal or epidural local anesthetics, including chloroprocaine, have been associated with CES. This is directly relevant to the predicted indication.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction most likely reflects an adverse-event association, not a therapeutic one. No clinical trials exist, and the literature describes CES as a complication of local anesthetics. Evidence is model-prediction level with only mechanistic and safety-related literature (L4).

**To proceed, the following is needed:**
- Confirm whether the prediction represents a treatment hypothesis or an adverse-event link. Currently the latter is more likely, and repurposing for CES is not supported.
- Obtain the Health Canada package insert (warnings, contraindications, approved indication and dosage form) to complete safety screening.
- Obtain mechanism of action data from DrugBank.
- Consider reviewing other predicted indications that are therapeutically plausible.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

