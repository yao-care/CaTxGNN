---
layout: default
title: Oxcarbazepine
parent: 僅模型預測 (L5)
nav_order: 587
evidence_level: L5
indication_count: 10
---

# Oxcarbazepine
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

# Oxcarbazepine: From Epilepsy (Partial-Onset Seizures) to Visual Epilepsy

## One-Sentence Summary

Oxcarbazepine is a well-established antiepileptic drug used for partial-onset and generalized tonic-clonic seizures, structurally related to carbamazepine. The TxGNN model predicts it may be effective for **Visual Epilepsy**, a rare reflex epilepsy subtype triggered by visual stimuli, with **1 clinical trial** and **19 publications** currently associated with this direction — though none of them studies this subtype specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, partial-onset (focal) seizures — established international use; no Health Canada product data available in this pack |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Canada Market Status | 未上市 (Not Marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not currently available (data gap, DG002). Based on established pharmacological knowledge, oxcarbazepine is a voltage-gated sodium channel blocker and a broad-spectrum antiepileptic drug (AED), structurally derived from carbamazepine, long used for partial-onset and generalized tonic-clonic seizures.

Visual epilepsy is a rare reflex epilepsy subtype in which seizures are triggered by visual stimuli (e.g., flickering light). Like other focal and reflex epilepsies, it is believed to arise from abnormal cortical hyperexcitability — the same underlying process that sodium-channel blockers such as oxcarbazepine are designed to dampen.

Because this mechanism is shared broadly across focal epilepsy subtypes, it is mechanistically plausible that oxcarbazepine could reduce seizure frequency in visual epilepsy. However, none of the evidence currently collected studies oxcarbazepine in visual epilepsy specifically — the supporting trial (LICEO) and literature evaluate AEDs and epilepsy broadly, not this reflex subtype. This is a meaningful evidentiary gap, not just a formality.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Prospective observational "LICEO" study assessing new AEDs (gabapentin, lamotrigine, levetiracetam, oxcarbazepine, pregabalin, tiagabine, topiramate) as first-choice bitherapy in focal epilepsy. Not specific to visual epilepsy (relevance grade C — general AED effectiveness only). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35429132](https://pubmed.ncbi.nlm.nih.gov/35429132/) | 2022 | Randomized Study | CNS Neuroscience & Therapeutics | Multicenter, open-label RCT comparing oxcarbazepine vs. levetiracetam monotherapy in newly diagnosed focal epilepsy (China); not visual-epilepsy specific. |
| [39899099](https://pubmed.ncbi.nlm.nih.gov/39899099/) | 2025 | Review | Continuum (Minneap Minn) | Update on antiseizure medications, covering pharmacokinetics, indications, and modes of use for agents including oxcarbazepine. |
| [35380580](https://pubmed.ncbi.nlm.nih.gov/35380580/) | 2022 | Review | JAMA | Overview of antiseizure medications for adults with epilepsy and treatment goals. |
| [33334546](https://pubmed.ncbi.nlm.nih.gov/33334546/) | 2020 | Review | Seizure | Current role of carbamazepine and oxcarbazepine in epilepsy management relative to newer AEDs. |
| [37092337](https://pubmed.ncbi.nlm.nih.gov/37092337/) | 2023 | Pharmacogenomics Review | Pharmacogenomics | Reviews genetic variation affecting oxcarbazepine efficacy/safety via metabolic enzymes and transporters. |
| [26844734](https://pubmed.ncbi.nlm.nih.gov/26844734/) | 2016 | Review | Continuum (Minneap Minn) | Individual AED review including oxcarbazepine's spectrum of efficacy and clinical use. |
| [22091603](https://pubmed.ncbi.nlm.nih.gov/22091603/) | 2012 | Clinical Study | Epilepsia | Efficacy, tolerability, and pharmacokinetics of oxcarbazepine oral loading in patients with epilepsy. |
| [30636182](https://pubmed.ncbi.nlm.nih.gov/30636182/) | 2019 | PK Study | J Clin Pharm Ther | Population pharmacokinetics and dose simulation of oxcarbazepine in Chinese pediatric epilepsy patients. |
| [12697143](https://pubmed.ncbi.nlm.nih.gov/12697143/) | 2003 | Cohort Study | Epilepsy & Behavior | Safety and tolerability of oxcarbazepine in elderly vs. younger adult epilepsy patients. |
| [27845825](https://pubmed.ncbi.nlm.nih.gov/27845825/) | 2016 | Systematic Review (Cochrane, Withdrawn) | Cochrane Database Syst Rev | Oxcarbazepine as add-on therapy for drug-resistant partial epilepsy. |

None of the above addresses visual epilepsy directly; all support oxcarbazepine's general efficacy and safety profile in focal/partial epilepsy.

---

## Canada Market Information

Oxcarbazepine is currently **not marketed in Canada** — no active Health Canada Drug Identification Numbers (DINs) are on record in this evidence pack (`total_licenses: 0`). No product-specific dosage form or approved-indication text is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No Health Canada product monograph warnings, contraindications, or drug interaction data are currently available in this evidence pack (DG001, blocking severity — required before any S1 safety screening can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Oxcarbazepine is not currently marketed in Canada (0 DINs) and the product-safety data gap (DG001) is rated Blocking, meaning a formal safety screen (S1) cannot yet be completed. Evidence strength for the specific predicted indication (visual epilepsy) is L3 — supported only by general AED trial/literature data, not by any study of this reflex subtype specifically.

**To proceed, the following is needed:**
- Health Canada product monograph — warnings, contraindications (DG001, blocking)
- DrugBank mechanism-of-action detail (DG002)
- Subtype-specific clinical evidence for visual/reflex epilepsy rather than general focal-epilepsy data
- Completed drug-drug interaction (DDI) query — current status is "not found"
- A safety monitoring plan addressing oxcarbazepine class risks noted in the broader literature (e.g., hyponatremia, HLA-associated cutaneous reactions), pending confirmation via the product monograph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

