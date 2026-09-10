---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Partial-Onset Epilepsy to Visual Epilepsy

## One-Sentence Summary

Levetiracetam is a second-generation antiepileptic drug used as adjunctive therapy for partial-onset seizures in patients with epilepsy. The TxGNN model predicts it may also be effective for **Visual Epilepsy** (a photosensitive/reflex epilepsy subtype), with **9 clinical trials** and **20 publications** currently identified in relation to this prediction — though most evidence addresses epilepsy and seizure disorders broadly rather than the visual/photosensitive subtype specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — adjunctive treatment of partial-onset seizures (regulatory label text unavailable; derived from trial-level evidence, e.g., NCT00203216: "levetiracetam is FDA approved as an add-on medication in the treatment of partial onset seizures in adults with epilepsy") |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available from DrugBank for this evidence pack (data gap). Based on information embedded in the trial evidence, Levetiracetam is a broad-spectrum antiepileptic drug (brand name Keppra) approved as adjunctive treatment for partial-onset seizures, with a well-characterized pharmacological action of binding synaptic vesicle protein 2A (SV2A) to modulate neurotransmitter release and reduce cortical hyperexcitability.

Visual epilepsy (photosensitive/reflex epilepsy) is generally classified as a reflex subtype of idiopathic generalized epilepsy (IGE), in which cortical hyperexcitability is triggered by visual stimuli (e.g., flickering light). Because IGE and its reflex subtypes share the same underlying pathophysiology of abnormal cortical excitability that Levetiracetam already targets in its approved indication, the TxGNN prediction has a plausible mechanistic basis.

According to the repurposing rationale associated with this candidate: *"Visually-induced (photosensitive) epilepsy belongs to the reflex subtype of idiopathic generalized epilepsy (IGE); its seizure mechanism relates to cortical hyperexcitability. Levetiracetam reduces cortical excitability via SV2A-mediated modulation of synaptic vesicle release, and has established efficacy in IGE/myoclonic seizures, so the mechanism can be reasonably extrapolated."* This is further supported indirectly by the drug's established role in generalized/myoclonic seizure control (see literature evidence below).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | LICEO observational study assessing new AEDs (including levetiracetam) as first-choice bitherapy in focal epilepsy under real-world conditions. |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | 19-week RCT evaluating cognitive/neuropsychological effects of adjunctive levetiracetam in children 4–16 with refractory partial-onset seizures; graded most directly relevant to photosensitive/photoparoxysmal response safety and efficacy. |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | Tested whether levetiracetam reduces hippocampal hyperactivity using visual scene-processing fMRI tasks in psychosis; terminated early. |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | Follow-up study on levetiracetam's effect on hippocampal hyperactivity (visual scene-processing fMRI) in patients with psychotic disorders. |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not yet recruiting | 580 | RCT of prophylactic levetiracetam for functional outcome improvement in acute intracerebral haemorrhage. |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not yet recruiting | 1649 | MAST trial defining optimal AED (levetiracetam vs. phenytoin) duration/choice for seizure prevention post-traumatic brain injury. |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Evaluated levetiracetam efficacy in controlling neonatal seizures versus traditional phenobarbital. |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A (open-label) | Completed | 31 | Open-label trial of levetiracetam for prophylactic treatment of migraine with/without visual aura. |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by invitation | 24 | Gene therapy study in Canavan disease; levetiracetam not the primary intervention, low direct relevance. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review/Meta-analysis | Epilepsy & Behavior | Levetiracetam compared with other ASMs for myoclonic seizures in idiopathic generalized epilepsy (including JME) — the IGE category most closely related to reflex/photosensitive epilepsy. |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Review (network meta-analysis) | Journal of Neurology | Compared efficacy/safety of antiseizure medications, including levetiracetam, for idiopathic generalized epilepsies. |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Randomized controlled trial: levetiracetam vs. phenobarbital for neonatal seizures — demonstrated efficacy and favorable safety profile. |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3) | The Lancet. Neurology | PEACH trial: randomised, double-blind, placebo-controlled Phase 3 trial of prophylactic levetiracetam for seizure prevention in acute intracerebral haemorrhage. |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT (open-label) | Seizure | Compared phenytoin and levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome. |
| [30487494](https://pubmed.ncbi.nlm.nih.gov/30487494/) | 2018 | RCT | Mymensingh Medical Journal | Randomized controlled trial comparing phenobarbital and levetiracetam in childhood epilepsy. |
| [36209676](https://pubmed.ncbi.nlm.nih.gov/36209676/) | 2022 | Systematic Review/Network Meta-analysis | Seizure | Reviewed treatments, including levetiracetam, for benzodiazepine-resistant status epilepticus. |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arquivos de Neuro-Psiquiatria | Reviewed diagnosis, monitoring, and treatment of status epilepticus, including levetiracetam's mechanistic role. |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review/Meta-analysis | Neurocritical Care | Evaluated levetiracetam's efficacy, dosing, and adverse events for seizure prophylaxis in neurocritical care populations. |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Overview of levetiracetam's established efficacy across partial-onset seizures, myoclonic seizures, and generalized tonic-clonic seizures in IGE. |

---

## Canada Market Information

Levetiracetam is currently **not marketed** in Canada per this evidence pack — no Drug Identification Numbers (DINs) or licensed products were found (`total_licenses: 0`). No Health Canada authorization or approved-indication text is available to reference for this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information. (No warnings, contraindications, or drug-interaction data were available in this evidence pack; a Health Canada label review is flagged as a blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Levetiracetam's established action in IGE/myoclonic seizures and the reflex/photosensitive pathophysiology of visual epilepsy is plausible, and one Phase 2 RCT (NCT00105040) is directly relevant to photosensitive/photoparoxysmal response safety and efficacy — supporting an L2 evidence level. However, no trial or publication in this pack directly studies levetiracetam in a visual-epilepsy-diagnosed population, so evidence remains indirect.

**To proceed, the following is needed:**
- Confirmed detailed mechanism-of-action documentation (DrugBank API data gap)
- Health Canada product label / warnings and contraindications (currently unavailable — blocking gap for safety pre-assessment)
- A trial or registry study specifically enrolling patients with photosensitive/visual epilepsy (rather than general partial-onset or generalized epilepsy)
- Confirmation of Canadian market/regulatory pathway, since the drug currently holds no DIN in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

