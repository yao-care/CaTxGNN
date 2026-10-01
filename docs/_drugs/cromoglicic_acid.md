---
layout: default
title: Cromoglicic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 226
evidence_level: L3
indication_count: 10
---

# Cromoglicic Acid
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Cromoglicic Acid: From Allergic Conditions to Ulcerative Proctosigmoiditis

## One-Sentence Summary

Cromoglicic acid (cromolyn) is a mast cell stabilizer, marketed in Canada in products such as eye drops and an oral form (Nalcrom). The Canadian licence records provided contain no approved-indication text, so the allergic-disease use here is inferred from the product types and the literature.
The TxGNN model predicts it may be effective for **ulcerative proctosigmoiditis**, but there are **0 clinical trials** and **2 publications**, and the only cromolyn-specific study found a **negative result**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic conditions (inferred; no indication text in the licence records) |
| Predicted New Indication | Ulcerative proctosigmoiditis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Cromoglicic acid is generally understood as a mast cell stabilizer that inhibits the release of inflammatory mediators. Its efficacy in allergic disease is established. Mechanistically, it could plausibly apply to mucosal inflammation such as ulcerative proctosigmoiditis, an inflammatory condition of the rectum and sigmoid colon.

That plausibility is weakened by clinical data. A double-blind, placebo-controlled study (PMID 3090860) tested rectal disodium cromoglycate in exactly this condition and found it ineffective. The very high TxGNN score (99.99%) is therefore contradicted by direct clinical evidence, and the prediction may reflect knowledge-graph proximity rather than true efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3090860](https://pubmed.ncbi.nlm.nih.gov/3090860/) | 1986 | Double-blind placebo-controlled study | Acta Med Scand | 43 patients with active ulcerative proctosigmoiditis received placebo (n=22) or 600 mg DSCG enemas (n=21) for 8 weeks. There were no statistically significant differences in bowel frequency, rectal bleeding or general assessments. Local DSCG was ineffective. |
| [1967326](https://pubmed.ncbi.nlm.nih.gov/1967326/) | 1990 | Review | Med Clin North Am | Review of topical therapy for ulcerative colitis. It notes that studies have not confirmed the superiority of one treatment over another, though high-dose 5-ASA enemas appear better than hydrocortisone enemas. The available excerpt shows no cromolyn-specific finding. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2009277 | CROMOLYN EYE DROPS |
| 500895 | NALCROM |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only cromolyn-specific clinical evidence in ulcerative proctosigmoiditis is a placebo-controlled study showing no benefit. There are no registered trials, and the high model score is not supported by clinical data. Nine other predicted indications were also assessed and all were rated Hold or Research Question. Allergic urticaria was the only one with usable signals, at L4 and Research Question, based on cromolyn food-allergy studies (PMIDs 1708197, 3091307). It may be a better candidate to pursue than this one.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently missing, which blocks safety screening)
- Mechanism-of-action data (e.g., from DrugBank)
- Critical appraisal of PMID 3090860 (dose, formulation, disease severity) to judge whether a different regimen could justify re-testing
- Approved-indication text and dosage forms for the two Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

