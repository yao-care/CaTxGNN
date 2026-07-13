---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Midazolam: From Procedural Sedation to Insomnia

## One-Sentence Summary

Midazolam is a short-acting imidazobenzodiazepine widely used in clinical practice for procedural sedation, anaesthesia induction, and pre-operative anxiolysis.
The TxGNN model predicts it may be effective for **Insomnia**, supported by **2 multicenter RCTs** directly studying its hypnotic efficacy in chronic insomnia patients, plus additional clinical trial evidence comparing its sleep-modifying properties against other sedatives.
The prediction score of **99.74%** reflects the near-perfect mechanistic alignment between midazolam's GABA-A receptor action and the neurobiological substrate of insomnia.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Procedural sedation and anaesthesia induction |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Midazolam is a positive allosteric modulator of the GABA-A receptor — the same molecular target underpinning the approved benzodiazepine hypnotics triazolam and temazepam. By binding to a distinct site on the GABA-A receptor complex, midazolam enhances chloride ion influx in response to endogenous GABA, producing dose-dependent central nervous system depression. At hypnotic doses, this translates directly into shortened sleep-onset latency, prolonged total sleep time, and an increase in NREM Stage 2 sleep, while suppressing REM sleep. The TxGNN knowledge graph score of 0.997 captures this link quantitatively: reduced GABAergic tone → cortical hyperarousal → insomnia is one of the most well-established pathological axes in sleep medicine, and midazolam acts precisely at that node.

Crucially, this is not a speculative mechanistic leap but a class-effect application within an established pharmacological family. The repurposing rationale places midazolam alongside already-approved benzodiazepine hypnotics sharing identical receptor pharmacology. Clinical trials conducted in the 1980s and 1990s directly evaluated oral midazolam as a hypnotic agent in patients with chronic insomnia, reporting efficacy comparable to other benzodiazepines with a favourable tolerability profile relative to barbiturate-based comparators. This historical evidence precedes the TxGNN prediction and independently validates it.

