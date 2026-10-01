---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 606
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Anaerobic Bacterial and Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is an antimicrobial used against anaerobic bacteria and protozoa. The TxGNN model predicts it may be effective for **pneumocystosis**, but the retrieved evidence does not support this. All **23 retrieved clinical trials** are unrelated to the drug, and the **10 publications** are reviews and case reports with no evidence of benefit. The high score is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaerobic bacterial and protozoal infections (general class use; the Canadian licence records contain no indication text) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Metronidazole is generally understood to work through reduction of its nitro group inside anaerobic bacteria and protozoa, which damages their DNA.

*Pneumocystis* is a fungus and lacks this activation pathway, so there is no plausible mechanistic link. The standard therapy for *Pneumocystis* pneumonia is trimethoprim-sulfamethoxazole. A 1980 review (PMID 7355683) lists metronidazole for amebiasis and trichomoniasis, not for pneumocystis.

The 0.9999 score most likely reflects the drug's membership in the antiparasitic class within the knowledge graph. It should not be treated as clinical evidence.

---

## Clinical Trial Evidence

The search returned 23 trials, and none tests metronidazole or targets pneumocystosis. Ten graded trials are shown below; the remaining 13 were not graded but are also unrelated by title and summary (health-services, behavioural and device studies).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02571673](https://clinicaltrials.gov/study/NCT02571673) | N/A | Completed | 65 | Head and neck cancer survivorship tool feasibility. Unrelated. |
| [NCT01909076](https://clinicaltrials.gov/study/NCT01909076) | N/A | Completed | 53 | Opioid risk reduction in primary care. Unrelated. |
| [NCT06160947](https://clinicaltrials.gov/study/NCT06160947) | N/A | Not yet recruiting | 24 | Chiropractic care and opioid use in spinal pain. Unrelated. |
| [NCT06597123](https://clinicaltrials.gov/study/NCT06597123) | N/A | Not yet recruiting | 150 | AI-augmented motivational interviewing training. Unrelated. |
| [NCT03466866](https://clinicaltrials.gov/study/NCT03466866) | Phase 3 | Completed | 156 | Diabetes education intervention. The Phase 3 label is not drug evidence. |
| [NCT03451630](https://clinicaltrials.gov/study/NCT03451630) | N/A | Completed | 1400 | Integrated care models for publicly insured adults. Unrelated. |
| [NCT05256303](https://clinicaltrials.gov/study/NCT05256303) | N/A | Completed | 160 | Hospital-at-home delivery model. Unrelated. |
| [NCT03542084](https://clinicaltrials.gov/study/NCT03542084) | N/A | Completed | 305 | Endocrinology e-consults for glycemic control. Unrelated. |
| [NCT02208947](https://clinicaltrials.gov/study/NCT02208947) | Phase 3 | Terminated | 77 | Advance care planning incentives. The Phase 3 label is not drug evidence. |
| [NCT05892666](https://clinicaltrials.gov/study/NCT05892666) | N/A | Recruiting | 4000 | Care-delivery comparison across clinic settings. Unrelated. |

---

## Literature Evidence

The 10 publications are all reviews or case reports, with no RCTs. None shows that metronidazole treats pneumocystosis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Metronidazole is the drug of choice for amebic colitis and trichomoniasis. Trimethoprim-sulfamethoxazole is the choice for pneumocystis pneumonia. |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | General overview of antiparasitic agents and their limitations. |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Pharmacokinetic rationale for antiprotozoal therapy. |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV-related opportunistic infections remain relevant. No metronidazole role shown. |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | Infectious complications of AIDS, including *P. carinii* pneumonia. |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | *P. carinii* and CMV pneumonia in a healthy adult who had previously received metronidazole for diarrhea. This is not a treatment result. |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | Two AIDS patients. Metronidazole treated amebic dysentery, and pneumocystis pneumonia occurred separately. |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | Amoebic and CMV colitis with perforation in an AIDS patient. |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | Critique of antimicrobial prophylaxis trials. |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | Drugs used against protozoan infections in humans. |

---

## Canada Market Information

Five of the 15 authorizations are shown. Dosage form and approved indication text are not present in the licence records.

| DIN | Product Name |
|---------|------|
| 02092832 | METROGEL 0.75% |
| 02297809 | METROGEL 1% |
| 02518767 | METRONIDAZOLE |
| 02519755 | M-METRONIDAZOLE |
| 00545066 | APO-METRONIDAZOLE TABLETS |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no relevant trials, no supportive literature and no plausible mechanism, since pneumocystis is a fungus and standard therapy is trimethoprim-sulfamethoxazole.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism-of-action data from DrugBank
- Any direct in vitro or clinical evidence that metronidazole has activity against *Pneumocystis*

**Other candidates for this drug:** two lower-ranked predictions were flagged as research questions and have more plausible support than pneumocystosis:
- **Cap polyposis:** case reports describe remission with metronidazole, and PMID 12141801 proposes an anti-inflammatory mechanism.
- **Vulvar ulceration:** the support comes from cause-specific case reports (amoebic and Crohn's-related), so a structured case series would be needed before the generic label could be assessed.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

