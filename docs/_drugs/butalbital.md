---
layout: default
title: Butalbital
parent: Moderate Evidence (L3-L4)
nav_order: 137
evidence_level: L4
indication_count: 8
---

# Butalbital
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

# Butalbital: From Headache Combination Analgesic to Visual Epilepsy

## One-Sentence Summary

Butalbital is a barbiturate marketed in Canada mainly as a component of combination analgesic products (for example Fiorinal and Teva-Tecnal), which the literature links to headache treatment.
The TxGNN model predicts it may be effective for **visual epilepsy**, but there are **0 clinical trials** and only **5 publications** (case reports, case series and one drug-monitoring study), none of which tests butalbital as a seizure treatment.
The literature instead shows that stopping butalbital abruptly can cause seizures.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this record. Butalbital is a barbiturate, and barbiturates as a class enhance GABA-A receptor activity, which suppresses neuronal firing. Phenobarbital is a well-known example of a barbiturate used against seizures, so a class-level anticonvulsant effect is plausible for butalbital.

The original use (headache) and the predicted use (a reflex epilepsy triggered by visual stimuli) are different conditions, and the only link between them is this shared GABAergic pharmacology. The very high TxGNN score most likely reflects that seizure and GABA neighborhood in the knowledge graph. It does not reflect direct evidence that butalbital works in visual epilepsy.

The same model also ranks seven other reflex or stimulus-triggered seizure types with scores of 99.06% to 99.15%: micturition-induced, thinking, audiogenic, eating, startle, orgasm-induced and reading seizures. Two of them (micturition-induced seizures and visual epilepsy) have some retrieved literature, all of it about withdrawal seizures. The other six have no trials or publications, so they are supported by model prediction alone (L5). The consistent scores across this cluster suggest a shared class-level signal rather than indication-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26565790](https://pubmed.ncbi.nlm.nih.gov/26565790/) | 2015 | Retrospective cohort | Ther Drug Monit | Therapeutic drug monitoring of **pentobarbital** (not butalbital), used for intractable seizures and raised intracranial pressure |
| [15262744](https://pubmed.ncbi.nlm.nih.gov/15262744/) | 2004 | Case report | Arch Neurol | Barbiturate withdrawal after unsupervised Internet purchase of Fioricet |
| [8742687](https://pubmed.ncbi.nlm.nih.gov/8742687/) | 1996 | Case series | Headache | Three migraine patients dependent on butalbital had grand mal seizures and behavioral disorder during withdrawal |
| [10349206](https://pubmed.ncbi.nlm.nih.gov/10349206/) | 1998 | Case report | Ann Ital Med Int | Barbiturate withdrawal (anxiety, tremor, seizures, psychosis) linked to abuse of a headache medication |
| [10431323](https://pubmed.ncbi.nlm.nih.gov/10431323/) | 1999 | Case report | Schweiz Med Wochenschr | Intractable vomiting, convulsions and megaloblastic anemia in a 43-year-old woman, where the medication history was the key to diagnosis |
| [34790421](https://pubmed.ncbi.nlm.nih.gov/34790421/) | 2021 | Case report | Case Rep Psychiatry | Severe Fioricet withdrawal presenting as new-onset psychosis in an inpatient psychiatric unit |

**Note:** The first five papers were retrieved for visual epilepsy and five for micturition-induced seizures, with the pentobarbital study and four case reports appearing in both sets. PMID 34790421 was retrieved only for micturition-induced seizures. None reports butalbital efficacy in any epilepsy. Their consistent finding is that butalbital dependence and withdrawal can provoke seizures.

---

## Canada Market Information

Showing 5 of 11 authorizations. Dosage form and approved indication text are not available in the current records.

| DIN | Product Name |
|---------|------|
| 1971409 | TRIANAL TABLET |
| 608238 | TEVA-TECNAL |
| 2554690 | APO-BUTALBITAL-ACETYLSALICYLIC ACID-CAFFEINE |
| 608211 | TEVA-TECNAL |
| 226327 | FIORINAL |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

The retrieved literature raises these signals:
- **Dependence and tolerance:** butalbital-containing products can cause physical and psychological dependence.
- **Withdrawal seizures:** abrupt discontinuation can provoke grand mal seizures, psychosis and behavioral changes, typically within days of stopping. This is directly relevant to any use in a seizure disorder.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score and class-level GABAergic pharmacology only. There are no clinical trials, and the available literature shows butalbital causing seizures on withdrawal rather than treating them. The dependence liability argues against repurposing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence that butalbital reduces seizures in visual epilepsy or other reflex epilepsies
- A dependence and withdrawal risk assessment for chronic use in a seizure population
- A comparison against established anticonvulsants, including phenobarbital
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

