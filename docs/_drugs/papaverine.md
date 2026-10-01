---
layout: default
title: Papaverine
parent: Moderate Evidence (L3-L4)
nav_order: 700
evidence_level: L4
indication_count: 10
---

# Papaverine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Papaverine: From Smooth Muscle Relaxant (Vasodilator) to Ischemic Disease

## One-Sentence Summary

Papaverine is a smooth muscle relaxant and vasodilator, marketed in Canada as an injectable. The TxGNN model predicts it may be effective for **ischemic disease**, but the support is weak: the **4 clinical trials** found are diagnostic, observational or surgical-technique studies rather than treatment trials of papaverine, and the **20 publications** are mostly old reviews, small clinical studies and animal work.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the registry data (drug class: smooth muscle relaxant / vasodilator) |
| Predicted New Indication | Ischemic disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The DrugBank mechanism-of-action field is empty for this drug. The Evidence Pack's analysis describes papaverine as a non-selective phosphodiesterase (PDE) inhibitor. Higher intracellular cAMP and cGMP relax smooth muscle and dilate blood vessels.

That mechanism fits ischemia caused by vasospasm or microvascular dysfunction. Intra-arterial papaverine is already used in non-occlusive mesenteric ischemia, and it is applied topically or intraluminally to prevent spasm in surgical grafts such as the internal thoracic and radial arteries.

"Ischemic disease" is a very broad term, and these uses concern specific spasm-related situations. They do not show that papaverine treats ischemia in general. The very high TxGNN score is a graph-based prediction only. Other predicted indications for this drug (such as vascular ectasia, angiodysplasia and fibrocartilaginous embolism) have little or no support, so the score alone should not drive decisions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05562908](https://clinicaltrials.gov/study/NCT05562908) | N/A | Completed | 165 | Randomised comparison of skeletonised vs pedicled internal thoracic artery harvesting in bypass surgery. Papaverine is at most a graft vasodilator, not the tested treatment. |
| [NCT06125392](https://clinicaltrials.gov/study/NCT06125392) | N/A | Recruiting | 1000 | Registry of chronic angina without coronary stenosis (microvascular dysfunction and spasm testing). Papaverine is at most a diagnostic agent. |
| [NCT06014242](https://clinicaltrials.gov/study/NCT06014242) | N/A | Withdrawn | 0 | Peripheral microvascular resistance as a predictor of limb salvage in critical limb ischemia. Withdrawn with no participants, so no evidence. |
| [NCT06795035](https://clinicaltrials.gov/study/NCT06795035) | N/A | Recruiting | 70 | Observational assessment of coronary microvascular dysfunction after STEMI using continuous saline thermodilution. No therapeutic evidence for papaverine. |

All four trials were graded C (low relevance) in the pack.

---

## Literature Evidence

No randomised controlled trials were found. Items are ordered with clinical studies first, then reviews, then preclinical work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16368347](https://pubmed.ncbi.nlm.nih.gov/16368347/) | 2006 | Clinical/experimental | Ann Thorac Surg | Compared glyceryl-trinitrate/verapamil solution with papaverine for treating internal thoracic artery spasm and identified the best delivery route. |
| [3661361](https://pubmed.ncbi.nlm.nih.gov/3661361/) | 1987 | Clinical physiology study | Am Heart J | Intracoronary papaverine was compared with radiographic contrast for measuring coronary flow reserve in ischemic heart disease. This is a diagnostic use. |
| [7590571](https://pubmed.ncbi.nlm.nih.gov/7590571/) | 1995 | Review | Hepato-gastroenterology | Non-occlusive mesenteric ischemia: a low-flow state with vasoconstriction and reperfusion injury. |
| [12964071](https://pubmed.ncbi.nlm.nih.gov/12964071/) | 2003 | Review | RoFo | Non-occlusive mesenteric ischemia is life-threatening, with survival not exceeding about 50% even under optimal care. |
| [8293164](https://pubmed.ncbi.nlm.nih.gov/8293164/) | 1993 | Review | Curr Opin Neurol | Interventional neuroradiology review, including superselective papaverine infusion for vasospasm after aneurysm rupture. |
| [4933650](https://pubmed.ncbi.nlm.nih.gov/4933650/) | 1971 | Review | Br Med J | Review of cerebral vasodilators (no abstract available). |
| [32713799](https://pubmed.ncbi.nlm.nih.gov/32713799/) | 2020 | Preclinical (mouse) | J Pharmacol Sci | Papaverine reduced infarct volume in mouse focal cerebral ischemia, with anti-inflammatory and immunomodulatory pathway effects. |
| [28832798](https://pubmed.ncbi.nlm.nih.gov/28832798/) | 2017 | Preclinical (rat) | Braz J Cardiovasc Surg | Studied papaverine and vitamin C against liver ischemia-reperfusion injury after aortic occlusion. |
| [30665449](https://pubmed.ncbi.nlm.nih.gov/30665449/) | 2019 | In vitro | J Cardiothorac Surg | Compared botulinum toxin A with papaverine as vasodilators in human radial artery grafts. |
| [9972912](https://pubmed.ncbi.nlm.nih.gov/9972912/) | 1998 | Preclinical (pig) | J Cardiovasc Surg | Papaverine with intrathecal cooling for spinal cord protection during aortic cross-clamping. |

---

## Canada Market Information

| DIN / License No. | Product Name |
|---------|------|
| 9881 | PAPAVERINE HYDROCHLORIDE INJECTION USP |

Dosage form, manufacturer and approved-indication text are not recorded in the available data.

---

## Safety Considerations

Please refer to the package insert for safety information. No interactions were found in the drug-interaction query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, but the indication is too broad and no trial tests papaverine as a treatment for ischemic disease. The clinical literature is mostly old, and the rest is animal or in-vitro work. The Canadian safety information has not been obtained, which blocks progress to safety screening.

**To proceed, the following is needed:**
- Health Canada product monograph or package insert (warnings, contraindications, approved indication), to clear the safety-screening block
- Mechanism-of-action data from DrugBank
- A narrower, clinically defined target indication (for example non-occlusive mesenteric ischemia, graft vasospasm or cerebral vasospasm) in place of "ischemic disease"
- Manual relevance review of the pending literature and a search for controlled trials in that narrower indication
- Dosage form and route data for the Canadian product, to check route compatibility

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

