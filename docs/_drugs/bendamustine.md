---
layout: default
title: Bendamustine
parent: High Evidence (L1-L2)
nav_order: 100
evidence_level: L1
indication_count: 10
---

# Bendamustine
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Bendamustine: From an Unlisted Original Indication to Mantle Cell Lymphoma

## One-Sentence Summary

Bendamustine is an alkylating chemotherapy that is marketed in Canada. The supplied license records do not state its original approved indication.
The TxGNN model predicts it may be effective for **mantle cell lymphoma (MCL)**.
This direction is supported by **50 clinical trials** and **20 publications**, including several completed Phase 3 randomized trials in which MCL patients received bendamustine plus rituximab.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records provided |
| Predicted New Indication | Mantle cell lymphoma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bendamustine is a bifunctional alkylating agent with a purine-like benzimidazole ring. It cross-links DNA and triggers apoptosis. A formal mechanism-of-action entry is not available in the source data, so this description comes from the evidence-pack rationale.

MCL is a B-cell non-Hodgkin lymphoma. DNA-damaging chemotherapy has well-documented activity in indolent B-cell malignancies and MCL, so the predicted use is biologically plausible. The clinical literature already treats bendamustine-rituximab (BR) as an established backbone for MCL, especially in older patients (PMID 26755518).

One caveat: in many of the Phase 3 trials, BR is the comparator or backbone, not the investigational agent. The evidence therefore supports BR use in MCL. It does not prove bendamustine alone is effective.

---

## Clinical Trial Evidence

