---
layout: default
title: Vincristine
parent: Model Prediction Only (L5)
nav_order: 970
evidence_level: L5
indication_count: 3
---

# Vincristine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Vincristine: From Cancer Chemotherapy (Original Indication Not Recorded) to Ganglioneuroblastoma

## One-Sentence Summary

Vincristine is an antimitotic cytotoxic chemotherapy agent that is marketed in Canada, though the Canadian records provided do not list an approved indication.
The TxGNN model predicts it may be effective for **ganglioneuroblastoma**, with **4 clinical trials** and **5 publications** currently supporting this direction.
Most of this evidence is indirect: vincristine appears to be background chemotherapy in the trials, and the publications are mostly case reports.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Canadian licence data |
| Predicted New Indication | Ganglioneuroblastoma |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L2 (as assigned in the Evidence Pack; see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The only completed trial is a Phase 2 pilot of an antibody-containing regimen, not a clear randomized trial. L2 is therefore the upper bound of what the evidence supports.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the drug record. Vincristine is known to bind tubulin and block microtubule polymerization. This causes mitotic arrest in rapidly dividing cells, including neural crest-derived tumour cells.

Ganglioneuroblastoma belongs to the neuroblastic tumour spectrum alongside neuroblastoma. In that spectrum, vincristine is a long-standing component of multi-agent induction chemotherapy. Two of the case reports retrieved describe ganglioneuroblastoma treated with vincristine-containing combinations, including one complete remission with chemotherapy alone.

Three caveats apply:
- **This may be established use rather than true repurposing.** The original indication list is empty in the input data.
- **Vincristine's role in each trial is inferred.** The registry records were not checked directly, so its presence comes from standard neuroblastoma protocols.
- **No trial isolates a vincristine effect.** In these trials vincristine is background chemotherapy, and the randomized questions concern added agents (dinutuximab, 131I-MIBG, ALK inhibitors).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03126916](https://clinicaltrials.gov/study/NCT03126916) | Phase 3 | Recruiting | 750 | 131I-MIBG or lorlatinib added to intensive therapy in newly diagnosed high-risk neuroblastoma or ganglioneuroblastoma. Vincristine is likely in the chemotherapy backbone. No results yet. |
| [NCT06172296](https://clinicaltrials.gov/study/NCT06172296) | Phase 3 | Recruiting | 478 | Dinutuximab added to induction chemotherapy and multimodal therapy in children with newly diagnosed high-risk neuroblastoma. Vincristine is likely backbone. No results yet. |
| [NCT03786783](https://clinicaltrials.gov/study/NCT03786783) | Phase 2 | Completed | 42 | Pilot induction regimen of dinutuximab and sargramostim combined with chemotherapy in newly diagnosed high-risk neuroblastoma. Vincristine's role is inferred. |
| [NCT01798004](https://clinicaltrials.gov/study/NCT01798004) | Phase 1 | Completed | 150 | Busulfan/melphalan consolidation with stem cell transplant after induction chemotherapy. Vincristine would appear only in the earlier induction, not in the tested intervention. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Prospective clinical trial | Pediatr Blood Cancer | Japan Children's Cancer Group trial (JN-L-10) using image-defined risk factors to guide surgical timing in low-risk neuroblastoma. It concerns surgical decisions rather than vincristine. |
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Case report | Postgrad Med J | Unresectable spinal ganglioneuroblastoma in a 21-year-old. Combination chemotherapy including vincristine produced a histologically proven complete remission. |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Case report | J Pediatr Hematol Oncol | Ganglioneuroblastoma presenting with obstructive jaundice, treated with chemotherapy that included vincristine. |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Case report | J Thorac Cardiovasc Surg | 31 patients with intrathoracic ganglioneuroblastoma (27 survivors, followed up to 25 years). Treatment was surgery, radiation or chemotherapy. |
| [3071124](https://pubmed.ncbi.nlm.nih.gov/3071124/) | 1988 | Case report | Hinyokika Kiyo | Multimodality treatment of adult adrenal ganglioneuroblastoma. |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Case report | J Pediatr Hematol Oncol | Gastric involvement in an infant with stage 4 multifocal ganglioneuroblastoma. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2183013 | VINCRISTINE SULFATE INJECTION USP |
| 2143305 | VINCRISTINE SULFATE INJECTION |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, antimitotic) |
| Myelosuppression Risk | Low to moderate. Neurotoxicity is the principal dose-limiting concern, and myelosuppression is also noted. |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function, and neurological assessment (peripheral and autonomic neuropathy) |
| Handling Protection | Must follow cytotoxic drug handling regulations. For intravenous use only. |

These entries reflect general knowledge of the drug class. Please confirm them against the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the interaction query. Neurotoxicity and myelosuppression are the main concerns noted in the evidence review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ganglioneuroblastoma sits within the neuroblastic tumour spectrum, where vincristine-containing induction chemotherapy is standard, and the target population is well represented in two large Phase 3 trials. However, no study isolates vincristine's effect. The trials are still recruiting or test other agents, and the supporting literature is mostly case reports. The lower-ranked predictions (a rare developmental syndrome and the broad "retroperitoneal neoplasm" category) are rated Hold because their evidence is weak or non-specific.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Registry verification that vincristine is part of the chemotherapy backbone in each listed trial
- Mechanism-of-action data from DrugBank
- Approved indication text, dosage form and manufacturer for the two DINs, to confirm whether this is established use or true repurposing
- A monitoring plan for neurotoxicity and myelosuppression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

