---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Azathioprine: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
---

# Azathioprine
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

# Azathioprine: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Azathioprine is an immunosuppressant originally used for rheumatoid arthritis.
The TxGNN model's top-ranked prediction is **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental malformation syndrome, but there are **0 clinical trials** and **0 publications** supporting it, so this result is most likely a model artifact.
The best-supported predictions further down the list are **inflammatory bowel disease** (22 trials, 20 publications) and **ulcerative colitis** (15 trials, 20 publications). These are already established clinical uses rather than new discoveries.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

*Note: The approved indication text was not available in the Canadian licence records. The original indication shown is taken from the knowledge-graph indication edge.*

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available. Based on known information, azathioprine is a thiopurine immunosuppressant. It is converted to 6-mercaptopurine and then to thioguanine nucleotides, which inhibit purine synthesis and suppress lymphocyte function. Its efficacy in rheumatoid arthritis, an immune-mediated condition, is established.

**For the top-ranked prediction, there is no identifiable mechanistic link.** Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare developmental malformation syndrome, and immunosuppression has no plausible relevance to its pathogenesis. The very high score (0.99999) most likely reflects a graph-embedding artifact. The next-ranked prediction, brachydactyly-syndactyly syndrome (a congenital limb malformation), has the same problem.

Other high-scoring predictions share this weakness:
- **WHIM syndrome** and **chronic granulomatous disease variants**: these are immunodeficiencies. Azathioprine's myelosuppression and infection risk make the mechanistic direction likely unfavourable.
- **Osteoarthritis**: it is mainly degenerative, and azathioprine's role in rheumatoid arthritis does not transfer to it.
- **Acromesomelic dysplasia, Hunter-Thompson type**: this is a genetic skeletal dysplasia with no plausible link.

**The only biologically plausible predictions are inflammatory bowel disease (IBD) and ulcerative colitis.** Thiopurine-mediated T-cell apoptosis reduces mucosal immune-mediated inflammation. Azathioprine is already widely used for steroid-sparing maintenance of remission in these conditions. They are therefore established uses, not novel repurposing findings.

---

## Clinical Trial Evidence

**For the top-ranked prediction (colobomatous microphthalmia-rhizomelic dysplasia syndrome):** Currently no related clinical trials registered.

