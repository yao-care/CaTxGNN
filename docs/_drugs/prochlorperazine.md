---
layout: default
title: Prochlorperazine
parent: 僅模型預測 (L5)
nav_order: 651
evidence_level: L5
indication_count: 10
---

# Prochlorperazine
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

# Prochlorperazine: From Antipsychotic/Antiemetic Use to Manic Bipolar Affective Disorder

## One-Sentence Summary

Prochlorperazine is a phenothiazine-class drug historically used as an antipsychotic and antiemetic; this specific evidence pack does not contain a structured original-indication or MOA record for it (both flagged as data gaps). Among 10 TxGNN-predicted new indications, only one — **Manic Bipolar Affective Disorder** — has any genuine supporting literature; the highest-scoring candidate (retinal dystrophy) is explicitly flagged in the evidence pack as a keyword-matching artifact, not real evidence. Overall evidentiary support is thin: **0 clinical trials** and a handful of pre-1980 case reports/reviews for the one plausible candidate.

*Note: The template convention is to lead with the top-scored prediction (rank 1). That candidate's own `repurposing_rationale` states its 15 supporting articles are unrelated ophthalmology case reports/reviews matched by text noise, not genuine signal. This report instead leads with rank 10 (manic bipolar affective disorder), the only candidate with a direct, drug-specific literature reference and a coherent mechanistic story — see the candidate comparison table below.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (data gap). Publicly known pharmacological class: phenothiazine antipsychotic/antiemetic. |
| Predicted New Indication (lead candidate) | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% (score 0.99979, rank 851 of model output) |
| Evidence Level | L4 |
| Canada Market Status | 未上市 (Not Marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DG002, High severity gap). Based on known information, prochlorperazine is a first-generation (typical) phenothiazine antipsychotic and antiemetic, acting primarily as a central dopamine D2 receptor antagonist — the same mechanistic class historically used to control psychotic agitation, mania, and severe nausea/vomiting.

Manic bipolar affective disorder is mechanistically plausible as a repurposing target because D2 antagonism is the pharmacological basis for antimanic effect in modern antipsychotics (e.g., olanzapine, quetiapine, risperidone are all approved for acute mania). The literature returned for this candidate includes a direct historical case report of prochlorperazine administered to a manic-depressive patient, plus several mid-20th-century reviews on phenothiazines in psychiatric and puerperal psychiatric disorders — consistent with prochlorperazine having been used clinically in psychiatric agitation/mania contexts before modern atypical antipsychotics became standard of care.

This evidence is dated (1959–2015), largely pre-RCT era, and one key article (PMID 13617778) actually documents an **adverse** confusional reaction to prochlorperazine in a manic-depressive patient rather than a therapeutic efficacy signal — so it demonstrates historical clinical exposure in this population, not proven benefit. By contrast, the top TxGNN-scored candidate (retinal dystrophy with extraocular anomalies) has no plausible mechanistic link — prochlorperazine has no known ophthalmic-developmental pharmacology — and its own rationale confirms the matched literature is text-mining noise.

---

## Other TxGNN-Predicted Candidates (Reviewed, No Actionable Evidence)

| Rank | Disease | Score | Evidence Level | Note |
|------|---------|-------|-----------------|------|
| 1 | Retinal dystrophy with/without extraocular anomalies | 99.998% | L5 | 15 literature hits, but flagged by evidence pack as keyword-matched noise — no genuine relevance |
| 2 | Hydranencephaly (disease) | 99.998% | L5 | No trials, no literature — score only |
| 3 | Congenital disorder of glycosylation w/ defective fucosylation | 99.998% | L5 | No trials, no literature — score only |
| 4 | Myopia X-linked | 99.998% | L5 | No trials, no literature — score only |
| 5 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 99.998% | L5 | No trials, no literature — score only |
| 6 | Polymicrogyria, perisylvian, w/ cerebellar hypoplasia and arthrogryposis | 99.997% | L5 | No trials, no literature — score only |
| 7 | Syndromic myopia | 99.997% | L5 | No trials, no literature — score only |
| 8 | Myopia 26, X-linked, female-limited | 99.997% | L5 | No trials, no literature — score only |
| 9 | Atypical glycine encephalopathy | 99.997% | L5 | No trials, no literature — score only |
| **10** | **Manic bipolar affective disorder** | **99.98%** | **L4** | Only candidate with direct drug-specific literature and coherent mechanism — **selected as lead candidate above** |

---

## Clinical Trial Evidence

