---
layout: default
title: Vorinostat
parent: Moderate Evidence (L3-L4)
nav_order: 975
evidence_level: L4
indication_count: 2
---

# Vorinostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Vorinostat: From Cutaneous T-Cell Lymphoma to Primary Cutaneous B-Cell Lymphoma

## One-Sentence Summary

Vorinostat (an HDAC inhibitor) is marketed as ZOLINZA and is known for treating cutaneous T-cell lymphoma (CTCL).
The TxGNN model predicts it may be effective for **primary cutaneous B-cell lymphoma (PCBCL)**, with a very high score (99.21%).
Evidence is weak: **7 related clinical trials** and **1 publication** are listed, but none enrolled PCBCL patients, and the only literature is a preclinical study in mantle cell lymphoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous T-cell lymphoma (the Canadian license text is not available) |
| Predicted New Indication | Primary cutaneous B-cell lymphoma |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vorinostat is a pan-HDAC (histone deacetylase) inhibitor. Blocking HDACs increases acetylation of histones and other proteins, which can reactivate tumour-suppressor genes and trigger apoptosis and cell-cycle arrest in lymphoid cancers. Detailed mechanism-of-action data are not included in the Evidence Pack, so this description comes from the drug class.

Both CTCL and PCBCL are lymphomas that arise in the skin. They differ in cell of origin, since CTCL is a T-cell disease and PCBCL is a B-cell disease. A 2011 preclinical study (PMID 21652541) showed that vorinostat induces apoptosis in mantle cell lymphoma, a B-cell cancer, by acetylating pro-apoptotic BH3-only gene promoters. This suggests B-cell lymphoma cells can respond to HDAC inhibition.

This is only indirect support. The high TxGNN score most likely reflects the drug's proximity to CTCL and other lymphomas in the knowledge graph, not B-cell-specific data. The CTCL indication rests on T-cell biology and cannot be extrapolated directly to PCBCL.

---

## Clinical Trial Evidence

No retrieved trial enrolled patients with PCBCL. The trials below are general lymphoma or cancer studies, vorinostat combinations, or class-level evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005634](https://clinicaltrials.gov/study/NCT00005634) | Phase 1 | Completed | N/A | Vorinostat (SAHA) in advanced solid tumours; general safety and PK data, no PCBCL-specific data |
| [NCT00045006](https://clinicaltrials.gov/study/NCT00045006) | Phase 1 | Completed | N/A | Oral vorinostat in advanced solid tumours and haematologic malignancies; dosing and safety context only |
| [NCT00499811](https://clinicaltrials.gov/study/NCT00499811) | Phase 1 | Completed | 15 | Vorinostat PK and dosing in solid tumours and lymphomas with liver dysfunction; no efficacy data for PCBCL |
| [NCT01567709](https://clinicaltrials.gov/study/NCT01567709) | Phase 1 | Completed | 34 | Alisertib plus vorinostat in relapsed lymphoid malignancies; the vorinostat effect cannot be isolated |
| [NCT01789255](https://clinicaltrials.gov/study/NCT01789255) | Phase 2 | Completed | 12 | Vorinostat with tacrolimus and methotrexate for graft-versus-host disease prevention after transplant; not a PCBCL treatment setting |
| [NCT01500538](https://clinicaltrials.gov/study/NCT01500538) | Phase 2 | Terminated | 1 | Vorinostat plus eltrombopag in lymphoma (to counter low platelets); terminated with 1 participant, uninformative |
| [NCT00007345](https://clinicaltrials.gov/study/NCT00007345) | Phase 2 | Completed | 131 | Depsipeptide (romidepsin), a different HDAC inhibitor, in CTCL and peripheral T-cell lymphoma; class-level T-cell evidence only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21652541](https://pubmed.ncbi.nlm.nih.gov/21652541/) | 2011 | Preclinical (in vitro) | Clin Cancer Res | Vorinostat induces apoptosis in mantle cell lymphoma through acetylation of pro-apoptotic BH3-only gene promoters |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2327619 | ZOLINZA |

The dosage form and approved indication text are not available for this licence.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HDAC inhibitor, epigenetic) |
| Myelosuppression Risk | Low platelet counts can occur early in treatment, as noted in the vorinostat plus eltrombopag trial (NCT01500538). Please refer to the package insert for the full profile |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Haematological parameters (CBC with platelets); please refer to the package insert for others |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no trial enrolled PCBCL patients. The only literature is a preclinical study in a different B-cell lymphoma (mantle cell lymphoma). The labelled CTCL indication is T-cell biology and cannot be extrapolated directly to PCBCL, so the evidence is too weak to advance beyond the model prediction.

Sezary syndrome, the second predicted indication, is a CTCL variant and falls within vorinostat's existing labelled use. It is supported by the Phase 2b pivotal trial (NCT00091559) and the Phase 3 MAVORIC trial (NCT01728805), in which vorinostat was the comparator against mogamulizumab. That is confirmation of an existing indication, not repurposing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Detailed mechanism-of-action data from DrugBank
- PCBCL-specific evidence: preclinical data in cutaneous B-cell lymphoma models, case series, or clinical trials
- Dosage form and approved-indication text for the Canadian licence, to confirm label scope
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

