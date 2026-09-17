---
layout: default
title: Vitamin E
parent: Moderate Evidence (L3-L4)
nav_order: 830
evidence_level: L4
indication_count: 10
---

# Vitamin E
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Vitamin E: From Vitamin E Deficiency to Inborn Disorder of Bilirubin Metabolism

## One-Sentence Summary

> Vitamin E (DB00163) is classically used as a fat-soluble antioxidant supplement for vitamin E deficiency states.
> The TxGNN model predicts it may be relevant for **Inborn Disorder of Bilirubin Metabolism**,
> but only **3 clinical trials** (none directly testing Vitamin E in this population) and **2 publications** currently support this direction, making the evidence base exploratory rather than confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Evidence Pack; classically used for vitamin E deficiency and as a general antioxidant |
| Predicted New Indication | Inborn Disorder of Bilirubin Metabolism |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Vitamin E is a fat-soluble antioxidant vitamin that protects cell membranes — including hepatocyte membranes — from oxidative damage caused by reactive lipid peroxidation.

Inborn disorders of bilirubin metabolism (e.g., Crigler-Najjar syndrome, progressive familial intrahepatic cholestasis) frequently disrupt bile flow, which secondarily impairs absorption of fat-soluble vitamins including Vitamin E. In this context, Vitamin E supplementation is understood as **supportive/corrective therapy for a secondary deficiency**, not a treatment directed at the underlying bilirubin-processing defect itself.

Mechanistically this is plausible but indirect — the model's high prediction score likely reflects the strong statistical association between "fat-soluble vitamin deficiency" and "cholestatic/bilirubin metabolism disease" nodes in the knowledge graph, rather than a specific disease-modifying pathway. This is reflected in the clinical evidence below, where none of the identified trials directly test Vitamin E as an intervention for this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03115086](https://clinicaltrials.gov/study/NCT03115086) | N/A | Active, not recruiting | 55 | Post-marketing observational registry for Cholbam (cholic acid); collects natural history data, does not test Vitamin E as an intervention |
| [NCT06465810](https://clinicaltrials.gov/study/NCT06465810) | N/A | Recruiting | 1,850 | Multi-country real-world registry for ATTR amyloidosis; Vitamin E not an evaluated treatment |
| [NCT01556906](https://clinicaltrials.gov/study/NCT01556906) | Phase 2 | Completed | 6 | Dose-escalation safety study of lomitapide (MTP inhibitor) in homozygous familial hypercholesterolemia; Vitamin E not the study drug |

*Note: All three trials were graded "C" (low relevance) — none directly test Vitamin E as a treatment for this indication.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [803225](https://pubmed.ncbi.nlm.nih.gov/803225/) | 1975 | Review | New England Journal of Medicine | Overview of neonatal nonhemolytic jaundice; background pathophysiology, no direct Vitamin E intervention data |
| [7915305](https://pubmed.ncbi.nlm.nih.gov/7915305/) | 1994 | Case report/Case series | Journal of Pediatrics | Describes 3β-hydroxy-C27-steroid dehydrogenase/isomerase deficiency as a cause of progressive intrahepatic cholestasis; mechanistic/diagnostic context only |

---

## Canada Market Information

Vitamin E is currently **not marketed** under this candidate profile in the Canadian regulatory dataset (0 DINs on file). No licensed product records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are currently unavailable for this candidate — flagged as a Blocking data gap, see below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence is L4 (preclinical/mechanistic plausibility only) — none of the three identified trials directly test Vitamin E for this indication, and the two literature citations provide background pathophysiology rather than interventional evidence.
- A **Blocking** data gap (DG001: missing TFDA/product-label warnings and contraindications) prevents this candidate from entering the S1 safety review stage regardless of efficacy signal strength.

**To proceed, the following is needed:**
- Product monograph / label warnings and contraindications (Blocking gap, DG001)
- Mechanism of action data from DrugBank (High priority gap, DG002)
- A dedicated interventional trial evaluating Vitamin E specifically in patients with inborn bilirubin metabolism disorders
- Consider evaluating the closely related broader term **"bilirubin metabolism disease"** (rank 2 in this Evidence Pack) separately — it carries stronger direct evidence (L2, one completed Phase 4 RCT: NCT04977661) and was scored "Proceed with Guardrails," suggesting it may be a more actionable near-term candidate than the specific inborn-disorder subtype evaluated here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

