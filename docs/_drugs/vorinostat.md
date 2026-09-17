---
layout: default
title: Vorinostat
parent: Moderate Evidence (L3-L4)
nav_order: 831
evidence_level: L3
indication_count: 2
---

# Vorinostat
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **2** 
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

Vorinostat (SAHA) is an oral histone deacetylase (HDAC) inhibitor originally established for the treatment of cutaneous T-cell lymphoma (CTCL). The TxGNN model predicts it may also be effective for **Primary Cutaneous B-Cell Lymphoma**, with **8 clinical trials** and **1 publication** currently available as supporting evidence — though none of these directly target this specific disease population, so the finding remains largely mechanistic at this stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous T-cell lymphoma (CTCL) |
| Predicted New Indication | Primary Cutaneous B-Cell Lymphoma |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The structured `original_moa` field for Vorinostat is currently a data gap. However, the evidence embedded in the clinical trial and literature records confirms that Vorinostat (suberoylanilide hydroxamic acid, SAHA) is a **histone deacetylase (HDAC) inhibitor**. It blocks enzymes required for cancer cell growth and has been used (e.g., approved in the United States) for CTCL in patients with progressive, persistent, or recurrent disease after at least two prior systemic therapies.

CTCL and primary cutaneous B-cell lymphoma are both cutaneous lymphoproliferative malignancies, differing mainly in the lineage of the malignant lymphocyte (T-cell vs. B-cell). Preclinical mechanistic work included in this evidence pack (PMID 21652541) shows that Vorinostat induces apoptosis in mantle cell lymphoma — a B-cell non-Hodgkin lymphoma — by acetylating promoters of pro-apoptotic BH3-only genes. This suggests a biologically plausible mechanism for activity against malignant B cells in general, even though the specific "primary cutaneous" B-cell subtype has not yet been studied clinically. Separately, NCT01567709 provides limited early-phase clinical exposure of Vorinostat in B-cell non-Hodgkin lymphoma patients (combined with an Aurora kinase inhibitor), but this trial is not disease-specific and offers only indirect support.

In short, the mechanistic rationale is reasonable, but direct clinical evidence for this exact indication is currently absent — all available trials involve broader lymphoid-malignancy or solid-tumor populations rather than primary cutaneous B-cell lymphoma itself.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005634](https://clinicaltrials.gov/study/NCT00005634) | Phase 1 | Completed | N/A | Dose-escalation study of SAHA in advanced solid tumors; general oncology population, not disease-specific. |
| [NCT00045006](https://clinicaltrials.gov/study/NCT00045006) | Phase 1 | Completed | N/A | Oral SAHA in advanced solid tumors and hematologic malignancies; not disease-specific. |
| [NCT01789255](https://clinicaltrials.gov/study/NCT01789255) | Phase 2 | Completed | 12 | Vorinostat + tacrolimus + methotrexate for GVHD prevention post-transplant; addresses GVHD, not lymphoma treatment itself. |
| [NCT01567709](https://clinicaltrials.gov/study/NCT01567709) | Phase 1 | Completed | 34 | Vorinostat + Aurora kinase inhibitor (alisertib) in relapsed Hodgkin lymphoma, B-cell NHL, and PTCL. |
| [NCT00007345](https://clinicaltrials.gov/study/NCT00007345) | Phase 2 | Completed | 131 | Depsipeptide (not Vorinostat) in CTCL/relapsed PTCL; different investigational drug, limited direct relevance. |
| [NCT00499811](https://clinicaltrials.gov/study/NCT00499811) | Phase 1 | Completed | 15 | PK study of Vorinostat in solid tumor/lymphoma patients with hepatic dysfunction. |
| [NCT01500538](https://clinicaltrials.gov/study/NCT01500538) | Phase 2 | Terminated | 1 | Vorinostat + eltrombopag pilot in lymphoma; terminated after only 1 patient enrolled. |
| [NCT02943642](https://clinicaltrials.gov/study/NCT02943642) | Phase 2 | Unknown | 162 | Resimmune vs. oral Vorinostat (Zolinza) in Stage IB/IIB mycosis fungoides; Vorinostat used as comparator arm. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21652541](https://pubmed.ncbi.nlm.nih.gov/21652541/) | 2011 | Preclinical/Mechanistic | Clinical Cancer Research | Vorinostat induces apoptosis in mantle cell lymphoma (a B-cell malignancy) by acetylating promoters of pro-apoptotic BH3-only genes, supporting a mechanistic basis for activity against B-cell lymphomas. |

## Canada Market Information

No Health Canada drug licenses (DINs) are currently on record for Vorinostat. Per the regulatory data as of 2026-09-17, the drug is **not marketed** in Canada (0 total licenses), so no authorized product/indication text is available for comparison.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy – epigenetic modulator (Histone Deacetylase inhibitor, HDACi) |
| Myelosuppression Risk | Moderate–High — trial evidence (NCT01500538) notes early-treatment thrombocytopenia; combination regimens with other antineoplastic agents in the trial set report additional cytopenias |
| Emetogenicity Classification | Low–Moderate (oral HDAC inhibitor) |
| Monitoring Items | CBC with platelet count, electrolytes (particularly potassium and magnesium), renal function, liver function |
| Handling Protection | Yes — handle as a hazardous/cytotoxic oral antineoplastic agent (avoid opening/crushing capsules; use PPE per institutional hazardous drug handling protocol) |

## Safety Considerations

Please refer to the package insert for safety information. No structured key warnings, contraindications, or drug–drug interaction data are currently available (DDI query status: not found), and TFDA/Health Canada label data is flagged as a blocking data gap (DG001).

## Additional Predicted Indication: Sézary Syndrome (Rank 2, Not Primary Focus of This Report)

TxGNN also ranked **Sézary syndrome** as a candidate (score 99.07%), backed by 13 clinical trials and 20 publications. Unlike the primary cutaneous B-cell lymphoma prediction above, this finding largely reflects **existing, well-established clinical use** rather than a genuinely novel indication: Sézary syndrome is the leukemic variant of CTCL, and Vorinostat served as the **active comparator arm** in the Phase 3 MAVORIC trial ([NCT01728805](https://clinicaltrials.gov/study/NCT01728805), n=372, Completed) against mogamulizumab in relapsed/refractory mycosis fungoides and Sézary syndrome — indicating Vorinostat is already part of standard clinical practice in this population. This candidate would need to be evaluated separately, as it does not represent a true repurposing opportunity but rather confirmation of an existing use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap exists (DG001: TFDA/Health Canada label warnings and contraindications), which prevents Vorinostat from entering the S1 safety pre-screening stage.
- The evidence for primary cutaneous B-cell lymphoma specifically consists of one preclinical mechanistic paper and no disease-specific completed clinical trials — supportive but not yet clinically validated.
- Vorinostat currently has zero DINs and is not marketed in Canada, so there is no existing regulatory or safety baseline to build on.

**To proceed, the following is needed:**
- TFDA/Health Canada product label (warnings, contraindications) — resolves DG001 (Blocking)
- Structured mechanism-of-action data from DrugBank — resolves DG002 (High)
- Dedicated preclinical or early-phase clinical data in primary cutaneous B-cell lymphoma (current evidence is indirect, from mantle cell lymphoma and general lymphoid-malignancy trials)
- A formal safety/DDI review once label data becomes available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

