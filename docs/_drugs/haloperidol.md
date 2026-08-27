---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Haloperidol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using the standard repurposing-evaluation format below. Note upfront: this Evidence Pack contains **10** TxGNN-predicted indications for haloperidol, but 9 of them (congenital disorder of glycosylation, retinal dystrophy, hydranencephaly, X‑linked myopia variants, CMT1G, polymicrogyria, atypical glycine encephalopathy) are rank-1–9 by raw TxGNN score yet carry **no supporting evidence and explicit "no biological plausibility" rationale**, scored L5/Hold. Only rank 10 — **manic bipolar affective disorder** — has real clinical trial and literature support (L1, Proceed with Guardrails). As the reviewer, I am reporting on that one actionable candidate and noting the others were screened out, rather than mechanically reporting on the top TxGNN-score (but evidence-free) hit.

---

# Haloperidol: From Psychotic Disorders to Manic Episodes in Bipolar Affective Disorder

## One-Sentence Summary

Haloperidol is a first-generation (typical) antipsychotic historically used to treat schizophrenia and other psychotic disorders via central dopamine D2 receptor antagonism (this evidence pack's formal `original_indications`/`original_moa` fields are a data gap, but the mechanism is well documented in the supporting literature below). Among 10 TxGNN-predicted indications screened, only **manic bipolar affective disorder** clears initial evidence review, supported by **9 clinical trials** and **20 publications**, with haloperidol repeatedly used as an active comparator/add-on in Phase 2–3 RCTs of antimanic therapy. The other 9 TxGNN predictions (rare congenital/structural/metabolic disorders) were rejected at screening (Hold) for lack of any mechanistic plausibility or supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia / acute psychotic disorders (well-established use; formal indication text is a data gap in this pack) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism-of-action data (DrugBank MOA field) is not available in this evidence pack — this is flagged as a High-severity data gap (DG002). However, the clinical trial and literature evidence collected for this candidate consistently describes haloperidol as a typical (first-generation) antipsychotic whose principal pharmacological action is central dopamine D2 receptor antagonism.

Acute mania is pathophysiologically associated with mesolimbic dopaminergic hyperactivity. D2 receptor blockade is a well-established strategy for rapidly controlling the core symptoms of mania — psychomotor agitation, racing thoughts, and irritability — and this mechanism is shared with other antipsychotics already approved for bipolar mania (risperidone, olanzapine, aripiprazole). Critically, the trial evidence below does not show haloperidol being *tested* for mania as a novel target — it shows haloperidol already serving as the **active comparator** in the pivotal registration trials of those newer antipsychotics, meaning its antimanic efficacy is long-established in clinical practice rather than a genuinely new discovery. The repurposing rationale in this pack explicitly flags this: it recommends verifying at the source whether haloperidol's local product label already includes acute mania/agitation control, since in most jurisdictions it likely does.

Of the remaining 9 TxGNN-predicted candidates in this evidence pack (rare congenital glycosylation disorders, retinal dystrophies, hydranencephaly, X-linked myopia variants, Charcot-Marie-Tooth disease type 1G, polymicrogyria, atypical glycine encephalopathy), none have any supporting clinical trial or literature evidence, and each rationale explicitly states there is no biological plausibility connecting D2 antagonism to these structural/genetic/metabolic conditions — in some cases (myopia, CMT1G) the mechanistic direction is arguably unfavorable. These were correctly scored L5/Hold and are not carried further in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Placebo- and haloperidol-controlled trial confirming olanzapine efficacy in manic/mixed bipolar I episodes; haloperidol as active comparator (Grade A relevance) |
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Risperidone vs. placebo vs. haloperidol in manic episodes of bipolar I disorder, including 12-week maintenance comparison vs. haloperidol (Grade A) |
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Risperidone add-on to mood stabilizers vs. placebo vs. haloperidol in mania, establishing haloperidol's role as add-on comparator (Grade A) |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | Completed | 615 | Aripiprazole monotherapy vs. placebo in acute mania; antipsychotic-class context supporting antimanic mechanism (Grade B) |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | Completed | 22 | Long-acting injectable antipsychotic + adherence program for chronic psychotic disorders in Tanzania; small sample, haloperidol's role needs confirmation (Grade B) |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Open-label valproate-amisulpride vs. valproate-haloperidol in bipolar I manic episode (Grade C) |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | Terminated | 11 | Olanzapine vs. conventional antipsychotics (incl. haloperidol) in acute mania; terminated for under-recruitment (Grade C) |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Unknown | 120 | Micronutrient/fish oil adjunct in bipolar disorder; no direct haloperidol mechanism link (Grade C) |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | Recruiting | 200 | Observational study of antenatal antipsychotic exposure and maternal/infant outcomes; not an efficacy trial (Grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | Journal of Affective Disorders | Randomized, double-blind, placebo- and haloperidol-controlled trial of olanzapine in Japanese patients with manic/mixed bipolar I episode |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | RCT | Archives of General Psychiatry | Double-blind controlled trial of lithium + haloperidol vs. placebo + haloperidol in excited schizoaffective disorder |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | RCT | The Journal of Clinical Psychiatry | Double-blind controlled comparison of clonazepam vs. lithium vs. haloperidol in acute mania |
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Systematic Review / Network Meta-analysis | Molecular Psychiatry | Network meta-analysis of double-blind RCTs for acute bipolar mania across antipsychotics including haloperidol |
| [10343182](https://pubmed.ncbi.nlm.nih.gov/10343182/) | 1999 | Clinical Study | Neuropsychobiology | Lithium and haloperidol treatments differentially affect leukocyte G-protein signaling in bipolar affective disorder |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatrica Scandinavica | Evidence-based treatment recommendations for acute mania, including antipsychotic mood-stabilizer combinations |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Review | BMJ Mental Health | Comparison of antipsychotic dose equivalents between acute mania and schizophrenia |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Review | CNS Neuroscience & Therapeutics | Refractory bipolar disorder treatment strategies; recommends adding haloperidol/other antipsychotics for partial responders |
| [19454110](https://pubmed.ncbi.nlm.nih.gov/19454110/) | 2007 | Review | BMJ Clinical Evidence | General overview of bipolar disorder management, mood swings between depression and mania |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Systematic Review | Journal of Clinical Psychopharmacology | Extrapyramidal side effects of antipsychotics (including haloperidol) in bipolar disorder vs. schizophrenia |

---

## Canada Market Information

Haloperidol currently has **no active product licenses on file** in this dataset — `market_status` is "未上市" (Not Marketed) with `total_licenses = 0`. No DIN-level product table can be produced from this Evidence Pack. This should be independently verified against Health Canada's Drug Product Database before any regulatory-facing decision, since haloperidol is a long-marketed generic in many jurisdictions and absence here may reflect a data collection gap rather than true non-availability.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `safety.key_warnings` and `safety.contraindications` are recorded as data gaps in this pack, and the DDI query returned no results. This is flagged in `meta.data_gaps` as DG001 — "TFDA/label warnings and contraindications" — with **Blocking** severity, meaning this candidate cannot yet clear a full safety pre-screen (S1) despite the favorable efficacy evidence.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Haloperidol has strong, consistent trial and literature support (L1 evidence: ≥2 completed Phase 3 RCTs with haloperidol as active comparator) for a role in controlling acute mania in bipolar affective disorder, sharing a plausible D2-antagonism mechanism with already-approved antimanic antipsychotics. However, this likely reflects an **existing, well-established clinical use** rather than a novel repurposing opportunity, and a Blocking data gap on formal safety/label information (DG001) prevents full regulatory sign-off at this stage.

**To proceed, the following is needed:**
- Retrieve official label warnings/contraindications for haloperidol (resolves Blocking gap DG001) before advancing past S1 safety pre-screen
- Confirm DrugBank/formal MOA record (resolves High-severity gap DG002) to complete mechanistic documentation
- Verify current Health Canada marketing/licensing status directly (this pack shows 0 licenses, which should be confirmed rather than assumed, given haloperidol's broad generic availability elsewhere)
- Clarify whether "manic bipolar affective disorder" is already an approved/labeled indication in the relevant jurisdiction — if so, this is a label-extension/formulary confirmation exercise rather than a true repurposing case
- No further action needed on the other 9 TxGNN-predicted indications in this pack; they remain correctly held at L5/Hold pending any future evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

