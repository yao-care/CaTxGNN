---
layout: default
title: Phenobarbital
parent: Model Prediction Only (L5)
nav_order: 728
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Phenobarbital: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (including generalized tonic-clonic and partial epilepsy)…"
monitor_inn: "PHENOBARBITAL"
predicted_indications: ["trigeminal nerve neoplasm", "micturation-induced seizures", "eating seizures", "orgasm-induced seizures", "startle epilepsy", "thinking seizures", "audiogenic seizures", "reading seizures", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenobarbital
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Phenobarbital: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenobarbital is an established anticonvulsant, originally used for epilepsy (including generalized tonic-clonic and partial seizures), and for migraine and cluster headache-type conditions.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but there are **0 clinical trials** and only **1 publication** (a Sturge-Weber syndrome case series that does not address this condition), so this prediction is not supported by real evidence.
The more credible repurposing directions are reflex-type seizure disorders (for example micturition-induced, eating, startle, audiogenic and reading seizures) and trigeminal neuralgia, which are mechanistically close to phenobarbital's existing use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (including generalized tonic-clonic and partial epilepsy), migraine, Lennox-Gastaut syndrome |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

*Note: Health Canada indication text was not available in the data compiled for this report, so the original indication is taken from the knowledge-graph indication list.*

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. From general pharmacology, phenobarbital is a barbiturate anticonvulsant that enhances GABA-A receptor-mediated inhibition. This is the basis of its use in epilepsy.

**For trigeminal nerve neoplasm (the top-ranked prediction):** the prediction is not mechanistically credible. Phenobarbital has no known antineoplastic or tumour-directed effect. The high score most likely reflects proximity in the knowledge graph to seizure and neurological phenotypes rather than a real biological link. The only retrieved paper is about Sturge-Weber syndrome and does not concern this tumour.

**For other predictions in the list:**
- **Reflex and stimulus-triggered seizures** (micturition-induced, eating, startle, thinking, audiogenic, reading, and orgasm-induced seizures) are seizure disorders. A GABAergic anticonvulsant could plausibly help, but the evidence is indirect. It comes from general seizure literature, case reports, and animal models, and nothing shows phenobarbital efficacy in these specific syndromes.
- **Trigeminal neuralgia** is treated with anticonvulsants, with carbamazepine as first line. Phenobarbital has been discussed historically, but one mechanistic study found it tended to depress, rather than facilitate, the inhibition that effective trigeminal neuralgia drugs enhance.
- **Beta-ketothiolase deficiency** is a metabolic disorder with no plausible link to phenobarbital and no supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction (trigeminal nerve neoplasm). No clinical trials were found for any of the other nine predicted indications either.

---

## Literature Evidence

For trigeminal nerve neoplasm, a single paper was retrieved, and it is not about the predicted condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases, covering clinical features, course and treatment response; does not address trigeminal nerve neoplasm |

For context, the most relevant evidence among the lower-ranked predictions (these are not for the top-ranked indication):

| PMID | Year | Type | Journal | Indication | Key Findings |
|------|-----|------|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Seizures (neonatal) | Levetiracetam compared with phenobarbital for neonatal seizures; general seizure evidence, not micturition-induced seizures |
| [37873971](https://pubmed.ncbi.nlm.nih.gov/37873971/) | 2023 | Systematic review | Cochrane Database Syst Rev | Seizures (neonatal) | Anti-seizure medication choices in neonates |
| [37655702](https://pubmed.ncbi.nlm.nih.gov/37655702/) | 2023 | Guideline | Epilepsia | Seizures (neonatal) | ILAE consensus recommendations for neonatal seizure treatment |
| [26690830](https://pubmed.ncbi.nlm.nih.gov/26690830/) | 2017 | Veterinary RCT | J Feline Med Surg | Audiogenic seizures | Levetiracetam compared with phenobarbital in cats with audiogenic reflex seizures |
| [11129121](https://pubmed.ncbi.nlm.nih.gov/11129121/) | 2000 | Review | Drugs | Trigeminal neuralgia | Anticonvulsants for neuropathic pain: mechanisms and place in therapy |
| [6264347](https://pubmed.ncbi.nlm.nih.gov/6264347/) | 1981 | Mechanism study | Neurology | Trigeminal neuralgia | Phenobarbital tended to depress segmental inhibition, unlike carbamazepine, baclofen and phenytoin |
| [24726506](https://pubmed.ncbi.nlm.nih.gov/24726506/) | 2014 | Case report | Seizure | Eating seizures | 50-year follow-up of a case of neonatal eating epilepsy |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02304090 | Phenobarbital Sodium Injection, USP | Not specified | Not specified |
| 00645575 | Phenobarb Elixir | Not specified | Not specified |
| 02304082 | Phenobarbital Sodium Injection, USP | Not specified | Not specified |
| 00178799 | Phenobarb | Not specified | Not specified |
| 00178810 | Phenobarb | Not specified | Not specified |

Seven valid single-ingredient licences are listed in total; the five above are shown.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these are drug-disease associations in the model's knowledge graph, not label text). Main items:
- Liver failure and liver disease
- Kidney disease
- Porphyria (including inherited porphyria)
- Chronic obstructive pulmonary disease
- Hypothyroidism
- Thrombocytopenia
- Systemic lupus erythematosus
- Psychotic and other mental disorders
- Peptic ulcer disease and gastritis
- Hypertension and hyperglycaemia

**Drug interactions:** 100 interactions were identified. Those rated **Major** include:
- Morphine (including liposomal morphine)
- Eliglustat
- Naldemedine
- Naloxegol
- Rolapitant

Many **Moderate** interactions were also found, including:
- Corticosteroids (dexamethasone, hydrocortisone, prednisone, prednisolone, betamethasone, triamcinolone)
- Doxycycline
- Metronidazole
- Bupropion
- Aprepitant
- Pioglitazone

**Additional safety signals from the literature:**
- Brief neonatal exposure to phenobarbital impaired learning and sensorimotor gating in rats.
- Early exposure was associated with later audiogenic seizures and neuronal deficits in mice.
- A follow-up of children given phenobarbital for febrile seizures reported lowered IQ.
- Phenobarbital induces liver enzymes (CYP) and can lower levels of co-administered drugs such as carbamazepine.

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, trigeminal nerve neoplasm, has no clinical trials, no relevant literature, and no plausible antineoplastic mechanism. The score appears to reflect graph proximity to seizure phenotypes rather than a real effect. The evidence level is L5 (model prediction only).
- The reflex seizure predictions (micturition-induced, eating, startle, thinking, audiogenic and reading seizures) and trigeminal neuralgia are better framed as research questions (L4). They rest on indirect evidence and would extend an existing anticonvulsant use rather than open a new therapeutic area.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Approved indication text, dosage form and manufacturer for the Canadian licences
- Re-ranking of the candidates so that reflex seizure syndromes and trigeminal neuralgia are prioritized over trigeminal nerve neoplasm
- A targeted literature review for phenobarbital in reflex epilepsies and trigeminal neuralgia, including comparison against first-line agents
- A safety plan covering CYP-mediated interactions (particularly with opioids and carbamazepine) and neurodevelopmental risks in young patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

