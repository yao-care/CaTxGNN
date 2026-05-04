---
layout: default
title: Desvenlafaxine
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Desvenlafaxine
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

# Desvenlafaxine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Desvenlafaxine (brand name: Pristiq) is a serotonin-norepinephrine reuptake inhibitor (SNRI) and the major active metabolite of venlafaxine, established in multiple Phase 3/4 RCTs as an effective treatment for major depressive disorder (MDD).
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, supported by **2 registered clinical trials** and **4 publications** — though neither source directly evaluates desvenlafaxine as a primary OCD treatment.
The most relevant mechanistic bridge derives from venlafaxine's demonstrated OCD efficacy in a Phase 3 double-blind RCT, but direct desvenlafaxine-specific OCD evidence remains absent, placing this prediction at Evidence Level **L4**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (MDD) |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (0 DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on published pharmacological literature, desvenlafaxine is the primary active metabolite of venlafaxine and acts as an SNRI — simultaneously inhibiting reuptake of both serotonin (5-HT) and norepinephrine (NE) at presynaptic terminals. This dual reuptake inhibition distinguishes SNRIs from SSRIs and is the basis for their broader neurobiological reach. Desvenlafaxine's efficacy in MDD has been confirmed in multiple Phase 3/4 RCTs and pooled analyses, with an established 50 mg/day maintenance dose.

OCD pathophysiology is characterized by dysfunction within the cortico-striato-thalamo-cortical (CSTC) loop, particularly involving hyperactivity of the orbitofrontal cortex (OFC) and caudate nucleus. This circuit is critically modulated by the serotonin system (5-HT2A, 5-HT1D receptors), and pharmacological augmentation of serotonergic tone via SRI agents (SSRIs and SNRIs) remains the pharmacological cornerstone of OCD treatment. SNRIs carry theoretical advantages over pure SSRIs in OCD due to concurrent noradrenergic effects on prefrontal executive function.

Venlafaxine — the parent compound of desvenlafaxine — was directly tested against paroxetine (an SSRI) in a Phase 3 double-blind RCT in OCD (n=150; PMID 14624187), demonstrating equivalent efficacy. Since desvenlafaxine *is* the principal pharmacologically active species of venlafaxine in vivo, the prediction that desvenlafaxine may replicate this benefit is mechanistically coherent. However, desvenlafaxine has a slightly different NE:5-HT inhibition ratio relative to venlafaxine, and the two are not considered fully interchangeable without direct confirmatory trials.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Troriluzole (glutamate modulator) as adjunctive therapy vs. placebo in OCD patients with inadequate response to SRI treatment (explicitly including venlafaxine or desvenlafaxine as permitted background therapy). Desvenlafaxine is a permissible standard-of-care medication, not the investigational drug. Provides large-scale OCD trial context and confirms SNRI agents are used as active background treatment in OCD populations. |
| [NCT01527786](https://clinicaltrials.gov/study/NCT01527786) | Phase 3 | Completed | 25 | Desvenlafaxine for functional outcome in postpartum depression. Drug specificity is high (desvenlafaxine), but the indication is postpartum depression — not OCD. Offers limited safety background for desvenlafaxine use in psychiatric populations; no direct relevance to OCD efficacy. |

> **Important caveat:** Neither trial evaluates desvenlafaxine as a primary investigational treatment for OCD. The overall direct clinical trial evidence for this indication is currently absent.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT (Double-Blind) | J Clin Psychopharmacology | First randomized double-blind head-to-head comparison of venlafaxine (SNRI) vs. paroxetine (SSRI) in primary OCD (n=150). Venlafaxine achieved equivalent symptom reduction on Y-BOCS, establishing SNRI efficacy in OCD. As the active metabolite of venlafaxine, this is the strongest indirect mechanistic support for desvenlafaxine in OCD. |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | Updated review of double-blind trials for serotonergic antidepressants in OCD. Confirms the central role of the 5-HT system in OCD pathophysiology and summarizes evidence for SNRI use alongside SSRIs. |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Narrative Review | Cureus | Comprehensive review of postpartum depression; notes that untreated PPD can later manifest as OCD or anxiety disorders. Peripheral relevance — identifies OCD as a longitudinal complication of mood disorders, not a desvenlafaxine-specific finding. |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Case Series | Psychiatry Clin Psychopharmacol | Risperidone augmentation in antidepressant-resistant somatic symptom disorder, with OCD referenced as a comparator condition. Provides context for treatment-resistant psychiatric augmentation strategies; minimal direct relevance to desvenlafaxine/OCD. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for desvenlafaxine in OCD is biologically plausible — grounded in the established role of SNRI agents in the serotonergic treatment of OCD and directly supported by venlafaxine's Phase 3 double-blind RCT data — but no clinical trial has directly evaluated desvenlafaxine as a treatment for OCD. The evidence level is L4 (mechanism-based inference), which does not meet the threshold for a development decision without additional targeted research.

**To proceed, the following is needed:**

- **Proof-of-concept clinical trial:** A dedicated Phase 2 randomized controlled trial comparing desvenlafaxine vs. placebo (or an active SSRI comparator) in patients meeting DSM-5 criteria for OCD
- **Mechanistic differentiation from venlafaxine:** Formal characterization of desvenlafaxine's NE:5-HT inhibition ratio relative to venlafaxine, to determine whether separate OCD efficacy data are required or whether a bridging study can leverage existing venlafaxine evidence
- **Regulatory pathway review:** Assessment of Health Canada's requirements for a new OCD indication, including whether existing MDD approval data can support a supplementary NDS (sNDS) filing
- **Safety characterization in OCD populations:** Current safety data in this Evidence Pack is incomplete (all items flagged as Data Gap); TFDA/Health Canada package insert review is required before any clinical development planning
- **Canadian market registration:** No DINs are currently on record for desvenlafaxine in Canada; a market authorization would be a prerequisite for any Health Canada–approved OCD indication

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

