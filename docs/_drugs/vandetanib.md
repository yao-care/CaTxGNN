---
layout: default
title: Vandetanib
parent: High Evidence (L1-L2)
nav_order: 966
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-13
description: "Vandetanib: predicted new indication Renal cell carcinoma (evidence level L2). Approved use: Thyroid gland carcinoma"
monitor_inn: "VANDETANIB"
predicted_indications: ["renal cell carcinoma (disease)", "renal cell carcinoma associated with neuroblastoma", "unclassified renal cell carcinoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal pelvis carcinoma", "clear cell renal carcinoma", "childhood kidney cell carcinoma", "renal carcinoma", "angiolipoma", "familial spontaneous pneumothorax"]
---

# Vandetanib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Vandetanib: From Thyroid Gland Carcinoma to Renal Cell Carcinoma
{: .text-alpha }

## One-Sentence Summary

Vandetanib is a multi-kinase inhibitor originally used for thyroid gland carcinoma (medullary thyroid cancer).
The TxGNN model predicts it may be effective for **renal cell carcinoma**,
with **4 clinical trials** (two terminated early with very few patients) and **5 publications** currently linked to this direction, none of which shows efficacy in renal cancer.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thyroid gland carcinoma |
| Predicted New Indication | Renal cell carcinoma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L2 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on the linked trial and literature material, vandetanib inhibits VEGFR2, RET and EGFR. Its efficacy in thyroid cancer (RET-driven medullary thyroid cancer) is established.

Clear cell renal cell carcinoma is typically driven by VHL loss and HIF/VEGF activation. Because vandetanib blocks VEGFR2, an anti-angiogenic effect is biologically plausible. Other VEGFR-targeting kinase inhibitors are already used in renal cancer, which supports the idea. However, this is a mechanistic inference only. Direct proof of benefit in renal cell carcinoma is lacking: the Phase 2 studies reported no results here, and two were terminated early with very small enrollment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Vandetanib in von Hippel-Lindau disease with renal tumors; closest biology to clear cell RCC, but no results provided |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib plus metformin in HLRCC/SDH-associated or sporadic papillary RCC; too small to draw conclusions |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Vandetanib in advanced clear cell renal carcinoma; terminated at 3 patients, essentially no efficacy information |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Carboplatin/gemcitabine ± vandetanib in advanced urothelial cancer; only indirectly relevant to renal cancer, no efficacy outcome provided |

---

## Literature Evidence

The publications linked to renal cell carcinoma are mostly indirect (thyroid/RET reviews and class-level safety analyses). None demonstrates vandetanib efficacy in renal cancer.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | Targeted therapy for fumarate hydratase-deficient RCC; no standard regimen, several Phase 2 combination trials ongoing |
| [22651902](https://pubmed.ncbi.nlm.nih.gov/22651902/) | 2012 | Meta-analysis (safety) | Cancer Treat Rev | Treatment-related mortality with VEGFR TKIs in advanced solid tumors |
| [23981115](https://pubmed.ncbi.nlm.nih.gov/23981115/) | 2014 | Meta-analysis (safety) | Br J Clin Pharmacol | Incidence and risk of hepatic toxicity with anti-angiogenic TKIs |
| [32105149](https://pubmed.ncbi.nlm.nih.gov/32105149/) | 2020 | Meta-analysis (safety) | Expert Rev Clin Pharmacol | Proteinuria risk with VEGFR TKIs, including vandetanib |
| [32691271](https://pubmed.ncbi.nlm.nih.gov/32691271/) | 2021 | Long-term follow-up | Endocrine | Long-term safety of vandetanib in advanced medullary thyroid cancer |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Anti-angiogenic agents, including vandetanib, in solid tumors |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educ Book | Systemic therapy for advanced thyroid cancers; vandetanib as a RET inhibitor in MTC |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical (mouse model) | Mol Cancer Res | TFE3-translocation RCC mouse model suggesting new therapeutic targets; does not establish vandetanib activity |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02378590 | CAPRELSA | Not specified | Not specified |
| 02378582 | CAPRELSA | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor targeting VEGFR2, RET and EGFR), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; QT interval/ECG, electrolytes (potassium, calcium, magnesium), thyroid function, blood pressure, renal and liver function are suggested by the contraindication and class-safety data |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**:
  - Cardiovascular and QT: long QT syndrome (including familial), torsades de pointes, hypertension, congestive heart failure
  - Metabolic and electrolyte: potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disorders
  - Thyroid: hypothyroidism, myxedema, congenital hypothyroidism
  - Organ: impaired renal function, interstitial lung disease
  - Neurovascular: brain ischemia, transient ischemic attack, posterior leukoencephalopathy syndrome
- **Drug Interactions**: 100 interactions were found. Major-level examples include clarithromycin, levofloxacin, dolasetron, palonosetron, picosulfuric acid, sodium sulfate and polyethylene glycol (3350 with electrolytes). Moderate-level examples include famotidine, metformin, loperamide, dexamethasone, bisacodyl and lactitol. Several major interactors are QT-prolonging or electrolyte-altering agents, consistent with the QT concerns above.
- **Class-level safety literature**: VEGFR TKIs are associated with hepatic toxicity, proteinuria and treatment-related mortality (see the meta-analyses above). A French drug bulletin review (PMID 23185843) also judged vandetanib too dangerous in medullary thyroid cancer.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible and two Phase 2 studies exist in kidney cancer, but one is completed without reported results, and two others were terminated at 3 and 7 patients. There is no demonstrated efficacy, and the safety profile (QT prolongation, hypertension and others) is substantial. This is best treated as a research question rather than a ready-to-use new indication. The other predicted indications (rare RCC subtypes, childhood kidney carcinoma, angiolipoma, familial pneumothorax) rest on model prediction alone and should be held.

**To proceed, the following is needed:**
- Retrieve the results of NCT00566995 (VHL-associated renal tumors) and confirm any efficacy signal
- Obtain and review the Health Canada package insert for warnings and contraindications (a blocking gap for safety screening)
- Obtain mechanism of action data from DrugBank to support the mechanistic-link analysis
- Define a safety monitoring plan covering QT/ECG, electrolytes, blood pressure, and liver and renal function
- Establish a DDI management plan, especially for QT-prolonging co-medications
- Compare against existing standard VEGFR-targeted RCC therapies before designing any new trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

