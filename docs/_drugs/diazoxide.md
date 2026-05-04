---
layout: default
title: Diazoxide
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Diazoxide
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

# Diazoxide: From Hyperinsulinism to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Diazoxide is an ATP-sensitive potassium (KATP) channel opener clinically approved for hyperinsulinemic hypoglycemia (congenital hyperinsulinism) and historically used for hypertensive emergencies.
The TxGNN model's top-ranked prediction is **hypotrichosis simplex of the scalp** (score: 99.96%), driven by diazoxide's well-documented hair-growth-promoting mechanism — the same pathway exploited by FDA-approved minoxidil.
This specific indication, however, is supported by **no clinical trials and no publications** (L5), and is best understood within the broader 10-indication prediction cluster, where **alopecia** (rank 4, 9 publications) is the most evidence-backed target and **autosomal dominant hyperinsulinism due to Kir6.2 deficiency** (rank 10) is the most mechanistically direct.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Canadian license on record; known clinical use: hyperinsulinemic hypoglycemia / congenital hyperinsulinism |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Diazoxide opens ATP-sensitive potassium (KATP) channels by binding to the SUR1 subunit in pancreatic beta cells and the SUR2 subunit in vascular smooth muscle. In the pancreas, this suppresses insulin secretion — forming the basis of its approved use in congenital hyperinsulinism. In peripheral vasculature, KATP channel opening causes vasodilation, which historically made diazoxide useful in hypertensive emergencies.

The hair-growth connection stems from a well-documented pharmacological side effect: diazoxide causes hypertrichosis (excessive hair growth) in 8–44% of treated patients. This occurs through the same mechanism as minoxidil — both agents open KATP channels in the vascular smooth muscle of the dermal papilla, increasing follicular blood flow and extending the anagen (active growth) phase of the hair cycle. Primate studies from the 1990s confirmed that topical 5% diazoxide induced significant hair regrowth in bald macaque scalps, further validating this mechanistic pathway (PMID 2085505, 8326148).

**Hypotrichosis simplex of the scalp**, however, presents a fundamental mechanistic mismatch. This hereditary condition arises from structural mutations in hair follicle developmental genes (CDSN, LPAR6), resulting in irreversible follicle loss — not vascular insufficiency. KATP channel activation cannot restore structurally absent follicles. The high TxGNN score reflects a superficial phenotypic association between "sparse hair" and "hair growth promotion" rather than true pathological correspondence, and this prediction is best classified as a likely knowledge graph false positive. The more mechanistically appropriate target within this prediction set is **alopecia** (rank 4, L4), where vascular and follicular mechanisms are treatable.

> ⚠️ **Critical flags across this 10-indication multi-candidate report:** Rank 5 (Ambras-type hypertrichosis universalis congenita) and rank 7 (hypertrichosis disease) are **direction-reversed false positives** — diazoxide is a known *cause* of hypertrichosis, not a treatment. These represent a knowledge graph edge directionality error and should be flagged as model improvement cases.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for diazoxide and hypotrichosis simplex of the scalp.

---

## Literature Evidence

Currently no related literature available for diazoxide and hypotrichosis simplex of the scalp.

---

**Supplementary — Evidence for Alopecia (Rank 4, L4)**

