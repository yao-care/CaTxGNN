---
layout: default
title: Topotecan
parent: High Evidence (L1-L2)
nav_order: 785
evidence_level: L2
indication_count: 10
---

# Topotecan
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

# Topotecan: From Ovarian, Cervical, and Small Cell Lung Cancer to Breast Carcinoma

## One-Sentence Summary

> Topotecan is a topoisomerase I inhibitor internationally approved for ovarian cancer, cervical cancer, and small cell lung cancer.
> The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
> with **5 clinical trials** and **20 publications** currently touching on this direction — though much of that evidence is older, single-arm, and shows only modest activity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer, cervical cancer, small cell lung cancer (international approvals; not captured in Canadian license data) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available for this record, but the evidence pack's own mechanistic rationale fills the gap: topotecan is a semisynthetic camptothecin derivative that inhibits Topoisomerase I, trapping the enzyme–DNA cleavage complex and causing single-strand DNA breaks that accumulate during replication, driving apoptosis in rapidly dividing cells. This is a broad-spectrum cytotoxic mechanism, not one tied to a specific tissue type.

Topotecan's approved indications (ovarian, cervical, small cell lung cancer) are all rapidly proliferating solid tumours, and breast carcinoma shares this proliferative biology — which is why topotecan has been tested clinically in breast cancer since the 1990s. However, the results have been mixed: a CALGB Phase 2 trial (PMID 10362325) and an infusional-dosing Phase 2 study (PMID 9413954, explicitly titled "no evidence of increased efficacy") both showed only modest single-agent activity in advanced breast cancer. More recent mechanistic work (e.g., TFDP1 as a therapeutic target in triple-negative breast cancer, PMID 40300683; MYC-driven synthetic lethality, PMID 37987734) suggests biologically plausible subgroups — particularly TNBC and MYC-amplified tumours — where topotecan or Topo I inhibition specifically might have renewed relevance, even though historical unselected trials underwhelmed.

In short: the mechanism is plausible and there is a real, if dated and mixed, clinical trial history. The prediction is reasonable as a research hypothesis, but it is not yet supported by a positive, modern, biomarker-selected trial.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab + olaparib + cediranib combinations vs. standard chemo in platinum-resistant recurrent ovarian/peritoneal/fallopian cancer; topotecan is one possible chemotherapy backbone option, not a primary study arm. |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed (n=266) | 266 | Olaparib vs. physician's choice single-agent chemo in gBRCA-mutated platinum-sensitive relapsed ovarian cancer; topotecan's specific role in the comparator arm needs confirmation. |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | Intensive-dose Topotecan/Ifosfamide/Etoposide (TIME) followed by autologous stem cell rescue in metastatic breast cancer. |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with multiple standard chemo/immunotherapy regimens in advanced malignancies; topotecan is one of several chemo comparator arms, not the primary focus. |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Organoid-based high-throughput drug screening to select chemotherapy in refractory solid tumours; exploratory platform study, not a direct efficacy trial. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | RCT/Phase 2 | American Journal of Clinical Oncology | CALGB Phase 2 trial of topotecan monotherapy in previously treated advanced breast cancer; modest activity observed. |
| [9626200](https://pubmed.ncbi.nlm.nih.gov/9626200/) | 1998 | Phase 2 | Journal of Clinical Oncology | Paclitaxel + topotecan with G-CSF support in stage IV breast cancer; combination feasibility and efficacy evaluated. |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Cohort | Onkologie | Pilot study of topotecan as primary chemotherapy for breast cancer brain metastases. |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Cohort | British Journal of Cancer | Continuous infusional topotecan in advanced breast cancer and NSCLC; no evidence of increased efficacy vs. standard dosing. |
| [21514634](https://pubmed.ncbi.nlm.nih.gov/21514634/) | 2011 | Phase 2 (ovarian) | Gynecologic Oncology | Lapatinib + topotecan in platinum-refractory ovarian/peritoneal carcinoma; mechanistic relevance via BCRP/P-gp efflux inhibition. |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Mechanistic | International Journal of Biological Macromolecules | TFDP1 identified as a therapeutic target for topotecan in triple-negative breast cancer via senescence suppression. |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Mechanistic | Cancer Research | Topoisomerase 1 inhibition in MYC-driven breast cancer promotes R-loop accumulation and synthetic lethality. |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic topotecan + pazopanib shows potent efficacy in preclinical models of triple-negative breast cancer. |
| [12089223](https://pubmed.ncbi.nlm.nih.gov/12089223/) | 2002 | PK study | Journal of Clinical Oncology | Oral bioavailability of topotecan increased when combined with BCRP/P-gp inhibitor GF120918. |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynäkologisch-Geburtshilfliche Rundschau | Overview of new drugs in breast carcinoma therapy, including topoisomerase inhibitors, in the context of adjuvant outcomes. |

## Canada Market Information

Topotecan currently has **no market authorization in Canada** — `market_status` is reported as "Not marketed" (not marketed) with **0 DINs** on file. No product listings are available to summarize.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Topoisomerase I inhibitor, camptothecin/topotecan class) |
| Myelosuppression Risk | High — dose-limiting toxicity; literature on related indications reports severe neutropenia and thrombocytopenia (e.g., nadir neutrophil ~1.55 ×10⁹/L, platelets ~20,500/mm³) |
| Emetogenicity Classification | Moderate |
| Monitoring Items | Complete blood count with differential (weekly during treatment), renal function (drug is renally cleared), liver function |
| Handling Protection | Yes — must follow institutional cytotoxic/hazardous drug handling protocols (preparation, administration, disposal) |

## Safety Considerations

Please refer to the package insert for safety information. Structured warnings, contraindications, and drug interaction data for this candidate are not yet available (see Conclusion below).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, and there is a genuine (if dated) body of Phase 2 trial and mechanistic literature exploring topotecan in breast cancer, supporting an L2 evidence level. However, historical single-agent trials showed only modest, inconsistent efficacy, no confirmatory modern RCT exists, safety documentation (warnings/contraindications) is currently a blocking data gap, and topotecan has no Canadian market authorization to build on.

**To proceed, the following is needed:**
- TFDA/Health Canada product warnings and contraindications (currently a blocking data gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Clarification of Canadian regulatory pathway/DIN status for topotecan, since it is not currently marketed
- A modern, biomarker-selected trial (e.g., TNBC or MYC-amplified subgroups) to test whether recent mechanistic findings translate into clinical benefit, given that historic unselected trials underwhelmed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

