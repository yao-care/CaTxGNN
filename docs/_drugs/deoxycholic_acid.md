---
layout: default
title: Deoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 3
---

# Deoxycholic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Deoxycholic Acid: From Bile Acid Biology to Diabetic Nephropathy

> **Report Note:** The TxGNN model's top two predicted indications—*autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome* (rank 1, 99.49%) and *brain small vessel disease 1 with or without ocular anomalies* (rank 2, 99.49%)—carry no supporting clinical trials or relevant literature, and the model's own rationale attributes both high scores to graph topology proximity rather than genuine mechanistic links. This report therefore focuses on the third-ranked prediction, **Diabetic Nephropathy** (99.32%), which is the most clinically actionable prediction with coherent mechanistic support and 20 relevant publications.

---

## One-Sentence Summary

Deoxycholic acid (DCA) is a secondary bile acid and endogenous signaling molecule that acts as a partial agonist of the farnesoid X receptor (FXR) and the G protein-coupled receptor TGR5—two pathways with established renoprotective roles in the kidney. The TxGNN model predicts it may be effective for **Diabetic Nephropathy**, with **0 clinical trials** and **20 publications** providing mechanistic context, primarily from structurally related bile acids rather than DCA directly. Evidence currently sits at the preclinical/mechanistic level (L4), and this prediction warrants systematic investigation before any clinical advancement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication in Canada; endogenous secondary bile acid metabolite |
| Predicted New Indication | Diabetic Nephropathy |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Deoxycholic acid is produced by the intestinal microbiome through biotransformation of primary bile acids. Its chief pharmacological roles involve activation of the nuclear hormone receptor FXR and the membrane receptor TGR5 (GPBAR1). Both receptors are expressed in renal proximal tubular cells and podocytes, where they regulate metabolic homeostasis, inflammation, and fibrogenesis. The mechanistic case for DCA in diabetic nephropathy rests on four proposed pathways: (1) FXR activation suppresses the TGF-β/SMAD fibrotic cascade in tubular cells; (2) TGR5 activation improves renal tubular energy metabolism and reduces reactive oxygen species; (3) FXR/TGR5 signaling reduces lipid accumulation in the kidney; and (4) modulation of the gut–kidney axis lowers systemic inflammatory burden that drives glomerular damage.

This hypothesis is substantiated by a consistent body of preclinical evidence—not for DCA itself, but for structurally related bile acids. Ursodeoxycholic acid (UDCA) has demonstrated renoprotection across multiple diabetic animal models, attenuating albuminuria, podocyte apoptosis, endoplasmic reticulum stress, and SGLT2 upregulation. Tauroursodeoxycholic acid (TUDCA) has similarly reduced renal tubular injury and glomerular damage in db/db and STZ-induced diabetic mice. Critically, a dual FXR/TGR5 agonist (INT-767) directly targeting both receptors prevented nephropathy progression in two separate diabetic mouse models, providing the most direct mechanistic parallel to DCA's receptor pharmacology. A 2024 human metabolomics study further confirms that bile acid metabolism is progressively disrupted in patients with diabetic kidney disease, establishing the pathway's relevance in human pathophysiology.

However, important limitations apply. DCA is pharmacologically distinct from UDCA and TUDCA—it exhibits significantly greater membrane-disrupting (cytolytic) activity and can promote intestinal inflammation at higher doses. This property is purposefully used in submental fat reduction (Kybella/Belkyra) but represents a meaningful safety concern for systemic repurposing. No preclinical or clinical study has directly tested DCA in diabetic nephropathy. The available evidence therefore supports a plausible class effect inference but cannot be equated with drug-specific data for DCA. A dedicated in vivo safety and efficacy program would be the necessary next step.

---

## Clinical Trial Evidence

No clinical trials investigating deoxycholic acid in diabetic nephropathy are currently registered in ClinicalTrials.gov or international trial registries (ICTRP).

---

## Literature Evidence

