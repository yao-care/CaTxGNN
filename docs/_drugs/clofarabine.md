---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine: From Relapsed/Refractory Pediatric ALL to Myeloid Leukemia

## One-Sentence Summary

Clofarabine (Clolar) is a second-generation purine nucleoside analog that received accelerated FDA approval in 2004 for the treatment of relapsed or refractory acute lymphoblastic leukemia (ALL) in pediatric patients after at least two prior regimens, though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Myeloid Leukemia (AML/MDS)**, with evidence from **multiple completed Phase 3 randomized trials** and **20 publications** firmly supporting this direction.
Notably, a 727-patient Phase 3 trial directly comparing clofarabine to standard-of-care chemotherapy in older adults with AML has already been completed, placing this prediction on exceptionally strong clinical footing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada; FDA-approved (2004) for pediatric relapsed/refractory ALL (ages 1–21, ≥2 prior regimens) |
| Predicted New Indication | Myeloid Leukemia (AML / MDS) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs identified in the evidence) |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on Evidence Level:** The automated scoring in this evidence pack assigned L2; however, manual review identified at least two completed Phase 3 randomized controlled trials directly in AML (NCT02085408, n=727; NCT00317642, n=326), qualifying this indication for L1 under the defined criteria.

---

## Why is This Prediction Reasonable?

Clofarabine exerts cytotoxicity through a dual mechanism that is highly relevant to myeloid malignancies. First, it inhibits ribonucleotide reductase (RNR), depleting the intracellular deoxyadenosine triphosphate (dATP) pool and blocking de novo DNA synthesis. Second, its active 5'-triphosphate form competes with natural deoxyribonucleotides for incorporation by DNA polymerase, causing direct chain termination. A third, distinct pathway involves direct disruption of mitochondrial membrane integrity, triggering cytochrome c release and caspase-mediated apoptosis—a route that can bypass Bcl-2 overexpression, one of the most common anti-apoptotic resistance mechanisms in AML blasts.

The connection between clofarabine's proven activity in ALL and its predicted efficacy in myeloid leukemia is mechanistically grounded: both diseases involve rapidly proliferating hematopoietic progenitor cells with high DNA replication demands and strong dependence on nucleotide salvage pathways. AML blasts and MDS-transforming cells are particularly vulnerable to RNR/DNA polymerase dual inhibition. Critically, clofarabine demonstrates well-characterized synergy with cytarabine—by depleting dCTP pools via RNR inhibition, it competitively enhances the incorporation of cytarabine triphosphate (ara-CTP), amplifying the combined cytotoxic effect. This pharmacodynamic synergy is the biological foundation for the widely studied CLARA (Clofarabine + Cytarabine) and CLAM (Clofarabine + Cytarabine + Mitoxantrone) regimens.