The mechanistically related indication **alopecia** (rank 4 in this multi-candidate report) has 9 supporting publications that establish the biological plausibility underlying the entire hair-loss prediction cluster:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [2085505](https://pubmed.ncbi.nlm.nih.gov/2085505/) | 1990 | Animal study (primate) | J Dermatol Sci | Topical 5% diazoxide induced significant hair regrowth in bald frontal scalp of stumptailed macaques; systemic absorption and hypertrichosis side effects were documented, raising formulation safety concerns |
| [8326148](https://pubmed.ncbi.nlm.nih.gov/8326148/) | 1993 | Review | J Invest Dermatol | Both minoxidil and diazoxide induced hair regrowth in the macaque androgenetic alopecia model via peripheral vasodilation; comparative review of KATP-mediated mechanism |
| [8018303](https://pubmed.ncbi.nlm.nih.gov/8018303/) | 1994 | Review | Drug Safety | Comprehensive review of drug-induced hair growth and hair loss; discusses the hypertrichotic properties of diazoxide and mechanism of follicle cycle modulation |
| [3214817](https://pubmed.ncbi.nlm.nih.gov/3214817/) | 1988 | Review | Clin Dermatol | Early survey of topical agents for male-pattern baldness; identifies diazoxide alongside minoxidil as a candidate compound with encouraging preclinical results |
| [4340017](https://pubmed.ncbi.nlm.nih.gov/4340017/) | 1972 | Case series | Arch Dis Child | Four neonates exposed to oral diazoxide in utero all developed hypertrichosis; confirms systemic hair growth effect and transplacental KATP activation |
| [37042338](https://pubmed.ncbi.nlm.nih.gov/37042338/) | 2023 | Case report | Pediatr Dermatol | Generalized hypertrichosis from topical minoxidil exposure; identifies diazoxide alongside phenytoin and minoxidil as established iatrogenic hypertrichosis agents — relevant to risk counselling |

---

## Canada Market Information

Diazoxide (DB01119) is **not currently marketed in Canada** and has no registered Drug Identification Numbers (DINs). Patients requiring this medication may access it through Health Canada's Special Access Programme. For reference, diazoxide (PROGLYCEM®) carries FDA approval in the United States for hyperinsulinemic hypoglycemia.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Safety signals documented in the literature reviewed for this Evidence Pack:**
>
> - **Hypertrichosis**: Reported in 8.6% of patients in long-term Japanese post-marketing surveillance (n=384, PMID 30083030); up to 44% in some pediatric hyperinsulinism series — the same pharmacological property driving repurposing hypotheses also constitutes a significant adverse effect requiring patient counselling
> - **Fluid retention / cardiac failure**: 8.3% and 3.4% respectively in long-term pediatric use; a critical safety concern that must be addressed in any new indication, particularly with systemic dosing
> - **Hyperglycemia**: Mechanism-based consequence of KATP channel activation suppressing insulin release; clinically significant outside of a hyperinsulinism context
> - **Gingival hyperplasia**: Known class effect (shared with amlodipine and phenytoin); may worsen pre-existing periodontal conditions — relevant to the rank 6 prediction flag
> - **Necrotizing enterocolitis**: Reported in neonates receiving diazoxide for hyperinsulinism (PMID 33483452); neonatal safety profile requires careful consideration

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction — hypotrichosis simplex of the scalp — is a likely knowledge graph false positive. The genetic etiology of this condition (irreversible structural follicle defects from CDSN/LPAR6 mutations) is mechanistically incompatible with diazoxide's vasodilatory KATP channel action. No clinical or preclinical evidence supports this specific indication, placing it firmly at evidence level L5. Two other high-ranking predictions (rank 5 and rank 7) compound this concern by representing direction-reversed errors where diazoxide causes the predicted disease rather than treating it.

**To proceed with investigation, the following is needed:**

For **alopecia / androgenetic alopecia** (rank 4 — the most evidence-supported target within this cluster):
- Retrieve formal MOA data from DrugBank to confirm KATP subunit specificity (Kir6.1/SUR2) in dermal papilla vasculature
- Systematic literature review for human topical diazoxide studies; current evidence is limited to 1990s primate models and observational case reports
- Topical formulation feasibility assessment — the primary development challenge is preventing transdermal absorption sufficient to cause systemic hypotension or fluid retention
- Proof-of-concept human study design with topical minoxidil as the active comparator, leveraging shared mechanism for non-inferiority framing

For **autosomal dominant hyperinsulinism due to Kir6.2 deficiency** (rank 10 — the most mechanistically direct prediction):
- Genotype-phenotype stratification: identify which KCNJ11 mutations retain partial KATP channel opening capacity (diazoxide-responsive phenotype) versus those with complete channel loss (diazoxide-unresponsive)
- Targeted literature search using mutation-specific terms (e.g., "KCNJ11 loss-of-function diazoxide responsive")
- Outreach to congenital hyperinsulinism patient registries to identify existing case series with genotype-stratified diazoxide response data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

