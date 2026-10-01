---
layout: default
title: Imatinib
parent: Moderate Evidence (L3-L4)
nav_order: 466
evidence_level: L4
indication_count: 10
---

# Imatinib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Imatinib: From Chronic Myeloid Leukaemia and GIST to Heart Fibrosarcoma

## One-Sentence Summary

Imatinib is a tyrosine kinase inhibitor first marketed for chronic myeloid leukaemia (CML) and some gastrointestinal stromal tumours (GIST). The TxGNN model predicts it may be effective for **heart fibrosarcoma**, but only **0 clinical trials** and **1 publication** (a general review) touch on this indication, so this is essentially a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CML and GIST (taken from the literature; the Canadian licence records list no indication text) |
| Predicted New Indication | Heart fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Published reviews describe imatinib as a small-molecule inhibitor of the ABL, KIT and PDGFR tyrosine kinases. Its efficacy in CML and KIT-driven GIST is well established.

The only link to fibrosarcoma is indirect. Dermatofibrosarcoma protuberans (DFSP) is a fibrosarcoma-spectrum skin tumour that carries a COL1A1-PDGFB fusion, which drives PDGFR signalling, and it responds to imatinib. TxGNN may be picking up this fibroblastic-tumour and PDGFR connection.

No data in the pack concerns the heart as a tumour site. Extending the DFSP logic to cardiac fibrosarcoma is therefore speculative and needs direct evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for heart fibrosarcoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire International | Overview of imatinib's expanding indications, concluding the evidence is not robust. For example, in Ph+ acute lymphoblastic leukaemia (55 patients), imatinib gave a higher haematological response rate than chemotherapy. It contains nothing specific to heart fibrosarcoma. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2504618 | IMATINIB | — | — |
| 2521202 | IMATINIB | — | — |
| 2399814 | TEVA-IMATINIB | — | — |
| 2253283 | GLEEVEC | — | — |
| 2253275 | GLEEVEC | — | — |

Showing 5 of 16 authorizations. Dosage form and indication text are not populated in the source records.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Medium (neutropenia, thrombocytopenia and anaemia are commonly reported with imatinib) |
| Emetogenicity Classification | Low to moderate (dose-dependent) |
| Monitoring Items | CBC with differential, liver function, renal function, weight and fluid retention |
| Handling Protection | Follow local hazardous-drug handling guidance; please refer to the package insert |

These entries reflect general knowledge of imatinib, not data in the Evidence Pack. Please refer to the package insert warnings and precautions for authoritative details.

---

## Safety Considerations

Please refer to the package insert for safety information.

One report in the retrieved literature is relevant to safety: a case of imatinib-induced drug reaction with eosinophilia and systemic symptoms (DRESS) in a DFSP patient, managed with desensitization ([PMID 30096127](https://pubmed.ncbi.nlm.nih.gov/30096127/), 2018).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on a very high model score but has no trials, no cardiac-specific literature and only an indirect DFSP-based mechanistic link. It is a hypothesis, not a repurposing candidate yet.

Among the other predictions in the pack, evidence is stronger for the fibroblastic neoplasm category, where the literature centres on DFSP (COL1A1-PDGFB-positive). That candidate is rated "Proceed with Guardrails", and the guardrail is to limit use to confirmed COL1A1-PDGFB-positive, unresectable or metastatic disease. It is still supported only by guideline, review and retrospective-level evidence, not by trials in the pack. Liposarcoma and conventional fibrosarcoma are at "Research Question" level, and the remaining predictions have little or no support.

**To proceed, the following is needed:**
- A targeted search for cardiac fibrosarcoma case reports, case series or PDGFRB/PDGFB molecular profiling data
- Detailed mechanism of action data for imatinib (DrugBank)
- Health Canada package insert warnings and contraindications
- Indication text and dosage forms for the Canadian licences, to confirm the original approved indications
- Review of trial outcomes (e.g., NCT00085475, NCT00154388) for any fibrosarcoma or cardiac sarcoma cohorts

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

