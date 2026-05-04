---
layout: default
title: Bromazepam
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 1
---

# Bromazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Bromazepam: From Anxiety to Migraine Disorder

## One-Sentence Summary

Bromazepam is a benzodiazepine (BZD) class drug, widely recognized for its anxiolytic, sedative, and muscle relaxant properties through positive modulation of the GABA-A receptor. The TxGNN model predicts it may be effective for **Migraine Disorder**, with **1 clinical trial** and **no published literature** currently supporting this direction. Overall evidence remains at the preclinical/mechanistic reasoning stage, and meaningful clinical validation is absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders (benzodiazepine class, anxiolytic/sedative) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bromazepam belongs to the benzodiazepine (BZD) class and acts as a positive allosteric modulator at the GABA-A receptor, enhancing inhibitory neurotransmission throughout the central nervous system. This results in anxiolytic, sedative, hypnotic, anticonvulsant, and muscle relaxant effects. The mechanistic rationale for its predicted use in migraine centres on the hypothesis that by suppressing cortical hyperexcitability and attenuating stress-triggered neural activation, BZD agents could theoretically reduce migraine frequency — particularly in patients with comorbid anxiety disorders, where migraine and anxiety are well-established bidirectional comorbidities.

However, this mechanistic link carries a critical internal contradiction. Benzodiazepines are themselves recognized as a high-risk drug class for inducing **Medication Overuse Headache (MOH)**, a condition where frequent use of headache-relieving or centrally-acting drugs paradoxically worsens headache chronification. The single identified clinical trial (NCT04410536) actually investigates *withdrawal* from overused medications — including agents like bromazepam — rather than assessing bromazepam as a migraine treatment. This inverts the repurposing hypothesis rather than supporting it.

In summary, while a theoretical mechanistic bridge exists (GABA-mediated suppression of central sensitization), the evidence profile is dominated by a known biological risk that actively counteracts the proposed benefit. The TxGNN model may be capturing a statistical association between BZD use and migraine patient populations, rather than a therapeutic opportunity. This warrants a cautious "Hold" posture until a more specific mechanistic hypothesis can be validated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT04410536](https://clinicaltrials.gov/study/NCT04410536) | Phase 4 | Completed | 25 | Home-based withdrawal program combined with behavioural therapy for Medication Overuse Headache (MOH) during COVID-19; assessed relapse incidence and clinical impact at 1-year follow-up. Bromazepam's likely role is as a **withdrawal management agent**, not as a migraine treatment — relevance to the repurposing hypothesis is indirect (Grade C). |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Bromazepam currently holds **no active Drug Identification Numbers (DINs)** in Canada and is **not marketed**. No regulatory authorizations are on record.

> **Note:** Bromazepam is a Schedule IV controlled substance under the *Controlled Drugs and Substances Act* (Canada) due to its benzodiazepine classification. Any future marketing authorization would require both a standard New Drug Submission and compliance with controlled substance regulations.

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, and drug interaction profiles) were not retrieved in this evidence pack. However, the following class-level considerations are known from the pharmacological literature and are highly relevant to this repurposing assessment:

- **Benzodiazepine dependence and withdrawal risk**: BZD agents carry a well-documented risk of physical dependence with prolonged use; abrupt discontinuation can precipitate withdrawal seizures.
- **Medication Overuse Headache (MOH)**: Regular use of BZDs in headache patients is associated with MOH chronification — a direct safety concern that is paradoxically central to the one existing clinical trial identified.
- **CNS depression**: Additive sedation with alcohol, opioids, and other CNS depressants is a major interaction risk.
- **Cognitive and psychomotor impairment**: Particularly in elderly patients; falls and driving impairment are class-level concerns.

Please refer to the current Health Canada product monograph (if available) and published benzodiazepine prescribing guidelines for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.06%), but real-world evidence does not support bromazepam as a migraine treatment — the sole clinical trial identified is oriented toward *treating harms caused by drugs like bromazepam*, not toward validating its use as a migraine therapy. Furthermore, bromazepam is not marketed in Canada, and safety data specific to this indication are unavailable. The mechanistic rationale is theoretically plausible but is undermined by a well-established class-level contraindication (MOH risk).

**To proceed, the following is needed:**

- **Mechanistic clarification**: Commission a formal literature review to determine whether any sub-population (e.g., migraine with comorbid anxiety disorder, short-term acute use only) could derive net benefit without triggering MOH — this is the central unresolved question.
- **MOH risk quantification**: Retrieve and review primary MOH literature specifically for bromazepam (vs. other BZDs) to assess whether the risk is class-wide or dose/duration-dependent.
- **Safety data retrieval**: Obtain the full DrugBank safety profile, TFDA package insert warnings, and contraindications to complete the baseline safety assessment (currently all flagged as data gaps).
- **Regulatory pathway assessment**: Confirm whether a controlled substance with no current Canadian market presence can enter a repurposing regulatory pathway, and under what conditions.
- **Reconsider TxGNN signal**: Investigate whether the high TxGNN score reflects a true therapeutic association or a spurious correlation driven by co-occurrence of BZD use and migraine diagnoses in training data. If the latter, the prediction score should be discounted significantly.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

