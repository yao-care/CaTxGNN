---
layout: default
title: Monopotassium Phosphate
parent: Moderate Evidence (L3-L4)
nav_order: 624
evidence_level: L4
indication_count: 7
---

# Monopotassium Phosphate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Monopotassium Phosphate: From Phosphate and Potassium Replacement to Renal Tubular Acidosis

## One-Sentence Summary

Monopotassium phosphate is an electrolyte salt that supplies potassium and phosphate, and Canadian products are mainly injectable phosphate and electrolyte solutions.
The TxGNN model ranks **renal tubular acidosis** as its top prediction, but there are **0 clinical trials** and only **6 publications**, all of them case reports or reviews that do not test this drug.
The prediction is best treated as a hypothesis. The same drug has far stronger evidence for a different predicted use, **nephrolithiasis** (see "Other Predicted Indications").

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (products are injectable phosphate and multi-electrolyte solutions) |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.95% (model rank 1471) |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Monopotassium phosphate is a source of potassium and phosphate, and its use as a replacement electrolyte is established. Whether it has any role in renal tubular acidosis (RTA) is unproven.

The linked literature does not describe treating RTA with this drug. Almost all of it concerns Fanconi syndrome, a generalized proximal tubule disorder that includes proximal (type 2) RTA. In these patients the kidney wastes phosphate, causing hypophosphatemia and osteomalacia, and oral phosphate is used to replace the loss. That corrects phosphate depletion, not the acid-base problem of RTA. The high TxGNN score most likely reflects a knowledge-graph link to phosphate wasting rather than a real benefit for acidosis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications tests monopotassium phosphate for RTA. They describe conditions in which RTA or Fanconi syndrome occurs alongside phosphate wasting.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8625085](https://pubmed.ncbi.nlm.nih.gov/8625085/) | 1995 | Cohort | Cancer | Prospective study of ifosfamide nephrotoxicity in children and young adults. Proximal tubular dysfunction with phosphaturia, hypophosphatemia and RTA. |
| [9280905](https://pubmed.ncbi.nlm.nih.gov/9280905/) | 1997 | Review | La Pediatria medica e chirurgica | Management of acute renal failure in hospitalized children. |
| [25148820](https://pubmed.ncbi.nlm.nih.gov/25148820/) | 2014 | Case report | Endocrine Practice | Severe hypophosphatemic osteomalacia from adefovir-induced Fanconi syndrome (proximal, type 2 RTA). |
| [26554665](https://pubmed.ncbi.nlm.nih.gov/26554665/) | 2015 | Case report | BMC Nephrology | Severe osteomalacia from tubulointerstitial nephritis with Fanconi syndrome in primary biliary cirrhosis. |
| [28725949](https://pubmed.ncbi.nlm.nih.gov/28725949/) | 2018 | Case report | Clinical Rheumatology | Hypophosphatemic osteomalacia as the first sign of renal tubular disease in Sjögren's syndrome. |
| [694607](https://pubmed.ncbi.nlm.nih.gov/694607/) | 1978 | Case report | South African Medical Journal | Nephropathic cystinosis with Fanconi syndrome: hypophosphataemia, hypokalaemia and systemic acidosis. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 711306 | POTASSIUM PHOSPHATE MONOBASIC INJECTION |
| 2139545 | POTASSIUM PHOSPHATES INJECTION, USP |
| 804789 | POTASSIUM PHOSPHATES |
| 800007 | TIS-U-SOL SOLUTION |
| 1931679 | ISOLYTE S PH 7.4 (MULTI-ELECTROLYTE INJECTION) |

---

## Other Predicted Indications

TxGNN also predicted six other indications. Their evidence differs sharply from the top-ranked one.

| Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| **Nephrolithiasis** | 99.57% | L1 | Strongest support. A completed Phase 3 double-blind RCT ([NCT00004284](https://clinicaltrials.gov/study/NCT00004284), n=300) compares potassium phosphate with potassium citrate in absorptive hypercalciuria. A 1976 double-blind trial ([PMID 782240](https://pubmed.ncbi.nlm.nih.gov/782240/)) found that phosphate cut urinary calcium by 33% but did not reduce stone disease. Slow-release potassium phosphate trials ([PMID 7785460](https://pubmed.ncbi.nlm.nih.gov/7785460/), [PMID 9554331](https://pubmed.ncbi.nlm.nih.gov/9554331/)) show sustained calcium lowering. A Phase 1/2 study in Dent disease ([NCT02016235](https://clinicaltrials.gov/study/NCT02016235)) is also relevant. No outcome data were supplied for the Phase 3 trial. |
| Potassium deficiency disease | 99.73% | L4 | Plausible for combined low potassium and low phosphate, but none of the shown trials tests this drug. They are HIV or pharmacokinetic studies. Potassium chloride remains the standard agent. |
| Acute urate nephropathy | 99.80% | L5 | Mechanistically doubtful and possibly harmful. Tumor lysis syndrome and rhabdomyolysis already involve excess phosphate and potassium. |
| Dyspepsia | 99.74% | L5 | No plausible mechanism. The one linked trial is an HIV study. |
| Calcium-alkali syndrome | 99.33% | L5 | All linked trials are unrelated. Phosphate during hypercalcemia risks metastatic calcification. |
| Primary bone dysplasia with defective mineralization | 99.02% | L5 | No trials or literature. Phosphate is used in phosphate-wasting rickets, but the category includes conditions such as hypophosphatasia where it is inappropriate. |

---

## Safety Considerations

- **Drug Interactions**: No interactions were found in the queried database.

Please refer to the package insert for warnings and contraindications. Health Canada label information was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RTA prediction has no clinical trials, and the literature consists of case reports and reviews about phosphate wasting in Fanconi syndrome. Phosphate repletion does not correct tubular acidosis, so a high model score alone is not enough to proceed.

**To proceed, the following is needed:**
- Any direct evidence for monopotassium phosphate in RTA, and clarification of which RTA subtype (if any) could benefit
- Health Canada package insert warnings and contraindications
- Mechanism of action data
- For the stronger nephrolithiasis candidate: published outcomes of NCT00004284, then evaluation under guardrails (exclude infection stones and calcium phosphate stone formers; monitor serum calcium, phosphate, potassium and renal function; watch for GI intolerance and hyperkalemia in renal impairment)

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

