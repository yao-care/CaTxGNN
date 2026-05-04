---
layout: default
title: Acebutolol
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 2
---

# Acebutolol
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

# Acebutolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Acebutolol is a cardioselective beta-1 adrenergic receptor blocker commonly used for hypertension and cardiac arrhythmias, with no current Canadian market registration.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, though **no clinical trials** and **no direct publications** currently support this specific indication (one related publication exists for the closely linked condition of malignant renovascular hypertension).
The overall evidence base is limited, and a Hold decision is recommended pending further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no Canadian DIN registrations) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Acebutolol is a cardioselective beta-1 adrenergic receptor blocker with intrinsic sympathomimetic activity (ISA). Detailed MOA data was not retrievable from DrugBank in this evidence pack, but acebutolol's mechanism is well-established: by blocking β1 receptors in the heart and kidneys, it reduces cardiac output and suppresses renin secretion from the juxtaglomerular apparatus, thereby lowering blood pressure through simultaneous cardiovascular and renal pathways.

Malignant hypertensive renal disease is a hypertensive emergency characterized by severely elevated blood pressure causing acute renal end-organ damage, including fibrinoid necrosis and thrombotic microangiopathy. The mechanistic rationale for acebutolol in this context centres on β1 blockade attenuating renin release — a critical upstream trigger of the renin-angiotensin-aldosterone system (RAAS) — and reducing pathological sympathetic overdrive, both of which drive the self-reinforcing cycle of malignant hypertension and progressive renal injury.

That said, the standard of care for acute malignant hypertensive emergencies relies on intravenous agents (e.g., sodium nitroprusside, intravenous labetalol), and oral acebutolol has never been directly validated in this acute-phase context. Additionally, acebutolol's ISA property may dampen its antihypertensive potency compared to beta-blockers without ISA, potentially limiting its role to adjunctive or chronic-phase management. While the mechanistic link is biologically plausible, direct clinical validation is absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acebutolol in malignant hypertensive renal disease.

---

## Literature Evidence

No direct literature was identified for the primary ranked indication (malignant hypertensive renal disease). One publication was retrieved for the closely related second-ranked indication, **malignant renovascular hypertension**, and is presented below for contextual reference:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [768911](https://pubmed.ncbi.nlm.nih.gov/768911/) | 1975 | Clinical Study | La Nouvelle Presse Médicale | Open-label trial in 50 hypertensive patients, including a renovascular hypertension subgroup; acebutolol alone or in combination showed good or moderate blood pressure response in 74% of patients at mean dose 10 mg/kg; the drug was well tolerated over one year. |

> **Important caveat:** This is a small, non-randomized, open-label study from the early beta-blocker era (1975) and does not meet modern evidence standards. It cannot be used to establish efficacy in malignant hypertensive renal disease.

---

## Canada Market Information

Acebutolol currently holds no Drug Identification Numbers (DINs) in Canada and has no active market authorizations on record. There is no regulatory approval history to extract.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high prediction score of 99.10% and a biologically plausible mechanistic link exists through β1 blockade and upstream RAAS suppression, the evidence base sits at Level L5 (model prediction only) with no registered clinical trials and no direct published literature for the primary indication. The absence of any Canadian regulatory registration further compounds the translational barrier.

**To proceed, the following is needed:**
- Retrieve complete MOA, key warnings, contraindications, and drug-drug interaction data from DrugBank to enable a full safety assessment
- Search Health Canada's drug product database and international registries (EMA, FDA) to determine whether acebutolol holds any existing approval that could support a regulatory pathway
- Conduct a systematic review of beta-blockers as a class in malignant hypertensive renal disease to establish whether a class-level evidence bridge is feasible
- Evaluate whether acebutolol's ISA property represents a clinical disadvantage relative to non-ISA beta-blockers in acute hypertensive emergencies
- Define a minimum evidence generation plan (e.g., retrospective cohort analysis or pharmacoepidemiological study) to upgrade the evidence level from L5 before any prospective investment is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