50 trials were matched. The 10 most relevant are listed below, prioritizing Phase 3 and directly MCL-focused studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00877006](https://clinicaltrials.gov/study/NCT00877006) | Phase 3 | Completed | 447 | BRIGHT: BR vs R-CVP or R-CHOP as first-line therapy in advanced indolent NHL or MCL; primary endpoint is complete response rate |
| [NCT00991211](https://clinicaltrials.gov/study/NCT00991211) | Phase 3 | Completed | 549 | BR vs R-CHOP as first-line therapy in low-grade NHL and MCL; non-inferiority on progression-free survival |
| [NCT01456351](https://clinicaltrials.gov/study/NCT01456351) | Phase 3 | Completed | 230 | BR vs fludarabine-rituximab in recurrent low-grade NHL and MCL; non-inferiority on event-free survival |
| [NCT06363994](https://clinicaltrials.gov/study/NCT06363994) | Phase 3 | Recruiting | 476 | Double-blind trial of orelabrutinib plus BR vs placebo plus BR in untreated MCL |
| [NCT00891839](https://clinicaltrials.gov/study/NCT00891839) | Phase 2 | Completed | 45 | Open-label BR in relapsed/refractory MCL, assessing efficacy and safety |
| [NCT04115631](https://clinicaltrials.gov/study/NCT04115631) | Phase 2 | Active, not recruiting | 360 | Randomized 3-arm comparison of BR-based regimens with high-dose cytarabine and/or acalabrutinib in untreated MCL (age ≤70) |
| [NCT01737177](https://clinicaltrials.gov/study/NCT01737177) | Phase 2 | Completed | 42 | Lenalidomide + bendamustine + rituximab (R2-B) as second-line therapy for relapsed/refractory MCL, followed by lenalidomide maintenance |
| [NCT01457144](https://clinicaltrials.gov/study/NCT01457144) | Phase 2 | Completed | 76 | RiBVD (rituximab, bendamustine, bortezomib, dexamethasone) as first-line therapy in older or transplant-unsuitable MCL patients |
| [NCT03567876](https://clinicaltrials.gov/study/NCT03567876) | Phase 2 | Completed | 141 | Venetoclax after rituximab-bendamustine-cytarabine (R-BAC) in high-risk older MCL patients; primary endpoint is progression-free survival |
| [NCT01415752](https://clinicaltrials.gov/study/NCT01415752) | Phase 2 | Active, not recruiting | 373 | Four-arm trial in untreated MCL (age ≥60) of BR ± bortezomib, followed by rituximab or lenalidomide-rituximab consolidation |

---

## Literature Evidence

20 publications were matched. The 10 most relevant are listed, with RCTs first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | RCT | N Engl J Med | Ibrutinib added to BR, followed by rituximab maintenance, in older patients with untreated MCL |
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | RCT (Phase 3) | Lancet | Open-label non-inferiority trial of BR vs R-CHOP as first-line therapy in indolent lymphoma and MCL |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | RCT | J Clin Oncol | Acalabrutinib plus BR in untreated MCL. Ibrutinib plus BR prolonged PFS without an OS gain, likely because of toxicity, and acalabrutinib is less toxic |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | RCT follow-up | J Clin Oncol | BRIGHT 5-year follow-up of BR vs R-CHOP/R-CVP in indolent NHL and MCL |
| [24591201](https://pubmed.ncbi.nlm.nih.gov/24591201/) | 2014 | RCT (Phase 3) | Blood | BRIGHT primary report: non-inferiority of BR vs standard rituximab-chemotherapy in treatment-naive indolent NHL or MCL |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | RCT (Phase 2/3) | Lancet | ENRICH: ibrutinib-rituximab vs standard immunochemotherapy (R-CHOP or BR) in untreated MCL, age 60 and over |
| [40975105](https://pubmed.ncbi.nlm.nih.gov/40975105/) | 2025 | Phase 2 | Lancet Haematol | FIL_V-RBAC: venetoclax added to rituximab-bendamustine-cytarabine in older high-risk MCL |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Phase 2 (pooled) | Blood Adv | Rituximab/bendamustine alternating with rituximab/cytarabine induction before autologous transplant in transplant-eligible MCL |
| [41132246](https://pubmed.ncbi.nlm.nih.gov/41132246/) | 2025 | Guideline | HemaSphere | EHA-EU MCL network guidelines for diagnosis and treatment |
| [41380101](https://pubmed.ncbi.nlm.nih.gov/41380101/) | 2026 | Retrospective | Blood Adv | Multicenter US/Canada analysis (911 patients) of whether rituximab maintenance after first-line BR is beneficial |

---

## Canada Market Information

5 of the 11 authorizations are shown.

| DIN | Product Name |
|---------|------|
| 2496852 | BENDAMUSTINE HYDROCHLORIDE FOR INJECTION |
| 2496895 | NAT-BENDAMUSTINE |
| 2496887 | NAT-BENDAMUSTINE |
| 2509261 | BENDAMUSTINE HYDROCHLORIDE FOR INJECTION |
| 2392569 | TREANDA |

The license records supplied do not include dosage form or approved indication text, so the Health Canada label status for MCL still needs to be confirmed.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. A trial of the R-BAC regimen (bendamustine + cytarabine + rituximab) reported relevant hematological toxicity, especially in previously treated and older patients (NCT01662050) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, plus liver and renal function |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

Signals from the supplied evidence:
- Adding ibrutinib to BR prolonged progression-free survival without an overall survival benefit, which the investigators attributed to likely toxicity (PMID 40311141).
- Immunosuppression from bendamustine may raise the risk of infection and second primary malignancy. This is a guardrail noted in the evidence pack, not a quantified finding for MCL.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least three completed Phase 3 randomized trials (BRIGHT, the StiL non-inferiority study, and the BR vs fludarabine-rituximab trial) included MCL patients treated with BR. Multiple Phase 2 studies and guidelines add support. Because most of this evidence is in mixed indolent NHL/MCL populations or uses BR as a backbone, and the label and safety data are incomplete, a full "Go" is not yet justified.

**To proceed, the following is needed:**
- Confirm the Health Canada label status for MCL, since the license records supplied have no indication text
- Obtain the package insert warnings and contraindications from Health Canada, which are the blocking safety gap
- Obtain the formal mechanism-of-action entry from DrugBank
- Review long-term safety (infection, second malignancy) and current local treatment guidelines for MCL
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

