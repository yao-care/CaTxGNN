---
layout: default
title: Nitrazepam
parent: High Evidence (L1-L2)
nav_order: 651
evidence_level: L2
indication_count: 3
---

# Nitrazepam
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **3** 
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

# Nitrazepam: From a Marketed Benzodiazepine Hypnotic to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Nitrazepam is a long-established benzodiazepine sleep medicine, sold in Canada as Mogadon, although the license records list no approved indication.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, with **0 registered clinical trials** and **20 publications** currently supporting this direction.
This looks like the model recovering a known use rather than discovering a new one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records (established use as a hypnotic) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Nitrazepam belongs to the benzodiazepine class, which enhances GABA-A receptor inhibition and produces sedative-hypnotic effects. That effect matches difficulty falling and staying asleep.

The original indication field is empty, so this is probably a data gap rather than true repurposing. Nitrazepam has been used as a hypnotic for decades, and the very high TxGNN score most likely reflects that known drug–disease link in the knowledge graph.

Two lower-ranked predictions have much weaker support:
- **Acute encephalopathy with biphasic seizures and late reduced diffusion** (score 99.59%): GABA-A enhancement could plausibly help control seizures. However, there is no trial or literature evidence, and benzodiazepines are not known to alter the delayed injury process. Sedation may also confound neurological assessment.
- **Wernicke-Korsakoff syndrome** (score 99.31%): the link likely comes from benzodiazepine use in alcohol withdrawal. Nitrazepam does not treat the underlying thiamine deficiency and may worsen confusion or mask encephalopathy signs.

Both are evidence level L5 (model prediction only) and are treated as hypothesis-level.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT | Acta Psychiatr Scand | Double-blind crossover in 26 geriatric inpatients: nitrazepam 5 mg and triazolam 0.25 mg gave similar sleep quantity, quality and psychomotor performance |
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | Other (double-blind trial) | Br Med J | Nitrazepam was as effective as butobarbitone as a hypnotic; acute overdose in 27 patients caused no untoward effects except drowsiness |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | Review | Clin Pharmacokinet | Review of nitrazepam pharmacokinetics |
| [238826](https://pubmed.ncbi.nlm.nih.gov/238826/) | 1975 | Review | Drugs | Hypnotic drugs assessed against the physiology of REM and non-REM sleep |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clin Evid | Insomnia in the elderly: up to 40% of adults affected, prevalence rising with age |
| [10804040](https://pubmed.ncbi.nlm.nih.gov/10804040/) | 2000 | Review | Drugs | Zolpidem's hypnotic efficacy is generally comparable to benzodiazepines including nitrazepam |
| [3281819](https://pubmed.ncbi.nlm.nih.gov/3281819/) | 1988 | Review | Drugs | Brotizolam improved sleep similarly to nitrazepam 2.5 and 5 mg |
| [15089115](https://pubmed.ncbi.nlm.nih.gov/15089115/) | 2004 | Review | CNS Drugs | Residual "hangover" effects of hypnotics and related accident risk |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | Case report | Br J Psychiatry | Nitrazepam (Mogadon) dependence |
| [32724021](https://pubmed.ncbi.nlm.nih.gov/32724021/) | 2020 | Review | Med Lett Drugs Ther | Lemborexant, an orexin antagonist, as a newer insomnia option |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 511536 | MOGADON |
| 511528 | MOGADON |

---

## Safety Considerations

No package insert warnings, contraindications or drug interaction data are available in the Evidence Pack. Please refer to the package insert for safety information.

The published literature raises these points:
- **Dependence and withdrawal**: reported with nitrazepam use (PMID 1125532).
- **Next-day sedation**: the long half-life can cause residual daytime impairment and accident risk (PMID 15089115).
- **Elderly patients**: falls and cognitive risk are a particular concern, so use should be short-term only.
- **Alternatives**: newer agents such as orexin antagonists exist (PMID 32724021).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (sleep disorder, initiating and maintaining sleep). The other two predicted indications are **Hold**.

**Rationale:**
The hypnotic use is supported by a published double-blind RCT, comparative trials and decades of clinical experience. However, the evidence is old and small, and there are no registered trials. The apparent "repurposing" is largely a known use, and the dependence, residual sedation and elderly-safety concerns require strict guardrails. The encephalopathy and Wernicke-Korsakoff predictions rest on knowledge-graph inference alone.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the approved indication, dosage form and manufacturer for both Mogadon licenses
- A short-term-use and elderly-patient safety plan, with comparison against newer hypnotics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

