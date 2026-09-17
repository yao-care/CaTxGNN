---
layout: default
title: Nelarabine
parent: Model Prediction Only (L5)
nav_order: 544
evidence_level: L5
indication_count: 1
---

# Nelarabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Nelarabine: From T-Cell Acute Lymphoblastic Leukemia/Lymphoma to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Nelarabine (DrugBank DB01280) is a deoxyguanosine analogue prodrug originally developed for T-cell malignancies (T-ALL/T-LBL), acting by selective accumulation and DNA incorporation in T cells to induce apoptosis. The TxGNN model predicts it may be effective for **Relapsing-Remitting Multiple Sclerosis (RRMS)** with a **99.43%** prediction score, but currently **0 clinical trials** and **0 publications** support this direction — the prediction rests on the model alone, and it directly conflicts with nelarabine's known neurotoxicity/demyelination risk.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | T-cell acute lymphoblastic leukemia / lymphoblastic lymphoma (T-ALL/T-LBL) |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, drug-label-level mechanism of action data is not yet available (flagged as a High-severity data gap). Based on the mechanistic rationale captured alongside this prediction, nelarabine is a deoxyguanosine analogue prodrug that, after dephosphorylation, is converted intracellularly to ara-GTP. It preferentially accumulates in T cells and incorporates into DNA, triggering T-cell apoptosis — the basis for its established use in T-cell malignancies (T-ALL/T-LBL).

The model's rationale for RRMS appears to follow the logic that "T-cell depletion" could suppress the autoreactive T-cell attack on myelin that drives MS pathology, giving the two indications a surface-level mechanistic link around "targeting T cells."

However, there is a serious counter-indicator that undermines this rationale: nelarabine carries a black-box warning for severe, dose-limiting neurotoxicity, including peripheral neuropathy, seizures, altered consciousness, and imaging-confirmed demyelination-like leukoencephalopathy. RRMS is itself a CNS demyelinating disease, so the drug's own demyelinating toxicity directly conflicts with the treatment goal. This is not a simple mechanistic extension — it is a mechanistic contradiction that must be resolved before this candidate can advance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Nelarabine currently has no market authorization (DIN) in Canada under this evidence pack (market status: Not Marketed, 0 licenses on record).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine/deoxyguanosine nucleoside analogue, antimetabolite) |
| Myelosuppression Risk | No formal myelosuppression data provided in this evidence pack; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function; given the known black-box neurotoxicity risk, neurological status (peripheral neuropathy, seizure, mental status) and MRI monitoring for leukoencephalopathy should also be considered |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. Note: a Blocking-severity data gap (TFDA/label warnings and contraindications) currently prevents a full S1 safety assessment for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (Evidence Level L5, decision stage S0) — there are zero clinical trials and zero publications for nelarabine in RRMS. More critically, the drug's known black-box neurotoxicity and demyelination-like leukoencephalopathy directly contradicts the treatment goal in a CNS demyelinating disease, making this a mechanistically high-risk rather than merely low-evidence candidate.

**To proceed, the following is needed:**
- Resolve the Blocking data gap: TFDA/regulatory label warnings and contraindications (required before any S1 safety evaluation)
- Confirm formal drug-label MOA data (currently a High-severity gap)
- Independent pharmacology/preclinical review specifically addressing whether nelarabine's demyelinating neurotoxicity is dose- or exposure-separable from any proposed immunomodulatory benefit in MS
- Any preclinical or case-level evidence in a demyelinating-disease model before considering further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

