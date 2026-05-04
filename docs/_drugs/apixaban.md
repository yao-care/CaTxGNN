---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Apixaban
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

# Apixaban: From Atrial Fibrillation / Venous Thromboembolism to Migraine Disorder

## One-Sentence Summary

Apixaban is a direct oral Factor Xa inhibitor (DOAC), approved globally for stroke prevention in non-valvular atrial fibrillation and for the treatment and prevention of venous thromboembolism, though no Canadian regulatory records were retrieved in this dataset.
The TxGNN model assigns it the highest repurposing score for **Migraine Disorder** (99.02%), currently supported by **1 indirect clinical trial** and **4 case-level publications**.
Critically, the available evidence raises a directional concern: existing case reports suggest Apixaban may be **inferior to warfarin** and may even **worsen migraine symptoms** in some patients — a cautionary signal that outweighs the model's high prediction confidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Canadian regulatory dataset; globally indicated for atrial fibrillation (stroke prevention) and venous thromboembolism (DVT/PE treatment and prophylaxis) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed (per dataset — likely a data collection gap; see note in Canada Market Information section) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved in this Evidence Pack. Based on known pharmacology, Apixaban is a selective Factor Xa (FXa) inhibitor, and its efficacy in thromboembolism prevention and atrial fibrillation is well-established. Mechanistically, FXa inhibition may be relevant to migraine through the following hypothesis: by reducing thrombin generation and downstream platelet activation, Apixaban could decrease the release of vasoactive mediators — including serotonin — that are implicated in migraine pathophysiology. An additional pathway involves Patent Foramen Ovale (PFO): PFO prevalence in patients with migraine with aura (~40–50%) is nearly double that in controls, and right-to-left cardiac shunting of microemboli may trigger cortical spreading depression. Anticoagulation theoretically reduces this embolic burden, potentially attenuating aura-related migraine attacks.

Despite this biologically plausible framework, the clinical evidence highlights a drug-specific limitation. Warfarin — a Vitamin K antagonist — appears meaningfully more effective than Apixaban for migraine, and likely exerts benefit through mechanisms beyond FXa inhibition. Vitamin K-dependent proteins such as Gas6 and Protein S regulate microglial activation, endothelial function, and neuroinflammation; warfarin's interference with these proteins may provide anti-migraine effects that Apixaban, as a selective FXa inhibitor, cannot replicate. A published case (PMID 28960288) vividly illustrates this distinction: a patient achieved 12 years of migraine remission on warfarin, relapsed within 3 weeks of switching to Apixaban, and remitted again upon warfarin resumption.

In summary, the TxGNN model likely captures the broad anticoagulant–migraine network proximity rather than Apixaban-specific biology. The available clinical data suggest that any anticoagulant benefit for migraine is **warfarin-specific**, not a class effect — making Apixaban a poor repurposing candidate for this indication even if the mechanistic hypothesis is ultimately validated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | CLOSE trial: randomized comparison of transcatheter PFO closure, oral anticoagulants (warfarin), and antiplatelet agents for secondary stroke prevention in cryptogenic stroke patients with PFO. The anticoagulant arm used warfarin, not Apixaban. Relevant because PFO-related stroke and migraine with aura share pathophysiological overlap, but provides only indirect, Grade B support for Apixaban repurposing in migraine. |

> No clinical trials directly evaluating Apixaban for migraine disorder were identified in this dataset.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Small Interventional Trial | *Lupus* | Retrospective study of 75 antiphospholipid antibody (aPL)-positive patients with refractory migraine treated with antithrombotic therapy; a subset showed symptomatic improvement with anticoagulation. Apixaban was not separately analysed. Suggests that aPL-positive patients may represent a biologically distinct subgroup where anticoagulation can benefit migraine — but does not specifically implicate Apixaban. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report + Literature Review | *The Neurologist* | Documents worsening of migraine with aura after Apixaban initiation. Accompanying literature review concludes that the impact of DOACs on migraine frequency and severity is "unclear and controversial." Raises a safety concern against Apixaban use in migraine patients. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | *Headache* | A 55-year-old woman achieved 12-year migraine with aura remission on warfarin; symptoms returned within 3 weeks of switching to Apixaban and resolved again within days of resuming warfarin. Directly and compellingly demonstrates that warfarin and Apixaban are not interchangeable for migraine. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | *Headache* | Vestibular migraine resolved on a combination of warfarin and topiramate. Apixaban was not evaluated. Provides indirect contextual support for the anticoagulation–migraine hypothesis but does not specifically support Apixaban. |

---

## Canada Market Information

No registered products for Apixaban were found in the Canadian regulatory dataset associated with this analysis (total DINs: 0; market status: Not Marketed per regulatory query).

> ⚠️ **Data Gap Notice:** This is almost certainly a data collection error. Apixaban (Eliquis®, co-marketed by Bristol-Myers Squibb and Pfizer) is a widely approved and commercially available DOAC in Canada and numerous other major markets, indicated for atrial fibrillation, DVT/PE treatment, and surgical VTE prophylaxis. Manual verification of the Canadian Drug Identification Number (DIN) registration via Health Canada's Drug Product Database is strongly recommended before drawing any market access conclusions.

---

## Safety Considerations

Safety data — including key warnings, contraindications, and drug-drug interactions — were not available in this Evidence Pack.

Please refer to the Eliquis® Canadian Product Monograph for complete safety information, with particular attention to: major and clinically relevant non-major bleeding risk; contraindications in patients with active pathological bleeding or prosthetic heart valves; interactions with strong dual CYP3A4/P-gp inhibitors (e.g., ketoconazole, itraconazole) and inducers (e.g., rifampin, carbamazepine); and dose adjustments for renal impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite holding the highest TxGNN repurposing score, the evidence for Apixaban in migraine disorder is not only insufficient (Level L4) but directionally negative — the most directly relevant case reports document either migraine worsening or a clear failure to replicate the benefit seen with warfarin. Even in the most biologically plausible subgroup (PFO-positive migraine with aura), the existing data favour warfarin or PFO closure over Apixaban. Pursuing Apixaban for this indication risks harm without a clear mechanistic advantage.

**To proceed, the following is needed:**
- Mechanistic studies clarifying whether anti-migraine benefit from anticoagulation is mediated by thrombin/FXa inhibition (potentially class-wide) or by Vitamin K-dependent protein modulation (warfarin-specific, Gas6/Protein S pathways)
- Prospective investigation in the targeted subgroup: PFO-positive patients with migraine with aura, including a direct Apixaban vs. warfarin arm
- Full pharmacological profile: MOA documentation, complete drug interaction data, and Health Canada–approved product monograph review
- Regulatory data correction: confirm Canadian DIN registration status for Apixaban (Eliquis®) via Health Canada Drug Product Database

---

> 💡 **Higher-Priority Repurposing Signal Identified:** Although ranked only 8th by TxGNN score, **Pulmonary Hypertension** — specifically chronic thromboembolic pulmonary hypertension (CTEPH) and systemic sclerosis-related pulmonary arterial hypertension (SSc-PAH) — carries substantially stronger evidence for Apixaban repurposing across this analysis (Evidence Level **L3**; Decision: **Proceed with Guardrails**). The SPHInX study ([PMID 27932335](https://pubmed.ncbi.nlm.nih.gov/27932335/)) is a dedicated multicentre randomised placebo-controlled trial specifically evaluating Apixaban in SSc-PAH, and lifelong anticoagulation is already guideline-supported for CTEPH. This indication represents the most clinically actionable repurposing opportunity in this Evidence Pack and warrants a separate focused evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

