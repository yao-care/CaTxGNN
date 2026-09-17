---
layout: default
title: Latanoprost
parent: High Evidence (L1-L2)
nav_order: 447
evidence_level: L2
indication_count: 10
---

# Latanoprost
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Latanoprost: From Glaucoma/Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin F2α analogue whose established pharmacology — FP-receptor agonism that increases uveoscleral aqueous humor outflow and lowers intraocular pressure (IOP) — already underlies its known use in glaucoma/ocular hypertension. The TxGNN model's top-ranked prediction, **Primary Hereditary Glaucoma**, is supported by **1 completed Phase 2 clinical trial**, and the evidence pack's own rationale notes this is closer to a confirmatory extension of existing pharmacology than a novel hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed by license text in this evidence pack (`original_indications` empty — see Data Gaps below); mechanistically consistent with known glaucoma/IOP-lowering use per the prediction rationale |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Local Market Status (`taiwan_regulatory`) | Not Marketed |
| Number of Licenses/DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A structured DrugBank mechanism-of-action record was not returned for this drug (Data Gap DG002, High severity). However, the evidence pack's own repurposing rationale documents latanoprost's core, well-established pharmacology: it is a prostaglandin F2α analogue acting as an FP-receptor agonist, which increases aqueous humor outflow via the uveoscleral pathway and thereby lowers intraocular pressure.

Primary hereditary glaucoma is pathophysiologically defined by impaired aqueous outflow leading to elevated IOP — precisely the target that latanoprost's mechanism addresses. Because of this near-complete mechanistic overlap, the evidence pack itself characterizes this "new" indication as essentially an extension of latanoprost's already-established pharmacological effect rather than a genuinely novel repurposing hypothesis — consistent with it scoring highest (99.88%) among all ten TxGNN candidates for this drug.

By contrast, the model's lower-ranked candidates for this drug (e.g., visceral calciphylaxis, thoracic outlet syndrome variants, angiodysplasia of stomach) have no identifiable mechanistic link to FP-receptor agonism and are flagged in the pack as likely knowledge-graph co-occurrence artifacts rather than biologically grounded hypotheses.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assessed ocular hypotensive efficacy and safety of latanoprost combined with dorzolamide in pediatric/primary glaucoma patients refractory to surgical treatment. |

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug-drug interactions) was retrieved for this record — all fields returned as data gaps, and the DDI query returned no results. This is flagged as a **Blocking** data gap (DG001: TFDA label warnings/contraindications) that currently prevents entry into the S1 safety pre-screening stage. Please refer to the official package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 RCT directly tests latanoprost (combined with a carbonic anhydrase inhibitor) in a closely related, surgically refractory glaucoma population, and the mechanistic overlap between latanoprost's FP-receptor pharmacology and this indication's pathophysiology is very strong. However, the drug is not currently marketed in this jurisdiction (0 licenses) and core safety documentation is missing.

**To proceed, the following is needed:**
- TFDA product label warnings/contraindications (DG001, Blocking) — retrieve via TFDA official site, download and parse label PDF
- Detailed DrugBank mechanism-of-action record (DG002, High) — query DrugBank API
- Confirmation of local marketing authorization status, given `total_licenses = 0`
- Additional literature search validation, since 0 publications were identified for this specific indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

