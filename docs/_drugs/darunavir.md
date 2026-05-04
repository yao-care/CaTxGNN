---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 4
---

# Darunavir
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

# Darunavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Darunavir is a second-generation HIV-1 protease inhibitor used as part of combination antiretroviral therapy (cART) for the treatment of HIV/AIDS in adults and paediatric patients.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV infection)**,
with **1 indirectly related clinical trial** and **no direct feline publications** currently supporting this direction.
This prediction is primarily driven by structural homology between the HIV-1 and Feline Immunodeficiency Virus (FIV) proteases, rather than direct veterinary clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV Infection) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (no DINs on file) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established clinical knowledge, Darunavir is a second-generation HIV-1 aspartyl protease inhibitor. It binds to the active site of the HIV-1 protease, blocking cleavage of viral polyprotein precursors (Gag and Gag-Pol) and preventing the maturation of new infectious viral particles. It is always co-administered with a pharmacokinetic booster (ritonavir or cobicistat) to maintain therapeutic plasma levels.

The Feline Immunodeficiency Virus (FIV) and HIV-1 both belong to the genus *Lentivirus* within the family *Retroviridae*. Their aspartyl proteases share structural homology, particularly around the catalytic Asp-Thr-Gly triad. *In vitro* experiments have demonstrated that several HIV-1 protease inhibitors retain measurable inhibitory activity against FIV protease, providing a legitimate mechanistic rationale for cross-species application.

However, a critical caveat applies: TxGNN's high prediction score for this indication is primarily the result of **disease ontology similarity mapping** (HIV/AIDS ↔ FIV) rather than direct experimental evidence in feline subjects. The single identified clinical trial (NCT02770508) is a human HIV-1 study with only indirect relevance. Real-world pharmacokinetic data in cats — including bioavailability, metabolism by feline cytochrome P450, and tolerability — is absent from this evidence pack. This prediction therefore represents a biologically plausible hypothesis requiring dedicated veterinary investigation before any application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Compared Darunavir/ritonavir + lamivudine (dual therapy) versus standard Darunavir/ritonavir + tenofovir/emtricitabine or tenofovir/lamivudine triple ART in ART-naïve HIV-1 patients. **This is a human HIV-1 trial. Its relevance to feline FIV is indirect only (Grade C — cross-species ontological mapping); it does not constitute direct evidence for FIV treatment.** |

---

## Literature Evidence

Currently no direct literature on Darunavir for feline acquired immunodeficiency syndrome is available.

> **Context note:** Although no feline-specific publications were identified, 4 animal studies were retrieved under the closely related Rank 2 prediction (Simian Immunodeficiency Virus infection; see Additional Predictions below). These NHP/SIV studies demonstrate that Darunavir-containing cART regimens effectively suppress lentiviral replication in non-human primates, lending indirect biological plausibility to broader lentiviral applications.

---

## Canada Market Information

No Health Canada Drug Identification Numbers (DINs) are currently on file for Darunavir in the regulatory dataset used for this analysis.

> **Important caveat:** Darunavir (brand name Prezista®, Janssen) is a globally approved antiretroviral agent with regulatory approvals in the US (FDA), EU (EMA), and numerous other jurisdictions. If the 0-DIN result reflects a **data gap in the queried database** rather than actual Health Canada non-approval, manual verification via the [Health Canada Drug Product Database](https://health-products.canada.ca/dpd-bdpp/) is strongly recommended before drawing conclusions about Canadian market status.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap DG001 (Blocking):** Package insert warnings and contraindications have not been retrieved for this evaluation. This is classified as a blocking gap — formal safety review cannot be completed until the full monograph is obtained. Known drug class effects for HIV protease inhibitors include hepatotoxicity risk (particularly in patients with underlying hepatitis B/C), skin rash (including Stevens-Johnson syndrome), lipid metabolic effects, and complex drug-drug interactions via CYP3A4 inhibition.

---

## Additional Predicted Indications (Summary)

The following lower-ranked predictions are noted for completeness:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Notes |
|------|---------|------------|---------------|----------------|-------|
| 2 | Simian Immunodeficiency Virus Infection | 99.97% | L3 | Research Question | 4 NHP/SIV animal studies (2011–2016) support Darunavir-containing cART for viral suppression in macaque models — the strongest mechanistic evidence in this pack |
| 3 | Neurodevelopmental Disorder with Ataxic Gait, Absent Speech, and Decreased Cortical White Matter | 99.97% | L5 | Hold | No mechanistic link; model-only prediction |
| 4 | Obsolete Familial Combined Hyperlipidemia | 99.19% | L5 | Hold | **Contraindicated direction** — HIV protease inhibitors are known to *cause* dyslipidaemia; this prediction should be discarded |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction for Darunavir points to a **veterinary indication** (feline FIV infection) rather than a new human therapeutic application. While structural homology between HIV-1 and FIV proteases provides biological plausibility, there are no direct feline clinical trials, no feline-specific publications, and the single identified clinical trial is a human HIV-1 study with only indirect relevance (Grade C). Separately, Rank 4 (familial combined hyperlipidemia) represents a potentially *harmful* direction given HIV protease inhibitors' known dyslipidaemic effects, and should be explicitly deprioritised.

**To proceed, the following is needed:**

- **Clarify the repurposing scope:** Determine whether the target is veterinary (cats with FIV) or human repurposing. If human, the Rank 2 prediction (SIV infection as a research model bridge) offers more tractable evidence to build on.
- **Resolve Data Gap DG001 (Blocking):** Retrieve Health Canada / TFDA package insert warnings, contraindications, and drug interaction profile before any safety evaluation can proceed.
- **Resolve Data Gap DG002 (High):** Obtain full MOA data from DrugBank API (DB01264) to support mechanistic rationale scoring.
- **Conduct dedicated veterinary literature search:** Search PubMed and CAB Abstracts for *in vitro* FIV protease inhibition studies and *in vivo* feline pharmacokinetic studies using HIV protease inhibitors.
- **Verify Canada regulatory status:** Manually confirm Darunavir's current DIN status via the Health Canada Drug Product Database; the 0-DIN result is likely a database query gap rather than true non-approval.
- **Review Rank 2 (SIV) evidence:** If the objective is to establish proof-of-concept for lentiviral protease cross-reactivity, the SIV/NHP literature (4 studies, L3 evidence) provides a more substantial starting point than the feline data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

