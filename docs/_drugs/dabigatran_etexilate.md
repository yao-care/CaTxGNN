---
layout: default
title: Dabigatran Etexilate
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 5
---

# Dabigatran Etexilate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Dabigatran Etexilate: From Thromboembolic Disorders to Sclerosing Cholangitis

## One-Sentence Summary

Dabigatran etexilate (Pradaxa) is a direct oral thrombin inhibitor (direct thrombin inhibitor, DTI) internationally approved for the prevention of stroke and systemic embolism in non-valvular atrial fibrillation, as well as for the treatment and prevention of venous thromboembolism.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**,
with **0 clinical trials** and **1 publication** (indirectly related) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Thromboembolic disorders (atrial fibrillation, VTE prevention/treatment) — not registered in Taiwan |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dabigatran etexilate is an oral prodrug that is converted in vivo to dabigatran, a potent, competitive, and reversible direct thrombin inhibitor. By blocking thrombin (Factor IIa), it prevents the conversion of fibrinogen to fibrin, inhibits thrombin-mediated platelet aggregation, and suppresses downstream coagulation cascade activation.

The biological rationale connecting thrombin inhibition to sclerosing cholangitis is highly speculative. Thrombin can activate hepatic stellate cells (HSCs) via protease-activated receptors PAR-1 and PAR-2, promoting periductal fibrosis — which is a hallmark pathological feature of primary sclerosing cholangitis (PSC). In theory, inhibiting thrombin could attenuate this pro-fibrotic signalling pathway and slow the progression of biliary fibrosis.

However, this mechanistic link currently lacks direct clinical or experimental validation in the context of sclerosing cholangitis. PSC is a complex, immune-mediated cholestatic liver disease driven primarily by biliary epithelial injury and dysregulated immune responses, not by coagulation cascade overactivation. The TxGNN model may have detected indirect network associations, but the biological plausibility is rated low-to-moderate, and no targeted clinical investigation has been initiated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | Pharmacokinetic/DDI Study | Clinical Pharmacokinetics | Evaluates DDI potential of cilofexor (an FXR agonist in development for PSC and NASH) — dabigatran is cited as a reference substrate. This paper concerns cilofexor, not dabigatran's effect on sclerosing cholangitis itself; relevance is indirect. |

> **Note:** No literature directly studying dabigatran in sclerosing cholangitis was identified. The single retrieved publication is a DDI study for a different investigational drug (cilofexor) in which dabigatran is referenced as a pharmacokinetic probe, not as a therapeutic agent for PSC.

---

## Taiwan Market Information

Dabigatran etexilate currently has **no approved Drug Identification Numbers (DINs) in Taiwan**. The drug is not marketed in the Taiwan market. No license records are available.

---

## Safety Considerations

Detailed safety data specific to the Taiwan label (TFDA prescribing information, warnings, contraindications) was not retrievable at the time of this report (Data Gap DG001).

> Please refer to the international package insert (e.g., Health Canada Product Monograph or EMA Summary of Product Characteristics) for safety information, including:
> - **Major known risks**: Bleeding (major and life-threatening), epidural/spinal haematoma with neuraxial anaesthesia
> - **Key contraindications**: Active bleeding, severe renal impairment (CrCl < 15 mL/min), prosthetic heart valves
> - **Drug interactions**: P-glycoprotein (P-gp) inhibitors (e.g., ketoconazole, dronedarone, rifampicin) significantly affect plasma levels

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.82%), but the mechanistic link between thrombin inhibition and sclerosing cholangitis is highly speculative and currently unsupported by any clinical trial or directly relevant literature. With an Evidence Level of L5 (model prediction only) and no registered trials in this indication, advancement is premature.

**To proceed, the following is needed:**

- **Preclinical validation**: Animal or in vitro studies demonstrating that thrombin inhibition reduces biliary fibrosis or improves PSC-related histological outcomes (e.g., in a Mdr2−/− mouse model or bile duct ligation model)
- **Mechanistic data (MOA, DG002)**: Retrieve full DrugBank pharmacological profile to confirm PAR-1/PAR-2-mediated HSC activation is a relevant pathway for dabigatran's class
- **Safety data (DG001)**: Download and parse TFDA prescribing information PDF to complete the safety screening (DG001 is classified as Blocking for S1 safety evaluation)
- **Literature deep-dive**: Search for studies on thrombin/coagulation pathway involvement in PSC or other cholestatic liver diseases to assess indirect biological plausibility
- **Regulatory pathway assessment**: Because dabigatran is not marketed in Taiwan, any repurposing development would need to start from market entry, adding substantial regulatory complexity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

