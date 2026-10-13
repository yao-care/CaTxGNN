---
layout: default
title: Terazosin
parent: Model Prediction Only (L5)
nav_order: 896
evidence_level: L5
indication_count: 10
---

# Terazosin
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

# Terazosin: From Hypertension and Benign Prostatic Hyperplasia to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Terazosin is an alpha-1 adrenergic blocker originally used to treat hypertension and benign prostatic hyperplasia (BPH).
The TxGNN model's top-ranked prediction is **hypotrichosis simplex of the scalp**, but there are **no clinical trials and no publications** supporting it, so this is a model-only prediction.
Among the other predicted indications, **Raynaud disease** (1 publication) and **migraine** (2 publications) have the most supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension; benign prostatic hyperplasia (from the knowledge graph, since no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Based on known pharmacology, terazosin is an alpha-1 adrenergic antagonist that relaxes vascular and prostatic smooth muscle. This explains its efficacy in hypertension and BPH.

For the top prediction, hypotrichosis simplex of the scalp, the link is speculative. One could argue that vasodilation might improve hair follicle perfusion, similar to minoxidil. However, hypotrichosis simplex is a genetic disorder, so a vasodilator is unlikely to address its root cause. The high score probably reflects proximity in the knowledge graph to other hair-related conditions rather than a true pharmacological signal.

The more plausible candidates are those tied to adrenergic vasoregulation. **Raynaud disease** has the strongest rationale: cold-induced vasospasm is driven by adrenergic vasoconstriction, and alpha-1 blockade produces peripheral vasodilation. **Migraine** is a second, weaker candidate, based on possible effects on adrenergic tone and cerebrovascular reactivity.

### Other Predicted Indications (Top 10)

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Hypotrichosis simplex of the scalp | 99.97% | L5 | Hold |
| 2 | Congenital hypotrichosis milia | 99.97% | L5 | Hold |
| 3 | Diffuse alopecia areata | 99.96% | L5 | Hold |
| 4 | Alopecia | 99.95% | L4 | Hold |
| 5 | Migraine disorder | 99.92% | L4 | Research Question |
| 6 | Migraine with brainstem aura | 99.91% | L4 | Hold |
| 7 | Raynaud disease | 99.83% | L3 | Research Question |
| 8 | Ambras type hypertrichosis universalis congenita | 99.65% | L5 | Hold |
| 9 | Manic bipolar affective disorder | 99.55% | L5 | Hold |
| 10 | Kyphoscoliotic heart disease | 99.49% | L5 | Hold |

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction (hypotrichosis simplex of the scalp). No trials were found for any of the other nine predicted indications either.

---

## Literature Evidence

No literature is available for the top-ranked prediction. The table below lists the publications found for lower-ranked predictions, which are the only supporting literature in the compiled data.

| PMID | Year | Type | Journal | Related Indication | Key Findings |
|------|-----|------|------|------|---------|
| [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/) | 1997 | Clinical study (design unverified) | Minerva Cardioangiologica | Raynaud disease | Terazosin reduced the number, intensity and duration of vasospastic attacks in idiopathic and secondary Raynaud's phenomenon, with improved thermographic and ultrasonographic findings. |
| [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/) | 1994 | Clinical study (small, open trial) | La Clinica Terapeutica | Migraine | Open trial in 46 patients with migraine without aura comparing terazosin (10 patients), buflomedil (29) and both (7) for prophylaxis. |
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Review / case series | Headache | Migraine | Ten patients given terazosin or doxazosin; all but one had reduced migraine frequency or severity, but 5 stopped because of side effects. |
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Review | Current Cardiology Reviews | Alopecia | Review of non-cardiac effects of cardiovascular drugs, including hair effects of vasoactive agents such as minoxidil. It does not show terazosin efficacy in alopecia. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02243521 | PMS-TERAZOSIN | Not specified | Not specified |
| 02234503 | APO-TERAZOSIN | Not specified | Not specified |
| 02243519 | PMS-TERAZOSIN | Not specified | Not specified |
| 02243518 | PMS-TERAZOSIN | Not specified | Not specified |
| 02243520 | PMS-TERAZOSIN | Not specified | Not specified |

Eight valid single-ingredient licences are held in total (PMS-TERAZOSIN and APO-TERAZOSIN); the five above are shown.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, priapism, intraoperative floppy iris syndrome.
- **Drug Interactions**: 100 interactions were identified. The ones listed are mostly of Moderate severity and include:
  - Corticosteroids: hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone
  - Opioids: morphine (including liposomal), opium
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Cannabinoids: dronabinol, nabilone
  - Others: bupropion
  - Unknown severity: calcitriol, pantoprazole, glimepiride
- **Practical concern**: for Raynaud disease, hypotension, dizziness and first-dose syncope are the main concerns, particularly in patients who already have low blood pressure.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hypotrichosis simplex of the scalp, has a very high model score but no trials, no literature, and an implausible mechanism for a genetic disorder. The evidence is Level L5. Of the lower-ranked predictions, Raynaud disease (L3) and migraine (L4) merit follow-up as research questions, but the supporting studies are old, small and of unverified design.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- For Raynaud disease: the full text of PMID 9273472 to confirm design, sample size and outcomes, followed by a search for modern controlled trials
- For migraine: a review of whether newer controlled data exist for alpha-1 blockers in prophylaxis
- A blood pressure monitoring and first-dose safety plan for any trial in populations prone to low blood pressure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

