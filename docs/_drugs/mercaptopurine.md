---
layout: default
title: Mercaptopurine
parent: High Evidence (L1-L2)
nav_order: 501
evidence_level: L2
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine (6-MP) is a purine antimetabolite historically established as a maintenance-therapy backbone for acute lymphoblastic leukemia (ALL). The TxGNN model predicts it may also be effective for **Myeloid Leukemia**, with **29 clinical trials** and **20 publications** retrieved — but most of this evidence is decades-old background material rather than direct, current confirmatory trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukemia (established public knowledge — not captured in this evidence pack; see note below) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

*Note: The evidence pack's `taiwan_regulatory.licenses` and `drug.original_indications` fields are empty, and `original_moa` is flagged as a data gap. The original-indication statement above reflects widely established pharmacology (mercaptopurine's classic ALL-maintenance use), not evidence-pack data.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack (flagged as data gap DG002). Based on known pharmacology, mercaptopurine is a purine analog antimetabolite (thiopurine class) that is converted intracellularly via HGPRT into thioguanine nucleotides; these are incorporated into DNA/RNA and block de novo purine synthesis, producing broad antiproliferative cytotoxicity in rapidly dividing cells. Its efficacy in acute lymphoblastic leukemia is well proven — it remains a cornerstone of ALL maintenance therapy.

Both acute lymphoblastic leukemia and myeloid leukemia are hematologic malignancies arising from bone-marrow precursor cells, so an antimetabolite that broadly disrupts nucleotide synthesis is mechanistically plausible against myeloid blasts as well as lymphoid blasts, even without lineage-specific targeting.

