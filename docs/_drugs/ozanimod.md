---
layout: default
title: Ozanimod
parent: 僅模型預測 (L5)
nav_order: 589
evidence_level: L5
indication_count: 1
---

# Ozanimod
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ozanimod: From Relapsing Multiple Sclerosis to Progressive Relapsing Multiple Sclerosis

## One-Sentence Summary

Ozanimod (DrugBank DB12612) is a sphingosine-1-phosphate (S1P) receptor modulator already established for relapsing forms of multiple sclerosis. The TxGNN model predicts it may also be effective for **Progressive Relapsing Multiple Sclerosis (PRMS)**, with **8 clinical trials** and **18 publications** currently identified as supporting evidence — though the pivotal Phase 3 trial did not specifically enroll a PRMS subgroup.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing forms of Multiple Sclerosis (per global approval literature; no local license on file) |
| Predicted New Indication | Progressive Relapsing Multiple Sclerosis (PRMS) |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Structured mechanism-of-action data was not available in DrugBank for this candidate. However, the repurposing rationale supplied with this evidence pack indicates that ozanimod is a selective S1P1/S1P5 receptor modulator: it inhibits lymphocyte egress from lymph nodes, reducing the number of autoreactive lymphocytes that reach the central nervous system. This is a pharmacologically well-established mechanism for MS immunomodulation, shared with the earlier-generation drug fingolimod, which has long-term clinical validation in the same class.

Progressive Relapsing MS is a pre-2013 disease classification describing MS that is progressive from onset but punctuated by relapses. Ozanimod's pivotal trial (NCT02576717, RADIANCE/SUNBEAM-type design) enrolled patients with "relapsing forms of MS," including relapsing-remitting disease and active secondary progressive disease, but explicitly excluded primary progressive MS and did not define PRMS as an independent enrollment stratum.

This means the mechanistic case for efficacy in PRMS is strong — it targets the same peripheral immune-trafficking pathway thought to drive relapse activity in this subtype — but the prediction represents a boundary extension of an already-approved indication rather than a mechanistically novel repurposing target. The population-level evidence gap (no dedicated PRMS trial arm) should be treated as the main uncertainty, not the mechanism itself.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02576717](https://clinicaltrials.gov/study/NCT02576717) | Phase 3 | Completed | 2,494 | Pivotal double-blind, double-dummy, active-controlled (vs interferon beta-1a) trial establishing efficacy/safety of ozanimod in relapsing MS; PRMS not a defined subgroup |
| [NCT06396039](https://clinicaltrials.gov/study/NCT06396039) | Phase 4 | Active, not recruiting | 84 | Post-marketing single-arm study confirming real-world effectiveness/safety of oral ozanimod in Chinese RMS patients |
| [NCT05828901](https://clinicaltrials.gov/study/NCT05828901) | N/A | Recruiting | 60 | Investigates predictors of disease activity and rebound risk in MS patients on S1P receptor modulators (mechanism-relevant, not an efficacy trial) |
| [NCT05605782](https://clinicaltrials.gov/study/NCT05605782) | N/A | Active, not recruiting | 9,000 | ORION: large multinational post-authorization safety study of ozanimod vs other S1PR modulators/DMTs in RRMS |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Active, not recruiting | 900 | TREAT-MS: pragmatic trial comparing early aggressive vs escalation DMT strategy; ozanimod is one of several eligible drugs, not drug-specific |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS: early intensive vs escalation treatment strategy trial; ozanimod one of several eligible DMTs |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | Enrolling by invitation | 323 | STATURE: observational study of treatment burden/adherence across six oral DMTs including ozanimod |
| [NCT05688436](https://clinicaltrials.gov/study/NCT05688436) | N/A | Recruiting | 1,178 | Pregnancy outcomes study for diroximel fumarate (different drug, same DMT class — low direct relevance) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385738](https://pubmed.ncbi.nlm.nih.gov/32385738/) | 2020 | Review | Drugs | "Ozanimod: First Approval" — confirms FDA/EU approval for relapsing forms of MS including active secondary progressive disease |
| [33287177](https://pubmed.ncbi.nlm.nih.gov/33287177/) | 2020 | Review | Neurology International | Comprehensive review of ozanimod's efficacy and side-effect profile in relapsing MS |
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | Review (Network Meta-analysis) | Cochrane Database of Systematic Reviews | Comparative efficacy/safety of immunomodulators, including S1PR modulators, specifically in progressive MS |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Review (Network Meta-analysis) | Cochrane Database of Systematic Reviews | Comparative efficacy/safety of immunomodulators and immunosuppressants in RRMS |
| [31598138](https://pubmed.ncbi.nlm.nih.gov/31598138/) | 2019 | Review | Therapeutic Advances in Neurological Disorders | Overview of therapeutic developments specifically for progressive MS, including pathogenic mechanisms relevant to PRMS |
| [36946625](https://pubmed.ncbi.nlm.nih.gov/36946625/) | 2023 | Review | Expert Opinion on Pharmacotherapy | Updated review of S1P receptor modulators (fingolimod, siponimod, ozanimod, ponesimod) in relapsing MS |
| [33797705](https://pubmed.ncbi.nlm.nih.gov/33797705/) | 2021 | Review | CNS Drugs | Class review of S1P receptor modulators for MS, covering shared mechanism of action |
| [38162670](https://pubmed.ncbi.nlm.nih.gov/38162670/) | 2023 | Review | Frontiers in Immunology | Reviews CNS-bioavailable DMTs and their limited efficacy in progressive disease, framing where S1PR modulators like ozanimod may add value |
| [28812220](https://pubmed.ncbi.nlm.nih.gov/28812220/) | 2017 | Review | Neurotherapeutics | Early class review of S1PR modulators' mechanism of lymphocyte sequestration in MS treatment |
| [30410033](https://pubmed.ncbi.nlm.nih.gov/30410033/) | 2018 | Review | Nature Reviews Disease Primers | General overview of MS pathophysiology and disease classification, providing background for PRMS as a historical subtype |

## Canada Market Information

Ozanimod is currently not marketed and has no DIN authorizations on record in this jurisdiction.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ozanimod has a completed, large Phase 3 pivotal trial (n=2,494) and a well-characterized S1P modulator mechanism supporting biological plausibility in relapsing MS populations, but PRMS was not an independently studied subgroup, and no local market authorization or safety-labeling data exists to support a clinical decision yet.

**To proceed, the following is needed:**
- Local drug label warnings and contraindications (currently a blocking data gap — needed before any S1 safety screening)
- Confirmed mechanism-of-action documentation from DrugBank
- Local (Canada) market authorization/licensing status, since none is currently on file
- Evidence specific to the PRMS subgroup, since the pivotal trial's "relapsing forms" definition did not isolate this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