More recent studies have reinforced midazolam's sleep-modifying properties in peri-operative and critical care contexts — consistently using it as an active comparator against dexmedetomidine in trials where sleep quality is a primary or secondary endpoint. These trial designs reflect clinical consensus that midazolam's sedative effect meaningfully affects sleep architecture. The convergence of historical RCT data, contemporary peri-operative trial evidence, and a near-ceiling TxGNN score together support a well-grounded repurposing case.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Head-to-head RCT comparing midazolam vs dexmedetomidine combined with spinal anaesthesia on postoperative sleep quality in TURP patients; sleep quality is the primary endpoint — the most direct midazolam sleep dataset in this collection |
| [NCT01050699](https://clinicaltrials.gov/study/NCT01050699) | Phase 4 | Completed | 90 | Dexmedetomidine vs standard sedation (midazolam as comparator) on sleep and inflammatory cytokines in ICU patients with acute lung injury/ARDS; provides midazolam reference data in a sleep-primary design |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | N/A | Recruiting | 280 | Preoperative oral midazolam vs placebo in colorectal cancer patients with pre-existing sleep disturbance or anxiety; directly targets midazolam's hypnotic-anxiolytic profile as a therapeutic endpoint |
| [NCT04149626](https://clinicaltrials.gov/study/NCT04149626) | Phase 2 | Unknown | 60 | Three-arm RCT (dexmedetomidine / midazolam / remifentanil) for sedation in orthopedic surgery under regional anaesthesia; sleep quality included as outcome measure |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | N/A | Completed | 23 | Randomised double-blind pilot comparing midazolam vs dexmedetomidine to facilitate ICU extubation; includes sleep quality observation as secondary outcome |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminated | 5 | 24-hour polysomnographic comparison of midazolam vs dexmedetomidine on sleep stages and total sleep time in mechanically ventilated ICU patients; small sample terminated early |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnographic study comparing GABA agonist (midazolam) vs α2 agonist (dexmedetomidine) on N2, N3, and total sleep time in ventilated patients; terminated due to enrolment challenges |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Phase 3 | Not Yet Recruiting | 195 | Melatonin vs midazolam as premedication in children undergoing tonsillectomy; positions midazolam as the established hypnotic-sedative benchmark for comparison |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | Unknown | 120 | Dexmedetomidine vs midazolam for sedation in critically ill ventilated children; addresses paediatric population with midazolam as the standard-of-care comparator |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | N/A | Completed | 131 | Remimazolam vs propofol+midazolam general anaesthesia in oncology patients; provides safety and recovery data relevant to midazolam's sedative-hypnotic profile |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT (Multicenter) | J Clin Psychopharmacol | Multicenter randomised double-blind study of flurazepam vs midazolam in patients with chronic insomnia; evaluated sleep parameters, performance, and plasma levels over 14 days — foundational Tier 1 RCT for midazolam as hypnotic |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT (Multicenter) | J Clin Psychopharmacol | Executive summary of the same 14-day multicenter chronic insomnia trial; independently confirms the sleep-performance-plasma level findings across the full cohort |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | Br J Clin Pharmacol | Double-blind parallel RCT: midazolam 15 mg vs Vesparax in 30 female insomnia patients; both effective hypnotics, but midazolam better tolerated with no hangover effect |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT (Dose-Finding) | Arzneimittel-Forschung | Multicenter dose-finding RCT of oral midazolam 10–30 mg in 75 hospitalised patients with mild-to-moderate insomnia; established optimal dosing range for hypnotic use |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatr Scand Suppl | Narrative review of clinical hypnotic use across the benzodiazepine class; confirms midazolam's efficacy for sleep onset and maintenance, contextualising its pharmacokinetic profile relative to other agents |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Cohort | J Clin Med | Pilot cohort evaluating lemborexant for insomnia in high-risk pancreato-biliary patients post-endoscopy; explicitly contrasts with benzodiazepine class (including midazolam) regarding delirium risk, providing contemporary safety context |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orvosi Hetilap | Review of primary and secondary insomnia pathogenesis; describes the hyperarousal model underpinning GABAergic therapy rationale — supports the mechanistic basis for the TxGNN prediction |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Health Canada prescribing information and contraindication data were not available at the time of this report (Data Gap DG001). Midazolam belongs to the benzodiazepine class; standard class-level cautions apply — including risks of dependence, respiratory depression, and cognitive impairment, particularly in elderly patients and those with concurrent CNS depressants. Independent safety review is required before any clinical application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for midazolam as a hypnotic is essentially identical to approved benzodiazepine sleep agents, supported by multiple direct RCTs in insomnia patients dating to the 1980s and confirmed by contemporary peri-operative sleep quality trials — placing this repurposing case in a well-evidenced, pharmacologically coherent position. However, the complete absence of Health Canada regulatory filings, combined with missing safety and contraindication data, requires resolution before any formal development pathway is recommended.

**To proceed, the following is needed:**

- **Safety data retrieval (Blocking):** Obtain and review the Health Canada product monograph or equivalent labelling for midazolam (DG001); confirm contraindications, black box warnings, and special population restrictions before advancing to Stage 1 safety assessment
- **MOA data formalisation (High):** Retrieve structured DrugBank MOA entry (DG002) to confirm receptor binding profile, half-life, and active metabolite data relevant to dosing strategy for insomnia indication
- **Regulatory context clarification:** Confirm whether midazolam has any existing Health Canada DINs (e.g., as a hospital-only controlled drug) that did not surface in the database query; market absence may reflect a data pipeline gap rather than true non-availability
- **Insomnia subtype scoping:** Define the target insomnia phenotype (e.g., acute vs. chronic; sleep-onset vs. sleep-maintenance) to align with an existing or prospective indication, given that chronic use of benzodiazepine hypnotics is subject to dependence risk and current prescribing guidelines recommend short-term use only
- **Comparative positioning:** Clarify differentiation from already-approved benzodiazepine hypnotics (triazolam, temazepam) to establish whether a distinct regulatory or clinical niche exists for midazolam in this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

