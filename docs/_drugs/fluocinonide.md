---
layout: default
title: Fluocinonide
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 7
---

# Fluocinonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Fluocinonide: From Inflammatory Dermatoses to Alopecia Mucinosa

## One-Sentence Summary

Fluocinonide is a high-potency topical corticosteroid (Class II) used for inflammatory and pruritic skin conditions such as eczema, psoriasis, and contact dermatitis.
The TxGNN model predicts it may be effective for **Alopecia Mucinosa**, with **no clinical trials** and **no literature** currently directly supporting this combination.
Across all 7 predicted indications (all alopecia-spectrum conditions), the strongest indirect evidence is for **Alopecia Areata** (rank 3, L4), which has one indirect clinical trial and one case report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory and pruritic manifestations of corticosteroid-responsive dermatoses (eczema, psoriasis, contact dermatitis) |
| Predicted New Indication | Alopecia Mucinosa |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, fluocinonide is a synthetic fluorinated glucocorticoid receptor (GR) agonist. It suppresses the inflammatory cascade by inhibiting the transcription of pro-inflammatory cytokines (IL-1, IL-6, TNF-α), reducing vascular permeability, and blocking leukocyte recruitment to inflamed tissue. As a Class II (high-potency) topical agent, its local anti-inflammatory effect is more potent than most other topical corticosteroids, making it particularly suited for inflammatory dermatoses with dense lymphocytic infiltration.

Alopecia mucinosa (follicular mucinosis) is characterized by abnormal mucin accumulation within hair follicles and sebaceous glands, accompanied by a perifollicular inflammatory infiltrate. The primary (idiopathic) form is often benign and self-limiting; the secondary form is associated with cutaneous T-cell lymphoma (CTCL/mycosis fungoides), which requires oncological differentiation before any treatment. In the primary form, the inflammatory microenvironment theoretically overlaps with fluocinonide's mechanism — suppressing perifollicular lymphocytic infiltration may slow follicular damage and mucin deposition.

However, the mechanistic link is indirect. Fluocinonide does not address the root cause of mucin deposition, and in the CTCL-associated form, topical steroids alone are inappropriate and potentially masking. The TxGNN high prediction score most likely reflects the proximity of alopecia mucinosa nodes to other inflammatory alopecia subtypes within the knowledge graph, rather than a well-characterized direct drug-disease relationship. Among all 7 predicted indications, **alopecia areata** (rank 3) carries the most mechanistic and clinical plausibility for fluocinonide, as topical high-potency corticosteroids are first-line guideline therapy for that condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for alopecia mucinosa and fluocinonide.

---

## Literature Evidence

Currently no related literature available for alopecia mucinosa and fluocinonide.

---

## Canada Market Information

Fluocinonide is not currently marketed in Canada. No Drug Identification Numbers (DINs) are registered. Clinical trial or expanded access pathways would be required before any use in Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Supplementary: All Predicted Indications Overview

The candidate ID `TW-DB01047-multi` covers 7 alopecia-spectrum predictions. The table below summarizes all:

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Mechanistic Plausibility |
|------|-----------|------------|----------------|---------------|--------------------------|
| 1 | Alopecia Mucinosa | 99.61% | L5 | Hold | Indirect (anti-inflammatory) |
| 2 | Telogen Effluvium | 99.61% | L5 | Hold | Weak (systemic cause, not inflammatory) |
| 3 | **Alopecia Areata** | **99.59%** | **L4** | **Research Question** | **Strong (first-line guideline therapy)** |
| 4 | Quinquaud's Folliculitis Decalvans | 99.58% | L5 | Hold | Conditional (bacterial co-factor risk) |
| 5 | Hereditary Hypotrichosis with Recurrent Skin Vesicles | 99.56% | L5 | Hold | Very weak (genetic etiology) |
| 6 | Alopecia Antibody Deficiency | 99.51% | L5 | Hold | Weak (systemic immune defect) |
| 7 | Alopecia-Intellectual Disability-Hypergonadotropic Hypogonadism Syndrome | 99.49% | L5 | Hold | Very weak (rare genetic syndrome) |

### Alopecia Areata — Evidence Detail (Rank 3, Best Supported)

**Clinical Trial:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | Recruiting | 250 | Multicenter comparison of treatment outcomes in Central Centrifugal Cicatricial Alopecia (CCCA) — **⚠️ Disease mismatch**: CCCA is a scarring alopecia distinct from alopecia areata (non-scarring, autoimmune); trial relevance to AA is low |

**Literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case Report | J Am Acad Dermatol | 4 cases of congenital alopecia areata with 3–5 year follow-up; treatments included minoxidil 2% and a range of topical agents (specific agents partially reported) |

**Mechanistic note for Alopecia Areata:** AA is driven by CD8+ T-cell-mediated collapse of immune privilege in hair follicles, with IFN-γ and IL-15 as key pathogenic cytokines. Fluocinonide, as a high-potency GR agonist, suppresses perifollicular lymphocyte infiltration and downregulates these cytokines. Topical Class I–II corticosteroids are explicitly recommended as first-line therapy for patchy AA in American Academy of Dermatology and British Association of Dermatologists guidelines. Fluocinonide 0.05% solution is specifically cited in multiple guidelines for scalp AA.

---

## Conclusion and Next Steps

**Decision: Hold** *(for Alopecia Mucinosa as primary prediction)*

**Rationale:**
Evidence Level L5 means TxGNN model prediction only — no clinical trials or literature directly support fluocinonide for alopecia mucinosa, and the mechanistic link requires CTCL exclusion before any consideration. Additionally, fluocinonide is not marketed in Canada (0 DINs), adding a regulatory barrier.

**Strategic redirect:** Alopecia Areata (rank 3) has a substantially stronger rationale — guideline-level first-line use, established mechanism, and it would be the more productive repurposing research question for this drug.

**To proceed (for the Alopecia Mucinosa indication), the following is needed:**
- Case series data or observational studies on topical corticosteroids in primary (non-CTCL) alopecia mucinosa
- Biopsy-confirmed patient cohort distinguishing primary vs. CTCL-associated forms (mandatory before any trial)
- Fluocinonide MOA data from DrugBank API to formalize the mechanistic rationale
- Safety profile from the package insert (TFDA or FDA monograph), particularly HPA-axis suppression risk with prolonged scalp application
- Regulatory pathway assessment for first-in-Canada use

**To proceed (for Alopecia Areata, recommended pivot), the following is needed:**
- Prospective observational registry study comparing fluocinonide vs. other Class I–II topical steroids for patchy AA
- Head-to-head efficacy data against clobetasol (Class I) to justify Class II fluocinonide as a differentiated option
- Canada regulatory DIN application for a topical solution formulation targeting scalp AA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

