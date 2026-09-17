---
layout: default
title: Tiotropium
parent: High Evidence (L1-L2)
nav_order: 776
evidence_level: L1
indication_count: 10
---

# Tiotropium
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Tiotropium: From Established COPD Bronchodilator to Obstructive Lung Disease

## One-Sentence Summary

> Tiotropium is a long-acting muscarinic antagonist (LAMA) whose literature record shows it is already an established maintenance bronchodilator for chronic obstructive pulmonary disease (COPD).
> The TxGNN model's top-ranked prediction — **Obstructive Lung Disease** — largely reconfirms this established use rather than identifying a novel indication,
> with **49 clinical trials** and **20 publications** currently associated with this evidence pack (including landmark trials such as TIOSPIR, n=17,183, and DYNAGITO, n=7,903).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Canadian regulatory data (data gap — drug not currently listed as marketed in this dataset); literature evidence consistently documents tiotropium as an established LAMA maintenance therapy for COPD |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, the structured mechanism-of-action field is a data gap (DG002). However, the literature evidence collected in this pack independently and consistently describes tiotropium's pharmacology: it is a long-acting antimuscarinic bronchodilator that binds muscarinic M1, M2, and M3 receptors, dissociating slowly from M1/M3 (located in bronchial smooth muscle) to produce a prolonged, once-daily bronchodilator effect (e.g., PMID 12010082, PMID 10069510, PMID 11281822).

The predicted new indication, "Obstructive Lung Disease," and the drug's well-documented established use are essentially the same disease category — the TxGNN model has, in effect, rediscovered tiotropium's own class-defining indication with very high confidence (99.99%). This is not a case of pharmacological repositioning into an unrelated disease, but a confirmation signal: the mechanism (M3-receptor antagonism → bronchodilation, reduced mucus secretion) maps directly onto the pathophysiology of obstructive airway disease. This is corroborated by the volume and quality of supporting evidence, including a 17,183-patient Phase 3 trial (TIOSPIR, NCT01126437) and Cochrane systematic reviews (PMID 25046211, PMID 26391969).

Because this is a confirmatory rather than exploratory signal, the primary open question for this jurisdiction is not efficacy — it is regulatory and safety documentation: tiotropium has no recorded Canadian market authorization in this dataset (0 DINs), and TFDA-equivalent (Health Canada) product monograph warnings/contraindications data are missing (DG001, flagged as Blocking).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01126437](https://clinicaltrials.gov/study/NCT01126437) | Phase 3 | Completed | 17,183 | TIOSPIR — large comparative safety/efficacy trial of tiotropium Respimat vs. HandiHaler formulations in COPD |
| [NCT00975195](https://clinicaltrials.gov/study/NCT00975195) | Phase 4 | Completed | 2,488 | Large RCT evaluating stepwise ICS withdrawal on top of optimized bronchodilator (incl. tiotropium) therapy in severe/very severe COPD |
| [NCT02296138](https://clinicaltrials.gov/study/NCT02296138) | Phase 3 | Completed | 7,903 | DYNAGITO — 52-week trial of tiotropium + olodaterol vs. tiotropium alone on COPD exacerbations |
| [NCT00528996](https://clinicaltrials.gov/study/NCT00528996) | Phase 2 | Completed | 2,080 | Multinational dose-comparison trial using tiotropium 5 µg as active control in COPD |
| [NCT00620516](https://clinicaltrials.gov/study/NCT00620516) | N/A | Completed | 3,008 | Korean post-marketing surveillance of Spiriva HandiHaler 18 mcg in COPD patients |
| [NCT02347072](https://clinicaltrials.gov/study/NCT02347072) | Phase 3 | Completed | 80 | Crossover study evaluating 24-hour lung function profile of tiotropium vs. placebo in moderate-to-very-severe COPD |
| [NCT00274521](https://clinicaltrials.gov/study/NCT00274521) | Phase 3 | Completed | 108 | Placebo-controlled 25-week trial of tiotropium's effect on exercise tolerance following pulmonary rehabilitation in COPD |
| [NCT01388166](https://clinicaltrials.gov/study/NCT01388166) | N/A | Completed | 1,253 | ADESPI — real-world adherence study of Spiriva maintenance therapy in COPD |
| [NCT02276222](https://clinicaltrials.gov/study/NCT02276222) | Phase 3 | Completed | 1,087 | GOLDEN-5 — 48-week long-term safety trial comparing nebulized therapy to Spiriva 18 mcg in COPD |
| [NCT03265145](https://clinicaltrials.gov/study/NCT03265145) | Phase 4 | Completed | 714 | Pragmatic community trial comparing Stiolto Respimat vs. ICS-LABA+LAMA triple therapy on exacerbation timing |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic review of tiotropium vs. placebo for stable COPD across multiple trials |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respiratory Research | Review of tiotropium's clinical development program and its role as LAMA monotherapy per GOLD recommendations |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Review (Cochrane) | Cochrane Database Syst Rev | Systematic comparison of tiotropium vs. ipratropium bromide for COPD |
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | New England Journal of Medicine | Long-term tiotropium use improves lung function and slows decline in mild/moderate early-stage COPD |
| [29605624](https://pubmed.ncbi.nlm.nih.gov/29605624/) | 2018 | RCT | Lancet Respiratory Medicine | DYNAGITO trial publication: tiotropium+olodaterol vs. tiotropium alone in COPD exacerbation prevention |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Review | Life Sciences | Mechanistic and clinical profile of tiotropium (Spiriva) in obstructive lung disease |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review | Current Medical Research and Opinion | Review of tiotropium+olodaterol fixed-dose combination for managing COPD exacerbations |
| [35510163](https://pubmed.ncbi.nlm.nih.gov/35510163/) | 2022 | Cohort | International Journal of COPD | Taiwan multicenter cohort comparing tiotropium/olodaterol vs. other LABA/LAMA combinations |
| [19402836](https://pubmed.ncbi.nlm.nih.gov/19402836/) | 2009 | Meta-analysis | Respirology | Meta-analysis of tiotropium efficacy and safety in Chinese patients with stable COPD |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Review | Drugs | Pharmacological review of tiotropium bromide as an anticholinergic bronchodilator for COPD |

---

## Canada Market Information

Currently no licensed products found in the Canadian regulatory dataset (0 DINs recorded; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Key warnings, contraindications, and drug–drug interaction data are recorded as data gaps in this evidence pack (DG001 — TFDA/Health Canada label warnings and contraindications, flagged as Blocking; DDI query returned no results).*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1) — a 17,183-patient Phase 3 trial (TIOSPIR), a 7,903-patient Phase 3 trial (DYNAGITO), and two Cochrane systematic reviews all support tiotropium's efficacy in obstructive airway disease. However, this signal largely confirms an already-established indication rather than revealing a novel one, and the drug currently has no recorded Canadian market authorization, with safety-label data (DG001) marked as a Blocking gap.

**To proceed, the following is needed:**
- Health Canada product monograph: warnings, contraindications, and precautions (resolves DG001, currently blocking safety pre-screening/S1)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (resolves DG002)
- Verification of current Canadian market/licensing status, since this dataset shows 0 DINs despite tiotropium being a globally established respiratory therapy
- Drug-drug interaction data, as the current DDI query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

