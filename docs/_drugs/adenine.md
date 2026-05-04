---
layout: default
title: Adenine
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Adenine
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

# Adenine: From Purine Nucleobase to Drug-Induced Osteoporosis

## One-Sentence Summary

Adenine is a fundamental purine nucleobase and essential building block of DNA, RNA, ATP, and NAD⁺, with no formally registered standalone therapeutic indication.
The TxGNN model predicts it may be relevant for **Drug-Induced Osteoporosis**, with **1 clinical trial** (indirectly related) and **3 publications** currently supporting this direction — making the evidence base preliminary at best.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formally registered therapeutic indication |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data for Adenine is not currently available. As a purine nucleobase, Adenine is a core structural component of DNA, RNA, ATP, coenzyme A, and NAD⁺ — molecules that are central to virtually every cellular process. In pharmaceutical applications, it is best known as a component of blood preservation solutions (e.g., CPDA-1), rather than as a standalone therapeutic agent.

The mechanistic link to drug-induced osteoporosis is indirect and largely inferred from the behaviour of adenine-backbone nucleotide analogues. The retrieved literature focuses on tenofovir — an antiretroviral nucleotide that shares the adenine scaffold — which causes bone density loss by inhibiting mitochondrial DNA polymerase and by downregulating key osteoclast-related genes (Gnas, Got2, Snord32a) in primary cell studies. Free adenine may theoretically modulate bone cell activity through purinergic receptors (P2X/P2Y), which are expressed on both osteoblasts and osteoclasts, but no direct experimental evidence supports a therapeutic role.

The TxGNN model likely captures the structural and metabolic proximity between adenine and bone-affecting nucleotide analogues in the knowledge graph. However, the leap from "adenine-containing drugs can harm bone" to "adenine itself can treat bone disease" requires substantially more mechanistic justification and remains undemonstrated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06065852](https://clinicaltrials.gov/study/NCT06065852) | N/A | Recruiting | 35,000 | National Registry of Rare Kidney Diseases (RaDaR) — long-term observational registry collecting clinical data from patients with rare kidney diseases to develop guidelines and audit outcomes. This is not an Adenine intervention trial; included because bone metabolism abnormalities are frequently observed in rare renal disease populations. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [20026012](https://pubmed.ncbi.nlm.nih.gov/20026012/) | 2010 | In vitro mechanistic | Biochemical and Biophysical Research Communications | Tenofovir (an adenine-backbone nucleotide analogue) downregulates Gnas, Got2, and Snord32a in primary osteoclasts at physiological concentrations, offering a molecular mechanism for antiretroviral-induced bone density loss in HIV management. Most directly relevant paper in this collection. |
| [22943210](https://pubmed.ncbi.nlm.nih.gov/22943210/) | 2012 | Pharmacokinetic Review | Expert Opinion on Drug Metabolism & Toxicology | PK/PD review of emtricitabine/tenofovir (FTC/TDF) fixed-dose combination in HIV treatment; describes intracellular pharmacology of adenine-containing antivirals acting as chain terminators of proviral DNA synthesis. Provides context for how adenine-backbone drugs distribute into bone-relevant cells. |
| [31026554](https://pubmed.ncbi.nlm.nih.gov/31026554/) | 2019 | Animal Study | Journal of Ethnopharmacology | Xian-Ling-Gu-Bao (a traditional herbal formula used for osteoporosis and bone necrosis) was associated with oxidative stress–mediated liver injury in a rat model; contextually related to the broader challenge of drug-induced bone-liver metabolic interactions, but not directly relevant to Adenine. |

---

## Canada Market Information

Adenine (DB00173) is **not currently marketed in Canada** and has no issued Drug Identification Numbers (DINs). No Health Canada–approved products containing Adenine as the sole active ingredient are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence for Adenine in drug-induced osteoporosis sits at L4 — restricted to indirect mechanistic observations derived from structurally related compounds (tenofovir), with no direct preclinical or clinical data for Adenine itself. The drug is not registered in Canada, and both its mechanism of action and safety profile are uncharacterised for this context.

**To proceed, the following is needed:**
- Direct in vitro or in vivo evidence of Adenine's effect on bone remodelling (osteoblast/osteoclast activity via P2X/P2Y purinergic receptor signalling)
- Pharmacokinetic data for systemic Adenine administration in the dose range relevant to any therapeutic effect
- Mechanism of action data from DrugBank or primary sources (addresses Data Gap DG002)
- Safety and toxicology profiling — particularly regarding 2,8-dihydroxyadenine crystal deposition risk (observed in animal models of high-dose adenine exposure)
- Regulatory consultation on whether standalone Adenine as a therapeutic agent requires a new Investigational New Drug (IND) submission in Canada
- Package insert and warning data to enable S1 safety screening (addresses Blocking Data Gap DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

