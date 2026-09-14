---
layout: default
title: Sodium Sulfate
parent: 僅模型預測 (L5)
nav_order: 725
evidence_level: L5
indication_count: 1
---

# Sodium Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Sodium Sulfate (DB09472): From Osmotic Laxative Use to Predicted Dyspepsia Indication

## One-Sentence Summary

Sodium sulfate (DB09472) has no formally recorded original indication in this evidence pack, but it is clinically known as an osmotic laxative / bowel-preparation agent.
The TxGNN model predicts it may be effective for **Dyspepsia**, with a prediction score of **99.09%**,
but the supporting evidence — **3 clinical trials** and **4 publications** — is weak and largely mismatched to the actual drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record in Health Canada data (drug not marketed in Canada); clinically known off-label/traditional use as osmotic laxative / bowel-preparation agent |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sodium sulfate. Based on known information, sodium sulfate acts as an osmotic agent, drawing water into the intestinal lumen — a property exploited in bowel-preparation and laxative use. This mechanism has no established pharmacological link to dyspepsia, which involves upper GI motility, acid secretion, and visceral sensitivity rather than colonic osmotic effects.

Critically, the evidence pack itself flags this prediction as poorly supported. All three clinical trials were graded **"C" (low relevance)** by the evidence review — none actually test sodium sulfate for dyspepsia. More importantly, the literature evidence is largely a **keyword mismatch**: most publications refer to "Dextran Sodium Sulfate (DSS)," a chemical reagent used to induce colitis in animal models, which is an entirely different substance from the drug DB09472 (sodium sulfate). The repurposing rationale explicitly states there is **no valid mechanistic link** ("無有效機轉關聯") between this drug and dyspepsia.

Given this, the prediction should be treated as a model-generated signal only, not as evidence of a genuine drug-disease relationship. It requires independent mechanistic and clinical validation before any further consideration.

---

## Clinical Trial Evidence

> ⚠️ All trials below were graded **"C" (low relevance)** by evidence review — none directly test sodium sulfate for dyspepsia.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06339697](https://clinicaltrials.gov/study/NCT06339697) | Phase 4 | Completed | 194 | Compared bowel-preparation laxatives (PEG electrolyte solution vs. sodium picosulfate) on gut microbiome changes in colon polypectomy patients; endpoint was microbiome composition, not dyspepsia |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Compared oxycodone vs. pregabalin for preemptive postoperative analgesia; unrelated to sodium sulfate or dyspepsia |
| [NCT07310927](https://clinicaltrials.gov/study/NCT07310927) | Phase 2/3 | Recruiting | 140 | Compared alginate vs. sucralfate for GERD symptom relief with PPIs; does not involve sodium sulfate |

---

## Literature Evidence

> ⚠️ Most publications concern **Dextran Sodium Sulfate (DSS)**, a colitis-induction reagent used in animal models — a distinct substance from the drug sodium sulfate (DB09472). This appears to be a keyword-matching artifact rather than genuine pharmacological evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33918638](https://pubmed.ncbi.nlm.nih.gov/33918638/) | 2021 | Animal model / PK study | Molecules (Basel, Switzerland) | Examined DSS-induced GI injury effects on donepezil pharmacokinetics and gastric myoelectric activity in pigs; dyspepsia mentioned only as a background donepezil side effect |
| [34207410](https://pubmed.ncbi.nlm.nih.gov/34207410/) | 2021 | Animal model / PK study | Pharmaceuticals (Basel, Switzerland) | Examined DSS-induced GI injury effects on galantamine's impact on porcine gastric myoelectric activity |
| [36614242](https://pubmed.ncbi.nlm.nih.gov/36614242/) | 2023 | Animal model | International Journal of Molecular Sciences | Tested atractylodin (an herbal compound, not sodium sulfate) in DSS-induced colitis mice; dyspepsia mentioned only as background indication for the herbal medicine source |
| [40391232](https://pubmed.ncbi.nlm.nih.gov/40391232/) | 2025 | Animal model | Journal of Inflammation Research | Tested Si-Ni Decoction (TCM formula) in DSS-induced ulcerative colitis; dyspepsia mentioned only as background context, no sodium sulfate involvement |

---

## Canada Market Information

Sodium sulfate (DB09472) is currently **not marketed in Canada** — no DIN records or Health Canada product authorizations are on file.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available for this drug in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only, no genuine supporting studies), no MOA data exists, and the retrieved literature/clinical trial evidence largely reflects a keyword mismatch between "sodium sulfate" and "dextran sodium sulfate" rather than actual pharmacological evidence for dyspepsia. The repurposing rationale itself explicitly concludes there is no valid mechanistic link.

**To proceed, the following is needed:**
- TFDA/Health Canada package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action for DB09472 — currently a High-severity data gap (DG002)
- Re-run literature/trial search with stricter entity disambiguation to exclude Dextran Sodium Sulfate (DSS) mismatches
- Genuine dyspepsia-specific pharmacological or clinical evidence for sodium sulfate, if any exists, before advancing beyond Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

