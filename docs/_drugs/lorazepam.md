---
layout: default
title: Lorazepam
parent: Model Prediction Only (L5)
nav_order: 554
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: From Anxiety Treatment to Insomnia

## One-Sentence Summary

Lorazepam is a benzodiazepine sedative-anxiolytic. The Health Canada licence records supplied here contain no indication text. The TxGNN model predicts it may be effective for **insomnia**, the best-supported of its top-10 predictions. Evidence for insomnia comes from **23 registered trials** (only a few directly relevant) and **18 retrieved publications**, including two lorazepam-specific insomnia studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records. Anxiety is used here based on general benzodiazepine pharmacology and the retrieved literature |
| Predicted New Indication | Insomnia (rank 2, best-supported). The rank 1 prediction, trigeminal nerve neoplasm, has no supporting evidence (see below) |
| TxGNN Prediction Score | 99.80% (insomnia); 99.87% (trigeminal nerve neoplasm) |
| Evidence Level | L2 (insomnia) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 19 |
| Recommended Decision | Proceed with Guardrails (insomnia) |

**Note on rank 1:** The top-scoring prediction, *trigeminal nerve neoplasm*, has no trials and no literature. There is also no plausible antineoplastic mechanism for lorazepam. It is most likely a knowledge-graph artifact and should be treated as a false-positive candidate (L5, Hold). This report therefore focuses on insomnia.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known benzodiazepine pharmacology, lorazepam is a positive allosteric modulator of GABA-A receptors. Enhancing this inhibitory signalling produces sedative-hypnotic, anxiolytic, and anticonvulsant effects.

Anxiety and insomnia commonly overlap. Sedation is the same pharmacological effect that underlies both uses, so the mechanistic link to insomnia is direct. Two published clinical studies support this: a double-blind crossover trial of lorazepam vs flurazepam in chronic insomniacs (1988), and a study of lorazepam TID for chronic insomnia (1999).

Current guidance favours short-term use only, because benzodiazepine hypnotic effects diminish after a few weeks and the risks accumulate.

**Other predictions in the top 10:**
- Six seizure-type predictions (reading, audiogenic, startle, thinking, micturition-induced and eating seizures) are plausible only through general GABA-A anticonvulsant pharmacology. Evidence is indirect and none has trials. Five are L4 research questions; eating seizures is L4 Hold because its retrieved literature is off-target.
- Orgasm-induced seizures and acute encephalopathy with biphasic seizures and late reduced diffusion have no evidence (L5, Hold).

## Clinical Trial Evidence

