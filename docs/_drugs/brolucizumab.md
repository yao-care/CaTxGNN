---
layout: default
title: Brolucizumab
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 4
---

# Brolucizumab
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

# Brolucizumab: From Neovascular Age-Related Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies

## One-Sentence Summary

Brolucizumab is a humanized single-chain antibody fragment that selectively inhibits VEGF-A, currently used intravitreally for neovascular (wet) age-related macular degeneration (nAMD) and diabetic macular edema (DME).
The TxGNN model predicts it may be effective for **Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies**, achieving a prediction score of **99.67%**.
However, this candidate is currently at **Evidence Level L5** — supported by **no clinical trials** and **no published literature** — making it a model-only signal at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Canada regulatory data (known approved indication: neovascular AMD / DME) |
| Predicted New Indication | Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Brolucizumab is a humanized single-chain antibody fragment (scFv) that binds and neutralizes VEGF-A with high affinity. It is delivered via intravitreal injection and is approved for the treatment of neovascular (wet) age-related macular degeneration and diabetic macular edema. Detailed mechanism of action data was not available in this evidence pack; however, its established pharmacology centers on blocking VEGF-A from binding to VEGFR-1 and VEGFR-2, thereby reducing pathological angiogenesis and vascular permeability in the retina.

VEGF-A signaling has been reported to play an indirect regulatory role in mitochondrial biology: VEGF can influence mitochondrial biogenesis and reactive oxygen species (ROS) balance, and low-level VEGFR-2 expression has been detected on mitochondrial membranes of select non-vascular cell types. This cross-talk could theoretically explain the high TxGNN score (0.997), as the model may have captured an indirect network association between the VEGF–ROS axis and mitochondrial energy metabolism pathways.

Despite this indirect connection, the biological plausibility remains weak. Mitochondrial oxidative phosphorylation disorders caused by nuclear DNA anomalies (e.g., mutations in *POLG*, *TWNK*, *SURF1*) are primarily genetic loss-of-function diseases affecting the structural integrity of respiratory chain complexes. VEGF-A inhibition does not address the underlying genetic defect, offers no compensatory mechanism for impaired ATP production, and — critically — intravitreal injection provides negligible systemic drug exposure, making it pharmacokinetically unsuitable for any systemic mitochondrial condition. The high TxGNN score most likely reflects an indirect graph-level association rather than a clinically actionable mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Brolucizumab (Beovu®) is not currently marketed in Canada. No Drug Identification Numbers (DINs) have been issued by Health Canada for this agent, and no approved product licenses are on record in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Based on the known post-marketing safety profile of brolucizumab, clinicians should be aware of serious risks including intraocular inflammation (IOI), retinal vasculitis, and retinal vascular occlusion, which have been reported in pharmacovigilance data following intravitreal use. Formal warnings and contraindications applicable to any new indication could not be assessed due to absent regulatory label data in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.67%), the mechanistic link between VEGF-A inhibition and nuclear DNA-driven mitochondrial oxidative phosphorylation disorders is indirect and lacks pathophysiological justification. With zero supporting clinical trials or published literature, this candidate cannot advance beyond L5 at this time.

**To proceed, the following is needed:**
- Mechanism of action data confirming any direct or indirect VEGF-A / mitochondrial respiratory chain interaction
- Preclinical studies (in vitro or in vivo mitochondrial disease models) evaluating anti-VEGF agents, including brolucizumab or class analogs
- Evaluation of an alternative systemic delivery route, as intravitreal injection provides insufficient systemic drug exposure for any non-ocular indication
- Pharmacokinetic modeling to determine whether systemic brolucizumab concentrations achievable via IV/SC routes could reach therapeutic levels in affected tissues
- Formal review of Health Canada regulatory pathway and DIN application requirements before any clinical development is considered in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

