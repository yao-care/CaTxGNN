---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: From Psoriasis to Seborrheic Keratosis

## One-Sentence Summary

Calcipotriol is a synthetic vitamin D₃ analogue with established international use for topical treatment of psoriasis, acting through the Vitamin D Receptor (VDR) to inhibit keratinocyte proliferation and promote differentiation.
The TxGNN model predicts it may be effective for **Seborrheic Keratosis**,
with **0 registered clinical trials** and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriasis (established internationally; no approved indication in Canada) |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Calcipotriol binds to the Vitamin D Receptor (VDR), a nuclear receptor broadly expressed in keratinocytes and other epithelial cells throughout the skin. Through VDR activation, calcipotriol suppresses excessive keratinocyte proliferation, drives terminal differentiation, and induces apoptosis via cell-cycle regulators such as p21 and p27. These are the same mechanisms responsible for its efficacy in psoriasis — a condition also defined by runaway keratinocyte hyperproliferation.

Seborrheic keratosis (SK) is the most prevalent benign epithelial tumour, arising from clonal keratinocyte overgrowth with impaired differentiation. Because VDR-mediated signalling directly counters both of these pathological features, the biological rationale for applying calcipotriol to SK is mechanistically coherent — not a speculative leap. Importantly, published case series (PMIDs 16043912, 15577148) specifically describe topical vitamin D₃ analogues including calcipotriol being used for "senile warts" (a lay synonym for seborrheic keratosis), with observed partial or complete lesion regression attributed to apoptosis induction.

The translational step from psoriasis to seborrheic keratosis is further supported by the fact that calcipotriol already exists in optimized topical formulations (ointment, cream, solution) designed for epidermal penetration. One study (PMID 15090020) directly compared calcipotriol head-to-head against standard cryosurgery for SK, an unusually direct piece of comparative evidence for a repurposing prediction at this stage. Taken together, the evidence suggests this is not merely a graph-model artefact but a pharmacologically plausible therapeutic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36752725](https://pubmed.ncbi.nlm.nih.gov/36752725/) | 2023 | Clinical Trial / Prospective Study | Australasian Journal of Dermatology | 12 patients with solitary facial SK treated with 0.005% calcipotriol ointment for 3–8 months; all achieved complete lesion regression, with remission sustained for 6–10 years |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Comparative Study (quasi-RCT) | International Journal of Dermatology | Direct comparison of cryosurgery vs. topical calcipotriol, tazarotene, and imiquimod for SK; assessed topical therapies as patient-preferred alternatives to cryotherapy |
| [16043912](https://pubmed.ncbi.nlm.nih.gov/16043912/) | 2005 | Case Series / Mechanistic Study | The Journal of Dermatology | 116 senile wart (SK) cases treated with vitamin D₃ ointments (tacalcitol, calcipotriol, maxacalcitol) for 3–12 months; 30.2% showed regression; apoptosis induction proposed as the mechanism |
| [15577148](https://pubmed.ncbi.nlm.nih.gov/15577148/) | 2004 | Case Series | Clinical Calcium | Review of topical vitamin D₃ analogues (including calcipotriol) for senile warts; once or twice daily application reported clinical benefit; discusses underlying keratinocyte biology |
| [10721662](https://pubmed.ncbi.nlm.nih.gov/10721662/) | 2000 | Case Report | The Journal of Dermatology | Keratosis lichenoides chronica with prominent seborrheic dermatitis-like facial eruption showed marked improvement with calcipotriol ointment, highlighting VDR sensitivity of keratotic lesions |
| [21534378](https://pubmed.ncbi.nlm.nih.gov/21534378/) | 2011 | Clinical Case / Review | JAAPA | Clinical presentation and treatment considerations for seborrheic keratosis on the shins; contextual reference for topical management approaches |

---

## Canada Market Information

Calcipotriol currently holds no Drug Identification Number (DIN) in Canada and is not marketed in the Canadian market. No approved indication data is available from Health Canada records.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** No Canadian package insert is available (no DIN). When sourcing safety data, refer to international labelling (e.g., EMA SmPC or US FDA label for Dovonex®/Sorilux®). Key areas to verify include local skin irritation, hypercalcaemia risk with extensive application, and contraindications in calcium metabolism disorders.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The VDR-mediated anti-proliferative and pro-apoptotic mechanism of calcipotriol maps directly onto the pathophysiology of seborrheic keratosis, and multiple published case series plus one comparative study provide L3-level human clinical evidence of efficacy. However, there are no registered randomized controlled trials, no Canadian regulatory approval, and critical safety data gaps remain unfilled.

**To proceed, the following is needed:**
- Retrieve full safety profile from international package insert (EMA or FDA labelling): warnings, contraindications, and drug interactions
- Confirm detailed MOA data via DrugBank API (DB02300) to formally document the VDR pathway
- Commission or identify a prospective Phase 2 RCT specifically designed for seborrheic keratosis, with standardized endpoints (lesion size, complete response rate)
- Assess Canadian regulatory pathway: a new indication filing or clinical trial application (CTA) to Health Canada would be required prior to any formal development program
- Define optimal formulation parameters (concentration, vehicle, treatment duration) based on the existing case-series data (0.005% ointment, 3–12 months)
- Establish a hypercalcaemia monitoring protocol for any study involving large body surface area application or occlusive dressings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

