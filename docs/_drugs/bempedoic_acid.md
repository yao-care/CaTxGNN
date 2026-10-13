---
layout: default
title: Bempedoic Acid
parent: Model Prediction Only (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid: From LDL-Cholesterol Lowering to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Bempedoic acid is a lipid-lowering drug that inhibits ATP-citrate lyase (ACL) and is marketed in Canada as NILEMDO.
The TxGNN model's top-ranked prediction is **hyperthyroidism**, but it has no supporting trials or literature, so this report focuses on the best-supported prediction, **homozygous familial hypercholesterolemia (HoFH)**.
HoFH has **0 registered clinical trials** and **18 publications** (mostly reviews, plus one real-world cohort study).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the licence data compiled for this report (the drug is a lipid-lowering agent) |
| Predicted New Indication | Homozygous familial hypercholesterolemia (best-supported of the top 10 predictions; the rank 1 prediction is hyperthyroidism) |
| TxGNN Prediction Score | 99.48% (hyperthyroidism, rank 1: 99.61%) |
| Evidence Level | L4 (HoFH); L5 (hyperthyroidism and all other predictions) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (HoFH may be treated as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known pharmacology, bempedoic acid inhibits ACL, an enzyme upstream of HMG-CoA reductase. This reduces hepatic cholesterol synthesis and upregulates LDL receptors, lowering LDL-C.

**HoFH (best-supported prediction):** HoFH is characterised by extremely high LDL-C, caused mainly by severely impaired or absent LDL receptor function. The mechanistic rationale for lowering cholesterol synthesis is reasonable. However, because bempedoic acid relies partly on LDL receptor upregulation, efficacy may be limited when receptor function is minimal. The drug is marketed for LDL-C lowering, which supports its general safety data, but not HoFH-specific efficacy.

**Top-ranked predictions (hyperthyroidism and others):** The high TxGNN scores for hyperthyroidism, thyroid hormone resistance, hyperthyroxinemia, and the veterinary or viral conditions (malignant catarrh, infectious bovine rhinotracheitis, cytomegalovirus infection) are graph-based predictions only. No clear mechanistic link or supporting evidence exists, and several are likely knowledge-graph artefacts. Thyroid status influences lipid metabolism, but this does not imply therapeutic benefit. The osteoporosis and multiple endocrine neoplasia predictions likewise lack a plausible mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 10 most relevant publications for HoFH are listed below (real-world and consensus documents first, then reviews).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Cohort (real-world) | J Clin Lipidol | Evaluates efficacy and tolerability of bempedoic acid in HoFH patients |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Review (expert consensus) | J Clin Lipidol | National Lipid Association update on familial hypercholesterolemia diagnosis and management |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | Emerging LDL-C-lowering therapies, including bempedoic acid and inclisiran |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Review | Exp Mol Pathol | Innovative therapies for managing HoFH |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Review | J Atheroscler Thromb | Advances in HoFH treatment aimed at aggressive LDL-C reduction |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Review | Cardiol Rev | Evinacumab for HoFH, discussed alongside PCSK9 inhibitors and bempedoic acid |
| [34081216](https://pubmed.ncbi.nlm.nih.gov/34081216/) | 2021 | Review | Curr Cardiol Rep | Updates in managing familial and refractory hypercholesterolemias beyond statins and PCSK9 inhibitors |
| [42761917](https://pubmed.ncbi.nlm.nih.gov/42761917/) | 2026 | Review | Methodist DeBakey Cardiovasc J | Overview of familial hypercholesterolemia genetics, prevalence and ASCVD risk |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Review | Am J Prev Cardiol | Importance of sustained LDL-C lowering for ASCVD prevention |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Traditional and novel non-statin lipid-lowering drugs |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02562782 | NILEMDO | Not specified | Not specified |

---

## Safety Considerations

**Drug Interactions:** 23 interactions were recorded in total, of which 20 are listed in the compiled data.

- **Major:** corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone, deflazacort, fludrocortisone), levofloxacin, and simvastatin.
- **Moderate:** empagliflozin, glyburide, repaglinide, rifaximin, rosuvastatin, selexipag, fexofenadine, and revefenacin.

Package insert warnings and contraindications were not available for this report; please refer to the Health Canada package insert. For the pregnancy-associated osteoporosis prediction, use of a lipid-lowering agent in pregnancy raises additional safety concerns.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The highest-scoring predictions (hyperthyroidism and others) rest on model scores alone, without trials, literature or a plausible mechanism, and are best treated as likely artefacts.
- HoFH has the strongest support (L4), but it consists of reviews and one real-world cohort study. The reliance of bempedoic acid on LDL receptor upregulation may limit efficacy in HoFH. It can be pursued as a research question rather than a clinical recommendation.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Approved indication and dosage form details for the NILEMDO licence
- Critical appraisal of the real-world HoFH study (PMID 41274797) and, ideally, a prospective controlled trial in HoFH with stratification by LDL receptor function
- A review of the major interactions (corticosteroids, simvastatin, levofloxacin) for a monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