For reference, the most relevant trials for the two best-supported predictions are listed below. Many trials use azathioprine as a comparator or as a combination partner with biologics.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Terminated | 242 | Infliximab alone or with azathioprine vs azathioprine alone in moderate to severe active UC |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Phase 4 | Completed | 211 | Infliximab-antimetabolite combination vs antimetabolite alone vs infliximab alone in Crohn's disease patients in steroid-free remission |
| [NCT00984568](https://clinicaltrials.gov/study/NCT00984568) | Phase 3 | Terminated | 28 | Conventional step-up (including azathioprine) vs infliximab monotherapy in active UC |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | Completed | 65 | Early infliximab plus azathioprine vs steroids plus azathioprine in acute severe UC |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Completed | 83 | Azathioprine vs mesalazine for preventing postoperative recurrence of Crohn's disease |
| [NCT00098111](https://clinicaltrials.gov/study/NCT00098111) | Phase 3 | Terminated | 31 | Dose-ranging study of azathioprine (Imuran) in active Crohn's disease |
| [NCT01564823](https://clinicaltrials.gov/study/NCT01564823) | Phase 3 | Completed | 86 | Adalimumab vs azathioprine for preventing endoscopic recurrence after Crohn's surgery |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Unknown | 84 | Low-dose azathioprine plus allopurinol vs azathioprine alone in UC |
| [NCT02247258](https://clinicaltrials.gov/study/NCT02247258) | Phase 2 | Terminated | 63 | Immediate vs endoscopy-directed azathioprine for postoperative ileal Crohn's recurrence |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | Recruiting | 300 | Top-down mirikizumab vs standard care with azathioprine in newly diagnosed UC |

---

## Literature Evidence

**For the top-ranked prediction:** Currently no related literature available.

For reference, key publications for the two best-supported predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: top-down infliximab plus azathioprine vs azathioprine alone in acute severe UC responsive to IV steroids |
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Updated review of azathioprine and 6-mercaptopurine for maintenance of remission in UC |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Earlier version of the review of thiopurines for maintaining remission in UC |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | Efficacy of azathioprine and mercaptopurine in UC |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohns Colitis | State-of-the-art overview of thiopurine treatment in IBD |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Review | J Gastroenterol Hepatol | Thiopurine pharmacogenetics and metabolite monitoring in IBD |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Rev Gastroenterol Hepatol | Molecular insights into azathioprine in IBD, with data from numerous trials and meta-analyses documenting efficacy |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Basic/translational | Cell Rep Med | Gut commensal bacteria (Blautia wexlerae) promote azathioprine failure by reducing 6-mercaptopurine bioavailability |
| [32799195](https://pubmed.ncbi.nlm.nih.gov/32799195/) | 2020 | Review | Digestion | Association between IBD and malignancy |
| [34287682](https://pubmed.ncbi.nlm.nih.gov/34287682/) | 2021 | Review | J Gastroenterol | Thiopurine pharmacogenomics and pregnancy in IBD, including NUDT15-associated myelotoxicity |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02236819 | TEVA-AZATHIOPRINE | Not specified | Not specified |
| 00004596 | IMURAN | Not specified | Not specified |
| 02242907 | APO-AZATHIOPRINE | Not specified | Not specified |

---

## Safety Considerations

- **Drug interactions:** 100 interactions were identified in total. The main ones are:
  - **Moderate:** mesalazine, balsalazide, olsalazine, sulfasalazine (5-aminosalicylates)
  - **Minor:** zinc acetate, zinc gluconate, zinc sulfate
  - **Unclassified severity:** epinephrine, amphotericin B, acetylsalicylic acid, calcitriol, pantoprazole, omeprazole, glimepiride, doxycycline, clotrimazole, morphine, metformin, sucralfate, rosiglitazone
- **Disease-level cautions from the knowledge graph:** The following conditions are flagged as contraindication-related: pancreatitis, thrombocytopenia, anaemia (including macrocytic anaemia), impaired renal function, fungal infections and dermatophytosis, infectious disease in general, lymphomas (including primary CNS lymphoma, lymphosarcoma and hepatosplenic T-cell lymphoma), and hepatic vein thrombosis / Budd-Chiari syndrome. These come from graph relationships, not label text.
- **Practical guardrails for IBD or UC use:** TPMT/NUDT15 genotyping, metabolite monitoring, regular blood count and liver monitoring, and surveillance for infection and malignancy (lymphoma, skin cancer).

Please refer to the package insert for the full official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, colobomatous microphthalmia-rhizomelic dysplasia syndrome)

**Rationale:**
The top prediction has a very high model score but no clinical trials, no literature, and no plausible mechanism. It is evidence level L5 and most likely a graph artifact. The same applies to the other developmental and skeletal syndromes in the top ten. For comparison, inflammatory bowel disease and ulcerative colitis are rated L1 with a "Proceed with Guardrails" recommendation. They are not novel findings, though, because azathioprine is already established in these conditions, and many of the supporting trials use azathioprine only as a comparator or combination partner, with several terminated early with small enrollment.

**To proceed, the following is needed:**
- For the top prediction: independent biological evidence linking azathioprine to the disease mechanism, which is currently absent. Without it, no further development is recommended.
- Mechanism-of-action data from DrugBank.
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening.
- Approved indication text, dosage forms and manufacturers for the three Canadian licences.
- If the goal is a genuine repurposing candidate, re-run the evaluation focused on predictions with a plausible mechanism, and clarify whether established uses such as IBD or UC count as new indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

