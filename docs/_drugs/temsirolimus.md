---
layout: default
title: Temsirolimus
parent: High Evidence (L1-L2)
nav_order: 889
evidence_level: L2
indication_count: 3
last_modified_at: 2026-10-13
description: "Temsirolimus: predicted new indication Liposarcoma (evidence level L2). Approved use: Mantle cell lymphoma, B-cell neoplasm…"
monitor_inn: "TEMSIROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "vulva sarcoma"]
---

# Temsirolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **3** 
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

# Temsirolimus: From Renal Cell Carcinoma and Mantle Cell Lymphoma to Liposarcoma

## One-Sentence Summary

Temsirolimus was originally used to treat renal cell carcinoma and mantle cell lymphoma.
The TxGNN model predicts it may be effective for **liposarcoma**,
with **2 clinical trials** (both combination regimens in sarcoma populations) and **1 publication** (a narrative review) currently supporting this direction. Direct evidence is still limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mantle cell lymphoma, B-cell neoplasm, renal cell carcinoma (including clear cell and non-papillary types) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

*Note: The Canadian licence record has no approved-indication text, so the original indications above come from the knowledge-graph indication data compiled for this report.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, temsirolimus is an mTOR inhibitor. It blocks a central signalling pathway that controls tumour cell growth, proliferation and survival.

The PI3K/AKT/mTOR pathway is frequently activated in soft tissue sarcomas. Well-differentiated and dedifferentiated liposarcomas, which are often driven by MDM2/CDK4 amplification, commonly show dysregulated mTOR signalling. This gives a plausible biological reason to test mTOR inhibition in liposarcoma.

The very high TxGNN score reflects this link, but it is a computational prediction, not clinical proof. Temsirolimus has proven activity in renal cell carcinoma and mantle cell lymphoma, which are different tumour types from sarcoma. Its benefit in liposarcoma has not been shown by the data available here.

Two other predicted indications, ovarian myxoid liposarcoma (score 99.47%) and vulva sarcoma (score 99.09%), have no supporting trials or literature. They are very rare, and evidence for them is unlikely to be generated on its own.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus plus liposomal doxorubicin in recurrent soft tissue and bone sarcoma. It aims to find a safe dose and assess efficacy. No liposarcoma-specific results were available, and the contribution of temsirolimus alone cannot be separated. (Relevance: B) |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab plus temsirolimus in pediatric patients with recurrent or refractory solid tumours, including sarcoma. Liposarcoma is rare in this age group, so direct relevance to adult liposarcoma is low. (Relevance: C) |

Both trials are early-phase studies of combination regimens. Neither is a Phase 3 randomised trial.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du Cancer | A review of targeted treatment for rare connective tissue tumours and sarcomas. It describes six molecularly defined sarcoma subgroups and their targeted therapies. It is general in scope and does not provide direct liposarcoma efficacy data for temsirolimus. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02304104 | TORISEL | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Haematological parameters (CBC), liver and renal function, blood glucose and lipids |
| Handling Protection | Please refer to the package insert warnings and precautions |

The monitoring items are suggested from the knowledge-graph contraindication signals below (kidney, liver, glucose and lipid disorders). They are not taken from label text.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these come from knowledge-graph drug-disease edges, not from package insert text):
- Metabolic: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hyperlipidaemia (including familial)
- Organ function: kidney disease, liver disease, gallbladder disease, hyperbilirubinaemia (including Gilbert syndrome)
- Cerebrovascular: stroke, cerebrovascular disorder, cerebral infarction
- Pulmonary: interstitial lung disease
- Brain tumours: brain cancer and several astrocytoma and glioma subtypes

**Drug Interactions** (100 interactions recorded; examples shown):
- **Major**: amphotericin B (including the lipid complex), dexamethasone, clarithromycin
- **Moderate**: antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide), corticosteroids (hydrocortisone, triamcinolone, betamethasone, budesonide), aprepitant, cimetidine, mesalazine, balsalazide

Package insert warnings and contraindications from Health Canada were not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mTOR rationale is biologically plausible and the TxGNN score is very high. However, the only trials are early-phase combination studies in mixed sarcoma populations, with no liposarcoma-specific results. The one publication is a general review. Official safety label data are also missing, so the evidence does not yet support moving forward.

**To proceed, the following is needed:**
- Download and review the Health Canada package insert for warnings and contraindications, and add the approved-indication text and dosage form for DIN 02304104
- Confirm the mechanism of action in DrugBank
- Obtain liposarcoma-specific results from NCT00949325 and other sarcoma studies, including subgroup data
- Search for temsirolimus monotherapy or mTOR-inhibitor data in well-differentiated and dedifferentiated liposarcoma
- Develop a safety monitoring plan covering metabolic risk (glucose and lipids), interstitial lung disease, and the major drug interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