All publications below relate to bile acid receptor signaling in diabetic nephropathy. No studies directly test DCA; studies involve UDCA, TUDCA, FXR agonists, or FXR knockout models.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29089371](https://pubmed.ncbi.nlm.nih.gov/29089371/) | 2018 | Animal Study | J Am Soc Nephrol | FXR/TGR5 dual agonist INT-767 prevents nephropathy progression in STZ-diabetic and db/db mice; demonstrates synergistic renoprotection through differential receptor-mediated pathways — most direct mechanistic parallel to DCA |
| [28696246](https://pubmed.ncbi.nlm.nih.gov/28696246/) | 2017 | Animal Study | J Am Soc Nephrol | TUDCA (FXR agonist) protects against diabetic tubulopathy by reducing maladaptive ER stress signaling; proposes FXR activation as a viable add-on therapeutic target in diabetic nephropathy |
| [39384774](https://pubmed.ncbi.nlm.nih.gov/39384774/) | 2024 | Clinical Cohort | Nutr Diabetes | Metabolomic profiling in human patients demonstrates step-wise disruption of bile acid metabolism correlating with diabetic kidney disease progression — supports bile acid pathway relevance in human disease |
| [27193377](https://pubmed.ncbi.nlm.nih.gov/27193377/) | 2016 | Animal Study | Biol Pharm Bull | UDCA ameliorates diabetic nephropathy in db/db mice by attenuating hyperglycemia-induced oxidative stress and endoplasmic reticulum stress |
| [26999661](https://pubmed.ncbi.nlm.nih.gov/26999661/) | 2016 | In vitro / Animal | Lab Invest | UDCA prevents ER stress-induced podocyte apoptosis in db/db mice, protecting glomerular cells against high-glucose-mediated injury; UDCA + 4-PBA combination evaluated |
| [22429686](https://pubmed.ncbi.nlm.nih.gov/22429686/) | 2012 | Animal Study | Diabetes Res Clin Pract | UDCA treatment reduces SGLT2 expression and oxidative stress markers in kidneys of streptozotocin-induced diabetic rats |
| [37790634](https://pubmed.ncbi.nlm.nih.gov/37790634/) | 2023 | Animal Study | PeerJ | FXR knockout in db/db mice accelerates dysregulated glucose metabolism and renal fibrosis, confirming FXR as a protective receptor in diabetic kidney disease |
| [26655953](https://pubmed.ncbi.nlm.nih.gov/26655953/) | 2016 | Animal Study | J Biol Chem | FXR activation protects against obesity-induced kidney injury in uninephrectomized high-fat-diet mice via anti-fibrotic, lipid-lowering, and anti-inflammatory mechanisms |
| [36690052](https://pubmed.ncbi.nlm.nih.gov/36690052/) | 2023 | Animal Study | Eur J Pharmacol | TUDCA evaluated as monotherapy and as add-on to telmisartan in STZ-induced diabetic kidney disease; ER stress inhibition identified as key mechanism |
| [36996678](https://pubmed.ncbi.nlm.nih.gov/36996678/) | 2023 | Animal Study | Biomed Pharmacother | Relaxin's renoprotective effects in STZ-diabetic mice are accompanied by elevated endogenous bile acid levels, suggesting upregulation of the bile acid signaling axis as part of the protective mechanism |

---

## Canada Market Information

Deoxycholic acid (DB03619) has no registered products with Health Canada. There are currently **0 Drug Identification Numbers (DINs)** issued. The drug is not marketed in Canada under any dosage form or brand name.

---

## Safety Considerations

No specific safety data—including key warnings, contraindications, or drug-drug interactions—was available in the current evidence pack.

Please refer to the package insert for safety information.

**Additional consideration for repurposing:** Deoxycholic acid has well-characterized membrane-disrupting (cytolytic) properties at therapeutic concentrations. This activity is intentionally leveraged in approved products for submental fat reduction (Kybella/Belkyra), where localized adipocyte lysis is the therapeutic goal. For systemic repurposing targeting renal disease, the safety window between FXR/TGR5-mediated efficacy (likely achieved at lower concentrations) and non-specific membrane cytotoxicity must be rigorously characterized before any dose selection.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis for DCA in diabetic nephropathy is biologically coherent—FXR and TGR5 receptor activation has demonstrated renoprotective effects in multiple preclinical models using related bile acids, and bile acid pathway dysregulation has been confirmed in human diabetic kidney disease. However, no study has directly tested DCA in this indication, the drug is not registered in Canada, and DCA's inherent cytolytic properties introduce a non-trivial systemic safety concern that distinguishes it from safer bile acid analogues such as UDCA and TUDCA.

**To proceed, the following is needed:**
- Direct preclinical testing of DCA in validated diabetic nephropathy models (db/db or STZ-induced mice) at doses below cytolytic thresholds to establish proof of concept
- Pharmacokinetic profiling to determine renal tissue DCA exposure and systemic plasma levels following oral or parenteral administration
- Comparative safety evaluation of DCA versus UDCA and TUDCA at equivalent FXR/TGR5-activating doses, with emphasis on intestinal and renal toxicity
- Full mechanism of action characterization from DrugBank and primary literature (currently a data gap)
- Health Canada package insert and TFDA monograph review to identify any existing warnings or contraindications relevant to systemic use
- Evaluation of whether a more selective, clinically advanced FXR agonist (e.g., obeticholic acid, TUDCA) would be a preferable repurposing candidate with a more favorable safety profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

