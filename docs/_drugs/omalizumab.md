---
layout: default
title: Omalizumab
parent: Model Prediction Only (L5)
nav_order: 685
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-04
monitor_inn: "OMALIZUMAB"
predicted_indications: ["bronchitis", "atopic eczema", "dermatitis", "bronchial neoplasm (disease)", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease"]
description: "Omalizumab: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Omalizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Omalizumab: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Omalizumab is a humanized monoclonal antibody that binds immunoglobulin E (IgE) and is marketed in Canada.
The TxGNN model predicts it may be useful for **bronchitis**.
The data compiled for this report contain **1 registered clinical trial** and several publications that touch on this direction, but **no published study directly shows benefit in bronchitis**, so the evidence is model prediction only (L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 8 of 8) |
| Number of DINs | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Omalizumab targets immunoglobulin E (the IGHE gene product). By binding free IgE, it lowers the IgE available to mast cells and basophils. It also reduces expression of the high-affinity IgE receptor (FcεRI) on mast cells, basophils and dendritic cells. Together these effects dampen allergic airway inflammation.

The link to bronchitis is indirect. The retrieved literature discusses omalizumab mainly in allergic airway disease, where chronic bronchitis features can coexist, and in patients with smoking-induced airway problems. No study tests bronchitis as the primary condition. The mechanism is therefore plausible only for an allergic or eosinophilic form of airway inflammation. It does not show that omalizumab would help bronchitis in general, such as infectious or smoking-related chronic bronchitis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Double-blind, placebo-controlled, 3-centre trial of whether omalizumab allows prednisone dose reduction in patients with persistent eosinophilic bronchitis. The population was a related airway disease with persistent sputum eosinophilia. The trial is very small, and its findings suggest omalizumab may be inadequate for this purpose. It does not support efficacy in bronchitis. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | Describes omalizumab's IgE-binding and FcεRI-lowering effects, which reduce airway inflammation. Does not address bronchitis directly. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Pooled safety analysis | Curr Med Res Opin | Pooled safety data for omalizumab in children with allergic airway disease. Does not address bronchitis. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Discusses managing allergic airway disease in smokers, including chronic bronchitis. Notes that these patients are excluded from most trials, so drug treatment is uncertain. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | Preoperative management of patients with airway disease or chronic bronchitis. Mentions omalizumab as a treatment option for severe allergic airway disease only. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | General overview of monoclonal antibodies in paediatrics. Not specific to bronchitis. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | Case report of plastic bronchitis after bronchial thermoplasty. No abstract available, so no efficacy conclusion can be drawn. |

## Canada Market Information

All licences below are valid. The approved indication text is not recorded in the local data.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02545136 | XOLAIR | Not listed | Not listed |
| 02553805 | OMLYCLO | Not listed | Not listed |
| 02545144 | XOLAIR | Not listed | Not listed |
| 02459795 | XOLAIR | Not listed | Not listed |
| 02545160 | XOLAIR | Not listed | Not listed |

## Safety Considerations

- **Drug Interactions**: 8 interaction records were compiled.
  - Moderate: omacetaxine mepesuccinate.
  - Minor: zinc sulfate, zinc acetate, zinc gluconate, zinc chloride, Echinacea and vitamin E.
- Warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no published study supports omalizumab in bronchitis. The only registered trial involved 11 patients with a related eosinophilic airway condition, and its findings suggest omalizumab may be inadequate. The remaining publications are reviews, a pooled safety analysis and a case report on related airway disease. The evidence is therefore model prediction only (L5).

**To proceed, the following is needed:**
- A defined bronchitis subtype (for example, eosinophilic or allergic) in which an IgE-driven mechanism is credible.
- Controlled clinical data in that population, with bronchitis as the primary condition.
- Package insert warnings and contraindications from Health Canada, and the approved indication and dosage form for each licence.
- A review of the interaction with omacetaxine mepesuccinate before any clinical use.

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

