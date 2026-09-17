---
layout: default
title: Zinc Sulfate
parent: High Evidence (L1-L2)
nav_order: 840
evidence_level: L2
indication_count: 4
---

# Zinc Sulfate
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **4** 
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

# Zinc Sulfate: From Mineral Supplement Use to Pharyngitis

## One-Sentence Summary

Zinc sulfate is a mineral supplement with no current Health Canada market authorization and no original approved indication recorded in the available data.
The TxGNN model predicts it may be effective for **Pharyngitis**,
with **4 clinical trials** and **3 publications** currently supporting this direction, though the evidence is mixed and a blocking safety data gap remains unresolved.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — zinc sulfate is not currently marketed in Canada and no approved indication text is on record |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for zinc sulfate is not available in the evidence pack (flagged as a High-severity data gap), and no original approved indication is recorded since the drug does not hold a current Health Canada authorization. In the absence of formal MOA data, the repurposing rationale relies on the mechanistic reasoning generated alongside the prediction: zinc ions exert local astringent and anti-inflammatory effects on the pharyngeal mucosa and may inhibit rhinovirus protease activity and replication — rhinovirus being a common causative agent of pharyngitis.

Zinc lozenges have a traditional history of use for relieving sore-throat symptoms, which provides some biological plausibility for pharyngitis as a repurposing candidate. However, most of the larger randomized trials identified in the evidence base were conducted in the context of COVID-19 outpatient treatment rather than pharyngitis specifically, and only one small, non-phase trial (NCT02405832) directly targets a pharyngitis-related endpoint (postoperative sore throat). This mismatch between the bulk of the clinical trial evidence and the target indication means the mechanistic linkage is plausible but requires independent, indication-specific validation before it can be considered confirmed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | N/A | Completed | 87 | Randomized, double-blind, placebo-controlled study of preoperative oral zinc lozenges for postoperative sore throat syndrome — the most directly relevant trial to pharyngitis (relevance grade A). |
| [NCT04446104](https://clinicaltrials.gov/study/NCT04446104) | Phase 3 | Completed | 4,257 | Randomized prophylaxis trial of zinc among high-risk migrant workers for COVID-19; sore throat is a component symptom but not the primary endpoint (relevance grade C). |
| [NCT04621461](https://clinicaltrials.gov/study/NCT04621461) | Phase 4 | Completed | 3 | Randomized, placebo-controlled trial of zinc for COVID-19 treatment in outpatients; extremely small sample and indication mismatch (relevance grade C). |
| [NCT04370782](https://clinicaltrials.gov/study/NCT04370782) | Phase 4 | Completed | 18 | Randomized trial of hydroxychloroquine and zinc combined with azithromycin or doxycycline for COVID-19; confounded by combination therapy and not specific to pharyngitis (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT (Tier 1) | J Med Assoc Thai | Randomized, double-blind, placebo-controlled trial of zinc sulfate supplementation for alleviating radiation-induced oral mucositis and pharyngitis in head and neck cancer patients. |
| [38693477](https://pubmed.ncbi.nlm.nih.gov/38693477/) | 2024 | RCT (Tier 2) | BMC Anesthesiology | Randomized controlled trial comparing preoperative zinc, magnesium, and budesonide gargles for reducing incidence and severity of postoperative sore throat (POST). |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Cohort (Tier 3) | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Cohort study on long-lasting post-tonsillectomy dysgeusia, discussing dietary zinc deficiency as a possible contributing factor; indirect relevance to pharyngitis. |

---

## Canada Market Information

Zinc sulfate currently holds **no Health Canada market authorization** — `total_licenses` is 0 and no DIN records are available in the evidence pack. As a result, no product/dosage-form/indication table can be generated at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. Note that a **Blocking**-severity data gap exists for Health Canada product-label warnings and contraindications (DG001), which currently prevents a formal safety pre-assessment (S1 stage) for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for pharyngitis is plausible and supported by one relevant Tier-1 RCT and one directly on-target trial, but most of the clinical trial evidence base is confounded by an unrelated COVID-19 indication, and a Blocking-severity safety data gap (missing product warnings/contraindications) currently prevents even an initial safety evaluation. The candidate is not currently marketed in Canada (0 DINs), further limiting near-term actionability.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain Health Canada / product-label warnings and contraindications before any S1 safety pre-assessment can proceed
- Resolve DG002 (High): obtain confirmed mechanism of action data from DrugBank to strengthen the mechanistic-link analysis
- Identify or conduct a pharyngitis-specific (non-COVID) randomized trial with an adequate sample size to substantiate the NCT02405832 finding
- Clarify original/approved indications for zinc sulfate, if any exist in other jurisdictions, to better contextualize the repurposing rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

