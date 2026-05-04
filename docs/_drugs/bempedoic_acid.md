---
layout: default
title: Bempedoic Acid
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Bempedoic acid is an ATP-citrate lyase (ACLY) inhibitor approved in the US and EU for lowering LDL cholesterol in adults with heterozygous familial hypercholesterolemia (HeFH) or established atherosclerotic cardiovascular disease, though it is not yet marketed in Canada.
The TxGNN model generated 10 predicted indications; the most clinically plausible is **Homozygous Familial Hypercholesterolemia (HoFH)** (model rank 6), supported by **0 registered clinical trials** but **17 publications** — including a 2026 real-world study confirming adjunctive clinical use in HoFH patients.

> **Note on TxGNN Rankings:** The model's top five predictions (hyperthyroidism, thyroid hormone receptor-β resistance, malignant catarrh, infectious bovine rhinotracheitis, and CMV infection) are mechanistically implausible or biologically inapplicable to bempedoic acid's ACLY-inhibiting mechanism; two are exclusively veterinary diseases. HoFH (rank 6, score 99.48%) is the highest-ranked prediction with a direct mechanistic rationale and real-world supporting evidence, and is therefore the focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia — LDL-C reduction in HeFH and established ASCVD (FDA/EMA approved 2020; not approved in Canada) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.48% (Rank 6 overall; rank 1 among biologically plausible predictions) |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bempedoic acid inhibits ATP-citrate lyase (ACLY), a hepatic enzyme that sits upstream of HMG-CoA reductase in the cholesterol biosynthesis pathway. By reducing the supply of cytosolic acetyl-CoA, it simultaneously curtails both cholesterol and fatty acid synthesis. A critical property of this mechanism is its partial independence from the LDL receptor (LDLR): it reduces hepatic cholesterol *output* rather than increasing receptor-mediated *clearance*, making it theoretically active even when LDLR function is impaired.

HoFH arises from biallelic loss-of-function mutations in LDLR (or, less commonly, APOB, PCSK9, or LDLRAP1), resulting in severely elevated LDL-C levels — often exceeding 400 mg/dL — and premature cardiovascular disease in childhood or early adulthood. Because LDLR is non-functional or markedly deficient, therapies that depend on receptor upregulation (statins, PCSK9 inhibitors) provide far less LDL-C reduction in HoFH than in HeFH. Bempedoic acid's LDLR-independent route therefore offers a plausible, if modest, adjunctive benefit that does not require a functioning receptor.

This mechanistic logic is confirmed in practice: a preclinical large-animal study (PMID 29449335) demonstrated that bempedoic acid lowers LDL-C and attenuates atherosclerosis in LDLR-deficient Yucatan miniature pigs — a well-accepted HoFH surrogate model. A 2026 real-world study (PMID 41274797) then documented its actual clinical use in HoFH patients, typically as add-on therapy to PCSK9 inhibitors and/or evinacumab. Multiple contemporary reviews further position bempedoic acid within the evolving HoFH treatment landscape, acknowledging its limited but real LDLR-independent LDL-C-lowering contribution.

---

## Clinical Trial Evidence

