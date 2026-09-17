---
layout: default
title: Ipilimumab
parent: High Evidence (L1-L2)
nav_order: 417
evidence_level: L2
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **2** 
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

# Ipilimumab: From Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Ipilimumab is an anti-CTLA-4 immune checkpoint inhibitor, originally developed and used for advanced (cutaneous) melanoma.
The TxGNN model predicts it may also be effective for **non-cutaneous melanoma** (e.g., uveal, mucosal subtypes),
with **50 clinical trials** and **5 publications** currently available as supporting context, including one directly relevant Phase 2 randomized trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma (cutaneous) — per clinical trial context in the evidence base (e.g., "already approved by the FDA to treat advanced melanoma") |
| Predicted New Indication | Non-cutaneous melanoma |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ipilimumab is an anti-CTLA-4 monoclonal antibody. Its mechanism of action is to block the CTLA-4 inhibitory checkpoint on T cells, releasing the brake on T-cell activation and thereby enhancing anti-tumor immune responses. This mechanism is not specific to any one melanoma histologic subtype — it depends on the presence of tumor antigens and a functioning T-cell compartment rather than on the anatomical origin of the melanocytes involved.

Non-cutaneous melanomas (uveal, mucosal, and other rarer subtypes) still arise from melanocytic cells and can express CTLA-4-relevant tumor antigens, providing a plausible mechanistic basis for extrapolating checkpoint inhibition beyond cutaneous disease. This is supported by real-world use: trials and reports in the evidence base include ipilimumab use in uveal melanoma (hepatic-metastatic uveal melanoma pilot study) and mucosal melanoma settings, and combination regimens (ipilimumab + nivolumab) are already standard practice in advanced/metastatic melanoma broadly.

The caveat is that non-cutaneous subtypes — particularly uveal melanoma — are known to have a lower tumor mutational burden and a less immunogenic tumor microenvironment than cutaneous melanoma, which has historically translated into lower response rates to checkpoint inhibition. The mechanistic rationale is sound, but efficacy should not be assumed to be equivalent to cutaneous disease.

*Note on a secondary model signal:* TxGNN also generated a second, higher-scoring prediction (choroideremia, 99.06%) for this drug. That signal was screened out — choroideremia is a CHM-gene, intracellular vesicular-trafficking retinal degeneration with no known relationship to CTLA-4 immune checkpoint biology, no clinical trials, and no literature support. It most likely reflects a graph-proximity artifact (anatomical overlap between "choroid" and choroidal/uveal melanoma terms) rather than a genuine pharmacological signal, and is not carried forward in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01950390](https://clinicaltrials.gov/study/NCT01950390) | Phase 2 | Completed | 169 | Randomized trial of ipilimumab ± bevacizumab in unresectable Stage III/IV melanoma; direct, controlled-design evidence (highest relevance grade) |
| [NCT03165422](https://clinicaltrials.gov/study/NCT03165422) | N/A (real-world) | Completed | 68 | Japanese real-world chart review of ipilimumab after nivolumab in melanoma |
| [NCT03527251](https://clinicaltrials.gov/study/NCT03527251) | Phase 1 | Unknown | 10 | CTLA-4 antibody (ipilimumab) followed by PD-1 antibody SHR-1210; explores checkpoint-sequencing rationale |
| [NCT01730157](https://clinicaltrials.gov/study/NCT01730157) | Early Phase 1 | Terminated | 6 | Pilot study of hepatic radioembolization plus systemic ipilimumab specifically in uveal melanoma liver metastases |
| [NCT02174172](https://clinicaltrials.gov/study/NCT02174172) | Phase 1 | Completed | 158 | Atezolizumab combined with ipilimumab/other immune-modulating therapies in advanced/metastatic solid tumors; ipilimumab is a secondary arm |
| [NCT04418167](https://clinicaltrials.gov/study/NCT04418167) | Phase 1 | Suspended | 71 | ERK1/2 inhibitor JSI-1187 ± dabrafenib in MAPK-mutant solid tumors; not ipilimumab-focused |
| [NCT03166397](https://clinicaltrials.gov/study/NCT03166397) | Phase 2 | Recruiting | 30 | Autologous adoptive cell therapy (TIL) with lymphodepletion in metastatic melanoma; ipilimumab likely adjunct/prior therapy |
| [NCT04311710](https://clinicaltrials.gov/study/NCT04311710) | Phase 1/2 | Terminated | 21 | Pharmacokinetics of subcutaneous ipilimumab ± subcutaneous nivolumab across multiple tumor types |
| [NCT06295159](https://clinicaltrials.gov/study/NCT06295159) | Phase 2 | Recruiting | 90 | Neoadjuvant/adjuvant anti-PD1 or combination regimens for locoregionally advanced melanoma |
| [NCT04899921](https://clinicaltrials.gov/study/NCT04899921) | Phase 2 | Terminated | 1 | Troriluzole + ipilimumab + nivolumab in melanoma brain metastases after prior anti-PD-1 therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohort/Phase 2 | The Medical Journal of Australia | Ipilimumab efficacy/tolerability in pretreated cutaneous, **uveal**, and **mucosal** melanoma; evaluates response by melanoma subtype |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Review | Current Cancer Drug Targets | Review of melanoma adjuvant treatment; notes non-cutaneous melanoma represents ~5% of cases with limited dedicated trial data |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Review | Discovery Medicine | Clinical update on anti-PD-1 antibodies as monotherapy or combined with ipilimumab in advanced melanoma |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohort | Current Oncology | Retrospective cohort comparing anti-PD-1 monotherapy vs. combination with ipilimumab by age group in advanced melanoma |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case Report | Cureus | Case report of metastatic melanoma to the transverse colon treated with immunotherapy including ipilimumab-class agents |

---

## Canada Market Information

Ipilimumab is not currently marketed in Canada under this evidence pack — no Drug Identification Numbers (DINs) are on file (0 licenses recorded).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 immune checkpoint inhibitor monoclonal antibody) |
| Myelosuppression Risk | Low — this class is not a direct myelosuppressive agent; its dominant toxicity is immune-related adverse events (colitis, hepatitis, endocrinopathy, pneumonitis) rather than bone marrow suppression. Please refer to the package insert for confirmed hematologic toxicity data. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function tests, thyroid/endocrine panel, GI symptom monitoring (colitis risk), CBC per package insert |
| Handling Protection | Not classified as a conventional cytotoxic agent; follow institutional hazardous/biologic drug handling policy and verify against local hazardous drug list |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale for extending CTLA-4 blockade beyond cutaneous melanoma is sound, and it is supported by a directly relevant completed Phase 2 randomized trial, real-world Japanese outcome data, and a dedicated uveal melanoma pilot study — but subtype-specific efficacy (especially in uveal melanoma) is historically lower than in cutaneous disease, and key safety/regulatory data for this evidence pack remain unresolved.

**To proceed, the following is needed:**
- Official product monograph / label data (warnings, contraindications) to resolve the current blocking data gap
- Formal mechanism-of-action documentation from DrugBank to support the S1 safety review
- Subtype-disaggregated efficacy data (uveal vs. mucosal vs. other non-cutaneous) given known differences in immunogenicity and response
- Confirmation of Canadian market/DIN status (currently zero licenses on file — verify whether this reflects true non-marketing or a data collection gap)
- Re-run of the drug interaction (DDI) query, currently returning no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

