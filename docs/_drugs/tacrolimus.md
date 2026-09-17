---
layout: default
title: Tacrolimus
parent: High Evidence (L1-L2)
nav_order: 743
evidence_level: L1
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **3** 
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

Using no additional skill — this is a direct content-generation task fully specified by the report template already provided; proceeding straight to the report.

# Tacrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

> Tacrolimus (DrugBank DB00864) is a calcineurin inhibitor whose topical formulation (Protopic®) is well established for atopic dermatitis and whose systemic formulations prevent organ transplant rejection.
> The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**, with **2 clinical trials** and **20 publications** currently supporting this direction, including two completed dermatology-specific trials directly on facial seborrheic dermatitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in regulatory dataset (data gap). Per literature evidence in this pack, topical tacrolimus is originally indicated for atopic dermatitis; systemic tacrolimus for prevention of organ transplant rejection |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A formal DrugBank mechanism-of-action entry is not currently available for this candidate (data gap). However, the literature evidence collected in this pack consistently and independently describes tacrolimus's mechanism: it is a **calcineurin inhibitor** that suppresses antigen-specific T-cell activation and downregulates the inflammatory cytokine cascade. This is the same mechanism that underlies its established, marketed use as a topical treatment for atopic dermatitis (Protopic®).

Seborrheic dermatitis shares key pathophysiological features with atopic dermatitis — both are chronic, relapsing inflammatory skin conditions with a T-cell–mediated component, and seborrheic dermatitis additionally involves an inflammatory host response to *Malassezia* yeast colonization rather than a primary infection. Because calcineurin inhibition dampens local T-cell–driven inflammation without the skin-atrophy risk of topical corticosteroids, it is mechanistically well suited to a condition like seborrheic dermatitis where long-term/maintenance therapy is needed and steroid-sparing is clinically desirable.

This mechanistic rationale is directly corroborated by clinical evidence: two completed trials in this pack (Phase 3 and Phase 4) evaluated tacrolimus ointment specifically as a **maintenance therapy** for severe facial seborrheic dermatitis, explicitly to reduce relapse frequency and reduce reliance on topical steroids — reinforcing that the TxGNN prediction reflects a pathway already being explored clinically, not a purely theoretical extrapolation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated tacrolimus ointment (Protopic®) as maintenance treatment for severe facial seborrheic dermatitis, aiming to prolong remission and reduce topical steroid use |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Assessed whether proactive once/twice-weekly 0.1% tacrolimus ointment maintains remission and reduces exacerbation incidence in adult facial seborrheic dermatitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter, double-blind RCT: tacrolimus 0.1% vs. ciclopiroxolamine 1% for maintenance therapy of severe facial seborrheic dermatitis |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | RCT/Cohort | Annals of Dermatology | 0.1% tacrolimus ointment maintenance therapy effective for facial seborrheic dermatitis, paralleling proactive maintenance strategy used in atopic dermatitis |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT | Annals of Parasitology | Clinical trial comparing sertaconazole 2% cream vs. tacrolimus 0.03% cream in 60 patients with seborrheic dermatitis |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | RCT | Indian J Dermatol Venereol Leprol | Compared oral itraconazole + topical tacrolimus vs. topical tacrolimus alone for maintenance treatment of seborrheic dermatitis (Vietnam cohort) |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Systematic Review/Meta-analysis | Clin Exp Allergy | Cochrane network meta-analysis of topical anti-inflammatory treatments for eczema, including topical calcineurin inhibitors |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments (antifungals, keratolytics, corticosteroids, calcineurin inhibitors) for facial seborrheic dermatitis |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Reviews pathophysiology, safety, and efficacy of topical calcineurin inhibitors specifically for seborrheic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Current status and therapeutic horizons for facial seborrheic dermatitis treatment |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open pilot study | J Am Acad Dermatol | Open-label pilot study of 0.1% tacrolimus in 18 seborrheic dermatitis patients: 61% achieved complete clearance |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | Review of topical tacrolimus/pimecrolimus future directions, including use in seborrheic dermatitis and other inflammatory dermatoses |

---

## Canada Market Information

No authorized products are currently listed in the regulatory dataset for this candidate (0 DINs; market status: Not Marketed). No licensure records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Formal warnings, contraindications, and drug interaction data are not currently available in this evidence pack (flagged as a **Blocking** data gap — DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong and directly supported by two completed dermatology-specific trials (Phase 3 and Phase 4) plus multiple RCTs and reviews evaluating tacrolimus specifically in seborrheic dermatitis — meeting an L1 evidence bar. However, this product is not currently marketed in Canada for any indication (0 DINs), and formal safety labeling data (warnings/contraindications) is missing, which blocks a full safety review.

**To proceed, the following is needed:**
- Product monograph / warnings & contraindications data (resolves Blocking data gap DG001)
- Formal DrugBank/regulatory MOA confirmation (resolves data gap DG002)
- Regulatory pathway assessment, since the drug currently has zero licensed products in Canada (new submission or import pathway required)
- Confirmation of topical route availability/compatibility, since the predicted indication requires a topical formulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

