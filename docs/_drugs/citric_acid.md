---
layout: default
title: Citric Acid
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 8
---

# Citric Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Citric Acid: From Diagnostic Aid to Stomach Disease

## One-Sentence Summary

Citric acid is a naturally occurring tricarboxylic acid with no formally approved therapeutic indication in Canada; it is widely used as a pharmaceutical excipient, food additive, and as a test meal component to enhance the accuracy of the ¹³C-Urea Breath Test (UBT) for *Helicobacter pylori* detection.
The TxGNN model predicts it may be effective for **Stomach Disease**, with **20 publications** providing indirect biological and mechanistic support for this direction.
However, existing evidence positions citric acid primarily as a diagnostic and metabolic reference compound rather than a standalone therapeutic agent — direct clinical treatment data are currently absent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved therapeutic indication (used as excipient and diagnostic test meal component) |
| Predicted New Indication | Stomach Disease |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for citric acid as a therapeutic agent. Citric acid is a naturally occurring tricarboxylic acid and a central intermediate in the TCA (Krebs) cycle, participating in cellular energy metabolism in all aerobic organisms. Its biologically active roles in the gastric environment provide a plausible, if preliminary, rationale for the TxGNN prediction.

The mechanistic link to stomach disease operates through at least three distinct pathways. **First**, citric acid is clinically validated as a functional test meal in ¹³C-UBT: its mild acidity delays gastric emptying, concentrates *H. pylori* urease activity in the gastric antrum, and measurably improves the sensitivity and specificity of non-invasive *H. pylori* diagnosis — an application directly supported by a clinical crossover study in Asian populations (PMID 31505905). **Second**, early preclinical data demonstrated that a bismuth-citric acid salt complex (MX1) conferred dose-dependent gastroprotective effects against stress-induced gastric ulcers in rats (PMID 9379358), suggesting citric acid can act synergistically with mucosal-protective agents in the gastric environment. **Third**, metabolomics research identifies citric acid as a biologically significant marker in gastric cancer: elevated serum citric acid levels were detectable in Korean individuals before gastric cancer onset (PMID 35900644), and TCA cycle upregulation has been identified as a defining feature of one gastric cancer molecular subtype (PMID 38959111), placing citric acid at the intersection of gastric tumor metabolic reprogramming.

