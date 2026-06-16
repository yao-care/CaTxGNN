---
layout: default
title: Fludarabine
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Fludarabine
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

# Fludarabine: From Chronic Lymphocytic Leukemia to Plasma Cell Myeloma

## One-Sentence Summary

Fludarabine is a fluorinated purine nucleoside analogue used primarily in treating chronic lymphocytic leukemia (CLL) and other indolent hematologic malignancies, and is well-established as a conditioning agent in allogeneic stem cell transplantation.
The TxGNN model predicts it may be effective for **Plasma Cell Myeloma** (multiple myeloma),
with **50+ clinical trials** and **20 publications** currently supporting this direction — primarily through its proven role as a reduced-intensity conditioning (RIC) backbone and CAR-T lymphodepletion agent in myeloma patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic lymphocytic leukemia (CLL) and indolent hematologic malignancies (not marketed in Canada) |
| Predicted New Indication | Plasma Cell Myeloma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evaluation package. Based on known information, Fludarabine is a fluorinated purine nucleoside analogue. It exerts cytotoxic effects by incorporating into DNA and RNA, competitively inhibiting ribonucleotide reductase and DNA polymerase, thereby disrupting DNA synthesis and inducing apoptosis in proliferating cells. It also potently depletes T lymphocytes, giving it a dual role as both a cytotoxic and immunosuppressive agent.

Plasma cell myeloma (multiple myeloma) shares deep biological roots with CLL and other B-cell malignancies — both arise from the B-lymphocyte lineage and are driven by clonal lymphoid proliferation. This mechanistic overlap provides a strong biological rationale: Fludarabine's ability to kill rapidly dividing lymphoid cells and suppress host immunity is directly applicable to the myeloma setting. In clinical practice, Fludarabine has been incorporated into myeloma treatment along two converging tracks: (1) as the backbone of reduced-intensity conditioning (RIC) regimens — most notably Flu+Mel and Flu+Bu — enabling donor engraftment and a graft-versus-myeloma (GVM) immune effect after allogeneic HSCT; and (2) as a standard lymphodepleting agent (with cyclophosphamide) before CAR-T cell infusion, creating cytokine space that enhances CAR-T expansion and anti-myeloma activity.

