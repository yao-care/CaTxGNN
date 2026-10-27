---
layout: default
title: Norethindrone Enanthate
parent: Model Prediction Only (L5)
nav_order: 666
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Norethindrone Enanthate: predicted new indication Antithrombin deficiency type 2 (evidence level L5). Approved use: Not available in the compiled Canadian license data"
monitor_inn: "Norethindrone enanthate"
predicted_indications: ["antithrombin deficiency type 2", "candidiasis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "rheumatoid arthritis", "leprosy", "heart neoplasm", "cardiovascular disease", "plasma cell myeloma", "thrombophilia"]
---

# Norethindrone Enanthate
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

## Norethindrone Enanthate: From Hormonal Contraception to Antithrombin Deficiency Type 2
{: .text-alpha }

## One-Sentence Summary

Norethindrone enanthate is a depot progestin, marketed in Canada in 18 licensed products, and the data compiled for this report did not list an approved indication for it.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2**, but this is a graph-based prediction only.
There are **no clinical trials and no publications** supporting this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled Canadian license data |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 98.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 18 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Norethindrone enanthate is a long-acting injectable progestin, a drug class generally used for hormonal contraception. Its efficacy in any thrombotic or coagulation disorder has not been shown.

The link to antithrombin deficiency type 2 looks like an artefact of the knowledge graph. Coagulation-related disease nodes cluster together, which can inflate scores for drugs near them. Antithrombin deficiency is a thrombophilia. Progestin-only injectables are generally thought to carry little or no venous thrombosis risk, but that is a safety observation and does not show therapeutic benefit. Use in thrombotic conditions could in principle be contraindicated.

Other top-ranked predictions show the same pattern: heparin cofactor 2 deficiency (98.90%), factor 5 excess with spontaneous thrombosis (98.87%) and thrombophilia (97.99%) all lack supporting evidence. Predictions such as candidiasis, leprosy, rheumatoid arthritis, heart neoplasm and plasma cell myeloma also have no trials or publications and no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications are available for antithrombin deficiency type 2. The only predicted indication with literature is cardiovascular disease (rank 8, score 98.07%), where six publications concern the drug's safety and metabolic effects as a contraceptive, not treatment of cardiovascular disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1533383](https://pubmed.ncbi.nlm.nih.gov/1533383/) | 1992 | Cohort | Horm Metab Res | One-year comparison of two injectable contraceptives (DMPA and norethisterone oenanthate) on serum and lipoprotein lipids |
| [1424623](https://pubmed.ncbi.nlm.nih.gov/1424623/) | 1992 | Cohort | Contraception | In 56 long-term users, no significant difference in triglycerides, total cholesterol, LDL or VLDL versus non-users; a significant reduction in mean HDL |
| [6434228](https://pubmed.ncbi.nlm.nih.gov/6434228/) | 1984 | Review | Contraception | Contraception with progestagens in systemic lupus erythematosus; 200 mg IM norethisterone enanthate was compared with oral levonorgestrel and controls, with no significant difference in active disease episodes |
| [2967589](https://pubmed.ncbi.nlm.nih.gov/2967589/) | 1987 | Review | Wien Med Wochenschr | Depot progestins are suitable when cardiovascular risk factors exclude estrogen-progestin combinations; covers mode of action, indications and contraindications |
| [5351331](https://pubmed.ncbi.nlm.nih.gov/5351331/) | 1969 | Cohort | Dtsch Med Wochenschr | Studies during use of a long-acting parenteral contraceptive |
| [4011568](https://pubmed.ncbi.nlm.nih.gov/4011568/) | 1985 | Review | The Practitioner | Overview of hormonal contraceptive methods |

## Canada Market Information

The compiled license data lists 18 valid licenses, all single-ingredient, but without dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 02458683 | MAEVE |
| 02441306 | JENCYCLA |
| 00023760 | NORLUTATE |
| 02410303 | MOVISSE |
| 02187108 | SYNPHASIC 21 TABLETS |

## Safety Considerations

Please refer to the package insert for safety information.

The following should be noted as general considerations from the predicted indications:
- The predicted targets (antithrombin deficiency type 2, heparin cofactor 2 deficiency, factor 5 excess, thrombophilia) are prothrombotic conditions, so any hormonal use would need a thorough thrombotic safety review first.
- The available cardiovascular literature is old (1969–1992) and addresses lipid effects, including a reduction in HDL with long-term use. It bears on risk assessment, not therapeutic benefit.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high TxGNN score. There are no clinical trials or publications, no established mechanism, and the target condition is prothrombotic, which raises safety concerns. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Mechanism of action data for the drug
- Original approved indication text and dosage form for the Canadian licenses
- A thrombotic safety assessment specific to antithrombin deficiency and related thrombophilias
- Any preclinical or clinical evidence of a therapeutic effect, which does not currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

