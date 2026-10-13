---
layout: default
title: Dobutamine
parent: Model Prediction Only (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
---

# Dobutamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Dobutamine: From Cardiac Inotropic Support to Alopecia (Prediction Only)

## One-Sentence Summary

Dobutamine is an injectable beta-1 adrenergic agonist (inotrope) marketed in Canada. The Health Canada records compiled for this report do not include approved indication text.
The TxGNN model predicts it may be effective for **alopecia**, but there are **0 clinical trials** and only **1 publication** (a veterinary case report about minoxidil toxicity, not a test of dobutamine), so this is a **model prediction without supporting evidence**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (Health Canada indication text is empty) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, dobutamine is a beta-1 adrenergic agonist used intravenously to increase cardiac contractility. It has no known action on hair follicle biology.

The one retrieved paper describes heart failure in a cat caused by minoxidil intoxication, in which dobutamine was used to treat hypotension. It documents an adverse cardiac effect of a hair-growth drug, not a therapeutic use of dobutamine for alopecia.

The high TxGNN score most likely reflects network proximity to minoxidil, a vasodilator that shares cardiovascular targets, rather than true efficacy. The link between the original use and the predicted indication is therefore weak.

Other predictions with similar scores were also reviewed and none has a credible mechanistic rationale: hypotrichosis simplex of the scalp, congenital hypotrichosis milia, diffuse alopecia areata, open-angle glaucoma, Raynaud disease, primary hereditary glaucoma, headache disorder, hypertrichosis and migraine. All are L5 (model prediction only) with a Hold recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case report (veterinary) | Journal of Veterinary Cardiology | A young cat developed heart failure after minoxidil intoxication, and dobutamine was used for hypotension. This is not evidence of benefit in alopecia. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242010 | DOBUTAMINE INJECTION USP | Injection | Not available |
| 02462729 | DOBUTAMINE INJECTION USP | Injection | Not available |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** hypertension and hypertensive disorder, potassium deficiency, atrial fibrillation, aortic stenosis (including aortic valve and supravalvular forms), myocardial infarction and coronary thrombosis, hemoglobinopathy, and hypertrophic cardiomyopathy (including the familial form).
- **Drug interactions:** 100 interactions were recorded. The 20 listed in the data are all rated Moderate, and most involve glucose-lowering drugs. These include acarbose, metformin, pioglitazone, repaglinide, insulin aspart, insulin degludec, and the GLP-1 and SGLT2 agents such as semaglutide, liraglutide, dulaglutide, albiglutide, canagliflozin, dapagliflozin and empagliflozin. DPP-4 inhibitors (alogliptin, linagliptin) and chlorpropamide are also listed. Others are cimetidine, vancomycin, and the appetite suppressants phentermine and diethylpropion.

Please also refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. There are no clinical trials and no supportive literature, and no plausible mechanism links a cardiac inotrope to hair growth. The only paper retrieved concerns toxicity from a different drug, minoxidil. An intravenous cardiac drug also carries significant cardiovascular risks, as the knowledge-graph contraindications show.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank) to test any biological link to hair follicles
- Any preclinical or clinical evidence that dobutamine affects hair growth
- An assessment of whether a systemic IV inotrope is compatible with any realistic route for alopecia treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

