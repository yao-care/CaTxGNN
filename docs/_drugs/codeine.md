---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 219
evidence_level: L5
indication_count: 4
---

# Codeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Codeine: From Established Opioid Use to Nasal Cavity Disease

## One-Sentence Summary

Codeine is an opioid medicine marketed in Canada, and the license data supplied here do not list its approved indications.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but **0 clinical trials** and only **2 publications** were found.
Both publications are case reports of opioid-related harm to the nose, not of benefit, so the prediction is not supported by the evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and the Canadian license records do not state any approved indication. Codeine is a well-known opioid used clinically for pain and cough suppression. However, no mechanism linking it to nasal cavity disease can be assessed from the data provided.

The high score (0.999) is a graph-based association only. The two retrieved papers describe harm rather than treatment. One reports tissue necrosis of the nasal cavity and pharynx after snorting crushed hydrocodone-acetaminophen tablets. The other reports a nasal stone (rhinolith) that formed around a hardened codeine-and-opium mixture. The literature therefore points toward risk, and the score most likely reflects a drug-disease co-occurrence rather than a therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Case report | The Laryngoscope | Intranasal abuse of hydrocodone-acetaminophen caused necrosis of the nasal cavity and pharynx. This is a harm report and involves a different opioid. |
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose, & Throat Journal | A rhinolith formed around a foreign body, a hardened codeine-opium mixture. It caused nasal obstruction and foul-smelling discharge, so the drug was the cause rather than the treatment. |

---

## Canada Market Information

Codeine has 20 licenses in total. Dosage form and approved indication text are not available in the supplied records. The main authorizations are:

| DIN | Product Name |
|---------|------|
| 00593451 | TEVA-CODEINE |
| 00593435 | TEVA-CODEINE |
| 02009757 | CODEINE 30 |
| 00050024 | CODEINE PHOSPHATE SYRUP |
| 00380571 | LINCTUS CODEINE BLANC |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found. The retrieved literature also raises a concern: intranasal misuse of opioids has been associated with nasal tissue damage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (evidence level L5). There are no trials, and the only publications describe opioid-related harm to the nasal cavity. Health Canada safety and indication data are also missing.

Other predicted indications also lack support:
- **Acute laryngopharyngitis:** no trials or literature. Codeine's known cough-suppressant use makes a symptom-relief link plausible, but nothing in the data supports it.
- **Trigeminal autonomic cephalalgia:** five case-level papers, none of which report codeine efficacy by title. One case report describes codeine phosphate helping a single cluster headache patient who could not take sodium-channel-blocking drugs.
- **Allergic urticaria:** the literature consistently shows codeine causing or provoking urticaria, the opposite of a therapeutic effect.

**To proceed, the following is needed:**
- Health Canada monograph warnings and contraindications, which is a blocking gap for safety screening.
- The approved indications and dosage forms of the Canadian licenses.
- Mechanism of action data, for example from DrugBank.
- Expert review of whether any evidence supports a therapeutic role in nasal cavity disease. Absent that, the candidate should not advance.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

