---
layout: default
title: Cyproterone Acetate
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Cyproterone Acetate
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

# Cyproterone Acetate: From Hyperandrogenism to Migraine Disorder

## One-Sentence Summary

Cyproterone acetate (CPA) is a synthetic antiandrogen and progestogen, widely recognized for treating conditions associated with androgen excess (such as hirsutism, acne, and polycystic ovary syndrome) and for hormonal management of prostate cancer, though no formal approvals are registered in Canada.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with a prediction score of 99.66%, currently supported by **3 publications** exploring hormonal and neuro-receptor mechanisms — but **no dedicated clinical trials** have been identified for this specific indication.
Given the mechanistic basis is largely speculative and significant safety concerns exist (particularly thromboembolism risk), this prediction warrants careful preclinical validation before any clinical development is pursued.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (CPA not marketed in Canada; known clinical use: hyperandrogenism, hirsutism, PCOS, prostate cancer) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on published pharmacology, cyproterone acetate is a C21-steroid progestogen with potent antiandrogenic activity achieved through competitive androgen receptor blockade. Importantly, a 2003 mechanistic review (PMID 14670648) highlights that CPA also activates GABA-A receptor subtypes, augments dopaminergic responses in striatal tissue, and binds opiate receptors independently of its classical antiandrogenic effect — all neurotransmitter systems with established roles in migraine pathophysiology.

The hormonal basis for migraine is well-established: fluctuations in estrogen and progesterone are recognized triggers for menstrual (catamenial) migraine. CPA's progestogenic activity may theoretically stabilize the hypothalamic-pituitary-gonadal axis, dampening hormone-related neuronal excitability changes that precipitate migraine attacks. In postmenopausal women, a 2002 clinical observation study (PMID 12390622) demonstrated that the type of progestin component in hormone therapy significantly influences migraine course, further supporting the plausibility of a progestin-mediated migraine modulation pathway.

However, these mechanistic and indirect clinical observations fall far short of establishing efficacy. No controlled study has evaluated CPA specifically for migraine prevention or treatment. The prediction likely reflects the TxGNN knowledge graph capturing shared hormonal and GABA-A receptor pathway nodes between CPA and migraine biology rather than a well-validated clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [14670648](https://pubmed.ncbi.nlm.nih.gov/14670648/) | 2003 | Review / Mechanism | *Maturitas* | CPA activates GABA-A receptors, increases dopaminergic responses in striatal tissue, and binds opiate receptors — all pathways involved in migraine threshold modulation |
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Clinical Observation | *Headache* | Different progestin-containing hormone replacement regimens produce meaningfully different effects on migraine frequency in postmenopausal women, supporting a progestin-specific CNS mechanism |
| [10857213](https://pubmed.ncbi.nlm.nih.gov/10857213/) | 2000 | Long-term Safety | *Zentralblatt für Gynäkologie* | Long-term safety registry of CPA-containing gynecological therapies (2,506 patients, 7,971 patient-years); no migraine efficacy data reported |

---

## Canada Market Information

Cyproterone acetate is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) have been issued. There are no approved product entries to display.

---

## Safety Considerations

⚠️ **Critical Safety Signals — Identified from Evidence Pack Literature**

Formal package insert warnings and contraindications are not available in this Evidence Pack (Data Gap). However, the evidence collected across multiple predicted indications reveals substantial safety concerns that directly affect the clinical feasibility of any repurposing effort:

**Thromboembolism Risk (Established)**
Multiple independent studies document that CPA-containing oral contraceptives significantly increase venous thromboembolism (VTE) risk:
- CPA increases thrombin generation and reduces protein C/S activity (PMID 15550051, 18064335, 18067603)
- A French hospital cross-sectional study (PMID 24634164) and large epidemiological studies (PMID 29614525, 32342502) confirm elevated VTE risk, particularly in carriers of Factor V Leiden or prothrombin G20210A mutations
- CPA alone (without ethinyl estradiol) in male-to-female transsexuals also altered haemostatic variables (PMID 14671159)

**Absolute Contraindication — Migraine with Brainstem Aura**
CPA combined with ethinyl estradiol is classified WHO Medical Eligibility Criteria Category 4 (absolute contraindication) in patients with migraine with brainstem aura, due to markedly elevated ischemic stroke risk (supported by PMID 25227335, 30389542). This is particularly relevant because the TxGNN model also predicts "migraine with brainstem aura" (Rank 2) as a potential indication — a prediction that is clinically contraindicated rather than therapeutically exploitable.

**Potential Mutagenic Concern at High Doses**
A long-term safety study (PMID 10857213) notes historically raised concerns about CPA's mutagenic potential at threshold doses, though a large multicentre registry did not confirm increased cancer incidence at continuous low doses.

Please refer to the complete package insert and EMA/Health Canada product monograph for full prescribing information before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.66%) based on plausible shared receptor pathway biology, but supporting evidence is limited to indirect mechanistic reviews (L4 level), with no clinical trials registered for migraine. More critically, CPA carries well-documented thromboembolism risks, and its combination formulation is absolutely contraindicated in migraine with aura — overlapping with the very patient population most likely to be considered for hormonal migraine therapy.

**To proceed, the following is needed:**

- **Mechanism of action characterization**: Retrieve complete DrugBank pharmacology data and package insert to formally establish CPA's CNS receptor interaction profile
- **Patient population delineation**: Define a target subpopulation where hormonal migraine is the dominant mechanism (e.g., menstrual migraine without aura) and where VTE risk is manageable
- **Safety feasibility assessment**: Evaluate whether progestogen-only CPA formulations (without ethinyl estradiol) carry a significantly lower thrombotic risk profile that might open a viable therapeutic window
- **Regulatory landscape review**: Confirm CPA's approval status and contraindication labelling in jurisdictions where it is marketed (EU, UK, Australia) to understand the regulatory precedent
- **Proof-of-concept study design**: If feasibility is confirmed, design a small observational or Phase 2 study in menstrual migraine with pre-specified safety monitoring for VTE events

> **Note on Other Predicted Indications:** The Evidence Pack also flags Rank 8 — **amenorrhea** — as the highest-evidenced indication (L2, 4 clinical trials, recommendation: *Proceed with Guardrails*). This indication reflects CPA's established clinical use in PCOS-related anovulation and menstrual irregularity (e.g., Diane-35), and may represent a more immediately actionable repurposing pathway if Canada market entry is pursued.

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Report generated: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

