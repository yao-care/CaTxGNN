---
layout: default
title: Acyclovir
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: From Herpes Virus Infection to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Acyclovir is a nucleoside analogue antiviral with well-established use against herpes simplex virus (HSV) and varicella-zoster virus (VZV) infections worldwide.
The TxGNN model assigns its highest repurposing score to **Punctate Epithelial Keratoconjunctivitis (PEK)** at 99.67%,
however this is supported by **0 clinical trials** and only **2 indirect background publications** — neither of which directly evaluates acyclovir as a treatment for PEK.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HSV/VZV infections (herpes labialis, genital herpes, herpes zoster, varicella) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, acyclovir is a synthetic purine nucleoside analogue that requires phosphorylation by viral thymidine kinase (TK) to become its active triphosphate form. Once activated, it competitively inhibits viral DNA polymerase and terminates DNA chain elongation. This mechanism is highly selective for herpesviruses — particularly HSV-1, HSV-2, and VZV — which encode their own TK.

Punctate epithelial keratoconjunctivitis (PEK) is a multifactorial corneal surface condition characterized by scattered epithelial defects. It can arise from numerous causes including viral infections (HSV, adenovirus), topical medication toxicity, dry eye disease, and blepharitis. In the HSV-subtype of PEK specifically, the mechanistic rationale for acyclovir would be sound: inhibiting HSV replication at the ocular surface to reduce epithelial damage. This is the likely basis for TxGNN's high prediction score, as the model's knowledge graph would connect acyclovir to the broader cluster of herpetic ocular diseases.

However, the two retrieved publications offer no direct clinical support. PMID 7825685 (1995) describes corneal lipidosis in AIDS patients receiving antivirals — an adverse effect observation, not a PEK treatment study. PMID 21934222 (2011) concerns microsporidial keratoconjunctivitis, an entirely different pathogen. The high TxGNN score most likely reflects broad graph connectivity between acyclovir and ocular herpes disease categories rather than a validated PEK-specific signal. This is a classic L5 scenario where model prediction outpaces available clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for acyclovir in punctate epithelial keratoconjunctivitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case Series | *Am J Ophthalmology* | Corneal lipidosis in AIDS patients treated with antivirals for opportunistic infections — reports drug-induced ocular surface changes (lamellar inclusions), not a PEK treatment study |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case Series | *Indian J Pathol Microbiol* | Microsporidial keratoconjunctivitis case series in eastern India — describes clinical characteristics of a non-herpetic keratoconjunctivitis; no acyclovir intervention evaluated |

> **Note:** Neither publication directly evaluates acyclovir for punctate epithelial keratoconjunctivitis. Both are retrieved as background context by semantic proximity only.

---

## Canada Market Information

Acyclovir currently has **no registered Drug Identification Numbers (DINs)** in this dataset, indicating it is not captured as marketed in Canada under this data snapshot.

> **Important caveat:** Acyclovir is a decades-old essential medicine available in numerous countries under multiple brand names (e.g., Zovirax). The absence of Canadian DIN records in this evidence pack may reflect a data collection gap rather than true market absence. The Health Canada Drug Product Database (HPFB) should be consulted directly to verify current authorization status and any approved indications.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Additional Context: Summary of All Top TxGNN Predictions

The following table provides a snapshot of all 10 ranked predictions from this evidence pack. While the report above focuses on the top-ranked prediction (Rank 1), several lower-ranked predictions carry substantially stronger clinical evidence and may warrant priority evaluation.

| Rank | Disease | TxGNN Score | Trials | Publications | Evidence Level | Decision |
|------|---------|------------|--------|-------------|---------------|---------|
| 1 | Punctate epithelial keratoconjunctivitis | 99.67% | 0 | 2 (indirect) | L5 | **Hold** |
| 2 | Common wart | 99.46% | 6 | 20 | **L2** | **Proceed with Guardrails** |
| 3 | Post-infectious neuralgia | 99.25% | 12 | 0 | L3 | Research Question |
| 4 | Hepatitis C induced liver cirrhosis | 99.23% | 0 | 2 (indirect) | L5 | Hold |
| 5 | Eosinophilic pustular folliculitis | 99.22% | 0 | 1 (indirect) | L5 | Hold |
| 6 | Sequela of COVID-19 | 99.16% | 0 | 20 (indirect) | L4 | Research Question |
| 7 | Vulvovaginal candidiasis | 99.11% | 0 | 4 (indirect) | L5 | Hold |
| 8 | Papular urticaria | 99.09% | 0 | 0 | L5 | Hold |
| 9 | Disease of orbital region | 99.08% | 50 | 3 | **L3** | **Proceed with Guardrails** |
| 10 | Epidemic keratoconjunctivitis | 99.07% | 0 | 7 | L4 | Research Question |

> **Analyst note:** **Rank 2 (Common wart)** is the most actionable repurposing candidate in this evidence pack — it has 6 registered clinical trials (including Phase 2/3 and Phase 4 RCTs with active recruitment as of 2025–2026) and 20 publications. The mechanistic hypothesis (intralesional acyclovir triggering local immune stimulation against HPV-infected cells) is supported by multiple direct comparative trials. A dedicated report for this indication is strongly recommended.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN high-score prediction for PEK is mechanistically plausible only for the HSV-subtype, but zero clinical trials and only two indirect background publications exist. This is insufficient to support any formulation, dosing, or regulatory pathway evaluation at this stage.

**To proceed, the following is needed:**

- **Verify Canada market status** directly via the Health Canada Drug Product Database (DPD) — acyclovir DIN records may exist but were not captured in this dataset
- **Retrieve the product monograph** for complete MOA, warnings, contraindications, and approved indications
- **Conduct a targeted literature search** for "acyclovir AND herpetic epithelial keratitis AND punctate" to identify any direct evidence missed by the current evidence pack query
- **Differentiate PEK subtypes** — a prospective case series restricted to HSV-positive PEK patients would be the appropriate first clinical step before any formal trial design
- **Prioritize evaluation of Rank 2 (Common wart)** — this indication has L2 evidence with ongoing Phase 4 RCTs and represents the strongest near-term repurposing opportunity in this evidence pack

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

