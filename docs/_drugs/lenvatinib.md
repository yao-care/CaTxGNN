---
layout: default
title: Lenvatinib
parent: High Evidence (L1-L2)
nav_order: 455
evidence_level: L2
indication_count: 10
---

# Lenvatinib
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

# Lenvatinib: Original Indication Data Gap — Evaluating Predicted Use in Liposarcoma

## One-Sentence Summary

Lenvatinib's original approved indication and detailed mechanism-of-action data are not yet documented in this evidence pack (data gaps DG001/DG002). The TxGNN model predicts it may be effective for **Liposarcoma**, currently supported by **1 clinical trial** and **4 publications**, with the strongest direct evidence coming from a completed Phase Ib/II combination study (lenvatinib + eribulin).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (data gap, see DG001/DG002) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Lenvatinib is not available in this evidence pack (DG002, High severity — pending DrugBank API remediation), and the drug's original approved indication is likewise undocumented (empty `original_indications`). This limits how confidently the mechanistic rationale below can be tied to a "known" original use.

That said, the evidence pack's own repurposing analysis characterizes Lenvatinib as a multi-targeted tyrosine kinase inhibitor (VEGFR1-3, FGFR1-4, PDGFRα, RET, KIT). Dedifferentiated and myxoid liposarcomas frequently show activated FGFR/PDGFRα signaling and are highly dependent on tumor angiogenesis, which provides a plausible mechanistic link to Lenvatinib's anti-angiogenic and anti-FGFR activity.

Importantly, the supporting clinical evidence is for **Lenvatinib used in combination with eribulin**, not as monotherapy — the LEADER study (NCT03526679) tested this combination specifically in advanced adipocytic sarcoma and leiomyosarcoma. Any forward evaluation should treat this as a combination-regimen signal rather than evidence for single-agent Lenvatinib activity in liposarcoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | Completed | 30 | Single-arm study of lenvatinib + eribulin in inoperable/metastatic adipocytic sarcoma and leiomyosarcoma (LEADER study), assessing safety and efficacy of the anti-angiogenic + mitotic-targeting combination |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase Ib/II (single-arm) | Clinical Cancer Research | Primary publication of the LEADER study (NCT03526679): lenvatinib + eribulin in advanced leiomyosarcoma and liposarcoma |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclinical/biomarker | Experimental Hematology & Oncology | CDK4 as a prognostic biomarker in soft tissue sarcoma; discusses treatment sequencing in dedifferentiated liposarcoma |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Research | Broad preclinical evaluation of eribulin combined with mechanistically distinct anticancer agents, including liposarcoma-relevant models |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case report | Case Reports in Oncology | Individualized targeted + surgical + chemotherapy approach produced marked tumor size reduction in metastatic dedifferentiated liposarcoma |

---

## Canada Market Information

Lenvatinib is currently not marketed in Canada under this evidence pack — 0 DINs on file, no license records available.

---

## Cytotoxicity

Lenvatinib's predicted and evidenced indications in this pack (liposarcoma, renal cell carcinoma subtypes) are oncologic, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted tyrosine kinase inhibitor: VEGFR1-3, FGFR1-4, PDGFRα, RET, KIT) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Evidence for Lenvatinib in liposarcoma consists of a single completed Phase Ib/II combination trial (n=30) plus supporting preclinical/case-report literature — sufficient to justify further investigation but not to support clinical decision-making yet. Note that a different candidate in this same evidence pack, **renal carcinoma** (rank 7), has substantially stronger evidence (Evidence Level L1, multiple completed Phase 3 RCTs including CLEAR, "Proceed with Guardrails" recommendation) and may warrant separate, higher-priority evaluation.

**To proceed, the following is needed:**
- Health Canada/TFDA label data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- Original approved indication data, to properly frame this as repurposing vs. label expansion
- Randomized/controlled evidence specifically in liposarcoma (current evidence is single-arm, combination-only)
- Drug interaction data for the lenvatinib + eribulin regimen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

