---
layout: default
title: Vinorelbine
parent: High Evidence (L1-L2)
nav_order: 827
evidence_level: L2
indication_count: 10
---

# Vinorelbine
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

# Vinorelbine: From Non-Small Cell Lung Cancer to Ewing Sarcoma

## One-Sentence Summary

Vinorelbine (DrugBank DB00361) is a semisynthetic vinca alkaloid chemotherapy agent internationally established for non-small cell lung cancer and other solid tumours, though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Ewing Sarcoma**,
with **4 clinical trials** and **5 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Canadian regulatory data (drug not marketed in Canada); internationally established for non-small cell lung cancer (NSCLC) and refractory pediatric solid tumours |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism-of-action data is not available from DrugBank in this evidence pack. Based on known pharmacology, Vinorelbine is a semisynthetic vinca alkaloid that binds tubulin and inhibits microtubule polymerization, arresting cells in mitotic metaphase and inducing apoptosis. This mechanism is well established in its use against high-proliferation solid tumours such as NSCLC.

Ewing sarcoma is a highly proliferative small round-cell malignancy that is known to be sensitive to microtubule-inhibiting agents. Vinorelbine combined with cyclophosphamide (the "VC" regimen) is already a recognized clinical salvage regimen for refractory or relapsed pediatric sarcomas, including Ewing sarcoma, rhabdomyosarcoma, and neuroblastoma — directly supporting the mechanistic plausibility of this predicted indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | Completed | 50 | Vinorelbine (Navelbine) monotherapy in children with recurrent or refractory malignancies |
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | Unknown | 210 | Vinorelbine + Cyclophosphamide (VC) in refractory/relapsed pediatric tumours, including Ewing sarcoma, rhabdomyosarcoma, osteosarcoma, neuroblastoma, medulloblastoma |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | N/A | Active, not recruiting | 100 | Prospective multicenter cohort study of risk-stratification-oriented treatment outcomes and safety in pediatric Ewing sarcoma (China) |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Phase 2 | Recruiting | 105 | CAMPFIRE master protocol for pediatric/young adult cancers; provides a shared research infrastructure covering relevant patient populations |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Cohort/Phase 2 | European Journal of Cancer | Phase II study of vinorelbine + continuous low-dose cyclophosphamide in relapsed/refractory pediatric and young adult solid tumours; good tolerance and efficacy demonstrated, notably in rhabdomyosarcoma |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Cohort/Phase 2 | Cancer | Vinorelbine activity in previously treated advanced childhood sarcomas, with demonstrated efficacy in rhabdomyosarcoma |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Frontiers in Pharmacology | Review of chemotherapeutic drugs for soft tissue sarcomas, including vinca alkaloid regimens |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | Preclinical | International Journal of Cancer | Synergistic apoptosis induction with PLK1 inhibitor BI 6727 and microtubule-interfering drugs (including vinorelbine) in Ewing sarcoma cells |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case Report | BMC Urology | Case report and literature review of extraosseous Ewing's sarcoma/PNET of the kidney |

## Canada Market Information

Vinorelbine currently has no Health Canada Drug Identification Number (DIN) records in this dataset. **Market status: Not Marketed.**

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Vinca alkaloid / anti-microtubule agent) |
| Myelosuppression Risk | High — neutropenia is the principal dose-limiting toxicity of vinorelbine |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (neutrophil count prior to each dose), liver function tests, peripheral neuropathy assessment, injection site/extravasation monitoring |
| Handling Protection | Required — vinorelbine is a vesicant and hazardous drug; must be prepared and administered per cytotoxic drug handling protocols (closed-system transfer devices, PPE) |

## Safety Considerations

Please refer to the package insert for safety information. No structured key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (DG001: regulatory label warnings/contraindications data gap, flagged as Blocking).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two tier-1 Phase II/cohort studies and one completed Phase II trial demonstrate vinorelbine (alone or with cyclophosphamide) activity in refractory/relapsed pediatric sarcomas including Ewing sarcoma, supported by preclinical mechanistic data on microtubule-inhibitor sensitivity in Ewing sarcoma cells. Evidence is directionally supportive (L2) but not yet definitive (no dedicated randomized Phase III trial in Ewing sarcoma specifically), and safety/regulatory documentation is currently absent.

**To proceed, the following is needed:**
- Regulatory product monograph safety warnings and contraindications (currently a Blocking data gap — DG001)
- Formal DrugBank/mechanism-of-action confirmation (High-priority data gap — DG002)
- Clarification of Canadian market access pathway, since vinorelbine is not currently marketed in Canada (Special Access Programme or new DIN submission)
- Pediatric-specific safety monitoring plan (myelosuppression, peripheral neuropathy, extravasation precautions)
- Confirmation of route compatibility (IV formulation) against standard Ewing sarcoma treatment protocols
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

