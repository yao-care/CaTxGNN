---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 687
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Ritonavir is a well-established antiretroviral (HIV-1 protease inhibitor); this specific evidence pack does not carry formally recorded original-indication or Canada license data, but its role as an HIV-1 protease inhibitor is referenced throughout the underlying mechanistic evidence.
> The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)** — a veterinary, not human, disease — supported by only **1 clinical trial** and **0 publications**, and that single trial is itself a human HIV-1 study, not an FIV study.
> Evidence quality is weak (**L5**), and the pack's own relevance grading (Grade C) flags this prediction as a likely species-mismatch artifact in the knowledge graph rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in regulatory license data (0 licenses); mechanistic evidence in this pack describes ritonavir as an **HIV-1 protease inhibitor** used in antiretroviral therapy |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) — a veterinary disease |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for ritonavir is not available as a discrete field in this evidence pack. Based on the mechanistic notes accompanying the predictions, ritonavir is an **HIV-1 protease inhibitor**: it binds a site specific to the structure of HIV-1 protease, and its efficacy as part of antiretroviral therapy in HIV-1 infection is well established.

The predicted new indication, however, is **feline immunodeficiency virus (FIV)-related disease** — a lentivirus infection in cats, not humans. FIV and HIV are both lentiviruses, but FIV protease sequence and active-site structure differ substantially from HIV-1 protease, and there is no known cross-inhibition evidence for ritonavir against FIV protease. The evidence pack itself flags this as a probable **species mismatch**: the only supporting clinical trial (NCT02770508) is a human HIV-1 trial comparing darunavir/ritonavir-based regimens, with no connection to cats or FIV, and its relevance to the predicted indication was graded **C** ("likely KG edge error or cross-species data contamination, not a genuine relevant trial").

In short, the mechanistic rationale that supports ritonavir's *known* action (HIV-1 protease inhibition) does not extend to the *predicted* indication (FIV) without direct evidence of cross-species protease inhibition, which is currently absent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Human HIV-1 trial comparing boosted darunavir + lamivudine vs. boosted darunavir + emtricitabine/tenofovir or lamivudine/tenofovir in treatment-naïve HIV-1 patients. **Not an FIV/feline study** — relevance to the predicted indication graded C (likely species-mismatched KG edge, not genuine supporting evidence). |

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only); the single associated clinical trial is a human HIV-1 study with no relevance to the predicted feline indication, and was independently graded C ("likely KG error / cross-species data contamination").
- The predicted indication (Feline Acquired Immunodeficiency Syndrome) is a **veterinary disease**, outside the scope of human drug repurposing evaluation, and mechanistic extrapolation from HIV-1 protease inhibition to FIV protease has no supporting cross-inhibition data.
- Ritonavir is not currently marketed in Canada under this evidence pack (0 DINs), and key safety/contraindication data (TFDA label, MOA) are flagged as data gaps (DG001 blocking, DG002 high severity).

**To proceed, the following is needed:**
- Resolve DG001 (product label warnings/contraindications) and DG002 (confirmed MOA) before any S1 safety screening can occur.
- Investigate and correct the likely species-mismatched knowledge-graph edge linking ritonavir to FIV before treating this as a genuine repurposing signal.
- If a human-relevant repurposing signal is sought, note that the pack's rank-2 prediction (simian immunodeficiency virus infection) has stronger preclinical support (L3, multiple in vitro/animal studies showing ritonavir activity against SIV/SHIV protease) — but SIV is itself an animal model of HIV, not a distinct human disease, so it likewise does not constitute a novel human indication and would only support translational/mechanistic research questions, not a Go decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

