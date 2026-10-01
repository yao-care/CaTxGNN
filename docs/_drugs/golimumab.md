---
layout: default
title: Golimumab
parent: Moderate Evidence (L3-L4)
nav_order: 435
evidence_level: L4
indication_count: 5
---

# Golimumab
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Golimumab: From Inflammatory Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Golimumab is a TNF-alpha inhibitor that the literature describes as approved for rheumatoid arthritis, psoriatic arthritis and ankylosing spondylitis.
The TxGNN model predicts it may be effective for **rheumatoid vasculitis**, but only **3 loosely related clinical trials** and **6 publications** exist, and none tests golimumab for this condition directly.
Overall evidence is weak (L4), so the current recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data. Literature describes rheumatoid arthritis, psoriatic arthritis and ankylosing spondylitis. |
| Predicted New Indication | Rheumatoid vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Golimumab is a fully human monoclonal antibody that neutralizes TNF-alpha. It is established in rheumatoid arthritis (RA). Rheumatoid vasculitis is a serious extra-articular complication that mostly affects patients with severe, seropositive RA. Both conditions share inflammatory pathways, so a link between them is plausible.

The link is indirect, however, and TNF blockade in vasculitis has given inconsistent results. Paradoxical vasculitis and Takayasu arteritis have been reported during anti-TNF therapy (PMID 22999907). The very high TxGNN score most likely reflects RA network proximity in the knowledge graph rather than vasculitis-specific evidence. Detailed mechanism of action data for golimumab are also not available in this evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients having shoulder arthroplasty. It does not test golimumab for vasculitis. |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of tocilizumab in RA. It gives RA context only and has no vasculitis endpoint. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Registry of new immune-mediated inflammatory diseases after biologics. It is a safety and epidemiology study with no vasculitis efficacy signal. |

All three trials were graded C for relevance.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network meta-analysis (36 RCTs) | Int J Mol Sci | Five TNF inhibitors, including golimumab, similarly reduce joint destruction in RA. There is no vasculitis data. |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Observational | Semin Arthritis Rheum | Frequency and causes of end-stage renal disease in RA patients. Only indirectly relevant. |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Med | Update on biologic therapy for autoimmune diseases, covering benefits and drawbacks such as cost and adverse events. |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case report | Rheumatol Int | Pyoderma gangrenosum and pyogenic arthritis presenting as severe sepsis in an RA patient on golimumab. It notes that rheumatoid vasculitis has become less frequent since biologics were introduced. |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case report | Joint Bone Spine | Two cases of Takayasu's arteritis arising during anti-TNF therapy. This is a caution against assuming benefit in vasculitis. |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case report | Ocul Immunol Inflamm | Behçet disease-associated uveitis treated successfully with golimumab. Suggestive for immune-mediated vascular inflammation, but a single case. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2324784 | SIMPONI |
| 2417472 | SIMPONI I.V. |
| 2413183 | SIMPONI |
| 2324776 | SIMPONI |
| 2413175 | SIMPONI |

---

## Safety Considerations

Please refer to the package insert for safety information.

Anti-TNF therapy has been associated with paradoxical vasculitis, including Takayasu's arteritis (PMID 22999907). This matters for a vasculitis indication. No drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but rests on RA network proximity. None of the supplied trials or papers tests golimumab in rheumatoid vasculitis, and reports of paradoxical vasculitis under anti-TNF therapy point the other way.

**To proceed, the following is needed:**
- Vasculitis-specific evidence, such as case series or controlled studies of anti-TNF therapy in rheumatoid vasculitis
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Approved indication text for the Canadian licenses

**Note on other predictions:** Two lower-ranked predictions have much stronger support. Inflammatory spondylopathy (score 99.66%) and polyarticular juvenile rheumatoid arthritis (score 99.59%) are both rated L1 with a "Proceed with Guardrails" recommendation. The pJIA rating rests on two completed Phase 3 trials, and the spondylopathy rating on guideline-level reviews and pivotal-trial data, since none of the supplied spondylopathy trials is itself a Phase 3 RCT. Both are on-label uses of golimumab, so they are not true repurposing, and the empty original-indication field hides this.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

