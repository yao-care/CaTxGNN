---
layout: default
title: Andexanet Alfa
parent: Model Prediction Only (L5)
nav_order: 61
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Andexanet Alfa: predicted new indication Glanzmann thrombasthenia (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "ANDEXANET ALFA"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "hemophilia"]
---

# Andexanet Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Andexanet Alfa: From DOAC-Associated Bleeding Reversal to Glanzmann Thrombasthenia
{: .text-alpha }

## One-Sentence Summary

Andexanet alfa is a recombinant factor Xa (FXa) decoy protein marketed in Canada as ONDEXXYA. Its approved indication text is not available in the data compiled for this report, but it is known to be used to reverse FXa-inhibitor anticoagulation.
The TxGNN model predicts it may be effective for **Glanzmann thrombasthenia** with a very high score, but there are **0 clinical trials** and **0 publications** supporting this specific indication. The evidence rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the Canadian license has no indication text) |
| Predicted New Indication | Glanzmann thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. From known pharmacology, andexanet alfa is a catalytically inactive recombinant FXa decoy. It binds and sequesters direct FXa inhibitors (and the antithrombin-heparin complex), restoring normal FXa activity.

Glanzmann thrombasthenia is an inherited platelet disorder caused by deficiency or dysfunction of integrin αIIbβ3 (GPIIb/IIIa), which impairs platelet aggregation. Andexanet alfa acts on the coagulation cascade, not on platelet aggregation, so **no plausible mechanistic link** was identified. The high TxGNN score is a graph-based prediction, likely driven by shared hemostasis-related network neighbours rather than biology.

The other predicted indications show the same pattern:

- **Primary release disorder of platelets** (score 99.76%): this involves defective platelet granule secretion or signalling, which andexanet alfa does not correct. There are no trials or literature.
- **Pseudo-von Willebrand disease** (score 99.65%): this is a gain-of-function defect in platelet GPIb-α, and andexanet alfa has no known effect on the VWF–GPIb axis. There are no trials or literature.
- **Hemophilia** (score 99.10%): this is a deficiency of factor VIII or IX. Andexanet alfa does not replace the missing factors. The retrieved publications concern DOAC reversal or laboratory interference, not hemophilia treatment (see Literature Evidence).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was found for Glanzmann thrombasthenia. The only literature retrieved was for the fourth-ranked prediction, hemophilia. These publications concern andexanet alfa in DOAC reversal or DOAC laboratory interference, **not** treatment of hemophilia, so the keyword match is incidental.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38620086](https://pubmed.ncbi.nlm.nih.gov/38620086/) | 2024 | Cohort (ANNEXA-4 subanalysis) | Circulation | Efficacy and safety of andexanet alfa in acute gastrointestinal bleeding on FXa inhibitors |
| [31962376](https://pubmed.ncbi.nlm.nih.gov/31962376/) | 2020 | Laboratory comparison | Haemophilia | Andexanet alfa or DOAC Stop used to neutralize rivaroxaban interference in FVIII/FIX assays |
| [33742436](https://pubmed.ncbi.nlm.nih.gov/33742436/) | 2021 | Guideline | Thromb Haemost | ICSH recommendations for laboratory measurement of DOACs, including the reversal agent |
| [42033142](https://pubmed.ncbi.nlm.nih.gov/42033142/) | 2026 | Position statement | Br J Haematol | British Society for Haematology position on andexanet alfa use |
| [36819179](https://pubmed.ncbi.nlm.nih.gov/36819179/) | 2023 | Review | EJHaem | Review of UK hospital protocols for andexanet alfa |
| [30309890](https://pubmed.ncbi.nlm.nih.gov/30309890/) | 2018 | Review | Blood | Reversal of anti-FXa agents and unmet needs in trauma patients |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Review | Curr Pharm Des | New hemostatic agents and perioperative anaesthetic considerations |
| [26519420](https://pubmed.ncbi.nlm.nih.gov/26519420/) | 2016 | Review | Drug Saf | NOAC reversal strategies: development status and future perspectives |
| [27254626](https://pubmed.ncbi.nlm.nih.gov/27254626/) | 2016 | Review | Dtsch Med Wochenschr | Coagulation disorders in intensive care, including NOAC antidotes |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02538539 | ONDEXXYA | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for Glanzmann thrombasthenia is supported only by a graph-based model score. There are no clinical trials and no relevant literature, and the drug's mechanism (neutralizing FXa inhibitors) does not address the platelet aggregation defect. The same applies to the other three predicted indications.

**To proceed, the following is needed:**
- The Health Canada package insert (approved indication, warnings, and contraindications), which is required before any safety screening
- Mechanism-of-action data from DrugBank to complete the mechanistic analysis
- Preclinical or mechanistic evidence showing a biological link between FXa-decoy activity and platelet function in Glanzmann thrombasthenia
- Consideration of whether the predicted indications are better treated as model artefacts than as repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

