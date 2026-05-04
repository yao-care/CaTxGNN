---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Buprenorphine: From Opioid Dependence & Pain Management to Acute Intermittent Porphyria

## One-Sentence Summary

Buprenorphine is a partial μ-opioid receptor agonist and κ-opioid receptor antagonist, internationally established for opioid use disorder treatment and chronic pain management, though it is currently not marketed in Taiwan.
The TxGNN model predicts it may be effective for **Acute Intermittent Porphyria (AIP)**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Opioid use disorder; pain management (not registered in Taiwan) |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, buprenorphine is a partial μ-opioid receptor agonist, κ-opioid receptor antagonist, and ORL-1 (nociceptin) receptor antagonist. Its efficacy for opioid dependence and pain management has been well established through decades of international clinical use.

Acute Intermittent Porphyria (AIP) is a rare autosomal dominant metabolic disorder caused by a deficiency of hydroxymethylbilane synthase, leading to toxic accumulation of heme precursors (ALA and PBG) during acute attacks. Attacks are frequently triggered by drugs that strongly induce hepatic CYP enzymes (particularly CYP1A2, CYP3A4), hormonal fluctuations, fasting, or infection. Pain management during acute attacks is clinically challenging, as many analgesics are potentially unsafe in this population.

The key mechanistic argument here rests on **drug safety rather than therapeutic efficacy**: buprenorphine does not strongly induce hepatic CYP enzymes, meaning it is considered relatively safe for analgesic use in AIP patients compared to many alternatives. However, the evidence pack explicitly flags that "safe use ≠ therapeutic effect" — buprenorphine's opioid receptor activity has no established intersection with AIP pathophysiology (hepatic ALA synthase induction). There is no credible mechanistic basis supporting buprenorphine as a disease-modifying treatment for AIP itself. The high TxGNN score likely reflects the drug-safety overlap rather than a true repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case Report | Masui. The Japanese Journal of Anesthesiology | Perioperative anesthetic management of a 40-year-old AIP patient undergoing radical hysterectomy; describes cautious selection of analgesics safe for AIP — does not report buprenorphine as a treatment for AIP itself |

---

## Taiwan Market Information

Buprenorphine is currently **not marketed in Taiwan**. No Drug Identification Numbers (DINs) are on record, and no approved indication text is available from the Taiwan FDA database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.41%), there are no registered clinical trials and only one peripheral anesthesiology case report describing perioperative *safe use* in an AIP patient — not therapeutic efficacy. The repurposing rationale lacks mechanistic credibility: AIP pathophysiology is driven by hepatic ALA synthase induction and porphyrin precursor accumulation, which has no established intersection with opioid receptor signalling.

**To proceed, the following is needed:**
- Retrieve full mechanism of action (MOA) data from DrugBank (DB00921) to formally document the opioid receptor pharmacology
- Download and parse the Taiwan TFDA package insert (仿單) to assess key warnings and contraindications
- Conduct a targeted literature search for any preclinical or mechanistic studies linking μ/κ-opioid receptor activity to heme biosynthesis or porphyrin metabolism
- Obtain a complete drug-drug interaction (DDI) profile, with particular focus on CYP enzyme induction/inhibition — this is the critical safety axis for AIP
- Clarify the clinical question: is the intended use **supportive analgesia in AIP attacks** (safety evaluation pathway) or **disease modification** (repurposing pathway)? These require fundamentally different evaluation frameworks
- If the goal is safe analgesic use in AIP, re-scope the assessment as a drug-safety review rather than a drug repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

