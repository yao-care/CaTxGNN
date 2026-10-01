---
layout: default
title: Isoniazid
parent: Moderate Evidence (L3-L4)
nav_order: 495
evidence_level: L4
indication_count: 1
---

# Isoniazid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a long-established anti-tuberculosis drug. The TxGNN model predicts it may be effective for **conjunctivitis**, with a very high score (99.36%). Direct support is thin: **1 clinical trial** (not relevant to conjunctivitis) and **20 publications**, almost all case reports or old articles on tuberculosis-related eye disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (general drug knowledge; the Canadian license records provide no indication text) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the DrugBank record. Isoniazid is known to inhibit mycolic acid synthesis (InhA), and it is bactericidal only against *Mycobacterium tuberculosis* complex. Its efficacy in tuberculosis is well established.

The link to conjunctivitis is narrow. Isoniazid could plausibly help in the rare **tuberculous conjunctivitis**, as part of a multidrug anti-TB regimen. It is not expected to work against the common causes of conjunctivitis (viral, bacterial, allergic).

The high TxGNN score most likely reflects knowledge-graph proximity between isoniazid, tuberculosis and ocular manifestations. It is not a validated repurposing signal. Because the DrugBank record has no original indications, this link could not be checked against label data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compared systemic drug reactions under 3HP (rifapentine + isoniazid) and 1HP regimens for latent tuberculosis infection. Conjunctivitis is not an efficacy endpoint, so it gives no direct evidence (relevance grade C). |

## Literature Evidence

Most records have no abstract, so the findings below are based on titles and available abstract text only. No RCTs were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Not classified | Am Rev Respir Dis | Title indicates a study of isoniazid prophylaxis for phlyctenular keratoconjunctivitis among Eskimos in Alaska. No abstract available. |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Not classified | Ann Oculist | Title indicates local isoniazid use in ocular tuberculosis. No abstract available. |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket in a woman with prior miliary TB. |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal tuberculosis, with literature review. |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Not classified | Cornea | Case of conjunctival tuberculosis presenting as chronic red eye. |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Not classified | Can J Ophthalmol | Conjunctival phlyctenulosis as a presenting sign of impending clinical tuberculosis. |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Not classified | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, 13 in children with primary TB. All had a positive tuberculin skin test. |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva. |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optom Clin | Review of ocular side effects of systemic drugs, including drug-associated conjunctivitis. |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Case report | Clin Pediatr | Case report of an unexpected cause of conjunctivitis in an adolescent. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 577812 | PDP-ISONIAZID |
| 577790 | PDP-ISONIAZID |
| 577804 | PDP-ISONIAZID |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial is unrelated to conjunctivitis, and the literature consists of case reports and old articles about tuberculosis-related eye disease. Isoniazid is not expected to help the common forms of conjunctivitis, so the high model score is not enough to proceed.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indications), which is currently missing and blocks safety screening
- Mechanism-of-action data from DrugBank
- Evidence from studies of tuberculous conjunctivitis showing whether isoniazid contributes beyond standard multidrug TB therapy
- A decision on whether the target should be narrowed to tuberculous conjunctivitis rather than conjunctivitis in general
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

