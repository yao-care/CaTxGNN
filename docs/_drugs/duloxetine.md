---
layout: default
title: Duloxetine
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

# Duloxetine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

> **Report Focus Note:** The TxGNN model's highest-scored prediction for duloxetine is *benign paroxysmal torticollis of infancy* (Rank #1, 99.85%), but this carries zero clinical evidence and a **Hold** recommendation. This report focuses on **Obsessive-Compulsive Disorder (Rank #3, 99.84%)**, which represents the most clinically actionable repurposing opportunity with the strongest evidence base across all 10 predictions evaluated.

---

## One-Sentence Summary

Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI) widely approved for major depressive disorder (MDD), generalized anxiety disorder (GAD), diabetic peripheral neuropathic pain, fibromyalgia, and chronic musculoskeletal pain.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, with **5 clinical trials** and **20 publications** currently supporting this direction — including one completed Phase 4 trial and one double-blind RCT directly evaluating duloxetine in OCD.
This represents a mechanistically coherent and evidence-supported repurposing hypothesis within the anxiety-spectrum disorders where duloxetine already has an established foothold.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major depressive disorder / generalized anxiety disorder (evidence pack data gap — based on established pharmacology) |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| Canada Market Status | Data gap — 0 DINs retrieved (manual Health Canada verification recommended) |
| Number of DINs | 0 (data gap) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on well-established pharmacological knowledge, duloxetine is a dual-acting **serotonin-norepinephrine reuptake inhibitor (SNRI)**. It simultaneously blocks the serotonin transporter (SERT) and the norepinephrine transporter (NET), increasing synaptic availability of both 5-HT and NE in the central nervous system. This dual mechanism distinguishes duloxetine from SSRIs, which act exclusively on serotonin reuptake, and is the basis for its broader approved indication set spanning mood, anxiety, and pain conditions.

OCD is pathophysiologically driven by hyperactivation of the cortico-striato-thalamo-cortical (CSTC) circuit — in particular, the orbitofrontal cortex and caudate nucleus. The serotonergic system is central to this dysfunction: SSRIs are the established first-line pharmacotherapy for OCD, and their antiobsessional efficacy is well replicated. Duloxetine's serotonin component shares this primary mechanism. The additional norepinephrine reuptake inhibition may offer a complementary advantage by enhancing prefrontal cortical executive function and inhibitory control, potentially providing therapeutic benefit in the substantial proportion of OCD patients who show incomplete response to SSRI monotherapy.