Currently no clinical trials registered for bempedoic acid specifically in homozygous familial hypercholesterolemia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Real-world Study | J Clin Lipidology | First real-world evaluation of bempedoic acid efficacy and tolerability specifically in HoFH patients; confirms adjunctive clinical use |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Expert Consensus | J Clin Lipidology | National Lipid Association consensus update on FH management; addresses bempedoic acid's role in treatment algorithms |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Narrative Review | Exp Mol Pathol | Comprehensive review of innovative HoFH therapies; bempedoic acid discussed as adjunct for residual LDL-C burden |
| [29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/) | 2018 | Preclinical Study | Arterioscler Thromb Vasc Biol | Bempedoic acid lowers LDL-C and attenuates atherosclerosis in LDLR-deficient (LDLR⁺/⁻ and LDLR⁻/⁻) miniature pigs — key HoFH animal model data |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Narrative Review | J Atherosclerosis Thrombosis | HoFH management review; acknowledges bempedoic acid as an LDLR-independent adjunct in multi-drug regimens |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review (JACC Focus Seminar) | J Am Coll Cardiology | Positions bempedoic acid among emerging LDL-C-lowering therapies alongside inclisiran and PCSK9i for refractory hypercholesterolemia |
| [34081216](https://pubmed.ncbi.nlm.nih.gov/34081216/) | 2021 | Review | Curr Cardiology Reports | Updates on management of familial and refractory hypercholesterolemias; bempedoic acid reviewed as post-statin option |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Review | Cardiology in Review | Bempedoic acid discussed alongside evinacumab as part of the expanding HoFH treatment arsenal |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Review | Am J Prev Cardiology | Emphasizes cumulative LDL-C exposure as ASCVD driver; bempedoic acid reviewed as adjunctive LDL-lowering strategy |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Non-statin lipid-lowering drugs including bempedoic acid for statin-intolerant and refractory patients |

---

## Canada Market Information

Bempedoic acid is **not currently marketed in Canada** (0 DINs on record). For reference, it has been approved in the following jurisdictions under these indications:

| Jurisdiction | Brand Name | Approval Year | Approved Indication |
|---|---|---|---|
| United States (FDA) | Nexletol® | 2020 | Adults with HeFH or established ASCVD requiring additional LDL-C reduction (as adjunct to diet ± other lipid-lowering therapies) |
| United States (FDA) | Nexlizet® (+ ezetimibe) | 2020 | Same as above, combination tablet |
| European Union (EMA) | Nilemdo® | 2020 | Adults with primary hypercholesterolaemia or mixed dyslipidaemia, as adjunct to diet |
| European Union (EMA) | Nustendi® (+ ezetimibe) | 2020 | Same as above, combination tablet |

A Health Canada regulatory submission pathway assessment would be required before any Canadian clinical use.

---

## Safety Considerations

Formal Canadian safety data (monograph or TFDA product insert) was not available in this evidence pack. Key safety concerns known from US/EU labelling and clinical literature include:

- **Hyperuricemia and Gout**: Bempedoic acid inhibits urate transporter OAT4, raising serum uric acid; gout flares occurred more frequently than placebo in clinical trials. Caution required in patients with gout history.
- **Tendon Rupture Risk**: Signal observed in clinical trials; patients with tendon disorders or on concomitant fluoroquinolones should be monitored closely.
- **Pregnancy Contraindication**: Animal studies demonstrate embryotoxicity and fetotoxicity. Use during pregnancy is absolutely contraindicated (comparable to Pregnancy Category X). The rank-10 TxGNN prediction for pregnancy-associated osteoporosis must be rejected on this safety ground alone.
- **Muscle-related Effects**: Though bempedoic acid acts upstream of the mevalonate pathway and does not inhibit HMG-CoA reductase directly, a small increase in CPK and rare myopathy reports warrant monitoring, particularly in combination with statins.
- **Drug Interactions**: No DDI data was available in this evidence pack. Known interactions include simvastatin and pravastatin (increased exposure); dose adjustments may be required.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bempedoic acid's ACLY-inhibiting, LDLR-independent mechanism is directly relevant to HoFH — a condition in which impaired LDL receptor function limits the efficacy of receptor-dependent standard therapies. A 2026 real-world study confirms it is already being used adjunctively in HoFH, and a preclinical LDLR-deficient large-animal study demonstrates proof-of-concept LDL-C reduction and anti-atherosclerotic effect. Evidence is L3 grade (observational/review-level), which justifies further structured evaluation but not first-line adoption.

**To proceed, the following is needed:**
- A dedicated prospective or randomized study in HoFH patients to quantify the incremental LDL-C reduction that bempedoic acid provides on top of current maximal therapy (PCSK9i ± evinacumab ± lomitapide ± LDL apheresis)
- Complete safety monograph review, with specific attention to hyperuricemia, tendon rupture, and embryotoxicity risks
- Health Canada regulatory pathway assessment — bempedoic acid is not marketed in Canada; a New Drug Submission (NDS) would be required
- Clarification of HoFH genotype-response relationships: patients with residual LDLR activity (missense mutations) may respond differently than those with null mutations
- Pharmacoeconomic analysis: given the high cost of existing HoFH therapies and the modest absolute LDL-C reduction expected from ACLY inhibition in an LDLR-null background, cost-effectiveness data will be essential for formulary consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

