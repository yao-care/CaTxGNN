---
layout: default
title: Phenylephrine
parent: 僅模型預測 (L5)
nav_order: 617
evidence_level: L5
indication_count: 3
---

# Phenylephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Phenylephrine: From Nasal/Ocular Decongestant Use to Nasal Cavity Disease

## One-Sentence Summary

Phenylephrine is a selective α1-adrenergic receptor agonist long used as a topical nasal and ocular decongestant/mydriatic.
The TxGNN model's top prediction — **Nasal Cavity Disease** — largely reconfirms this established pharmacology rather than identifying a novel use,
with **8 clinical trials** and **8 publications** currently retrieved, though only a subset directly tests phenylephrine itself.
Two lower-ranked predictions (acute laryngopharyngitis, trigeminal autonomic cephalalgia) represent more speculative, model-only extrapolations with far less supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Canada regulatory data (drug not marketed); known pharmacologically as a nasal/ocular decongestant and mydriatic |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The formal DrugBank mechanism-of-action field for this record is currently a data gap (DG002). Based on well-established pharmacology reflected in the evidence pack's own analysis, phenylephrine is a selective α1-adrenergic receptor agonist that acts on nasal mucosal vascular smooth muscle to cause vasoconstriction, reducing mucosal congestion and swelling — a textbook-level, already-known mechanism rather than a genuinely novel therapeutic hypothesis.

This is reflected in the TxGNN score itself: at 99.97%, the model is essentially recognizing an existing, decades-old clinical use (topical nasal decongestion) rather than surfacing new biology. The clinical evidence — most notably a completed randomized trial of a lidocaine/phenylephrine combination spray (Co-phenylcaine) improving visualization and comfort during nasoendoscopy — supports this as a confirmatory rather than exploratory finding.

By contrast, the model's lower-ranked predictions (laryngopharyngitis, trigeminal autonomic cephalalgia) extrapolate this same α1-agonist vasoconstrictive mechanism to anatomically or mechanistically adjacent conditions where direct evidence is sparse or absent — these are genuinely more novel and warrant separate, more cautious evaluation (see below).

---

## Clinical Trial Evidence
*(for Nasal Cavity Disease — top-ranked prediction)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | NA | Completed | 106 | Co-phenylcaine (lidocaine + phenylephrine) nasal spray vs. nasal nebulization prior to rigid nasoendoscopy — directly tests the phenylephrine-containing product for decongestion/anesthesia (Grade A relevance) |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Compares topical oxymetazoline vs. epinephrine for bleeding/visualization before endoscopic sinus surgery; phenylephrine not confirmed as a study arm (Grade B) |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Four-way crossover, placebo-controlled study of an H3-antagonist on nasal congestion after allergen challenge; phenylephrine's role as comparator unconfirmed (Grade B) |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Compares cocaine vs. lidocaine/xylometazoline vs. saline for intranasal analgesia; phenylephrine not a study drug (Grade C) |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | NA | Unknown | 120 | Endoscopic vs. external dacryocystorhinostomy technique comparison; phenylephrine at most an intraoperative adjunct (Grade C) |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | Active, not recruiting | 60 | Esmolol vs. lidocaine IV infusion for recovery quality after sinus surgery; no direct phenylephrine link (Grade C) |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Withdrawn | 0 | Kovanaze (tetracaine+oxymetazoline) vs. articaine for dental anesthesia; withdrawn, no phenylephrine (Grade C) |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated | 3 | Same Kovanaze vs. articaine comparison; terminated early, no phenylephrine (Grade C) |

---

## Literature Evidence
*(for Nasal Cavity Disease — top-ranked prediction)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | RCT | Int J Clin Pract | Double-blind RCT (n=98): cophenylcaine spray vs. placebo before flexible nasendoscopy; no significant difference in pain/discomfort |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT | PLoS One | Triple-blind RCT of topical tranexamic acid (not phenylephrine) on bleeding/surgical field quality during FESS |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Review | Vestnik Otorinolaringologii | Endoscopic evaluation of nasal mucosa after Polydexa spray containing phenylephrine, used post-surgically and for granulomatosis with polyangiitis |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik Otorinolaringologii | Pathogenesis-based approach to treating inflammatory nasal/sinus disease, emphasizing decongestant mechanisms |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Cohort | Vestnik Otorinolaringologii | Experimental/clinical safety-efficacy evaluation of Polydexa spray with phenylephrine in acute rhinosinusitis |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Cohort | Int J Pediatr Otorhinolaryngol | Acoustic rhinometry of nasal cavity/nasopharynx before and after adenotonsillectomy |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | In vitro | Clin Otolaryngol Allied Sci | In vitro study of drug effects (including sympathomimetics) on nasal ciliary beat frequency |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case report | Arch Ophthalmol | Toxicity from intranasal cocaine plus phenylephrine during dacryocystorhinostomy in two patients |

---

## Additional Predicted Indications (Lower Priority)

The evidence pack includes two further TxGNN predictions for phenylephrine, both with substantially weaker evidence than Nasal Cavity Disease:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Evidence Summary |
|------|---------|------|------|------|------|------|
| 2 | Acute Laryngopharyngitis | 99.97% | L5 | S0 | Hold | No clinical trials or literature retrieved; purely a model extrapolation based on knowledge-graph proximity to nasal cavity disease |
| 3 | Trigeminal Autonomic Cephalalgia | 99.30% | L4 | S1 | Research Question | 16 publications found, but all use topical phenylephrine as a **pharmacological diagnostic probe** (pupillometry, ciliospinal reflex testing) in cluster headache/Horner's syndrome research — not as a therapeutic intervention. No treatment-outcome evidence exists |

Neither of these should be pursued as active repurposing candidates without new primary evidence; rank 3 may merit a hypothesis-generating literature deep-dive given the biologically plausible autonomic mechanism, but it is not currently actionable.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are currently unavailable in this evidence pack (data gap DG001, flagged as **Blocking** — this prevents the drug from entering initial safety screening).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction (Nasal Cavity Disease) is supported by one completed RCT and one relevant completed non-randomized trial directly involving a phenylephrine-containing product, consistent with an L2 evidence level. However, this finding largely validates known pharmacology rather than revealing a new indication, and the Canada regulatory/safety record for this drug is currently empty, so no product-specific safety guardrails can yet be defined.

**To proceed, the following is needed:**
- TFDA/Health Canada package insert (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed DrugBank mechanism-of-action record (DG002)
- Clarification of whether "Nasal Cavity Disease" represents a genuinely new regulatory indication or simply an extension of existing decongestant labeling, before treating it as a repurposing candidate
- For Trigeminal Autonomic Cephalalgia (rank 3): a scoping review to determine whether the diagnostic-probe literature supports any therapeutic hypothesis before advancing past Research Question stage
- Acute Laryngopharyngitis (rank 2) should remain on Hold pending any primary evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

