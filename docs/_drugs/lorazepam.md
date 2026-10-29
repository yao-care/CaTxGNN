---
layout: default
title: Lorazepam
parent: Model Prediction Only (L5)
nav_order: 559
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "LORAZEPAM"
predicted_indications: ["trigeminal nerve neoplasm"]
description: "Lorazepam: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Lorazepam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Lorazepam: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Lorazepam is a benzodiazepine originally used for anxiety disorders and seizure conditions such as status epilepticus, absence epilepsy and Lennox-Gastaut syndrome.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.
Among the other top predictions, only insomnia has a meaningful body of literature (16 publications, mostly reviews and older small studies).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 17 of 19) |
| Number of DINs | 19 (valid: 17) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacology, lorazepam is a positive allosteric modulator of the GABA-A receptor. It produces anxiolytic, sedative and anticonvulsant effects.

For the top-ranked prediction, **trigeminal nerve neoplasm**, no identifiable mechanistic link exists to lorazepam's original indications. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Lorazepam has no known antitumor activity. Any use would be limited to symptomatic supportive care, such as managing anxiety or seizures, and would not modify the disease.

Other high-ranking predictions are more plausible mechanistically, mainly because they overlap with lorazepam's existing indications:

- **Reflex seizure types (reading, audiogenic, startle, thinking, micturition-induced, orgasm-induced and eating seizures)**: Enhancing GABA-A activity is a rational mechanism for seizure suppression, and these conditions resemble lorazepam's established epilepsy indications. The supporting evidence is thin, indirect or based on animal withdrawal studies.
- **Acute encephalopathy with biphasic seizures and late reduced diffusion**: Benzodiazepines are used for acute seizure control as symptomatic care, but lorazepam would not be expected to alter the underlying course of the disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal nerve neoplasm. No clinical trials were found for any of the other top-10 predicted indications either.

---

## Literature Evidence

Currently no related literature available for trigeminal nerve neoplasm.

For reference, the most relevant publications for the next-ranked indication, **insomnia**:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Clinical study | Int Clin Psychopharmacol | Compared lorazepam 0.5 mg three times daily with 1.5 mg at bedtime in patients with primary chronic insomnia |
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | Comparative crossover study | J Clin Pharmacol | Double-blind study in 8 chronic insomniacs: 2 mg lorazepam performed better than 30 mg flurazepam on most sleep parameters |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Med Lett Drugs Ther | Overview of drugs for chronic insomnia |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharm | Tranquilizer therapy in elderly patients with chronic non-communicable diseases: dose, outcomes and adverse effects |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs |
| [19514972](https://pubmed.ncbi.nlm.nih.gov/19514972/) | 2009 | Preclinical | Drug Deliv | Intranasal microemulsions of diazepam, lorazepam and alprazolam tested for sleep induction in rats |

---

## Canada Market Information

Lorazepam has 19 valid single-ingredient authorizations in Canada. Dosage form and approved-indication text were not available in the data compiled for this report.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02041464 | ATIVAN | Not available | Not available |
| 02041456 | ATIVAN | Not available | Not available |
| 02410761 | LORAZEPAM SUBLINGUAL | Not available | Not available |
| 02550962 | LORAZEPAM INJECTION, USP | Not available | Not available |
| 02243278 | LORAZEPAM INJECTION USP | Not available | Not available |

Other marketed brands include TEVA-LORAZEPAM, PRO-LORAZEPAM, APO-LORAZEPAM and PMS-LORAZEPAM.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

**Contraindication signals from the knowledge graph** (not label text) include:
- Liver disease, liver failure, hepatic encephalopathy and hepatic coma
- Kidney disease
- Respiratory conditions: respiratory failure, obstructive sleep apnea, sleep apnea syndrome, congenital central hypoventilation syndrome
- Open-angle and angle-closure glaucoma
- Porphyria (inherited porphyria and porphyrin metabolism disease)
- Substance-related disorder, substance abuse/dependence
- Gallbladder disease, pyoureter, neurotic disorder, dysthymic disorder

**Drug interactions** (100 interactions recorded; the main ones are listed):
- **Major**: Morphine, liposomal morphine (additive central nervous system and respiratory depression is the typical concern with opioids)
- **Moderate**: Bupropion, dronabinol, nabilone, teduglutide, metoclopramide, opium, sibutramine
- **Minor**: Antacids such as magnesium oxide, magnesium hydroxide, magnesium carbonate, aluminum hydroxide, calcium carbonate and magaldrate

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, trigeminal nerve neoplasm, has only a model score behind it: no trials, no literature, and no plausible antitumour mechanism. Lorazepam could at most provide symptomatic support. The more credible predictions (insomnia and reflex seizure types) largely reflect existing or off-label benzodiazepine use rather than new repurposing opportunities, and long-term use carries known dependence and cognitive risks.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Any preclinical or clinical evidence linking lorazepam to trigeminal nerve neoplasm, or a decision to re-focus on a better-supported indication
- For insomnia, a risk-benefit review against current guidance on long-term benzodiazepine use
- Indication text and dosage forms for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