While the convergence of diagnostic, cytoprotective, and metabolic evidence supports the plausibility of the TxGNN prediction, the pathway from "biologically relevant" to "therapeutically effective" remains uncharted. Citric acid's current clinical role in gastric disease is as a diagnostic adjunct, not a treatment — and no interventional trials have evaluated it as a primary therapeutic agent for any stomach disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03342456](https://clinicaltrials.gov/study/NCT03342456) | Phase 4 | Completed | 184 | Ilaprazole/doxycycline-based bismuth-containing quadruple therapy for H. pylori-infected duodenal ulcers; most directly relevant completed RCT for gastric disease in this dataset, though citric acid is not the primary intervention |
| [NCT03320538](https://clinicaltrials.gov/study/NCT03320538) | NA | Completed | 360 | Multicenter double-blind RCT of Hou Gu Mi Xi herbal compound for peptic ulcer disease; disease directly relevant, and the complex herbal formulation may include organic acid components |
| [NCT04095975](https://clinicaltrials.gov/study/NCT04095975) | Phase 4 | Completed | 31 | Baking soda vs. LithoLyte (citrate-containing formulation) to raise urinary citrate and pH; the only completed RCT directly investigating a citrate-based formulation, providing safety and bioavailability reference data for citric acid salts |
| [NCT03812380](https://clinicaltrials.gov/study/NCT03812380) | Phase 3 | Terminated | 62 | Effervescent calcium magnesium citrate to prevent PPI-related complications (fragility fractures, hypomagnesemia, CKD); citrate formulation directly studied in a gastric acid/PPI clinical context; terminated early, limiting conclusions |
| [NCT04329494](https://clinicaltrials.gov/study/NCT04329494) | Phase 1 | Recruiting | 49 | PIPAC chemotherapy (cisplatin, oxaliplatin, etc.) for peritoneal carcinomatosis including gastric cancer; provides gastric cancer disease context but no direct connection to citric acid |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Clinical Crossover Study | Gut and Liver | Citric acid test meal significantly improves ¹³C-UBT accuracy for H. pylori detection in Asian populations; the most direct clinical evidence of citric acid's functional role in the stomach |
| [9379358](https://pubmed.ncbi.nlm.nih.gov/9379358/) | 1997 | Animal Study | J Pharmacy and Pharmacology | MX1 (roxatidine + bismuth-citric acid complex) produced dose-dependent gastroprotection against restraint stress-induced gastric ulcers in rats; supports citric acid's potential synergistic role in mucosal protection |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | Observational Study | Metabolomics | Elevated serum citric acid negatively correlated with alkaline phosphatase was detectable in Korean patients before gastric cancer onset; supports citric acid as a metabolic biomarker in early gastric carcinogenesis |
| [38959111](https://pubmed.ncbi.nlm.nih.gov/38959111/) | 2024 | Translational Research | Cell Reports | Metabolic signature clustering identified three gastric cancer subtypes; the MSC1 subtype featured TCA cycle upregulation and distinct prognosis, positioning citric acid metabolism as a key driver |
| [37477784](https://pubmed.ncbi.nlm.nih.gov/37477784/) | 2024 | Review | Clin Transl Oncology | Comprehensive review of energy metabolism as a therapeutic target in gastric cancer; TCA cycle intermediates, including citric acid, play central roles in Warburg effect modulation and mitochondrial reprogramming |
| [26088916](https://pubmed.ncbi.nlm.nih.gov/26088916/) | 2015 | Metabolomics Study | Applied Biochem Biotechnology | LC/MS metabolomics of gastric cancer identified altered organic acid profiles including citric acid as candidate biomarkers; supports metabolic pathway relevance |
| [6027230](https://pubmed.ncbi.nlm.nih.gov/6027230/) | 1967 | Clinical Measurement Study | Gastroenterology | Foundational measurement of lactic, pyruvic, citric, and uric acid in human gastric juice; established citric acid as a physiological constituent of the gastric luminal environment |
| [2072799](https://pubmed.ncbi.nlm.nih.gov/2072799/) | 1991 | Narrative Review | Med Clinics of North America | Dietary management in peptic ulcer disease; discusses the role of dietary acids — including citric acid — in modulating gastric acid secretion and mucosal irritation |

---

## Canada Market Information

Citric acid (DrugBank ID: DB04272) currently has **no approved drug products registered in Canada** (0 DINs, not marketed as a standalone therapeutic agent). Citric acid is extensively used as a pharmaceutical excipient across many approved drug products — serving as a pH adjuster, chelating agent, buffering component, and flavor modifier — but holds no independent drug product approval. Any future therapeutic application would require a new drug submission.

---

## Safety Considerations

No drug-specific warnings, contraindications, or drug-drug interaction data were identified for citric acid in this evaluation. Citric acid is designated as Generally Recognized as Safe (GRAS) by the FDA for food use and is a well-characterized pharmaceutical excipient (listed in USP/NF). For any proposed therapeutic formulation or clinical application, refer to relevant excipient safety monographs (e.g., Handbook of Pharmaceutical Excipients) and consult regulatory labeling requirements.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.74%) and plausible mechanistic rationale exists — spanning H. pylori diagnostic utility, preclinical gastroprotective data, and metabolomic relevance in gastric cancer — no clinical trials currently evaluate citric acid as a standalone therapeutic agent for any stomach disease. The current evidence level (L4: metabolomics, animal studies, and mechanism research) is insufficient to advance to a repurposing development track without first defining a precise therapeutic hypothesis and generating targeted proof-of-concept data.

**To proceed, the following is needed:**
- **Define the therapeutic hypothesis**: Is the target H. pylori-associated gastritis (building on the UBT diagnostic mechanism), gastric ulcer/mucosal protection (building on the bismuth-citrate cytoprotective data), or gastric cancer metabolic modulation (building on TCA cycle dysregulation findings)?
- **Complete MOA characterization**: Query DrugBank API (DG002) and retrieve any available regulatory safety data to close the known data gaps
- **Conduct a systematic literature review** specifically focused on citric acid in gastric mucosal biology and H. pylori interaction
- **Design a proof-of-concept study** (in vitro/ex vivo gastric epithelial models) to evaluate direct gastroprotective, antibacterial, or metabolic effects of citric acid at physiologically relevant concentrations
- **Assess formulation feasibility**: Determine optimal dose, pH, delivery vehicle, and administration route for any proposed gastric therapeutic application
- **Screen for drug interaction potential** with PPIs, bismuth preparations, and H. pylori eradication regimens, given citric acid's known chelating properties
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

