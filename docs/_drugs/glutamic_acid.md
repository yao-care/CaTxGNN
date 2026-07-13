---
layout: default
title: Glutamic Acid
parent: 僅模型預測 (L5)
nav_order: 368
evidence_level: L5
indication_count: 4
---

# Glutamic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Glutamic Acid: From Amino Acid Supplement to Postmenopausal Osteoporosis

## One-Sentence Summary

Glutamic acid is a non-essential amino acid naturally abundant in protein-rich foods, used clinically as a nutritional supplement and food additive (monosodium glutamate), with no currently registered pharmaceutical indications in Canada.
The TxGNN model predicts it may have therapeutic potential in **Postmenopausal Osteoporosis**, supported by a plausible mechanistic hypothesis centred on osteocalcin carboxylation and glutamate receptor signalling in bone.
Supporting evidence comprises **1 contextual clinical trial** (evaluating a bisphosphonate, not glutamic acid directly) and **11 publications**, of which only one animal study and one human intervention study address glutamic acid itself — direct randomized controlled trial evidence is absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nutritional amino acid supplement (no registered pharmaceutical indications in Canada) |
| Predicted New Indication | Postmenopausal Osteoporosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Glutamic acid sits at the biochemical foundation of bone quality through two distinct pathways. First, osteocalcin — the most abundant non-collagen protein in bone matrix — contains multiple glutamic acid residues that undergo vitamin K-dependent γ-carboxylation to form γ-carboxyglutamic acid (Gla). Only after this carboxylation can osteocalcin bind hydroxyapatite mineral and regulate bone remodelling. This places glutamic acid as a structural prerequisite for functional osteocalcin, independent of calcium and vitamin D pathways. Multiple RCTs on vitamin K2 (menatetrenone) confirm this mechanism in vivo: increasing osteocalcin γ-carboxylation sustains lumbar bone mineral density and reduces vertebral fracture rates in postmenopausal women (PMIDs 14529146, 14584089, 19172219).

Second, osteoblasts and osteoclasts both express NMDA-type and AMPA-type glutamate receptors. Activation of these receptors modulates intracellular Ca²⁺ signalling and downstream gene expression governing bone formation and resorption. In estrogen-deficient states — the hallmark of postmenopausal osteoporosis — glutamatergic signalling in bone may become dysregulated. A 2015 mouse study (PMID 26144993) directly demonstrated that glutamic acid supplementation attenuates bone metabolism abnormalities in ovariectomized (OVX) mice, a standard animal model for postmenopausal osteoporosis. Separately, a human intervention study (PMID 18187428) showed that poly-γ-glutamic acid acutely enhances intestinal calcium absorption in postmenopausal women, suggesting a gut-mediated pathway complementary to direct bone effects.