However, the retrieved evidence shows this rationale is largely historical rather than reflecting current standard practice. From the 1960s through the 1990s, several studies combined mercaptopurine with cytarabine or cyclophosphamide for post-remission/maintenance therapy of AML, and mercaptopurine also appears as a maintenance component in classic acute promyelocytic leukemia (APL) protocols (e.g., AIDA, PETHEMA LPA2005). But modern AML standard-of-care (anthracycline + cytarabine induction, with targeted agents in appropriate subsets) no longer includes mercaptopurine as a core agent. This places the association at L2 evidence — supported by a real RCT and multiple cohort/case series, but largely superseded by current guidelines rather than actively pursued.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | ApoAML trial: venetoclax + 6-mercaptopurine combination for relapsed/refractory AML |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | Hydroxyurea+VPA or 6-MP+VPA combination in AML/high-risk MDS patients unfit for standard therapy |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | Completed | N/A | ATRA+idarubicin (AIDA) induction for APL; MTX+mercaptopurine used as salvage therapy for molecular/hematological relapse |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | Completed | 300 | PETHEMA LPA2005: risk-adapted APL protocol using ATRA + low-dose methotrexate + mercaptopurine as maintenance |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Phase 4 | Unknown | 80 | AIDA2000: risk-adapted APL therapy; 2-year maintenance with 6-mercaptopurine, methotrexate, and ATRA |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Tretinoin ± arsenic trioxide consolidation for APL; maintenance with intermittent tretinoin plus mercaptopurine/methotrexate vs. tretinoin alone |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | N/A | Unknown | 1068 | AIDA protocol guideline for newly diagnosed APL; evaluates intermittent maintenance with ATRA, methotrexate, and 6-mercaptopurine |
| [NCT00599937](https://clinicaltrials.gov/study/NCT00599937) | Phase 3 | Completed | 576 | Assessed optimal timing of chemotherapy with/after ATRA and the role of maintenance therapy (incl. mercaptopurine) in APL |
| [NCT02521493](https://clinicaltrials.gov/study/NCT02521493) | Phase 3 | Active, not recruiting | 280 | Risk-stratified chemotherapy for AML/MDS in Down syndrome — background trial, mercaptopurine not a primary study drug (relevance grade C) |
| [NCT00700544](https://clinicaltrials.gov/study/NCT00700544) | Phase 3 | Completed | 330 | Androgen therapy during post-remission maintenance for elderly AML — background trial, not a direct mercaptopurine intervention (relevance grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | Int J Hematol | JALSG-AML92: adding etoposide to daunorubicin/cytarabine/6-MP induction showed no additional benefit in adult AML |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | J Korean Med Sci | Oral maintenance chemotherapy with 6-MP and methotrexate improved leukemia-free survival in transplant-ineligible AML patients |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Cohort | Cancer Investigation | High-dose continuous-infusion 6-MP + intermediate-dose cytarabine explored as first-remission consolidation in pediatric AML |
| [5220682](https://pubmed.ncbi.nlm.nih.gov/5220682/) | 1966 | Case Series | Minnesota Medicine | Early report of AML treatment with 6-mercaptopurine and cyclophosphamide |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | Case Series | Int J Hematol | Intensive individualized induction with behenoyl cytarabine, daunorubicin, and 6-MP followed by intensive consolidation in adult AML |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | RCT | Cancer Chemother Pharmacol | Nationwide randomized trial comparing daunorubicin vs. aclarubicin combined with BHAC, 6-MP, and prednisolone in untreated adult AML |
| [8558199](https://pubmed.ncbi.nlm.nih.gov/8558199/) | 1996 | RCT | J Clin Oncol | Japan Leukemia Study Group randomized trial of BHAC vs. cytarabine (with 6-MP-containing regimens) ± ubenimex in adult AML |
| [1657335](https://pubmed.ncbi.nlm.nih.gov/1657335/) | 1991 | Case Series | Chinese Medical Journal | Combination induction/consolidation with cytarabine, daunorubicin, and 6-mercaptopurine in adult AML |
| [265178](https://pubmed.ncbi.nlm.nih.gov/265178/) | 1977 | Case Series | Blood | Sequential subcutaneous cytarabine and oral mercaptopurine in juvenile chronic myeloid leukemia (3 cases) |
| [28152123](https://pubmed.ncbi.nlm.nih.gov/28152123/) | 2017 | Cohort | JAMA Oncology | Association of autoimmune-disease immunosuppressive therapy (including thiopurines) with subsequent MDS/AML — safety-signal context, not efficacy evidence |

---

## Canada Market Information

Mercaptopurine currently has no Health Canada Drug Identification Number (DIN) on file in this evidence pack — the drug is marked **Not Marketed**, with 0 total licenses recorded.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Purine antimetabolite / thiopurine class) |
| Myelosuppression Risk | High — well-documented risk of neutropenia and thrombocytopenia; risk is markedly increased in patients with TPMT or NUDT15 genetic deficiency |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests, renal function; consider TPMT/NUDT15 genotyping or phenotyping before initiation |
| Handling Protection | Must follow institutional cytotoxic/hazardous drug handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack — DG001 is a Blocking-severity gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The myeloid-leukemia signal is supported by only L2 evidence, and the underlying rationale is largely historical (1960s–1990s combination regimens and legacy APL maintenance protocols) rather than current standard-of-care practice.
- A Blocking-severity data gap (TFDA/regulatory warnings and contraindications, DG001) currently prevents any S1 safety pre-assessment, and the drug is not marketed in Canada (0 DINs).
- For context: two other predicted indications for this drug — **precursor lymphoblastic lymphoma/leukemia** and **acute lymphoblastic leukemia** — show much stronger L1 evidence and a "Proceed with Guardrails" recommendation, consistent with mercaptopurine's established mechanism; these may warrant prioritization over the myeloid-leukemia signal.

**To proceed, the following is needed:**
- TFDA/Health Canada product-label warnings, contraindications, and drug-interaction data (DG001, Blocking)
- Confirmed mechanism-of-action documentation from DrugBank (DG002, High)
- A focused literature/trial search for contemporary (post-2010) mercaptopurine-AML combination studies, since current evidence is dominated by legacy regimens no longer in standard use
- Clarification of whether the TxGNN "myeloid leukemia" node maps to AML specifically or a broader myeloid neoplasm category, given the mixed APL/AML/CML trial matches retrieved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

