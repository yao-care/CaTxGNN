---
layout: default
title: Mepolizumab
parent: Moderate Evidence (L3-L4)
nav_order: 500
evidence_level: L4
indication_count: 5
---

# Mepolizumab
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Mepolizumab: From Hypereosinophilic Syndrome to Immune Thrombocytopenia

## One-Sentence Summary

Mepolizumab is an anti-IL-5 monoclonal antibody used clinically in eosinophil-mediated conditions such as hypereosinophilic syndrome (HES). The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**, but this direction is currently supported by only **1 case report** and **no clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypereosinophilic syndrome (HES) — inferred from supporting literature; not documented in the supplied Canada regulatory data |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record (drug-level MOA is a documented data gap). Based on the supporting evidence, mepolizumab inhibits IL-5, depleting eosinophils, and is used to treat hypereosinophilic syndrome (HES).

The link to immune thrombocytopenia is indirect rather than mechanistic: in some HES patients, eosinophil-mediated processes drive secondary/consumptive platelet destruction, and resolving the underlying HES with mepolizumab can improve the resulting thrombocytopenia. This is a case of treating an upstream disease that secondarily resolves a downstream hematologic finding — it is **not** evidence that mepolizumab acts on the classic immune thrombocytopenia (ITP) pathway (autoantibody-mediated platelet clearance by splenic macrophages).

Because the only supporting reference is a single case report of a complement-mediated, hypereosinophilic diathesis (not idiopathic ITP), the biological rationale for this indication is plausible in a narrow eosinophil-driven subgroup but should not be generalized to immune thrombocytopenia as a whole.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case Report | Blood Cells, Molecules & Diseases | Steroid-resistant, hypereosinophilic immune diathesis (with mixed thrombotic microangiopathy) resolved with mepolizumab, alongside improvement in a concomitant platelet-consumption process |

## Other TxGNN-Predicted Indications (Lower Priority)

The same model run also surfaced four additional platelet-related diseases (primary platelet release disorder, pseudo-von Willebrand disease, autoimmune thrombocytopenia, Glanzmann thrombasthenia) with similarly high scores (99.3–99.6%). None have supporting clinical trials, and only one has a single tangential literature reference; all are staged as **Hold (S0)**. These conditions involve structural or intrinsic platelet defects with no known IL-5–related mechanism, and are most likely artifacts of embedding proximity within the platelet-disease node cluster rather than genuine repurposing signals.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a single case report describing an indirect, HES-specific mechanism rather than a direct effect on immune thrombocytopenia; there are no clinical trials, no Canada market presence, and safety/labeling data (TFDA warnings and contraindications) are marked as a **blocking** data gap.

**To proceed, the following is needed:**
- Health Canada / TFDA label data (warnings, contraindications) — currently blocking (DG001)
- Confirmed original mechanism of action documentation (DG002)
- Additional case series or a clinical study specifically evaluating mepolizumab in immune thrombocytopenia (not solely HES-associated cases)
- Mechanistic work clarifying whether any direct IL-5/eosinophil pathway link to immune-mediated platelet destruction exists, versus a purely secondary effect of treating HES
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