It is important to note that the current evidence base reflects glutamic acid's *mechanistic role* in bone biochemistry rather than outcomes from controlled supplementation trials. Most clinical literature in this field examines vitamin K2 or bisphosphonates, with glutamic acid appearing as a biochemical component rather than an active intervention under study. The pathway is biologically sound, but a direct randomized controlled trial of oral glutamic acid supplementation for postmenopausal osteoporosis has not yet been conducted.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00048061](https://clinicaltrials.gov/study/NCT00048061) | Phase 3 | Completed | 1,609 | Compared monthly oral ibandronate (100 mg / 150 mg) versus daily 2.5 mg in postmenopausal osteoporosis over 2+ years, with all participants receiving supplemental vitamin D and calcium. ⚠️ **Background evidence only**: the intervention is ibandronate (a bisphosphonate), not glutamic acid. Included for context on the therapeutic landscape. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26144993](https://pubmed.ncbi.nlm.nih.gov/26144993/) | 2015 | Animal Study (in vivo) | Nutrition Research | **Most directly relevant**: Oral glutamic acid attenuated estrogen deficiency-induced menopausal symptoms and bone metabolic abnormalities in OVX mice, including improvements in bone-related markers — the only study testing glutamic acid as a direct intervention in a postmenopausal model. |
| [18187428](https://pubmed.ncbi.nlm.nih.gov/18187428/) | 2007 | Human Intervention | J Am Coll Nutrition | **Only human study**: Poly-γ-glutamic acid acutely increased intestinal calcium absorption in postmenopausal women, suggesting glutamate polymers can improve bone mineral substrate availability via a gut-mediated mechanism. |
| [14529146](https://pubmed.ncbi.nlm.nih.gov/14529146/) | 2003 | RCT | Keio J Medicine | Vitamin K2 (menatetrenone) enhances γ-carboxylation of bone glutamic acid residues in osteocalcin, sustaining lumbar BMD and preventing osteoporotic vertebral fractures in postmenopausal women — directly validates the glutamic acid carboxylation pathway in human bone. |
| [14584089](https://pubmed.ncbi.nlm.nih.gov/14584089/) | 2003 | RCT | Yonsei Med J | Vitamin K2 combined with bisphosphonate in osteoporosis; confirms that glutamic acid residue γ-carboxylation by vitamin K2 drives osteocalcin secretion and bone protection. |
| [19172219](https://pubmed.ncbi.nlm.nih.gov/19172219/) | 2009 | RCT | J Bone Miner Metab | 6-month randomised menatetrenone study in 109 postmenopausal osteoporosis patients: increased γ-carboxylation of osteocalcin glutamic acid residues and reduced undercarboxylated osteocalcin levels, confirming the in vivo relevance of this pathway. |
| [29437025](https://pubmed.ncbi.nlm.nih.gov/29437025/) | 2018 | Genetic Association | Endocrine Metab Immune Disord Drug Targets | VKORC1 −1639G>A polymorphism influences vitamin K-mediated γ-carboxylation of glutamic acid residues; associated with osteoporosis risk in postmenopausal women — genetic evidence linking the glutamic acid modification pathway to disease susceptibility. |
| [40950804](https://pubmed.ncbi.nlm.nih.gov/40950804/) | 2025 | Metabolomics Cohort | J Diabetes Metab Disord | Serum amino acid profiles (including glutamic acid) differ significantly by sex hormone levels and aging in elderly individuals — observational evidence that glutamic acid metabolic status shifts in concert with the postmenopausal hormonal environment. |
| [34529430](https://pubmed.ncbi.nlm.nih.gov/34529430/) | 2021 | Preclinical / Drug Delivery | Nano Letters | Bone-targeting polymer vesicle using a poly(l-glutamic acid) block as the bone-homing moiety for targeted estradiol delivery in osteoporotic bone — exploits glutamic acid's inherent affinity for bone mineral as a drug delivery anchor. |
| [39698319](https://pubmed.ncbi.nlm.nih.gov/39698319/) | 2024 | Animal Study | Front Cell Infect Microbiol | TCM ointment modulated postmenopausal osteoporosis in rats via a gut microbiome–intestinal mucosal barrier–bone metabolism axis; provides mechanistic context for gut–bone crosstalk pathways that glutamic acid may also influence. |
| [18414001](https://pubmed.ncbi.nlm.nih.gov/18414001/) | 2008 | Genetic Association | Molecules and Cells | SNPs in hOAT4, which mediates estrone sulfate transport, associated with postmenopausal osteoporosis in Korean women — indirect context for estrogen pathway involvement in bone loss relevant to the disease model. |

---

## Safety Considerations

Please refer to the package insert for safety information. As glutamic acid is currently not registered as a pharmaceutical product in Canada (0 DINs), no formal drug-level regulatory safety dossier is available from Health Canada sources. Glutamic acid is a naturally occurring amino acid with generally recognised as safe (GRAS) status at food-level intakes; however, therapeutic dose safety data specific to postmenopausal populations, including neurological considerations (glutamic acid functions as an excitatory neurotransmitter and high systemic levels may carry CNS risks), has not been formally established for this proposed indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis is scientifically plausible — glutamic acid's role in osteocalcin Gla-residue formation and glutamate receptor signalling in bone cells is well-documented — but no randomised controlled trial has evaluated exogenous glutamic acid supplementation as a standalone treatment for postmenopausal osteoporosis; the sole animal study (PMID 26144993) and poly-γ-glutamic acid human study (PMID 18187428) provide directional but not confirmatory evidence.

**To proceed, the following is needed:**
- A proof-of-concept Phase 1/2 human study assessing oral glutamic acid supplementation's effect on osteocalcin γ-carboxylation levels and bone turnover markers (e.g., CTX, P1NP) in postmenopausal women
- Dose-finding and formulation work: clarifying whether free glutamic acid, glutamate salts, or poly-γ-glutamic acid is the appropriate therapeutic form
- Pharmacokinetic data confirming that exogenous glutamic acid reaches bone tissue at concentrations sufficient to influence osteocalcin carboxylation
- Neurological safety assessment for sustained high-dose oral glutamic acid supplementation in elderly women (excitatory neurotoxicity risk at supra-physiological systemic exposure)
- Competitive positioning analysis against established first-line therapies (bisphosphonates, vitamin K2, denosumab) to identify where glutamic acid could meaningfully add clinical value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