The clinical data go well beyond mechanistic inference. Clofarabine has been evaluated in AML across the full treatment continuum—from induction in newly diagnosed patients (including Phase 3 trials in older adults) to salvage therapy in relapsed/refractory disease, to conditioning regimens for allogeneic stem cell transplantation. The TxGNN model's high-confidence prediction therefore aligns with a mature and extensively validated clinical direction, rather than representing speculative extrapolation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT02085408](https://clinicaltrials.gov/study/NCT02085408) | Phase 3 | Completed | 727 | Randomized Phase 3 trial comparing clofarabine-based induction and post-remission therapy vs. standard daunorubicin/cytarabine (7+3), followed by decitabine maintenance vs. observation, in newly diagnosed AML in adults ≥60 years |
| [NCT00317642](https://clinicaltrials.gov/study/NCT00317642) | Phase 3 | Completed | 326 | Randomized, double-blind, controlled Phase 3: clofarabine + cytarabine vs. cytarabine alone in adults ≥55 years with relapsed or refractory AML after 1–2 prior induction regimens |
| [NCT00703820](https://clinicaltrials.gov/study/NCT00703820) | Phase 3 | Completed | 324 | AML08 multicenter randomized trial: clofarabine + cytarabine vs. conventional anthracycline-based induction in newly diagnosed pediatric AML, with MRD-adapted therapy and NK cell transplantation arm |
| [NCT01101880](https://clinicaltrials.gov/study/NCT01101880) | Phase 2 | Completed | 50 | CLARA regimen (clofarabine + high-dose cytarabine + G-CSF priming) in adults <65 years with newly diagnosed AML, advanced MDS, or advanced myeloproliferative neoplasm |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | Completed | 86 | Clofarabine salvage monotherapy in relapsed/refractory AML; primary aim to achieve complete remission as a bridge to allogeneic HCT in younger patients |
| [NCT00778375](https://clinicaltrials.gov/study/NCT00778375) | Phase 2 | Completed | 122 | Clofarabine + low-dose cytarabine induction alternating with decitabine consolidation in frontline AML and high-risk MDS in patients ≥60 years |
| [NCT01457885](https://clinicaltrials.gov/study/NCT01457885) | Phase 2 | Completed | 75 | Multicenter single-arm study of myeloablative clofarabine + busulfan ×4 (CloBu4) conditioning for allogeneic HCT in non-remission AML; targeted the historically poor-prognosis population |
| [NCT01534702](https://clinicaltrials.gov/study/NCT01534702) | Phase 1/2 | Unknown | 60 | AMLSG 17-10 trial: three-drug induction (cytarabine + idarubicin + escalating clofarabine) in AML patients at high risk for induction failure; 60 patients enrolled |
| [NCT00838240](https://clinicaltrials.gov/study/NCT00838240) | Phase 1/2 | Unknown | 114 | EORTC-LG/GIMEMA AML-14A trial: randomized Phase 1/2 studying clofarabine + cytarabine + idarubicin in untreated intermediate/high-risk AML and high-risk MDS in adults aged 18–60 years |
| [NCT00088218](https://clinicaltrials.gov/study/NCT00088218) | Phase 2 | Completed | 95 | Randomized Phase 2: clofarabine monotherapy vs. clofarabine + low-dose cytarabine in previously untreated AML/high-risk MDS in patients ≥60 years; established activity of the combination |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | Phase 3 RCT Report | J Clin Oncol | AML08 trial report (Rubnitz et al.): clofarabine can replace anthracyclines and etoposide in remission induction for childhood AML without compromising efficacy, meaningfully reducing cumulative cardiotoxicity |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Prospective Phase 2 | Cancer Medicine | CLAM regimen (Gill et al.): clofarabine 30 mg/m²/d + cytarabine + mitoxantrone in relapsed/refractory AML (ages 18–65) achieved high response rates and served as an effective bridge to allogeneic HCT |
| [29773602](https://pubmed.ncbi.nlm.nih.gov/29773602/) | 2018 | Phase 1B | Haematologica | van Eijkelenburg et al.: clofarabine replacing fludarabine in combination with high-dose cytarabine and liposomal daunorubicin for pediatric relapsed/refractory AML; Phase 1B dose-finding identifying the recommended Phase 2 dose |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | Cohort Analysis | Cancers | Fenwarth et al.: CLARA consolidation regimen improves relapse-free survival specifically in younger AML patients with micro-complex karyotype, identifying a key genomic subgroup most likely to benefit |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Retrospective Cohort | Transplant Cell Ther | Connor et al.: clofarabine + busulfan (Clo/Bu4) myeloablative conditioning for allogeneic HCT in patients with active, chemotherapy-refractory myeloid malignancies; demonstrated antileukemic activity with acceptable toxicity in patients ≤70 years |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leuk Lymphoma | Ghanem et al.: comprehensive review of clofarabine's dual RNR/DNA polymerase mechanism and clinical role in AML including first-line and salvage settings; covers combination strategies and resistance patterns |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncol Hematol | Fozza et al.: systematic review of clofarabine in adult AML; covers monotherapy, combination regimens in first and second line, and pharmacodynamic synergy with cytarabine |
| [31281098](https://pubmed.ncbi.nlm.nih.gov/31281098/) | 2019 | Clinical Study Report | Lancet Oncol | Stirrups: summary report on clofarabine and cytarabine clinical outcomes in AML; contextualizes findings within the evolving treatment landscape |
| [19852733](https://pubmed.ncbi.nlm.nih.gov/19852733/) | 2009 | Review | Future Oncol | Thomas et al.: early evidence review of clofarabine activity in adult AML; described favorable single-agent activity and emerging combination strategies with cytarabine that would become the CLARA regimen |
| [21182488](https://pubmed.ncbi.nlm.nih.gov/21182488/) | 2011 | Review | Curr Med Chem | Robak et al.: survey of novel and emerging drugs for AML including clofarabine; situates clofarabine among nucleoside analogs, molecular targets, and monoclonal antibodies in the AML therapeutic pipeline |

---

## Canada Market Information

Clofarabine (DrugBank ID: DB00631) is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) are registered with Health Canada, and no product licenses are on file. The drug is commercially available in the United States under the brand name Clolar (Genzyme/Sanofi) with FDA approval for pediatric relapsed/refractory ALL, and has received approval in the European Union and Japan for the same pediatric indication.

Any clinical use of clofarabine for myeloid leukemia in Canada would currently require one of the following pathways:
- A **Special Access Programme (SAP)** request to Health Canada for individual patient access
- Enrolment in an authorized **clinical trial** with a valid CTA (Clinical Trial Application) filed with Health Canada
- A formal **New Drug Submission (NDS)** by a sponsor seeking Canadian market authorization

---

## Cytotoxicity

Clofarabine is a conventional cytotoxic antineoplastic agent (purine nucleoside analog) with well-characterized hematologic toxicity.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Second-generation purine nucleoside analog (deoxyadenosine analog; halogenated purine) |
| Myelosuppression Risk | **High** — Profound, dose-dependent myelosuppression is the primary dose-limiting toxicity; severe neutropenia, thrombocytopenia, and anemia are expected and universal in both AML and ALL settings; prolonged aplasia is common and intentional in induction contexts |
| Emetogenicity Classification | Low to moderate (consistent with other purine nucleoside analogs such as fludarabine and cladribine) |
| Monitoring Items | Complete blood count with differential (CBC + diff) at baseline and at least twice weekly during induction; serum creatinine and eGFR before each cycle; liver function tests (AST, ALT, total bilirubin) before and during treatment; daily monitoring of blood pressure, weight, and respiratory status for capillary leak syndrome / SIRS signals |
| Handling Protection | Must be prepared and administered under full cytotoxic drug handling precautions per institutional hazardous drug policies: closed-system drug transfer devices (CSTDs), biological safety cabinet (BSC), PPE including nitrile gloves, gown, and eye protection; cytotoxic waste disposal per regulatory standards |

---

## Safety Considerations

Detailed Health Canada product monograph data (key warnings and contraindications) are not available in this evidence pack.

> Please refer to the FDA prescribing information (Clolar package insert) and available peer-reviewed safety analyses as an interim reference. Based on the clinical trial literature, clinically important safety signals include: **capillary leak syndrome**, **systemic inflammatory response syndrome (SIRS)**, **severe hepatotoxicity** (including veno-occlusive disease in the transplant setting), **serious and opportunistic infections** during prolonged aplasia, and **tumor lysis syndrome**. A full drug interaction screen should be performed prior to any clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clofarabine's activity in myeloid leukemia is backed by an exceptionally mature evidence base—including two large completed Phase 3 randomized controlled trials in AML and a mechanistic rationale that is among the best-characterized in the drug repurposing field. The TxGNN prediction at 99.88% confidence correctly identifies a direction that has already been the subject of over two decades of active clinical investigation. The primary barrier to use in Canada is regulatory (no Health Canada authorization, no DINs), not scientific.

**To proceed, the following is needed:**

- **Regulatory pathway clarification**: Determine whether to pursue Health Canada SAP access, sponsor a New Drug Submission, or incorporate clofarabine as a comparator/experimental arm within a Canadian clinical trial
- **Full safety documentation**: Retrieve Health Canada-equivalent safety data from the FDA product monograph (Clolar), published toxicity analyses, and the EORTC/GIMEMA safety databases to complete a formal risk assessment
- **MOA data retrieval**: Query the DrugBank API (DB00631) to populate the missing mechanism of action fields required for the complete evidence package
- **Target population definition**: Based on the Phase 3 evidence, prioritize one of: (a) newly diagnosed AML in adults ≥60 years unfit for intensive anthracycline therapy; (b) relapsed/refractory AML as salvage bridge to allogeneic HCT; or (c) pediatric AML as part of a clofarabine-based induction protocol
- **Canadian landscape assessment**: Compare clofarabine's benefit-risk and cost-effectiveness profile against currently reimbursed AML therapies in Canada (azacitidine, venetoclax + hypomethylating agents, midostaurin for FLT3+ AML) to identify where clofarabine offers distinct clinical value
- **Pharmacovigilance plan**: Given the high myelosuppression burden, design a monitoring and toxicity management protocol appropriate for the Canadian clinical setting before any patient exposure

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require formal clinical validation before therapeutic application. All predictions are exploratory and must be evaluated through appropriate regulatory and clinical trial processes.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

