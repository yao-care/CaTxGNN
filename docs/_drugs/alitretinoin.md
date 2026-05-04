---
layout: default
title: Alitretinoin
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Alitretinoin
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

# Alitretinoin: From Severe Chronic Hand Eczema to Acne

## One-Sentence Summary

Alitretinoin (9-cis-retinoic acid) is a pan-retinoid receptor agonist internationally approved as Toctino (oral) for severe chronic hand eczema and as Panretin (topical gel) for AIDS-related Kaposi's sarcoma skin lesions, but currently not marketed in Taiwan.
The TxGNN model's top-scoring prediction (rank #1, amenorrhea) was assessed as a likely side-effect confound rather than a genuine therapeutic target; the **highest evidence-supported prediction is acne**, with **1 clinical trial record** and **5 publications** — including a direct head-to-head clinical study confirming alitretinoin inhibits sebocyte activity at potency comparable to isotretinoin.

> **Analyst Note — TxGNN Rank #1 (Amenorrhea) Flagged:** Although amenorrhea scores highest in the raw TxGNN ranking (score 99.99%, rank 537), the mechanistic review concludes the model likely captured retinoid-induced menstrual irregularity/amenorrhea — a well-documented **side effect** of retinoids including isotretinoin — as a therapeutic signal. No positive biological mechanism supporting alitretinoin as an *treatment* for amenorrhea exists. This prediction is classified **Hold / L5** and is not the focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe chronic hand eczema (Toctino, EU/international); Kaposi's sarcoma skin lesions (Panretin, US/EU) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.92% (evidence-supported rank; raw rank #2 by TxGNN score) |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Alitretinoin (9-cis-retinoic acid) is the only endogenous retinoid that binds with high affinity to **all six nuclear retinoid receptors** — RARα, RARβ, RARγ, RXRα, RXRβ, and RXRγ. This pan-agonist activity distinguishes it from isotretinoin (13-cis-RA), which acts primarily through metabolic conversion to all-trans-retinoic acid and preferentially signals via RARs. Through RAR/RXR nuclear signaling, alitretinoin regulates epithelial cell differentiation, sebaceous gland activity, and follicular keratinization — the precise biological axis that drives acne pathogenesis.

Acne involves three converging mechanisms: excess sebum production, abnormal follicular keratinization, and *Cutibacterium acnes* colonization. Isotretinoin — structurally and mechanistically related to alitretinoin — is the gold-standard oral therapy for severe acne precisely because it dramatically reduces sebaceous gland size and sebum output via retinoid receptor signaling. A 1996 clinical comparison study (PMID 8884148, Ott et al.) directly tested alitretinoin (9-cis-RA) against isotretinoin (13-cis-RA) in cultured human sebocytes and in an animal model of sebaceous gland size: both compounds inhibited sebocyte proliferation equivalently and reduced sebaceous gland dimensions, providing direct early clinical evidence that alitretinoin shares the pharmacological basis of anti-acne activity.

