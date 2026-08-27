---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 3
---

# Lopinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the evidence pack content directly (no fabricated data), here is the evaluation report:

---

# Lopinavir: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

Lopinavir is an HIV-1 protease inhibitor, most familiar as a component of combination antiretroviral therapy for HIV-1 infection. The TxGNN model predicts a high similarity score for **Simian Immunodeficiency Virus (SIV) Infection**, but this "new indication" is not a human disease — it is the standard non-human primate model used to test HIV antiretrovirals — so the signal is currently supported only by **3 animal-model publications** and **zero clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack's regulatory data (no `taiwan_regulatory.licenses` entries); based on the mechanistic rationale supplied with the prediction, Lopinavir is an HIV-1 protease inhibitor used in antiretroviral therapy |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is not available in the evidence pack (flagged as data gap DG002). Based on the rationale accompanying the prediction, Lopinavir is an HIV-1 protease inhibitor, and SIV protease shares high sequence/structural homology with HIV-1 protease — which is precisely why SIV-infected macaques are routinely used as a **pre-clinical animal model** for testing HIV antiretroviral drugs, including protease inhibitors like Lopinavir.

However, this mechanistic link needs to be read carefully: SIV infection is **not a human disease**. It is a veterinary/research condition confined to non-human primates. The three supporting publications describe Lopinavir (often as part of combination antiretroviral regimens) being used to suppress SIV/SHIV replication in macaques as a *proxy* for studying HIV-1 dynamics — not as evidence of a genuinely novel, independently actionable human indication.

In effect, this candidate largely reconfirms Lopinavir's known antiretroviral mechanism via an animal-model term rather than surfacing a new treatable human condition. The two lower-ranked candidates in this evidence pack (feline acquired immunodeficiency syndrome, and a rare neurodevelopmental disorder) are similarly not clinically actionable: the former is a non-human disease with no supporting literature, and the latter shows no known biological pathway connecting HIV protease inhibition to neurodevelopmental pathology — both are flagged in the evidence pack as likely knowledge-graph embedding artifacts (L5, Hold) rather than real signals, and are not carried further in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal Study | Journal of Virology | Quadruple antiretroviral therapy in SIVmac251-infected cynomolgus macaques produced rapid viral decay, used to model HIV-1 viral dynamics |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal Study | Microbes and Infection | Constructed a novel SHIV carrying the HIV-1 protease gene in rhesus macaques as an in vivo tool for testing protease inhibitor efficacy |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal Study | Journal of Virological Methods | Oral HAART (AZT + 3TC + Lopinavir/Ritonavir) evaluated for impact on CD8 T-cell subsets in SHIV(89.6P)-infected rhesus macaques |

---

## Canada Market Information

No Health Canada marketing authorizations (DINs) were found for this ingredient in the evidence pack — `total_licenses` = 0 and market status is recorded as **Not Marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the evidence pack flags the absence of product-monograph warnings/contraindications as a **Blocking** data gap — DG001 — meaning this candidate cannot yet enter safety pre-screening (S1) regardless of the efficacy signal above.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication, SIV infection, is not a human disease and functions as an HIV-1 animal model rather than an independently actionable repurposing target; supporting evidence is limited to 3 animal studies (L4) with no clinical trials. Combined with the drug's non-marketed status in Canada (0 DINs) and a Blocking data gap on safety/product-monograph information (DG001), this candidate is not ready to advance past S0.

**To proceed, the following is needed:**
- Resolve DG001 (Health Canada product monograph warnings/contraindications) — Blocking, required before any S1 safety pre-screening
- Resolve DG002 (formal mechanism-of-action documentation from DrugBank)
- Re-evaluate whether a clinically meaningful human indication (rather than the SIV animal-model term) should be pursued for this protease-inhibitor mechanism
- If pursued, obtain human clinical evidence (trials/RCTs) rather than relying on animal-model literature alone
- If repurposing is to move forward, assess the Health Canada regulatory pathway given the drug is currently not marketed in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

