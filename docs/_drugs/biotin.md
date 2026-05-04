---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 2
---

# Biotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Biotin: From Nutritional Supplement to Dyspepsia

## One-Sentence Summary

Biotin (Vitamin B7) is an essential water-soluble coenzyme used primarily as a nutritional supplement for biotin deficiency and metabolic support.
The TxGNN model predicts it may have potential utility in **Dyspepsia**, with **2 clinical trials** (both of low direct relevance) and **7 publications** (largely indirect) identified to date.
No biotin pharmaceutical products are currently licensed in Canada, and direct clinical evidence for this indication is absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nutritional supplement — Vitamin B7 / biotin deficiency |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Biotin (Vitamin B7) is an essential cofactor for multiple carboxylase enzymes involved in fatty acid synthesis, gluconeogenesis, and amino acid catabolism. Biotin deficiency is well documented to produce gastrointestinal symptoms—including nausea, vomiting, and abdominal bloating—that overlap substantially with the clinical presentation of dyspepsia. The theoretical basis for the TxGNN prediction is that correcting an underlying biotin deficiency could alleviate metabolism-related gastrointestinal dysfunction.

However, this mechanistic link is highly indirect and requires several unverified assumptions: that the dyspepsia in question is caused or substantially worsened by biotin deficiency, and that replenishing biotin would correct the relevant metabolic disturbance. In practice, functional dyspepsia is a multifactorial condition with diverse etiologies—including Helicobacter pylori infection, gastric motility disorders, visceral hypersensitivity, and gut–brain axis dysregulation—in which biotin deficiency plays no established causal role.

Currently, detailed mechanism of action data is not available from the source dataset. Based on known biochemistry, biotin's role as a carboxylase cofactor provides a plausible but unconfirmed rationale for gastrointestinal symptom modulation. The available literature captures co-occurrence rather than causation: one case report documented biotin deficiency arising in an infant who had been diagnosed with dyspepsia on an amino acid formula, and one supplement trial evaluated a multi-ingredient product containing biotin for functional dyspepsia—but neither isolates biotin's individual contribution. The prediction is biologically speculative and lacks a direct experimental evidence chain.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Observed serum micronutrient concentrations (potentially including biotin) after transdermal patch use in post-bariatric surgery patients; primary endpoint is absorption kinetics, not dyspepsia treatment |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Compared oxycodone vs. pregabalin for postoperative pain control in elective surgery patients; no connection to biotin or dyspepsia |

> **Note:** Neither trial investigates biotin's efficacy in dyspepsia. Both were retrieved as low-relevance search results and should not be interpreted as supporting evidence for this repurposing hypothesis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Clinical Observation | Minerva Gastroenterol Dietol | Multi-ingredient supplement (sodium alginate, calcium carbonate, enzymes, ginger, fennel, **and biotin**) improved quality of life in functional dyspepsia after H. pylori eradication; biotin's individual contribution cannot be isolated from the combination |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case Report | J Dermatology | 5-month-old infant diagnosed with dyspepsia and fed only amino acid formula subsequently developed classic biotin deficiency (alopecia, dermatitis); establishes co-occurrence, not a causal treatment relationship |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Intervention Study | Exp Clin Gastroenterol | Supplement containing inulin, oligofructose, **biotin**, and other vitamins improved gut microbiota in patients with bronchopulmonary disease on antibiotics; GI relevance is indirect |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Cross-Sectional Study | Int J Mol Med | Characterised stomach antral endocrine cell populations in IBS patients vs. healthy controls; no connection to biotin |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Cross-Sectional Study | World J Gastrointest Endosc | Studied endocrine cell types in the oxyntic mucosa of IBS patients; no connection to biotin |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.43%), no clinical trial directly investigates biotin for dyspepsia, and the retrieved literature provides only indirect or incidental associations. The mechanistic hypothesis—that biotin supplementation corrects metabolism-driven gastrointestinal dysfunction—is biologically plausible but entirely unverified, placing this candidate firmly at the preclinical hypothesis stage (L4). With zero licensed products in Canada and no safety profile data available, advancement is not yet warranted.

**To proceed, the following is needed:**
- Retrieve mechanism of action (MOA) data from DrugBank (DB00121) to formally characterise biotin's carboxylase pathways and their relevance to gastric physiology
- Commission a targeted preclinical study or hypothesis-driven systematic review examining the biotin–gut motility axis
- Obtain safety profile data (key warnings, contraindications, DDI profile) from the package insert or Health Canada databases
- Conduct a dedicated clinical literature search using MeSH terms combining "biotin" with "functional dyspepsia," "gastrointestinal motility," and "gastric emptying" to rule out missed evidence
- If a plausible patient subgroup can be defined (e.g., dyspepsia with confirmed biotin deficiency or post-bariatric surgery malabsorption), consider a proof-of-concept pilot study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