Duloxetine is already approved for GAD, an anxiety-spectrum disorder that shares amygdala-prefrontal dysregulation with OCD, demonstrating that its SNRI profile exerts meaningful anxiolytic effects beyond depression. Multiple clinical publications — including a double-blind, placebo-controlled RCT of duloxetine augmentation in treatment-resistant OCD (Mowla et al., 2016) and a completed Phase 4 monotherapy trial (NCT00464698) — directly validate this mechanistic reasoning. The repurposing rationale is therefore grounded in both pharmacological logic and emerging clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Phase 4 | Completed | 20 | Prospective assessment of duloxetine efficacy specifically for OCD — the most direct existing clinical trial of duloxetine monotherapy in this indication |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | OCD medication response predictor study; duloxetine included as a comparator arm for patients with prior exposure to clomipramine or escitalopram — provides biomarker and comparative efficacy data relevant to patient stratification |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Unknown | 8,800 | Large individual patient data (IPD) meta-analysis of antidepressant efficacy across anxiety disorder spectrum; provides population-level evidence on initial severity as a moderator of response, with indirect applicability to OCD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | Double-blind RCT | J Clin Psychopharmacology | Duloxetine augmentation was significantly effective in treatment-resistant OCD versus placebo — the highest-quality direct evidence for duloxetine in this indication |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Frontiers in Psychiatry | Comprehensive review of antidepressant efficacy, tolerability, and suicidality across multiple paediatric and adolescent psychiatric disorders including OCD; contextualises duloxetine within the broader antidepressant class |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Systematic review / Meta-analysis | J Affective Disorders | OCD demonstrates a significantly reduced antidepressant and placebo response compared to other anxiety disorders, underscoring the clinical need for alternative pharmacological approaches such as dual-mechanism agents |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | Open-label study | Int J Neuropsychopharmacology | Open-label investigation of duloxetine monotherapy for DSM-IV OCD; supports feasibility, tolerability, and initial efficacy signals for prospective investigation |
| [39735048](https://pubmed.ncbi.nlm.nih.gov/39735048/) | 2024 | Case report | Cureus | Supratherapeutic duloxetine combined with CBT achieved sustained remission in a patient with severe treatment-resistant OCD and comorbid MDD after over a decade of failed treatments; highlights dose-optimisation as a potential strategy |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | Narrative review | Frontiers in Psychiatry | Systematic synthesis of duloxetine use across a range of psychiatric disorders beyond its approved indications, including a dedicated section on OCD evidence |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | Critical review | J Clinical Psychiatry | Foundational critical review establishing the antiobsessional properties of SNRIs (venlafaxine, clomipramine) as a class — the pharmacological basis for investigating duloxetine in OCD |
| [18208931](https://pubmed.ncbi.nlm.nih.gov/18208931/) | 2008 | Case series | J Psychopharmacology | Switching SRI-resistant OCD patients to duloxetine resulted in partial-to-full response in several cases; first case-series evidence supporting duloxetine as a rescue strategy |
| [22567604](https://pubmed.ncbi.nlm.nih.gov/22567604/) | 2012 | Case report | Innovations in Clinical Neuroscience | Suprathreshold duloxetine dosing associated with remission in comorbid treatment-resistant OCD and depression — raises dose-response considerations for future study design |
| [17632660](https://pubmed.ncbi.nlm.nih.gov/17632660/) | 2007 | Case report | Prim Care Companion J Clin Psychiatry | Among the earliest reported cases of OCD responding to duloxetine; establishes initial proof-of-concept |

---

## Canada Market Information

No Canadian regulatory data were successfully retrieved for duloxetine in this evidence pack. The evidence pack records **0 Drug Identification Numbers (DINs)** with a market status of "not found." This almost certainly represents a **data collection gap** rather than a true absence from the Canadian market: duloxetine (brand name Cymbalta, and multiple generics) is known to be an approved and commercially available medication in Canada. Manual verification via Health Canada's **Drug Product Database (DPD)** is strongly recommended before drawing any regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack and should be retrieved from the official Health Canada product monograph or the full DrugBank record (DB00476).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 4 clinical trial (NCT00464698) and a double-blind, placebo-controlled RCT (PMID 27811556) directly evaluate duloxetine in OCD, supported by over 20 publications spanning meta-analyses, open-label studies, and case series. Duloxetine's SNRI mechanism is pharmacologically coherent with OCD pathophysiology, and its existing approval for GAD confirms its clinical activity across the anxiety spectrum — substantially narrowing the mechanistic evidence gap for this repurposing hypothesis.

**To proceed, the following is needed:**

- **Regulatory data**: Verify Canada market status and retrieve all DINs via the Health Canada Drug Product Database; obtain the current Canadian product monograph
- **Safety assessment**: Extract key warnings, contraindications, and clinically significant drug interactions from the product monograph (currently a blocking data gap)
- **Mechanism of action**: Retrieve complete MOA data from DrugBank (DB00476) to formally complete the mechanistic rationale
- **Efficacy deep-dive**: Obtain full results from NCT00464698 (Phase 4 trial); contact investigators if results are unpublished
- **Comparative analysis**: Commission a systematic review or network meta-analysis comparing duloxetine vs. SSRIs in OCD to quantify relative efficacy and clarify where duloxetine adds value (e.g., SSRI-resistant subgroup)
- **Patient population definition**: Define target subpopulation — treatment-resistant OCD, OCD with comorbid depression/pain, or first-line candidates — to frame the regulatory and clinical development pathway
- **Dose optimisation**: Evaluate supratherapeutic dosing data (case reports suggest doses above standard range may be needed for full antiobsessional effect) and design a formal dose-finding component if proceeding to a prospective study

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

