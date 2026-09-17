---
layout: default
title: Phenytoin
parent: Moderate Evidence (L3-L4)
nav_order: 618
evidence_level: L3
indication_count: 10
---

# Phenytoin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Phenytoin: From Epilepsy to Trigeminal Neuralgia

> **Note on methodology:** This evidence pack contains 10 TxGNN-predicted indications for phenytoin. The single highest-scoring candidate ("trigeminal nerve neoplasm," score 99.99%) is explicitly flagged in the pack's own rationale as a likely **TxGNN disease-entity confusion / false positive** — its literature actually discusses trigeminal *neuralgia* and Sturge-Weber syndrome, not neoplasm, and no clinical trials support it. Seven other top-ranked candidates (startle epilepsy, micturition-induced seizures, audiogenic seizures, thinking seizures, orgasm-induced seizures, eating seizures, reading seizures, beta-ketothiolase deficiency) are rare reflex-epilepsy phenomena or metabolic conditions with no or only animal-model evidence (L4–L5, all scored "Hold"). This report instead features **trigeminal neuralgia** (rank 9, score 99.97%), the only candidate in the pack with real clinical and observational evidence (L3, "Proceed with Guardrails") — the more clinically meaningful signal in this evidence set.

## One-Sentence Summary

Phenytoin is a long-established antiepileptic drug used for seizure disorders. Within this evidence pack, the TxGNN model's most credible new-indication signal points to **Trigeminal Neuralgia**, with **1 dedicated clinical study** and **19 related publications** — including a European neurology guideline and multi-institution cohort data — supporting the use of intravenous phenytoin for acute pain crises.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (well-established clinical use; not captured as structured data in this evidence pack — see Safety/Data Gap note below) |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.97% (rank 1119 of predictions) |
| Evidence Level | L3 |
| Canada Market Status | Not marketed (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not provided as structured input for this evidence pack (flagged as data gap DG002). Based on the mechanistic reasoning captured for this candidate: phenytoin is a **voltage-gated sodium channel blocker**, which suppresses abnormal high-frequency neuronal firing. This is the same core mechanism as carbamazepine and oxcarbazepine, the guideline-recommended first-line drugs for trigeminal neuralgia (TN).

Trigeminal neuralgia is a paroxysmal facial pain syndrome driven by aberrant, high-frequency discharge in the trigeminal nerve — pharmacologically analogous to epileptic discharge, which is why sodium-channel-blocking anticonvulsants are the mainstay of TN treatment. Because first-line oral agents (carbamazepine, oxcarbazepine) cannot be used during severe pain exacerbations when patients become dehydrated or anorectic, intravenous phenytoin has an established off-label niche as **acute rescue therapy** during TN crises, bridging patients back onto oral prophylaxis. This clinical practice pattern, documented in multiple retrospective cohorts, is the practical basis for the TxGNN association.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03712254](https://clinicaltrials.gov/study/NCT03712254) | N/A | Completed | 15 | Prospective systematic study of IV phenytoin for acute exacerbations of trigeminal neuralgia; addresses the treatment gap when oral first-line agents cannot be used during severe flares. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | European Academy of Neurology consensus guideline on TN diagnosis and management. |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Cohort | Cephalalgia | Retrospective analysis of 144 cases using IV lacosamide and phenytoin for acute TN exacerbations. |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Cohort/Case series | Headache | Retrospective cohort on IV phenytoin as acute rescue treatment for TN crisis. |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Retrospective comparison | Journal of Pain Research | Compares phenytoin and carbamazepine in TN: marketing-based vs. evidence-based treatment patterns. |
| [39993829](https://pubmed.ncbi.nlm.nih.gov/39993829/) | 2024 | Clinical review | Clinical Medicine & Research | In-hospital management approaches for acute TN pain crises. |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Pathophysiology-to-pharmacology overview of TN, including sodium-channel-targeted therapies. |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian Journal of Neurosurgery | General overview of TN diagnosis, mechanisms, and treatment options. |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | Review | BMJ Clinical Evidence | Evidence-based summary of TN treatment options. |
| [38421578](https://pubmed.ncbi.nlm.nih.gov/38421578/) | 2024 | Review | CNS Drugs | Pharmacological approaches to neuropathic pain in multiple sclerosis, including TN. |
| [15062534](https://pubmed.ncbi.nlm.nih.gov/15062534/) | 2004 | Review | Neurologic Clinics | Clinical review of TN and glossopharyngeal neuralgia management. |

## Canada Market Information

Phenytoin currently has **no active Health Canada drug identification numbers (DINs) recorded in this evidence pack** — market status is "Not marketed" (Not marketed), with 0 total licenses. No product/dosage-form table can be generated from this data.

## Safety Considerations

Please refer to the package insert for safety information.

**Outstanding data gap (Blocking):** TFDA/Health Canada label warnings, contraindications, and DDI data were not available in this evidence pack (DG001), which blocks a formal S1 safety review. This must be resolved before clinical guardrails can be defined.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Among the 10 TxGNN-predicted indications in this pack, trigeminal neuralgia is the only one backed by a dedicated clinical study, multiple retrospective cohorts, and a specialty guideline — reflecting an existing, real-world off-label practice pattern (IV phenytoin as acute TN rescue therapy) rather than a novel, unvalidated hypothesis. The evidence level (L3) supports cautious clinical use pending formal safety review.

**To proceed, the following is needed:**
- Retrieve TFDA/Health Canada label warnings and contraindications (DG001, Blocking) to complete S1 safety assessment
- Obtain formal DrugBank mechanism-of-action data (DG002) to fully document the sodium-channel rationale
- Clarify and discard the top-ranked TxGNN candidate ("trigeminal nerve neoplasm") as a likely entity-confusion artifact before this candidate set is used for any automated downstream decisioning
- Confirm route/dosage compatibility for IV administration in the acute-crisis use case (route_compatibility data currently marked "pending" in this pack)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

