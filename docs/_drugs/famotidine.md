---
layout: default
title: Famotidine
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Famotidine
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

# Famotidine: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Famotidine is a potent histamine H2-receptor antagonist (H2RA) with a long-established clinical role in reducing gastric acid secretion for peptic ulcer disease and acid hypersecretory conditions.
The TxGNN model predicts it may be effective for **Duodenogastric Reflux**,
with **0 clinical trials** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease and acid hypersecretory conditions (based on pharmacological literature; no regulatory record in current dataset) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed (per dataset — may reflect a data collection gap) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, famotidine belongs to the histamine H2-receptor antagonist (H2RA) class. Its ability to reduce gastric acid secretion and promote peptic ulcer healing has been extensively documented across decades of clinical use, and this same acid-suppressive property may be mechanistically applicable to duodenogastric reflux.

Duodenogastric reflux (also called bile reflux gastritis) involves the retrograde flow of duodenal contents — primarily bile acids and pancreatic enzymes — into the stomach. While bile is the primary mucosal irritant, co-existing gastric acid significantly amplifies the mucosal damage caused by the refluxed material. By reducing basal gastric acid secretion by approximately 60–70% and stimulated secretion by up to 90%, famotidine may attenuate the combined acid-bile mucosal insult, providing partial symptomatic relief and mucosal protection even without addressing the bile component directly.

The mechanistic support is therefore only partial: famotidine has no effect on bile acid composition, biliary secretion, or pyloric sphincter tone — which are the primary pathological drivers of duodenogastric reflux. A 2003 ICU observational study (PMID 12532466) and a 2004 clinical observational study (PMID 16259441) both examined famotidine in gastroduodenal reflux contexts and reported some benefit, but neither study was a controlled RCT with duodenogastric reflux as the primary endpoint. The overall evidence base remains at L3, making this indication best characterised as a research question rather than a clinical signal ready for advancement.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Observational/ICU Study | World Journal of Gastroenterology | Examined famotidine's effect on both gastroesophageal reflux (GER) and duodeno-gastro-esophageal reflux (DGER) in critically ill patients; explored possible mechanisms and identified clinical factors associated with reflux severity |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Observational Study | Experimental & Clinical Gastroenterology | Evaluated famotidine 20 mg twice daily in patients with early-stage gastroduodenal reflux disease (Savary-Miller grades 0–1); assessed treatment response using clinical and endoscopic criteria and reported therapeutic benefit in this population |

---

## Canada Market Information

The current dataset contains no registered Drug Identification Numbers (DINs) for famotidine and records the market status as not marketed. This likely reflects a data collection gap rather than an actual absence from the Canadian market, given famotidine's long international availability as both a prescription and over-the-counter product. Health Canada regulatory records should be independently verified through a direct DPD (Drug Product Database) query before drawing any conclusions on Canadian market status.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for famotidine in duodenogastric reflux is limited to two small observational studies (evidence level L3) with no registered clinical trials. While famotidine's acid-suppressive mechanism offers a biologically plausible partial benefit, it does not address bile — the primary pathological driver in this condition — limiting the expected therapeutic effect and making advancement to clinical development premature at this stage.

**To proceed, the following is needed:**
- Retrieve and parse the Health Canada product monograph (package insert) to complete the safety evaluation — this is currently a blocking data gap preventing formal S1 safety screening
- Query the DrugBank API to populate full mechanism of action data and drug interaction profile
- Verify Canadian regulatory status directly via the Health Canada Drug Product Database (DPD) to correct the apparent market status data gap
- Conduct a prospective pilot RCT or well-designed controlled observational study with duodenogastric reflux as the primary endpoint and famotidine as the study intervention
- Evaluate whether combination therapy (e.g., famotidine with a prokinetic agent such as domperidone, or a bile acid sequestrant) could more comprehensively address the dual acid-bile pathophysiology of this condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

