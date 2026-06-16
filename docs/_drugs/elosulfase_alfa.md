---
layout: default
title: Elosulfase Alfa
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 9
---

# Elosulfase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Elosulfase Alfa: From Mucopolysaccharidosis IVA (Morquio A) to Scheie Syndrome

## One-Sentence Summary

Elosulfase alfa (Vimizim) is a recombinant human N-acetylgalactosamine-6-sulfatase (GALNS) enzyme replacement therapy, developed and approved for Mucopolysaccharidosis Type IVA (MPS IVA, Morquio A syndrome) in multiple jurisdictions outside Canada.
The TxGNN model predicts potential efficacy in **Scheie syndrome** (MPS IS), supported by **0 clinical trials** and **2 publications** — neither of which examines elosulfase alfa in this context.
This prediction is assessed as a knowledge graph false positive: Scheie syndrome requires a biochemically distinct enzyme (alpha-L-iduronidase), making mechanistic transfer implausible.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucopolysaccharidosis Type IVA (Morquio A syndrome) — GALNS enzyme deficiency |
| Predicted New Indication | Scheie syndrome (MPS IS) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, elosulfase alfa is an enzyme replacement therapy that provides functional GALNS (N-acetylgalactosamine-6-sulfatase) to patients with MPS IVA. GALNS deficiency causes lysosomal accumulation of keratan sulfate and chondroitin-6-sulfate, which progressively damages cartilage, ligaments, bone, and respiratory tissue — the hallmarks of Morquio A syndrome.

Scheie syndrome (MPS IS) is caused by deficiency of an entirely different enzyme: alpha-L-iduronidase (IDUA), which degrades dermatan sulfate and heparan sulfate. The correct enzyme replacement for MPS I (including Scheie, Hurler-Scheie, and Hurler phenotypes) is laronidase (Aldurazyme), not elosulfase alfa. There is no biochemical or mechanistic overlap between GALNS deficiency (MPS IVA) and IDUA deficiency (MPS IS) — the accumulated substrates, affected pathways, and target enzymes are all distinct.

The TxGNN model's high prediction score (99.90%) almost certainly reflects a knowledge graph artifact: MPS disease subtypes share disease-class nodes and phenotypic descriptors in the graph, placing them in close structural proximity regardless of the underlying enzyme specificity. This is a recognised limitation of graph-based repurposing models — phenotypic clustering among rare diseases does not imply therapeutic transferability when the therapeutic target enzymes are biochemically unrelated. **This prediction is assessed as a false positive and does not support a viable repurposing hypothesis.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered for elosulfase alfa in Scheie syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35005816](https://pubmed.ncbi.nlm.nih.gov/35005816/) | 2022 | Registry/Cohort | Human Mutation | Molecular characterisation of 302 Iranian MPS patients across subtypes (including MPS I and IVA); epidemiological and genetic data only — no elosulfase alfa therapeutic data |
| [18584975](https://pubmed.ncbi.nlm.nih.gov/18584975/) | 2009 | Cohort | Pathologie-biologie | Clinical features of MPS I and MPS IVA in Tunisian patients; describes enzyme deficiency profiles but no treatment outcomes relevant to Scheie syndrome |

> ⚠️ Neither publication examines elosulfase alfa in the context of Scheie syndrome. Both are epidemiological or diagnostic studies of the broader MPS disease spectrum. These do not constitute evidence for the repurposing hypothesis.

---

## Canada Market Information

Elosulfase alfa currently has no Drug Identification Numbers (DINs) on file based on available regulatory data.

> **Note for clinical context:** Vimizim (elosulfase alfa) received regulatory approval in the United States (FDA, February 2014) and the European Union (EMA, April 2014) for the treatment of MPS IVA (Morquio A syndrome). Its absence from the Canadian DIN registry may reflect a data gap rather than a definitive non-approval. Clinicians should verify the current status via Health Canada's Drug Product Database before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Elosulfase alfa targets GALNS deficiency (MPS IVA), while Scheie syndrome is caused by deficiency of a completely different enzyme (alpha-L-iduronidase). No mechanistic basis exists for this repurposing, and neither clinical trial nor disease-specific literature supports it. The TxGNN high score is attributable to graph-proximity artifact among MPS disease nodes.

**To proceed with any MPS-related repurposing assessment, the following is needed:**

- **Redirect to Rank 2 candidate:** The most mechanistically valid and evidence-supported candidate in this Evidence Pack is **Lysosomal Storage Disease with Skeletal Involvement** (Rank 2, TxGNN score 99.59%, Evidence Level L2, Recommendation: *Proceed with Guardrails*), which represents MPS IVA-spectrum patients where elosulfase alfa's GALNS activity is directly relevant
- **Verify Canadian authorization status:** Confirm whether Vimizim (elosulfase alfa) has obtained a Health Canada Notice of Compliance; the current DIN count of 0 requires manual verification against the Drug Product Database
- **Obtain safety data:** Retrieve the Health Canada-approved product monograph or FDA/EMA labelling for complete key warnings, contraindications, and infusion-related reaction management protocols
- **Mechanistic documentation:** Obtain formal MOA data from DrugBank (DB09051) to complete mechanistic link analysis for any future indication under review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