Of the 23 trials retrieved for insomnia, the most relevant are listed below. Several are combination-product trials or deprescribing studies, not direct efficacy tests of lorazepam alone.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03331042](https://clinicaltrials.gov/study/NCT03331042) | Phase 3 | Completed | 85 | 4-way crossover of SM-1 (diphenhydramine + zolpidem + lorazepam) vs two comparators and placebo in a transient insomnia model. Lorazepam's role (test drug or comparator) needs arm-level verification |
| [NCT04396327](https://clinicaltrials.gov/study/NCT04396327) | Phase 2 | Not yet recruiting (listed) | 14 | 2-way crossover of SM-1 vs a diphenhydramine + lorazepam comparator in a 3-hour phase-advance model. No results; registry dates are from 2020 |
| [NCT02671760](https://clinicaltrials.gov/study/NCT02671760) | Phase 2 | Completed | 39 | SM-1 vs comparator and placebo on total sleep time in short-term insomnia |
| [NCT03338764](https://clinicaltrials.gov/study/NCT03338764) | Phase 3 | Withdrawn | 0 | Home-use SM-1 vs placebo in adults with a history of transient insomnia. Never enrolled |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1400 | Taiwanese prospective cohort on hypnotic risk and benefit in the elderly. Observational safety context |
| [NCT06584513](https://clinicaltrials.gov/study/NCT06584513) | N/A | Recruiting | 470 | BE-SAFE: intervention to reduce benzodiazepine and sedative-hypnotic use in older adults (deprescribing, not efficacy) |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Self-management intervention for benzodiazepine cessation in veterans |
| [NCT02135198](https://clinicaltrials.gov/study/NCT02135198) | Phase 1 | Completed | 12 | Crossover biomarker study of the GABA modulator AZD7325 in healthy volunteers. Early-phase pharmacodynamic context only |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnography in ventilated patients sedated with α2 agonists vs GABA agonists. Different population |
| [NCT04109118](https://clinicaltrials.gov/study/NCT04109118) | Phase 2 | Completed | 4 | Benzodiazepine discontinuation in opioid agonist therapy. Off-target for efficacy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | RCT | J Clin Pharmacol | Double-blind crossover (n=8) of lorazepam 2 mg vs flurazepam 30 mg over 3 weeks in chronic insomniacs. Lorazepam performed better on most sleep parameters |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Clinical study | Int Clin Psychopharmacol | Compared lorazepam 0.5 mg TID (24-hour) with 1.5 mg at bedtime in primary insomnia |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Review | J Multidiscip Healthc | Efficacy, safety and drug interactions of insomnia therapies in COVID-19 patients |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | Med Lett Drugs Ther | Overview of drugs for chronic insomnia |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharm | Tranquilizers in elderly patients with chronic non-communicable diseases: dose, outcomes, adverse effects |
| [19514972](https://pubmed.ncbi.nlm.nih.gov/19514972/) | 2009 | Preclinical | Drug Deliv | Intranasal microemulsions of diazepam, lorazepam and alprazolam in a rat sleep-induction model |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Cohort | Sleep Med | Hypnotic prescription patterns in a large managed-care population |
| [25453732](https://pubmed.ncbi.nlm.nih.gov/25453732/) | 2014 | Observational | Clin Ther | Benzodiazepine and sedative-hypnotic use among older seriously ill veterans, framed against the Choosing Wisely caution |
| [40110386](https://pubmed.ncbi.nlm.nih.gov/40110386/) | 2025 | Observational | Alpha Psychiatry | Trends in benzodiazepine and Z-drug prescriptions in Eastern China, 2015-2021 |
| [15040803](https://pubmed.ncbi.nlm.nih.gov/15040803/) | 2004 | Observational | Health Qual Life Outcomes | Sleep quality and sedating-drug use in hospitalized adults |

## Canada Market Information

The licence records list 19 authorizations; five main ones are shown. Dosage form, manufacturer and approved indication text are blank in the records provided.

| DIN / Licence No. | Product Name |
|---------|------|
| 2410761 | LORAZEPAM SUBLINGUAL |
| 711101 | TEVA-LORAZEPAM |
| 655678 | PRO-LORAZEPAM |
| 2410753 | LORAZEPAM SUBLINGUAL |
| 655767 | APO-LORAZEPAM |

## Safety Considerations

- **Guardrails for insomnia use:** dependence, tolerance, next-day impairment, and falls and cognitive risk in the elderly. Current guidance favours short-term use only.
- **Drug interactions:** the interaction query returned no entries.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (insomnia)

**Rationale:**
The GABA-A mechanism is a direct fit for sleep induction. Published lorazepam-specific studies exist, including a small double-blind crossover RCT, and the drug is widely marketed in Canada. The evidence is not strong enough for L1. The larger Phase 3 and 2 trials involve a combination product, and lorazepam's role in them is unconfirmed. The other nine predictions should not advance: the six seizure-type predictions with weak indirect evidence are research questions (eating seizures is on Hold), and rank 1, orgasm-induced seizures and the encephalopathy prediction are Hold with no supporting evidence.

**To proceed, the following is needed:**
- Verify the arms of NCT03331042 and NCT04396327 (whether lorazepam is the test drug or a comparator) and check for posted results
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- A short-duration, elderly-specific risk plan (dependence, falls, cognition)
- Route and formulation compatibility assessment (currently pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

