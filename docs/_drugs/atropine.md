---
layout: default
title: Atropine
parent: Model Prediction Only (L5)
nav_order: 82
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Atropine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not specified in the data compiled for this report"
monitor_inn: "Atropine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Atropine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Atropine: From Its Approved Uses to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Atropine is a non-selective muscarinic acetylcholine receptor antagonist that is currently marketed in Canada in multiple injectable and other single-ingredient products.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 registered clinical trials** and only **preclinical or indirect literature** supporting this direction.
This is a computational prediction only and does not yet amount to clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the data compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atropine blocks muscarinic acetylcholine receptors, so it reduces signalling through the parasympathetic (cholinergic) system. The data compiled for this report did not include a detailed mechanism-of-action entry, but this class action is well established.

Several preclinical studies link cholinergic signalling to migraine biology:

- **Neurogenic inflammation:** a 2024 rat study found that meningeal mast cell-mediated cholinergic modulation contributes to neurogenic inflammation in a migraine model (PMID 36485173).
- **Parasympathetic activation:** stimulating the parasympathetic sphenopalatine ganglion caused plasma protein leakage in rat dura mater (PMID 9344563).
- **Pain pathways:** the central cholinergic system was involved in antinociception by the antimigraine drug sumatriptan in rodents (PMID 8930196).
- **Autonomic involvement in headache:** in chronic paroxysmal hemicrania, systemic atropine markedly reduced attack-related sweating, tearing and nasal secretion (PMID 2943405). This is a different headache disorder, and it shows an effect on autonomic features rather than on pain.

Together these findings make it plausible that muscarinic blockade could modulate trigeminovascular and parasympathetic pathways. However, no direct evidence of atropine efficacy in migraine in humans was identified.

**A second prediction, migraine with brainstem aura (score 99.42%, Evidence Level L5), is less convincing.** A mouse study showed that muscarinic activation *inhibits* cortical spreading depression, the presumed basis of migraine aura (PMID 31945385). If so, a muscarinic antagonist like atropine could plausibly worsen or fail to reduce susceptibility, so the mechanistic direction is uncertain or possibly contradictory.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the papers below tests atropine for migraine in patients. Several are only loosely related, such as adverse-event reports for other drugs.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Pharmacology of anisodamine, a naturally occurring atropine derivative and non-specific cholinergic antagonist, which is less potent and less toxic than atropine |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Clinical observation | Cephalalgia | In four chronic paroxysmal hemicrania patients, systemic atropine markedly reduced attack-related sweating, tearing and nasal secretion |
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preclinical/Mechanistic | Eur J Neurosci | Meningeal mast cell-mediated cholinergic modulation of neurogenic inflammation in a rat migraine model |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preclinical (animal) | Exp Neurol | Parasympathetic sphenopalatine ganglion stimulation induced plasma protein extravasation in rat dura mater |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Preclinical (animal) | J Pharmacol Exp Ther | Central cholinergic system contributes to sumatriptan-induced antinociception in rodents |
| [31945385](https://pubmed.ncbi.nlm.nih.gov/31945385/) | 2020 | Preclinical (animal) | Neuropharmacology | Cholinergic activation of muscarinic receptors inhibited cortical spreading depression in mouse neocortex (relevant to the brainstem aura prediction) |
| [1786517](https://pubmed.ncbi.nlm.nih.gov/1786517/) | 1991 | Preclinical | Br J Pharmacol | Ergotamine and dihydroergotamine are potent 5-HT1C agonists in piglet choroid plexus (indirect migraine pharmacology) |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Preclinical (in vitro) | Br J Pharmacol | Analgesic drugs and progesterone inhibited nicotine-evoked relaxation of guinea-pig basilar artery |
| [40590589](https://pubmed.ncbi.nlm.nih.gov/40590589/) | 2024 | Case report | Pain Med Case Rep | Botulinum treatment induced dropped head syndrome in a patient with chronic migraine and multiple sclerosis |
| [18091300](https://pubmed.ncbi.nlm.nih.gov/18091300/) | 2007 | Case report | Optom Vis Sci | Elevated intraocular pressure and myopic shift linked to topiramate use |

---

## Canada Market Information

Eleven valid single-ingredient licences are on record. The data compiled for this report did not include dosage forms or approved indication text, so those columns are left blank.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02148358 | MINIMS ATROPINE SULPHATE | Not available | Not available |
| 00392693 | ATROPINE SULFATE INJECTION USP | Not available | Not available |
| 00328154 | ATROPINE SULFATE INJECTION USP | Not available | Not available |
| 02432196 | ATROPINE INJECTION BP | Not available | Not available |
| 02432188 | ATROPINE INJECTION BP | Not available | Not available |

---

## Safety Considerations

**Drug Interactions:** The interaction screen returned 100 interacting drugs. Most of those listed are Moderate, and a few are Minor. The main ones are:

- **Additive anticholinergic effects:** aclidinium, hyoscyamine, chlorpheniramine, acrivastine, phenyltoloxamine, amitriptyline and amantadine.
- **Opioids and CNS depressants:** fentanyl, alfentanil, codeine, dihydrocodeine, tramadol and ethanol.
- **Cholinergic agents (opposing effect):** acetylcholine and galantamine.
- **Others:** botulinum toxin type A, acebutolol and loperamide (Moderate); acetaminophen and hydrochlorothiazide (Minor).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is a computational prediction only. The supporting evidence is preclinical or indirect, there are no registered trials, and no human efficacy data exist for atropine in migraine. For the brainstem aura prediction, the mechanistic direction may even be contradictory.

**To proceed, the following is needed:**
- Label warnings and contraindications from the Health Canada package inserts (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian licences
- Detailed mechanism-of-action data and a clearer account of whether muscarinic blockade would help or harm in migraine
- Direct clinical evidence, such as a pilot or proof-of-concept study, with a review of the route and dose needed for migraine, since the current products are mainly injectable or ophthalmic
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

