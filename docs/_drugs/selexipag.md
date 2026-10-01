---
layout: default
title: Selexipag
parent: Model Prediction Only (L5)
nav_order: 833
evidence_level: L5
indication_count: 10
---

# Selexipag
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Selexipag: From Pulmonary Arterial Hypertension to PAH Associated with Congenital Heart Disease

## One-Sentence Summary

Selexipag is an oral drug used to treat pulmonary arterial hypertension (PAH). The TxGNN model predicts it may also be useful for **pulmonary arterial hypertension associated with congenital heart disease (CHD-PAH)**. Evidence is thin: **2 clinical trials** (one terminated with 9 participants, one long-term follow-up platform study) and **no publications** are currently registered for this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (general PAH; the Canadian license records supplied contain no indication text) |
| Predicted New Indication | Pulmonary arterial hypertension associated with congenital heart disease |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L3 (per the Evidence Pack scoring; see the note under Clinical Trial Evidence) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the supplied record. Based on general pharmacology, selexipag is an oral prodrug whose active metabolite is a selective prostacyclin (IP) receptor agonist. It relaxes pulmonary blood vessels and has antiproliferative effects.

CHD-associated PAH belongs to Group 1 PAH, the same group as the drug's established use. It shares the pulmonary vasoconstriction and vascular remodeling that IP-receptor agonism targets, so the prediction is mechanistically plausible.

The very high score (98%) most likely reflects selexipag's known link to PAH as a whole, not a signal specific to CHD. The score therefore should not be read as evidence of efficacy in this subtype.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04435782](https://clinicaltrials.gov/study/NCT04435782) | Phase 4 | Terminated | 9 | Single-arm, open-label study of selexipag's effect on right ventricular function (cardiac MRI) in PAH. Stopped early with only 9 participants, so no efficacy or safety conclusion can be drawn. |
| [NCT05179876](https://clinicaltrials.gov/study/NCT05179876) | Phase 3 | Recruiting | 280 | Open-label platform study giving continued access to, and long-term safety follow-up of, pulmonary hypertension patients from parent studies. It is not designed to test efficacy, and its CHD-specific content cannot be confirmed from the title. |

Neither trial is a completed randomized efficacy study in CHD-PAH. The L3 level comes from the Evidence Pack's own scoring, and the actual support is weaker than that label suggests.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage form, manufacturer and approved-indication text are blank in the supplied license records. Five of the 8 authorizations are listed.

| DIN | Product Name |
|---------|------|
| 2451174 | UPTRAVI |
| 2451220 | UPTRAVI |
| 2451182 | UPTRAVI |
| 2451158 | UPTRAVI |
| 2451204 | UPTRAVI |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For this indication, the only direct data are a terminated 9-patient single-arm study and a long-term follow-up platform study, and there is no supporting literature. A high model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Review the CHD (including Eisenmenger syndrome) subgroup data from the pivotal GRIPHON trial, which sits outside this dataset, and run a CHD-PAH-specific literature search.
- Check whether NCT05179876 includes CHD-PAH participants and reports outcomes for them.
- Obtain the Health Canada package insert (warnings, contraindications, drug interactions), which is currently missing and blocks safety screening.
- Obtain mechanism-of-action data from DrugBank to replace the general-pharmacology reasoning used here.
- Consider prioritizing **PAH associated with connective tissue disease** (rank 3) instead. It has a selexipag-specific GRIPHON subgroup analysis plus real-world series, giving it more evidence than CHD-PAH. It is the only predicted indication scored "Proceed with Guardrails".
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