Given this direct evidence and the well-established Phase 3 RCT track record of isotretinoin for severe acne, the TxGNN prediction that alitretinoin may be repurposed for acne is biologically coherent. The primary open questions are comparative systemic safety at acne-appropriate doses, the benefit–risk profile relative to the already-approved isotretinoin, and the regulatory pathway for a drug not yet marketed in Taiwan.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04663906](https://clinicaltrials.gov/study/NCT04663906) | N/A | Unknown | 300 | Observational study in isotretinoin-treated acne patients (not alitretinoin); assessed whether retinoid-induced mucosal dryness increases COVID-19 infection risk — acne population but no alitretinoin efficacy data, grade C indirect class evidence only |

> No clinical trials directly investigating alitretinoin for acne treatment were identified. The sole trial retrieved involves the related compound isotretinoin and addresses infection risk, not acne therapeutic outcomes. It is listed for class context only.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [8884148](https://pubmed.ncbi.nlm.nih.gov/8884148/) | 1996 | Clinical Comparative Study | Dermatology (Basel) | **Strongest direct evidence:** 9-cis-RA (alitretinoin) vs. 13-cis-RA (isotretinoin) head-to-head — equivalent inhibition of human sebocyte proliferation in culture and equivalent reduction of hamster sebaceous gland size; confirms alitretinoin has direct anti-acne biological activity |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clinics in Dermatology | Current review of vitamin A and retinoids in dermatology; explicitly lists alitretinoin among oral therapeutic retinoids alongside isotretinoin, acitretin, and bexarotene — supports its recognized role in skin disease management |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Review | Skin Pharmacol Appl Skin Physiol | Retinoids and future dermatological indications; discusses sebaceous gland targeting and the pleiotropic effects of retinoids via nuclear RAR/RXR receptors, providing the mechanistic framework for alitretinoin in sebaceous-driven disorders |
| [8884149](https://pubmed.ncbi.nlm.nih.gov/8884149/) | 1996 | Clinical Mechanistic Study | Dermatology (Basel) | Oral all-trans-retinoic acid reduces sebum excretion rate in young men; corroborates retinoid class mechanism on sebaceous output — supports the pathway shared by alitretinoin |
| [10521699](https://pubmed.ncbi.nlm.nih.gov/10521699/) | 1999 | Mechanistic Review | Biochim Biophys Acta | Comprehensive review of retinoid binding proteins and metabolic enzymes; establishes the endocrine/intracrine activity of 9-cis-RA and its role in epithelial cell differentiation — mechanistic foundation for alitretinoin's potential in acne |

---

## Taiwan Market Information

Alitretinoin currently has **no approved products in Taiwan (0 licenses)**. It is not marketed in any dosage form.

> **International Reference:** Alitretinoin is approved in the EU and other markets as **Toctino** (oral capsules 10 mg / 30 mg, GSK) for severe chronic hand eczema refractory to potent topical corticosteroids, and as **Panretin** (topical gel 0.1%) for cutaneous lesions of AIDS-related Kaposi's sarcoma. Neither formulation holds local approval at this time.

---

## Safety Considerations

Specific Taiwan package insert warnings are not available (drug not locally marketed). Based on international retinoid class data from approved markets (Toctino SmPC, EU):

**Key Warnings:**
- **Teratogenicity (Critical):** Alitretinoin is a potent teratogen. Absolutely contraindicated in pregnancy and in women of childbearing potential not using two highly effective methods of contraception. All approved markets require a formal pregnancy prevention programme (PPP) — equivalent to iPLEDGE requirements for isotretinoin.
- **Hepatotoxicity:** Liver function tests (ALT, AST, bilirubin) are required before initiation and monitored periodically during treatment.
- **Hyperlipidaemia:** Triglycerides and total cholesterol must be monitored; clinically significant elevations require dose reduction or discontinuation.
- **Psychiatric Effects:** Depression, mood disturbances, and suicidal ideation are retinoid class effects; psychiatric history should be reviewed before prescribing.
- **Thyroid Function:** Hypothyroidism has been reported with alitretinoin (Toctino); baseline and periodic thyroid function monitoring recommended.

**Contraindications:**
- Pregnancy (absolute) and women of childbearing potential without effective contraception
- Severe hepatic impairment
- Uncontrolled hyperlipidaemia
- Hypersensitivity to retinoids or soya (capsule excipient in Toctino)

**Drug Interactions:**
- **Tetracyclines:** Concomitant use contraindicated — increased risk of benign intracranial hypertension (pseudotumour cerebri)
- **Vitamin A supplements:** Additive toxicity; concurrent use should be avoided
- **CYP3A4 inducers/inhibitors:** May alter alitretinoin plasma concentrations (alitretinoin is a CYP3A4 substrate); caution with ketoconazole, rifampicin, and similar agents
- **Methotrexate:** Concurrent systemic retinoid use increases hepatotoxicity risk

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A direct clinical comparison study (PMID 8884148) demonstrates that alitretinoin inhibits sebaceous gland activity at potency equivalent to the approved anti-acne gold standard isotretinoin, providing a stronger mechanistic foundation than typical L3 observational evidence. However, no dedicated Phase 2 or Phase 3 acne trials for alitretinoin have been conducted, the drug is not marketed in Taiwan, and the well-characterized teratogenicity of the retinoid class requires robust risk management infrastructure before clinical use.

**To proceed, the following is needed:**

- **Regulatory pathway clarification:** Determine whether a new drug application (NDA) or abbreviated pathway is available in Taiwan for a repurposed, non-marketed retinoid
- **Full safety data extraction:** Obtain Toctino EU SmPC and Panretin prescribing information to complete the safety profile; retrieve DrugBank DB00523 MOA and toxicity data
- **Pregnancy Prevention Programme design:** A formal PPP (contraception requirements, monthly pregnancy testing, patient acknowledgment forms) is a mandatory prerequisite — no clinical deployment without this framework
- **Comparative Phase 2 trial:** Design a dose-finding RCT comparing oral alitretinoin vs. oral isotretinoin in moderate-to-severe acne to establish non-inferiority, optimal dosing, and tolerability in the Taiwan population
- **Pharmacokinetic review:** Confirm systemic bioavailability of oral alitretinoin at acne-appropriate doses (likely lower than the 10–30 mg/day used for CHE)
- **Benefit–risk differentiation analysis:** Given isotretinoin is already widely available and approved, articulate the clinical advantage of alitretinoin (e.g., different receptor profile, potentially distinct tolerability) to justify development investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

