---
layout: default
title: Famciclovir
parent: 僅模型預測 (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
---

# Famciclovir
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

# Famciclovir: From Herpes Zoster to Post-Infectious Neuralgia

## One-Sentence Summary

Famciclovir is an orally bioavailable antiviral prodrug (of penciclovir) that is internationally approved for herpes zoster (shingles) and herpes simplex virus infections, though it currently holds no approved product in Canada.
The TxGNN model predicts it may be effective for **Post-Infectious Neuralgia** — most notably post-herpetic neuralgia (PHN) following VZV infection — with **2 related clinical trials** identified, neither of which directly evaluates famciclovir for this endpoint, and **no supporting literature** retrieved for this specific indication.
Overall evidence is at the mechanistic hypothesis stage (L4), making this a research-stage candidate requiring further dedicated study before any advancement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Herpes zoster and herpes simplex infections (internationally approved; not currently approved in Canada) |
| Predicted New Indication | Post-Infectious Neuralgia |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Famciclovir is a prodrug that is rapidly converted after oral administration to penciclovir. Inside VZV-infected cells, penciclovir is phosphorylated by the viral thymidine kinase to penciclovir triphosphate, which then competitively inhibits the viral DNA polymerase and terminates viral DNA chain elongation. This mechanism is highly selective for herpesvirus-infected cells and underpins famciclovir's approved use against herpes zoster (VZV reactivation) in adults across multiple regulatory jurisdictions.

Post-infectious neuralgia — in the VZV context synonymous with post-herpetic neuralgia (PHN) — arises when extensive VZV replication during the acute shingles episode damages the dorsal root ganglia, triggering persistent neuropathic pain that can last months to years. The mechanistic link to famciclovir is therefore direct: earlier and more complete suppression of VZV replication during the acute phase is expected to reduce neuronal injury, thereby shortening the duration or preventing the development of PHN altogether. This hypothesis is reflected in current herpes zoster management guidelines, which recommend antivirals (including famciclovir) initiated within 72 hours of rash onset specifically to reduce PHN risk.

Detailed MOA data was not available from this evidence pack's DrugBank query, but the pharmacological basis described above is well-established in the primary literature. The TxGNN model's high score (99.75%) most likely captures this causal pathway within the knowledge graph, connecting VZV-suppression nodes to nerve injury and PHN outcomes. To fully characterize the repurposing case, PHN incidence data from completed famciclovir herpes zoster RCTs (several of which are documented in the chickenpox/VZV evidence stream) should be reviewed as a priority next step.

---

## Clinical Trial Evidence

Neither retrieved trial directly tests famciclovir for post-infectious neuralgia. Both represent adjacent interventions in the herpes zoster/PHN space.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | NA | Not Yet Recruiting | 120 | Evaluates multimodal nerve block (liposomal bupivacaine vs ropivacaine) plus pulse radiofrequency for acute herpes zoster pain. Intervention is regional anaesthesia, not antiviral therapy. Aims to reduce gabapentin requirement. No famciclovir arm. |
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | NA | Unknown | 140 | Tests early oxycodone during acute herpes zoster to prevent PHN (>90-day persistence). Opioid-focused; no famciclovir involvement. Trial status unverified. |

> **Key gap:** PHN prevention data for famciclovir exists within herpes zoster trials (e.g., NCT01327144 — Phase 3 RCT, completed, 177 participants) but was captured under the chickenpox/VZV evidence stream rather than queried under post-infectious neuralgia. A targeted re-query of VZV RCTs for PHN secondary endpoints is recommended.

---

## Canada Market Information

Famciclovir is currently **not marketed in Canada** and has no active Drug Identification Numbers (DINs) on file. The drug is approved and commercially available in the United States (Famvir®, Novartis), the European Union, and multiple Asian markets for herpes zoster and herpes simplex indications.

There are no approved Canadian product monographs available within this evidence pack. All prescribing information must be sourced from approved international labels (FDA, EMA) or the originator's package inserts.

---

## Safety Considerations

Safety information specific to Canadian regulatory filings was not retrieved in this evidence pack. Please refer to the current prescribing information and international package inserts for warnings, contraindications, dose adjustments in renal impairment, and drug interaction profiles.

---

## Additional Predicted Indications — Summary

The TxGNN model generated 10 predictions for famciclovir. Below is a summary to support prioritization decisions:

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Mechanistic Basis |
|------|---------|-------------|----------------|----------|-------------------|
| 1 | Post-infectious neuralgia | 99.75% | L4 | Hold | Biologically plausible (VZV ganglionic damage → PHN); no direct famciclovir trial |
| 2 | Sequela of COVID-19 | 99.73% | L5 | Hold | SARS-CoV-2 is RNA virus; penciclovir targets DNA polymerase — no direct mechanism |
| 3 | Hepatitis C induced liver cirrhosis | 99.73% | L5 | Hold | HCV is RNA virus; famciclovir has no activity against HCV |
| 4 | Malignant pleural mesothelioma | 99.46% | L5 | Hold | No herpesvirus-driven oncology mechanism; graph topology artifact |
| **5** | **AIDS-related disorder** | **99.30%** | **L3** | **Proceed with Guardrails** | **Famciclovir suppresses HSV-1/2, VZV, and HHV-8 (KSHV) in HIV/AIDS patients** |
| 6 | Malignant epithelioid mesothelioma | 99.14% | L5 | Hold | Same as #4 — no biological basis |
| **7** | **Chickenpox (VZV)** | **99.11%** | **L1** | **Proceed with Guardrails** | **Direct mechanism; ≥2 completed Phase 3 RCTs including pediatric PK study** |
| 8 | Sarcomatoid mesothelioma | 99.09% | L5 | Hold | Graph structure similarity only; no biological rationale |
| 9 | Malignant visceral pleura tumor | 99.04% | L5 | Hold | Same as #4, #6, #8 |
| 10 | Anogenital HPV infection | 98.97% | L5 | Hold | HPV uses E1 helicase; penciclovir has no HPV mechanism — off-target prediction |

> **Analyst note:** The two highest-priority actionable indications from this full set are **chickenpox (L1, rank 7)** and **AIDS-related herpesvirus complications (L3, rank 5)**, both with stronger evidence bases than the top-ranked post-infectious neuralgia prediction. A separate focused report is recommended for each.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis connecting famciclovir to post-infectious neuralgia prevention is biologically coherent and clinically intuitive, but neither the clinical trials nor the literature retrieved in this evidence pack directly test famciclovir for this endpoint. With an L4 evidence level and no Canada market presence, this indication cannot advance beyond research-stage consideration without additional data.

**To proceed, the following is needed:**

- **PHN endpoint data extraction:** Review completed herpes zoster RCTs (particularly NCT01327144, Phase 3, n=177) for PHN incidence as a secondary endpoint; conduct targeted PubMed queries combining "famciclovir" AND "postherpetic neuralgia" AND "prevention"
- **Comparative antiviral analysis:** Systematic review comparing famciclovir, valacyclovir, and acyclovir for PHN prevention to contextualize famciclovir's relative benefit
- **MOA data completion:** Retrieve full pharmacological profile from DrugBank API (DB00426) to complete mechanistic analysis
- **Safety profile acquisition:** Download and parse international prescribing information (FDA label, EMA SmPC) to complete safety assessment; address data gap DG001
- **Canada regulatory pathway assessment:** Evaluate requirements for New Drug Submission (NDS) or potential use under Health Canada's Special Access Program given current zero-DIN status
- **Prioritized action:** Before investing further in post-infectious neuralgia, consider advancing the chickenpox (L1) and AIDS-related disorder (L3) indications in parallel, where evidence is materially stronger

---

*⚠️ Disclaimer: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

