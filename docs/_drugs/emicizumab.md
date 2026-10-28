---
layout: default
title: Emicizumab
parent: Model Prediction Only (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "EMICIZUMAB"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "thrombotic thrombocytopenic purpura", "fetal and neonatal alloimmune thrombocytopenia", "flood factor deficiency"]
description: "Emicizumab: predicted new indication Pseudo-von Willebrand disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Emicizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Emicizumab: Pseudo-von Willebrand disease
{: .text-alpha }

## One-Sentence Summary

Emicizumab is a bispecific antibody originally used to treat hemophilia, including the symptomatic form in female carriers.
The TxGNN model predicts it may be effective for **acquired coagulation factor deficiency** (in practice, acquired hemophilia A), with **20 publications** currently supporting this direction. Of these, 10 were available for review, including two prospective phase 2/3 studies. No clinical trials are registered under this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 4 of 4) |
| Number of DINs | 4 (valid: 4) |
| Recommended Decision | Proceed with Guardrails |

**Note on selection:** The TxGNN top-ranked prediction was pseudo-von Willebrand disease (0.9999). It has no supporting trials or literature and no clear mechanistic link, so it is rated L5 / Hold. This report focuses on acquired coagulation factor deficiency (rank 5), the prediction with the strongest evidence. Other predictions are summarised at the end.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the data compiled for this report. From the available pharmacology information, emicizumab is a bispecific antibody that binds activated factor IX (KD about 1.52 µM) and factor X (KD about 0.98 µM). It brings them together and mimics the cofactor function of activated factor VIII.

In acquired hemophilia A, autoantibodies neutralise the patient's own factor VIII, causing severe bleeding. Because emicizumab replaces factor VIII function through a different structure, these autoantibodies do not neutralise it. This gives a direct mechanistic rationale that follows from its original use in congenital hemophilia A with inhibitors.

The evidence supports acquired hemophilia A specifically. It should not be extended to other acquired factor deficiencies without further data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in the data compiled for this report. Prospective studies appear in the literature below. A Japanese phase 3 trial in acquired hemophilia A is also mentioned in the pharmacology data.

---

## Literature Evidence

The 10 most relevant publications, prioritising prospective studies:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase 2, single-arm, open-label | Lancet Haematol | GTH-AHA-EMI: emicizumab prophylaxis protected patients with acquired hemophilia A from bleeding and allowed immunosuppression to be deferred in the first 12 weeks |
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Phase 3, single-arm, open-label | J Thromb Haemost | First prospective multicenter phase 3 study of emicizumab prophylaxis in acquired hemophilia A |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Phase 3 final analysis (AGEHA) | Thromb Haemost | Final results, including patients ineligible for immunosuppression and long-term prophylaxis |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Cohort | Blood Adv | Two-year follow-up of GTH-AHA-EMI: sustained survival benefit with postponed immunosuppression |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Real-world cohort | Blood Adv | 62 patients treated off-label at 12 US hemophilia centres; real-world impact of emicizumab and immunosuppression |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Consensus recommendations | Hamostaseologie | GTH-AHA working group recommendations on emicizumab use, based on the GTH-AHA-EMI study |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | Study | J Thromb Haemost | Compares emicizumab with immunosuppressive therapy and its potential to reduce early aggressive immunosuppression |
| [37276345](https://pubmed.ncbi.nlm.nih.gov/37276345/) | 2023 | Case series | Haemophilia | Emicizumab use in acquired hemophilia A, with no randomised trials available |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Review | J Thromb Haemost | Management of acquired hemophilia A in the emicizumab era |
| [42290320](https://pubmed.ncbi.nlm.nih.gov/42290320/) | 2026 | Study | Haemophilia | Breakthrough bleeding during emicizumab prophylaxis: 22 clinically relevant new bleeds in 14 of 47 patients, most needing haemostatic treatment |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02479621 | HEMLIBRA | Not specified | Not specified |
| 02479648 | HEMLIBRA | Not specified | Not specified |
| 02479656 | HEMLIBRA | Not specified | Not specified |
| 02479664 | HEMLIBRA | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions** (5 recorded):
  - **Anti-inhibitor coagulant complex (aPCC): Major.** This combination is associated with thrombotic complications, including thrombotic microangiopathy.
  - Antihemophilic factor, human recombinant: Moderate.
  - Coagulation factor VIIa, recombinant human: Moderate.
  - Pharmacological targets: coagulation factor IX and factor X (the intended mechanism, not a harmful interaction).

Package insert warnings and contraindications were not available. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Prospective phase 2 and phase 3 studies, a real-world cohort and consensus recommendations support emicizumab in acquired hemophilia A, with a strong mechanistic rationale. The studies are non-randomised and the evidence covers only this subtype, so the rating is L2 rather than L1.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, and the approved indication text for the four DINs (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- A thrombosis risk plan, especially to avoid concomitant aPCC or to limit bypassing agents
- Monitoring guidance: chromogenic factor VIII assays are needed, because emicizumab interferes with standard clotting assays
- Clarification of the role of immunosuppression alongside emicizumab, and a Canadian regulatory pathway for acquired hemophilia A
- Review of the remaining 10 publications not included in the data

---

## Other Predictions (All Hold)

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Pseudo-von Willebrand disease | 0.9999 | L5 | Platelet-type disorder with no clear link to factor VIII mimicry; no evidence |
| Primary release disorder of platelets | 0.9999 | L5 | Emicizumab does not correct platelet secretion; speculative |
| Glanzmann thrombasthenia | 0.9998 | L5 | Only an indirect review of rFVIIa; no emicizumab-specific evidence |
| Scott syndrome | 0.9992 | L5 | Defective phospholipid exposure may limit efficacy; no plausible basis |
| Bleeding diathesis due to a collagen receptor defect | 0.9986 | L5 | Platelet receptor defect; weak link |
| Hemorrhagic disorder due to constitutional thrombocytopenia | 0.9985 | L5 | Theoretical only; no data |
| Thrombotic thrombocytopenic purpura | 0.9961 | L5 | **Safety concern:** the problem is thrombosis, and emicizumab promotes coagulation; likely a spurious association |
| Fetal and neonatal alloimmune thrombocytopenia | 0.9952 | L5 | Does not address the immune mechanism; no evidence |
| "Flood factor deficiency" | 0.9940 | L5 | Ambiguous name, possibly a data error; verify against the source ontology |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

