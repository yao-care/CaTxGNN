---
layout: default
title: Atropine
parent: Model Prediction Only (L5)
nav_order: 82
evidence_level: L5
indication_count: 2
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Atropine: From Muscarinic Antagonist Therapy to Migraine Disorder

## One-Sentence Summary

Atropine is a non-selective muscarinic (anticholinergic) antagonist that is marketed in Canada in injectable and ophthalmic products.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 registered clinical trials** and **13 publications**, all preclinical, observational, review or unrelated case reports, with no human efficacy data for atropine in migraine.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atropine blocks muscarinic acetylcholine receptors. Preclinical work links parasympathetic and cholinergic signalling to migraine biology:
- Stimulating the parasympathetic sphenopalatine ganglion in rats causes plasma protein extravasation in the dura mater.
- Cholinergic modulation acts on meningeal mast cells in neurogenic inflammation.
- Nicotinic and CGRP pathways influence cranial vascular tone.
- A 1986 study in chronic paroxysmal hemicrania (a different headache disorder) reported that systemic atropine markedly reduced attack-related sweating, tearing and nasal secretion, which points to autonomic involvement in headache.

Together these findings support a plausible anticholinergic mechanism. None of them shows that atropine reduces migraine frequency or severity in humans. The very high TxGNN score is a computational prediction and does not replace clinical data.

Detailed mechanism of action data and the original approved indications are not available in the current data. The mechanistic reasoning above therefore rests on atropine's known pharmacology and on the published preclinical literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No RCTs were found. The table lists the most relevant items, ordered by study type. Unrelated case reports (topiramate adverse effects, botulinum toxin, stunned myocardium) and a 1977 paper without an abstract were excluded.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Anisodamine, an atropine derivative, is a non-specific cholinergic antagonist, less potent and less toxic than atropine. This is a pharmacology overview and not migraine data. |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Clinical observation | Cephalalgia | In 4 patients with chronic paroxysmal hemicrania, systemic atropine reduced attack-related sweating, tearing and nasal secretion, indicating autonomic involvement. This is not a migraine study. |
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preclinical | Eur J Neurosci | In a rat nitroglycerin migraine model, cholinergic modulation and a mast cell stabiliser affected neurogenic inflammation, implicating meningeal mast cells. |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preclinical | Exp Neurol | Stimulating the parasympathetic sphenopalatine ganglion caused plasma protein extravasation in rat dura mater, supporting a neurogenic inflammation mechanism. |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | Preclinical | Neurosci Lett | CGRP and nicotinic receptors are involved in centrally evoked facial blood flow changes. |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Preclinical | Br J Pharmacol | Studied nicotine-evoked relaxation of the guinea-pig basilar artery and its inhibition by drugs linked to migraine (atropine was present as a background agent). |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Not classified | J Pharmacol Exp Ther | The central cholinergic system contributes to the antinociception induced by sumatriptan in rodents. |
| [31945385](https://pubmed.ncbi.nlm.nih.gov/31945385/) | 2020 | Preclinical | Neuropharmacology | In mouse neocortex, cholinergic activation of muscarinic receptors inhibits cortical spreading depression, the presumed substrate of migraine aura. See the note on the second prediction below. |

---

## Canada Market Information

Five of the 11 authorisations are shown. Dosage form and approved indication text are not available for these records.

| DIN | Product Name |
|---------|------|
| 02148358 | MINIMS ATROPINE SULPHATE |
| 00392693 | ATROPINE SULFATE INJECTION USP |
| 00328154 | ATROPINE SULFATE INJECTION USP |
| 02432196 | ATROPINE INJECTION BP |
| 02432188 | ATROPINE INJECTION BP |

---

## Safety Considerations

No structured warning, contraindication or drug interaction data is available for this candidate, and the interaction query returned no records. Please refer to the Health Canada package insert for safety information.

Atropine's anticholinergic adverse effects would need weighing in any future migraine study. They include dry mouth, tachycardia, blurred vision and raised intraocular pressure.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and indirect preclinical mechanistic links. There are no clinical trials and no human data showing atropine benefits migraine. Safety information from the Canadian package insert has also not yet been reviewed, which blocks any safety screening.

**Second prediction (migraine with brainstem aura):** This is also on Hold at evidence level L5. Its only supporting paper is a single mouse study in which muscarinic activation *suppresses* cortical spreading depression. A muscarinic antagonist such as atropine could therefore plausibly remove that inhibition and worsen aura susceptibility. The direction of effect must be clarified before this indication is considered.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications for the marketed atropine products
- Approved indications and dosage forms for each DIN
- Mechanism of action data from DrugBank
- Human data, such as clinical observations or trials of anticholinergic therapy in migraine
- Clarification of the effect direction of muscarinic antagonism on cortical spreading depression and aura
- Assessment of route and formulation compatibility for a migraine use, since the marketed products are injectable and ophthalmic

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

