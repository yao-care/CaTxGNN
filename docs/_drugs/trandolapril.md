---
layout: default
title: Trandolapril
parent: Model Prediction Only (L5)
nav_order: 789
evidence_level: L5
indication_count: 6
---

# Trandolapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Trandolapril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Trandolapril is an angiotensin-converting enzyme (ACE) inhibitor established for the management of hypertension. The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a mechanism-based computational hypothesis only.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (ACE inhibitor class; specific labelled indication text not available — drug not marketed in Canada) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for trandolapril is not currently available in DrugBank. Based on information embedded in the prediction rationale, trandolapril belongs to the angiotensin-converting enzyme inhibitor (ACEi) class. ACE inhibitors suppress the renin-angiotensin-aldosterone system (RAAS), lowering systemic blood pressure and reducing intraglomerular pressure — a mechanism already recognized as a standard therapeutic approach for hypertensive kidney disease.

Malignant hypertensive renal disease is a severe manifestation of uncontrolled hypertension that causes rapid glomerular and vascular kidney damage. Because ACE inhibitors act directly on the RAAS pathway responsible for both systemic hypertension and glomerular hyperfiltration, there is a plausible mechanistic link between trandolapril's established antihypertensive effect and this new indication.

However, this connection remains theoretical. The TxGNN score reflects structural/mechanistic similarity in the knowledge graph only — no clinical trial or published literature currently confirms trandolapril's efficacy specifically in malignant hypertensive renal disease. A closely related candidate in the same evidence pack (malignant renovascular hypertension) carries an explicit mechanistic warning: ACEi use in bilateral renal artery stenosis can precipitate acute kidney injury, illustrating that high TxGNN similarity scores within this disease cluster do not equate to safety or efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Trandolapril currently has no Health Canada Drug Identification Number (DIN) on file — the drug is marked as **Not Marketed** in Canada, with 0 registered licenses.

## Safety Considerations

- **Mechanism-Based Caution**: For a closely related predicted indication (malignant renovascular hypertension) in this evidence pack, ACE inhibitors are known to precipitate acute kidney injury in patients with bilateral renal artery stenosis by blocking angiotensin II–mediated efferent arteriolar constriction. This is a well-recognized class contraindication and should be weighed carefully before advancing trandolapril for any hypertensive renal indication.

Beyond this, please refer to the package insert for full safety information — formal warnings, contraindications, and drug interaction data are not yet available in the evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (malignant hypertensive renal disease) is supported only by TxGNN's model score, with no clinical trials or literature (L5, S1 "Research Question" stage). Combined with a Blocking data gap on Canadian product-label warnings/contraindications (DG001) and the drug's current "Not Marketed" status in Canada, there is insufficient evidence and regulatory groundwork to advance beyond a research hypothesis at this time.

**To proceed, the following is needed:**
- Health Canada / TFDA product label — warnings and contraindications (DG001, Blocking)
- Detailed mechanism of action (MOA) data from DrugBank (DG002, High)
- Preclinical or clinical evidence specific to malignant hypertensive renal disease (none currently registered)
- Clarification of the regulatory pathway for a currently unmarketed drug in Canada
- Careful exclusion of renal artery stenosis / renovascular pathology before any hypertensive-renal indication is pursued, given the class-level AKI risk flagged for the related candidate indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

