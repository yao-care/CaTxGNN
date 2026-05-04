---
layout: default
title: Dorzolamide
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Dorzolamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dorzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase inhibitor (CAI) with established global efficacy in lowering intraocular pressure (IOP) for open-angle glaucoma and ocular hypertension, though it currently has no registered products in Canada.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with **1 completed Phase 2 clinical trial** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / Ocular hypertension (established global approval; no Canadian DINs on file) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dorzolamide is a sulfonamide-class carbonic anhydrase inhibitor that acts locally on the ciliary epithelium of the eye. By inhibiting carbonic anhydrase isoforms II and IV, it blocks bicarbonate and sodium secretion, reducing aqueous humor production by approximately 17–26%. When combined with timolol as a fixed formulation (Cosopt®), the synergistic IOP-lowering effect reaches approximately 33%. Although formal MOA data from DrugBank could not be retrieved for this report, the drug's pharmacological mechanism is extensively documented across decades of published literature and regulatory submissions.

Primary hereditary glaucoma (PHG; also known as primary congenital glaucoma, PCG) is a rare genetic disorder caused by developmental defects of the trabecular meshwork that impair aqueous humor outflow, leading to pathologically elevated IOP and progressive optic nerve damage. Surgical goniotomy or trabeculotomy remains first-line treatment, but adjunctive medical IOP reduction is critical for pre-surgical optimization, post-surgical management, and cases where surgery carries prohibitive risk. Because dorzolamide reduces aqueous production rather than improving outflow, it directly compensates for the outflow obstruction characteristic of PHG — a mechanistically coherent approach even when the anatomical route of drainage is compromised.

Dorzolamide's well-established pediatric tolerability profile, already observed in trials for juvenile and congenital glaucoma, further supports its applicability here. The IOP-lowering pathway shared between open-angle glaucoma and hereditary glaucoma makes this TxGNN prediction biologically plausible, even though the underlying genetic etiology of PHG (e.g., *CYP1B1*, *LTBP2* mutations) differs from acquired open-angle disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assessed ocular hypotensive effects of latanoprost and dorzolamide in primary pediatric glaucoma (PG) refractory to surgical procedures; evaluated both IOP-lowering efficacy and safety in a pediatric population — the only completed Phase 2 trial directly targeting this glaucoma subtype using a CAI-class agent |

Currently no ICTRP-registered trials are available for this indication.

---

## Literature Evidence

Currently no related literature directly linking dorzolamide to primary hereditary glaucoma is available.

---

## Canada Market Information

Dorzolamide has no registered Drug Identification Numbers (DINs) in Canada. There are no approved products or licensing records on file with Health Canada at this time. Patients requiring dorzolamide in Canada would need to access it through the Special Access Program (SAP) or via cross-border importation under physician oversight.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not retrievable from local regulatory sources for this report (Data Gaps DG001 and DG002). Remediation requires downloading the TFDA/Health Canada product monograph PDF and querying the DrugBank API for complete MOA and safety profiles.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model assigns a near-maximum prediction score (99.99%), and dorzolamide's carbonic anhydrase inhibition mechanism directly addresses the core pathophysiology of elevated IOP in primary hereditary glaucoma. The one completed Phase 2 trial (NCT01527682) provides direct clinical evidence for the CAI drug class in pediatric glaucoma refractory to surgery. However, the overall evidence base for PHG specifically remains thin, and no Canadian regulatory authorization exists for any indication.

**To proceed, the following is needed:**
- Resolve Data Gap DG001: Retrieve the product monograph / package insert (PDF) from TFDA or Health Canada to complete safety profiling (key warnings, contraindications)
- Resolve Data Gap DG002: Query DrugBank API for formal MOA documentation (DB00869)
- Retrieve and review the full published results from NCT01527682 (completed 2016) for specific efficacy and safety endpoints in the PHG population
- Conduct a pediatric-specific risk assessment, including long-term ocular surface effects and systemic absorption in neonates and infants
- Consult a pediatric ophthalmologist to assess whether filing a New Drug Submission (NDS) or using the Special Access Program (SAP) with Health Canada is the appropriate regulatory pathway
- Consider whether a prospective registry study or dedicated Phase 3 trial in PHG patients is feasible given the orphan disease classification of this condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

