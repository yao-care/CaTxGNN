---
layout: default
title: Butalbital
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 8
---

# Butalbital
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Butalbital: From Tension Headache to Visual Epilepsy

## One-Sentence Summary

Butalbital is a short- to intermediate-acting barbiturate, best known as a component of combination analgesic products (e.g., Fioricet: butalbital + acetaminophen + caffeine) used for tension-type headaches and migraines.
The TxGNN model predicts it may be effective for **Visual Epilepsy**, with **0 clinical trials** and **5 publications** identified — though critically, none of these publications directly support this therapeutic use.
The mechanistic rationale is theoretically plausible at the class level but is undermined by a key safety paradox: butalbital withdrawal itself can trigger seizures.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tension headache / migraine (combination analgesic component; no formal Taiwan regulatory record) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed |
| Number of Product Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Butalbital belongs to the barbiturate class, which acts by enhancing GABAergic inhibition: barbiturates prolong the opening of GABA-A receptor chloride ion channels, suppressing neuronal excitability and raising the seizure threshold. This mechanism is the foundation of phenobarbital's established use as an antiepileptic drug, and it provides the theoretical basis for TxGNN's prediction that butalbital could suppress the cortical hyperexcitability underlying visual epilepsy.

Visual epilepsy is a form of reflex epilepsy in which seizures are triggered by specific visual stimuli — flickering lights, geometric patterns, or high-contrast images. The primary lesion involves abnormal excitability in the occipital cortex. In principle, broad GABAergic enhancement could dampen this hyperexcitability. However, butalbital's relatively short half-life (approximately 35 hours) makes it ill-suited for maintaining the stable therapeutic plasma concentrations required for continuous anticonvulsant protection — unlike long-acting phenobarbital, for which this class effect is clinically validated.

The most important concern is a direct safety contradiction: all retrieved literature on butalbital and seizures describes seizures as a **consequence of butalbital withdrawal** in headache patients, not as a condition suppressed by butalbital therapy. Multiple case reports document grand mal seizures emerging after barbiturate discontinuation. This paradox — the drug's withdrawal triggers the very event it might theoretically prevent — constitutes a fundamental mechanistic red flag for its anticonvulsant repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [8742687](https://pubmed.ncbi.nlm.nih.gov/8742687/) | 1996 | Case Series | Headache | Three migraineurs on butalbital (Fioricet) developed grand mal seizures and behavioural disturbance upon withdrawal; highlights high barbiturate dependence risk in this population |
| [10349206](https://pubmed.ncbi.nlm.nih.gov/10349206/) | 1998 | Case Report | Annali italiani di medicina interna | Barbiturate withdrawal from a headache analgesic caused seizures, psychosis, and risk of circulatory failure; confirms withdrawal syndrome severity |
| [10431323](https://pubmed.ncbi.nlm.nih.gov/10431323/) | 1999 | Case Report | Schweizerische medizinische Wochenschrift | Intractable vomiting, convulsions, and megaloblastic anaemia traced to misuse of a barbiturate-containing combination analgesic; diagnosis delayed by lack of medication history |
| [15262744](https://pubmed.ncbi.nlm.nih.gov/15262744/) | 2004 | Case Report | Archives of Neurology | Severe barbiturate withdrawal syndrome after internet purchase of Fioricet without medical supervision; neurological consequences documented |
| [26565790](https://pubmed.ncbi.nlm.nih.gov/26565790/) | 2015 | Retrospective Case Series | Therapeutic Drug Monitoring | Therapeutic drug monitoring of **pentobarbital** for intractable seizures; indirect class-level data only — not specific to butalbital or visual epilepsy |

> **Important caveat:** None of the retrieved publications describe butalbital being used to *treat* visual epilepsy. All seizure-related literature pertains to barbiturate withdrawal as a cause of seizures. The evidence does not support efficacy in this indication.

---

## Taiwan Market Information

Butalbital is **not currently approved or marketed in Taiwan**. No product licenses are on record in the Taiwan regulatory database.

---

## Safety Considerations

No formal package insert warnings or contraindications data were retrieved for this evaluation. Based on barbiturate class properties and the retrieved literature, the following concerns are material:

- **Dependence and withdrawal risk**: Multiple case reports confirm physical dependence develops with sustained use; abrupt discontinuation can trigger grand mal seizures, psychosis, hyperthermia, and circulatory failure — paradoxically the opposite of the proposed anticonvulsant effect.
- **CNS and respiratory depression**: Dose-dependent sedation and respiratory suppression are inherent barbiturate risks; narrow therapeutic index increases overdose danger.
- **Medication overuse headache**: Chronic use in headache patients is associated with rebound headache and escalating consumption patterns.

Please refer to the package insert and authoritative pharmacological references for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model identifies a plausible class-level mechanistic link (GABA-A enhancement → raised seizure threshold), but there are no clinical trials and no supportive literature for butalbital in visual epilepsy; crucially, all available evidence points to butalbital withdrawal as a *cause* of seizures, which represents a direct safety contradiction to the proposed therapeutic application.

**To proceed, the following is needed:**

- Retrieve complete MOA data from DrugBank (DG002) to confirm pharmacokinetic parameters relevant to sustained anticonvulsant dosing (e.g., half-life, CNS penetration)
- Obtain Taiwan package insert or international prescribing information for full warnings and contraindications (DG001)
- Conduct a systematic evidence review for **phenobarbital** (the long-acting barbiturate comparator) in reflex epilepsy subtypes to determine whether class-level evidence is transferable
- Formally assess whether the seizure-triggering withdrawal profile of butalbital is a disqualifying safety contraindication for any anticonvulsant repurposing pathway
- Consult a clinical epileptologist to evaluate whether visual epilepsy management guidelines leave a clinical gap that a GABAergic agent could feasibly fill, and whether butalbital's pharmacokinetic profile could ever be made suitable (e.g., extended-release formulation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

