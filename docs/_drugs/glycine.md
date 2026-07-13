---
layout: default
title: Glycine
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 2
---

# Glycine
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

# Glycine: From Nutritional Amino Acid to Nasal Cavity Disease

## One-Sentence Summary

Glycine (DB00145) is a non-essential amino acid with endogenous roles in protein synthesis and neurotransmission, used primarily as a nutritional supplement with no formal approved therapeutic indications on record.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **1 clinical trial** and **2 publications** currently identified — though neither directly evaluates glycine as a treatment for this condition.
The overall evidence base is weak, and this candidate is currently rated **Hold** pending mechanistic validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved therapeutic indication on record; used as nutritional amino acid supplement |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Glycine is the simplest amino acid and the only non-chiral proteinogenic amino acid. It acts as an inhibitory neurotransmitter in the central nervous system through glycine receptors (GlyR), and has been studied for its anti-inflammatory properties — most notably its ability to suppress macrophage and neutrophil activation, inhibit NF-κB signalling, and reduce pro-inflammatory cytokine release. These immunomodulatory effects form the mechanistic basis for the TxGNN prediction.

The proposed link to nasal cavity disease rests on this anti-inflammatory rationale: glycine, by dampening innate immune cell activity via GlyR-mediated chloride influx, could theoretically reduce mucosal inflammation in the nasal cavity. Nasal cavity diseases (including rhinitis, nasal polyposis, and chronic rhinosinusitis) are characterised by persistent mucosal inflammation driven by the very pathways glycine is thought to modulate.

However, it must be emphasised that this mechanistic chain has not been validated in nasal tissue models or clinical studies. The connection is inferential — extrapolated from general glycine immunopharmacology rather than nasal-cavity-specific experimentation. No direct mechanistic or preclinical data establishing glycine's effect on nasal mucosa has been identified. This prediction should be treated as a hypothesis-generating signal, not a confirmed mechanistic pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | PET/CT imaging study using 18F-FPPRGD2 (an RGD peptide tracer containing glycine as a backbone component) to assess αvβ3 integrin expression as a biomarker of angiogenesis in GBM, gynaecological cancers, and RCC. **Glycine is not the therapeutic agent in this trial; it is a structural component of the radiolabelled peptide. No relevance to nasal cavity disease treatment.** |

> **Note:** No clinical trials evaluating glycine as a therapeutic agent for nasal cavity disease were identified. The single trial retrieved is rated Grade C relevance.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Animal histochemistry study | Veterinary Pathology | Examined glycoconjugate composition of normal and BHV1-infected bovine nasal mucosa using lectin histochemistry. Investigates mucosal glycan changes following herpesvirus infection in cattle. Not a glycine treatment study; glycine is referenced only as part of the amino acid context of mucosal glycoproteins. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | In vitro / drug delivery study | Chemical & Pharmaceutical Bulletin | Evaluated oligoarginine-conjugated polymers as nasal mucosal adjuvants for influenza vaccination in mice. Arginine-based peptides (not glycine) are the active components. Glycine is not the study drug; findings are not directly applicable. |

> **Note:** Neither publication directly evaluates glycine as a treatment for nasal cavity disease. Both are Tier 3 (animal or in vitro studies with indirect relevance).

---

## Canada Market Information

Glycine (DB00145) currently has **no Drug Identification Numbers (DINs)** issued by Health Canada and is not marketed as a pharmaceutical product in Canada.

It may be available as a natural health product or nutritional supplement under separate NHP regulations, which are outside the scope of this evaluation.

---

## Safety Considerations

Detailed prescribing information, Health Canada–approved warnings, and contraindications for glycine as a pharmaceutical product are not available in the current dataset (no Canadian DINs on file, no package insert retrieved).

No drug–drug interactions were identified in the evidence pack query.

> Please refer to any available product monograph or package insert for safety information. For high-dose glycine use (e.g., irrigation solutions in urological procedures), clinically relevant risks include hyponatraemia and neurotoxicity from systemic absorption — these should be considered if any non-oral route is under evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high predictive score (99.85%), but the evidence base for glycine in nasal cavity disease consists only of mechanistic inference — no preclinical in vivo nasal models, no Phase 1 trials, and no published clinical studies directly testing this indication have been identified. The evidence level (L4) reflects this gap.

**To proceed, the following is needed:**

- **Preclinical validation**: In vitro or animal studies demonstrating glycine's effect on nasal mucosal inflammation (e.g., nasal epithelial cell cultures, murine rhinosinusitis models) to establish biological plausibility.
- **MOA data**: Formal mechanism-of-action characterisation from DrugBank or primary literature confirming glycine's anti-inflammatory pathway at therapeutically achievable concentrations.
- **Route-of-administration assessment**: Clarification of whether intranasal delivery of glycine is feasible and at what concentration the anti-inflammatory effect is active locally.
- **Regulatory classification review**: Determine whether glycine would be regulated as a drug or natural health product in Canada for this indication, as this affects the regulatory pathway.
- **Safety profile**: Retrieve the Health Canada product monograph or equivalent regulatory document to complete the S1 safety screening that is currently blocked.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