Crucially, there is also direct laboratory evidence of Fludarabine's intrinsic anti-myeloma activity: studies using the RPMI8226 myeloma cell line demonstrate that Fludarabine inhibits Akt phosphorylation, suppresses myeloma cell proliferation, and induces apoptosis both in vitro and in vivo (PMID 17976186). An early clinical report also noted activity in plasma cell leukemia, an aggressive plasma cell malignancy closely related to myeloma (PMID 7781758). Together, these mechanistic, preclinical, and clinical convergences make the TxGNN prediction highly plausible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01453101](https://clinicaltrials.gov/study/NCT01453101) | Phase 2 | Completed | 54 | Allo-HSCT conditioning with Fludarabine + Melphalan + Bortezomib for multiple myeloma — primary objective to improve progression-free survival vs historical Flu+Mel alone |
| [NCT01408563](https://clinicaltrials.gov/study/NCT01408563) | Phase 2 | Completed | 33 | Reduced-intensity double umbilical cord blood transplantation using Flu+Mel+low-dose TBI for MM; evaluated engraftment, viral infection risk reduction, and survival |
| [NCT00802568](https://clinicaltrials.gov/study/NCT00802568) | Phase 2 | Completed | 48 | Pilot allo-HSCT with Flu+Busulfan+Antithymocyte Globulin conditioning for multiple myeloma; assessed long-term disease control and safety of RIC approach |
| [NCT00006251](https://clinicaltrials.gov/study/NCT00006251) | Phase 1/2 | Completed | 21 | Flu+low-dose TBI to induce mixed hematopoietic chimerism in patients with hematopoietic cancers including MM; studied graft-versus-tumor effect with donor lymphocyte infusion |
| [NCT01503242](https://clinicaltrials.gov/study/NCT01503242) | Phase 1 | Completed | 15 | ⁹⁰Y-BC8 radiolabeled antibody + Fludarabine + TBI followed by HLA-matched allo-PBSC transplant specifically for multiple myeloma patients |
| [NCT00054353](https://clinicaltrials.gov/study/NCT00054353) | Phase 1/2 | Completed | 16 | Multi-center reduced-intensity allo-HSCT with Flu+Mel+TBI from matched related and unrelated donors for MM; assessed engraftment and GVM effects |
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | Completed | 20 | Fludarabine + Methoxyamine (TRC102, a base excision repair inhibitor) for relapsed/refractory hematologic malignancies including plasma cell tumors; dose-finding and safety |
| [NCT05594797](https://clinicaltrials.gov/study/NCT05594797) | Phase 2 | Recruiting | 100 | BCMA-targeted CAR-T injection for R/R multiple myeloma — all patients receive Flu+Cyclophosphamide lymphodepletion prior to CAR-T infusion |
| [NCT07477912](https://clinicaltrials.gov/study/NCT07477912) | Phase 1/2 | Recruiting | 30 | Anti-BCMA CAR-T cell immunotherapy for adults with R/R multiple myeloma — Fludarabine is the lymphodepleting backbone enabling CAR-T engraftment |
| [NCT06196255](https://clinicaltrials.gov/study/NCT06196255) | Phase 1/2 | Recruiting | 20 | Anti-FcRL5 CAR-T cells in R/R multiple myeloma — Flu+Cyclophosphamide lymphodepletion regimen used prior to CAR-T infusion |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 | Am J Clin Oncol | Phase 1 study of Bortezomib+Fludarabine+Melphalan (±total marrow irradiation) as allo-HSCT conditioning for high-risk or refractory MM; assessed dose-limiting toxicities |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | Cohort | Blood Cancer J | Compared Bendamustine vs Flu/Cy lymphodepletion prior to BCMA CAR-T in MM; outcomes and toxicity profiles assessed across regimens |
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | Preclinical | Eur J Haematol | Direct antitumor activity of Fludarabine against MM demonstrated — inhibits myeloma cell proliferation via Akt phosphorylation suppression in RPMI8226 line in vitro and in vivo |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 | Leuk Res Rep | Allo-SCT for MM with novel myeloablative split-dose Busulfan+Fludarabine+post-transplant Cyclophosphamide; 1-year OS 50%, NRM 33% in 6 MM patients |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Retrospective cohort | Bone Marrow Transplant | Multicenter retrospective of Flu+Treosulfan RIC before allo-SCT in 34 MM patients; myeloablation achieved in all, feasibility of RIC approach confirmed |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | Case Report | Eur J Haematol | Early clinical evidence of Fludarabine activity in plasma cell leukemia, an aggressive plasma cell malignancy closely related to myeloma |
| [31378662](https://pubmed.ncbi.nlm.nih.gov/31378662/) | 2019 | Phase 2 | Lancet Haematol | Phase 2 trial of humanised anti-CD19+anti-BCMA CAR-T (with Flu-based lymphodepletion) in R/R MM; ORR 88%, deep responses including stringent CRs |
| [35333600](https://pubmed.ncbi.nlm.nih.gov/35333600/) | 2022 | Phase 2 (long-term) | J Clin Oncol | Long-term follow-up of dual BCMA+CD19 CAR-T therapy (Flu lymphodepletion) in R/R MM; high response rates and extended remissions documented |
| [36690811](https://pubmed.ncbi.nlm.nih.gov/36690811/) | 2023 | Phase 1 | Nat Med | UNIVERSAL trial of allogeneic BCMA CAR-T (ALLO-715) in 43 R/R MM patients using modified lymphodepletion containing anti-CD52; ORR 56% |
| [33784005](https://pubmed.ncbi.nlm.nih.gov/33784005/) | 2021 | Phase 1 | Clin Transl Med | Phase 1 anti-BCMA CAR-T with Flu-based lymphodepletion in R/R MM and plasma cell leukemia; safety established, preliminary anti-myeloma efficacy observed |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Purine nucleoside analogue — fluorinated adenine analogue) |
| Myelosuppression Risk | **High** — severe myelosuppression is the primary and expected dose-limiting toxicity; neutropenia, thrombocytopenia, and anemia occur regularly and require close monitoring |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (at baseline and regularly during therapy); liver function tests; renal function and serum creatinine; monitoring for opportunistic infections (PCP prophylaxis recommended); CD4+ T-cell counts for prolonged immunosuppression |
| Handling Protection | Must follow cytotoxic drug handling regulations; given profound and prolonged immunosuppression, infection control precautions beyond standard chemotherapy handling are warranted |

---

## Safety Considerations

Please refer to the package insert for safety information. Based on the drug class (fluorinated purine analogue, conventional cytotoxic), key known safety concerns include severe myelosuppression, increased risk of opportunistic infections (including Pneumocystis jirovecii pneumonia and viral reactivation), autoimmune hemolytic anemia, and neurological toxicity at high doses. Formal safety data including package insert warnings, contraindications, and drug interaction profiles were not available in this evaluation pack and must be obtained before clinical application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 trials (NCT01453101, n=54; NCT01408563, n=33; NCT00802568, n=48) have evaluated Fludarabine-based conditioning specifically in multiple myeloma patients, and direct preclinical evidence confirms antitumor activity against myeloma cell lines. Fludarabine is also in active use as a lymphodepleting agent across ongoing CAR-T trials in myeloma, further embedding it in the disease's treatment ecosystem. The evidence base reaches L2 level, and the mechanistic rationale — shared B-cell lineage biology, proven immunosuppressive capacity, and documented graft-versus-myeloma effects — is coherent and compelling. However, Fludarabine is not currently marketed in Canada, and formal safety data for this evaluation is absent.

**To proceed, the following is needed:**
- Obtain and review the full package insert (TFDA or equivalent) to document warnings, contraindications, and precautions
- Conduct a formal drug-drug interaction (DDI) assessment — no DDI data was identified in this evaluation
- Clarify the intended clinical role: (a) direct cytotoxic agent for myeloma, (b) RIC conditioning backbone for allo-HSCT, or (c) lymphodepleting pretreatment for CAR-T — each pathway carries distinct evidence requirements and regulatory implications
- Retrieve MOA data from DrugBank (DB01073) to complete mechanistic linkage analysis
- Assess Canada regulatory pathway for potential market entry or compassionate access
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