Currently no related clinical trials registered (0 results for "Manic Bipolar Affective Disorder" across ClinicalTrials.gov and ICTRP).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13617778](https://pubmed.ncbi.nlm.nih.gov/13617778/) | 1959 | Case Report | Annales médico-psychologiques | Direct case report: a mild manic-depressive patient given prochlorperazine developed a confusional dream-like episode (clinical/EEG findings reported). Documents direct drug exposure in this population but as an **adverse reaction**, not efficacy evidence. |
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | Journal of Psychiatric Practice | Reviews use and safety of antipsychotic drugs (including older typical agents) in psychiatric illness and pregnancy; establishes class-level precedent for antipsychotic use beyond schizophrenia. |
| [26819726](https://pubmed.ncbi.nlm.nih.gov/26819726/) | 2015 | Pharmacovigilance (FAERS) | J Pharm Health Care Sci | FAERS analysis of hyperglycemic adverse events in antipsychotics explicitly used "to treat schizophrenia and bipolar disorder" — confirms the drug class' established role in bipolar disorder management. |
| [6069087](https://pubmed.ncbi.nlm.nih.gov/6069087/) | 1967 | Cohort/Case Series | Neurology | Documents seizures and EEG changes occurring during phenothiazine therapy — class-level neuropsychiatric effect data, no abstract available. |
| [4238455](https://pubmed.ncbi.nlm.nih.gov/4238455/) | 1969 | Review | Clinical Pharmacology and Therapeutics | General review of psychotherapeutic drug classes and clinical status circa 1969; no abstract available. |
| [14242542](https://pubmed.ncbi.nlm.nih.gov/14242542/) | 1965 | Review/Clinical | Obstetrics and Gynecology | Recommended clinical approach to severe psychologic disorders of the puerperium (postpartum psychiatric illness); no abstract available. |
| [14233737](https://pubmed.ncbi.nlm.nih.gov/14233737/) | 1964 | Review | American Journal of Psychiatry | Survey of electroshock therapy combined with phenothiazines and reserpine in psychiatric treatment; no abstract available. |
| [14222730](https://pubmed.ncbi.nlm.nih.gov/14222730/) | 1964 | Pending classification | L'Encéphale | Discusses psychodysleptic (psychiatric) manifestations occurring during treatment with psycholeptic drugs; no abstract available. |
| [235013](https://pubmed.ncbi.nlm.nih.gov/235013/) | 1975 | Case Report (non-target drug: pimozide) | Journal of the Neurological Sciences | Double-blind study of pimozide (a different D2-antagonist antipsychotic) for tardive dyskinesia — related drug class, not prochlorperazine itself. |
| [15863814](https://pubmed.ncbi.nlm.nih.gov/15863814/) | 2005 | Case Report (non-target drug: quetiapine) | American Journal of Psychiatry | Describes quetiapine discontinuation syndrome — different (atypical) antipsychotic, included by the model but not prochlorperazine-specific. |

---

## Canada Market Information

Prochlorperazine currently has **0 Health Canada drug identification numbers (DINs)** on file in this evidence pack — market status is **未上市 (Not Marketed)**. No licensed product records are available to summarize dosage forms or approved indication text.

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack contains no structured warnings, contraindications, or drug-interaction data for prochlorperazine (all fields flagged as data gaps — DG001, Blocking severity: TFDA/product-label warnings and contraindications are unavailable, which by itself blocks entry into the S1 safety review stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity data gap (DG001) means no safety/contraindication data exists to run even an initial (S1) safety review, and the drug is not currently marketed in Canada (0 DINs).
- The only mechanistically coherent and literature-supported candidate — manic bipolar affective disorder — is backed solely by pre-1980 case reports/reviews (L4, no RCTs, no modern trials), and its most specific reference documents an adverse reaction rather than efficacy.
- The highest TxGNN-scored candidate (retinal dystrophy) is explicitly flagged by the evidence pack itself as spurious/noise-matched literature; the remaining eight candidates have zero supporting evidence beyond the raw model score (L5).

**To proceed, the following is needed:**
- TFDA/product monograph data: warnings, contraindications, and drug-interaction profile (resolves DG001, Blocking)
- Confirmed DrugBank/product-label mechanism of action and original approved indication text (resolves DG002)
- Modern controlled clinical data (observational or RCT) evaluating prochlorperazine specifically in bipolar/manic patients, since existing evidence predates current antimanic-agent standards
- A biological-plausibility screen for the eight zero-evidence L5 candidates before any further pursuit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

