---
layout: default
title: Chloroprocaine
parent: Model Prediction Only (L5)
nav_order: 181
evidence_level: L5
indication_count: 1
---

# Chloroprocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Chloroprocaine: From Local Anesthesia to Cauda Equina Syndrome (a Safety Signal, Not a Treatment)

## One-Sentence Summary

Chloroprocaine is a short-acting local anesthetic that blocks sodium channels, and it is used for regional and spinal anesthesia.
The TxGNN model predicts a link with **cauda equina syndrome**, but this most likely reflects a **known adverse-event association** rather than a therapeutic effect.
Only **1 observational safety study** and **4 publications** exist, and none shows that chloroprocaine treats this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (no indication text in the license record) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 for therapeutic efficacy (the evidence pack labels it L4; the available studies concern safety only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Chloroprocaine is a local anesthetic that blocks voltage-gated sodium channels, which interrupts nerve conduction.

The high score most likely reflects a drug-disease association in the knowledge graph. Cauda equina syndrome is a rare complication of intrathecal or epidural local anesthetics, including chloroprocaine, through neurotoxicity or compressive injury. The literature describes these neurological sequelae, particularly after large doses of preservative-containing formulations.

No plausible mechanism links sodium channel blockade to treating cauda equina syndrome. That condition is managed by surgical decompression. This prediction should be read as a **safety signal**, not a repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02067806](https://clinicaltrials.gov/study/NCT02067806) | N/A (observational) | Completed | 394 | Prospective safety study of 1% 2-chloroprocaine in intrathecal anesthesia. It tracked neurological adverse events, especially transient neurological symptoms and cauda equina syndrome. It does not test treatment of the condition. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22236346](https://pubmed.ncbi.nlm.nih.gov/22236346/) | 2012 | RCT | Acta Anaesthesiol Scand | Chloroprocaine vs lidocaine for selective spinal anesthesia in outpatient transurethral prostatectomy. This is an anesthesia comparison, not a study of cauda equina syndrome. |
| [23320599](https://pubmed.ncbi.nlm.nih.gov/23320599/) | 2013 | Review | Acta Anaesthesiol Scand | Chloroprocaine as an alternative to intrathecal lidocaine for short procedures. It notes neurologic sequelae after large doses of preservative-containing formulations. |
| [11368250](https://pubmed.ncbi.nlm.nih.gov/11368250/) | 2001 | Review | Drug Safety | Incidence and prevention of regional anesthesia complications, including neural injury and local anesthetic toxicity. |
| [9338907](https://pubmed.ncbi.nlm.nih.gov/9338907/) | 1997 | Case report | Regional Anesthesia | Two cases of cauda equina syndrome after spinal-epidural anesthesia. Chloroprocaine has been implicated in earlier reports. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2551063 | CLOROTEKAL |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.
- **Neurotoxicity signal**: Cauda equina syndrome and transient neurological symptoms are recognized complications of intrathecal and epidural local anesthetics, including chloroprocaine. This is the likely origin of the model's prediction.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction most likely reflects an adverse-event association rather than a therapeutic effect. There is no efficacy evidence, no plausible mechanism, and the standard treatment is surgical decompression. Repurposing is not supported.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, to complete safety screening
- Detailed mechanism of action data
- Confirmation that the score reflects an adverse-event edge in the knowledge graph. If so, record it as a safety signal and remove it from the repurposing pipeline.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

