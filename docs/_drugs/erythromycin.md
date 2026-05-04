---
layout: default
title: Erythromycin
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 5
---

# Erythromycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Erythromycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Erythromycin is a macrolide antibiotic with well-established clinical use for a broad range of bacterial infections, including respiratory tract infections, skin and soft tissue infections, and sexually transmitted diseases caused by *Chlamydia trachomatis*.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis** (top prediction, score 99.89%), with **0 clinical trials** and **2 publications** currently supporting this specific direction.
This is a multi-indication evidence pack covering 5 predicted indications; notably, **Lymphogranuloma Venereum** (rank 4) carries the strongest evidence at L3 level with 1 Phase 4 clinical trial and 20 publications — and is already cited in CDC/WHO guidelines as an indication for erythromycin.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Canada DIN records available (data gap — see note below) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Canada Market Status | Not found in evidence pack (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

> **Note on Canada market status:** The evidence pack returns 0 DINs for erythromycin, which is inconsistent with erythromycin's known status as a long-established antibiotic likely available in Canada under multiple brand names (e.g., Erythrocin, PCE). A direct Health Canada Drug Product Database query is required to resolve this data gap before regulatory status can be confirmed.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on established pharmacological knowledge, erythromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit, blocking translocation and peptide chain elongation. Its spectrum covers gram-positive bacteria (*Staphylococcus*, *Streptococcus*), atypical intracellular pathogens (*Chlamydia trachomatis*, *Mycoplasma pneumoniae*), and select gram-negative organisms (*Haemophilus influenzae*).

Punctate epithelial keratoconjunctivitis (PEK) is a superficial corneal and conjunctival inflammatory condition frequently associated with bacterial pathogens — most notably *Chlamydia trachomatis* and staphylococcal blepharitis — both of which fall squarely within erythromycin's antibacterial coverage. Crucially, erythromycin ophthalmic ointment 0.5% is an approved topical formulation for bacterial ocular infections (including neonatal ophthalmia prophylaxis) in the United States and other markets, establishing local ocular delivery as a clinically feasible and already-validated route.

However, PEK as a distinct diagnostic entity has not been directly studied in the available literature collected for this prediction. The two supporting publications address related but non-identical conditions — blepharokeratoconjunctivitis in children (PMID 11495307) and microsporidia keratoconjunctivitis in an adult (PMID 32826651) — providing only indirect mechanistic and contextual support. The high TxGNN score likely reflects the model recognising erythromycin's broad antimicrobial-ocular disease relationship rather than PEK-specific clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for erythromycin in punctate epithelial keratoconjunctivitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Narrative Review / Case Series | Journal of Pediatric Ophthalmology and Strabismus | Describes the history, symptoms, clinical signs, and antibiotic management of blepharokeratoconjunctivitis in children; provides clinical context for topical antibiotic use in overlapping ocular inflammatory/infectious conditions |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | Cornea | Reports microsporidia (*Encephalitozoon hellem*) keratoconjunctivitis in an immunocompetent adult acquired through avian transmission, diagnosed by metagenomic deep sequencing and confirmed by PCR; highlights the diagnostic challenge in atypical keratoconjunctivitis |

---

## Canada Market Information

No DIN records were retrieved for erythromycin in this evidence pack (`total_licenses: 0`). This is likely a data completeness issue rather than a true absence from the Canadian market. A targeted query to the Health Canada Drug Product Database is required to retrieve current approved indications, dosage forms, and DIN list.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Data gaps identified: TFDA/Health Canada package insert warnings (DG001, Blocking severity) and contraindications data have not been retrieved in this evidence pack. This must be resolved before any S1 safety evaluation can proceed.

---

## Additional Predicted Indications

This evidence pack covers 5 predicted indications. The table below summarises all findings:

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Publications | Recommendation |
|------|---------|------------|----------------|--------|-------------|----------------|
| 1 | Punctate Epithelial Keratoconjunctivitis | 99.89% | L4 | 0 | 2 | Hold |
| 2 | Acute Contagious Conjunctivitis | 99.55% | L5 | 0 | 0 | Hold |
| 3 | Exposure Keratitis | 99.50% | L4 | 0 | 8 | Hold |
| **4** | **Lymphogranuloma Venereum** | **99.05%** | **L3** | **1** | **20** | **Proceed with Guardrails** |
| 5 | Necrotizing Ulcerative Gingivitis | 99.00% | L4 | 0 | 5 | Hold |

### Lymphogranuloma Venereum — Highlighted Evidence (Rank 4)

**Lymphogranuloma venereum (LGV)** represents the most clinically actionable finding in this evidence pack. LGV is caused by *Chlamydia trachomatis* serovars L1/L2/L3 — the same intracellular pathogen for which erythromycin's 50S ribosomal inhibition is mechanistically well-established.

**Clinical Trial:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT03608774](https://clinicaltrials.gov/study/NCT03608774) | Phase 4 | Completed | 177 | Double-blind RCT comparing azithromycin vs. doxycycline for rectal *Chlamydia trachomatis* in MSM. Azithromycin is a macrolide (same class as erythromycin), directly validating macrolide class efficacy against the LGV pathogen |

**Selected Literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33462582](https://pubmed.ncbi.nlm.nih.gov/33462582/) | 2021 | Case Series / Observational | Clinical Infectious Diseases | Weekly oral azithromycin 1 g × 3 weeks demonstrated effective treatment of LGV proctitis in MSM in Europe; supports macrolide class efficacy |
| [40815293](https://pubmed.ncbi.nlm.nih.gov/40815293/) | 2025 | Cohort / Registry | Sexually Transmitted Diseases | Alberta, Canada LGV surveillance 2018–2022 among gbMSM; characterises epidemiology and treatment patterns in the Canadian context — directly relevant to a Canada-focused repurposing evaluation |
| [22760150](https://pubmed.ncbi.nlm.nih.gov/22760150/) | 2012 | Case Report | Rev Soc Bras Med Trop | LGV patient treated with erythromycin directly; confirms historical clinical use |
| [13239093](https://pubmed.ncbi.nlm.nih.gov/13239093/) | 1955 | Uncontrolled Clinical Series | Antibiotic Medicine & Clinical Therapy | Erythromycin–triple sulfonamide combination in early LGV treatment; earliest direct erythromycin–LGV evidence |
| [25870512](https://pubmed.ncbi.nlm.nih.gov/25870512/) | 2015 | Review | Infection and Drug Resistance | Comprehensive LGV diagnostic and treatment review; doxycycline first-line, erythromycin and azithromycin as alternatives |
| [2246945](https://pubmed.ncbi.nlm.nih.gov/2246945/) | 1990 | Review | Medical Clinics of North America | Reviews *Chlamydia trachomatis* infections including LGV; erythromycin cited for treatment in penicillin-contraindicated patients |
| [3545650](https://pubmed.ncbi.nlm.nih.gov/3545650/) | 1987 | Review | Clinical Pharmacy | Erythromycin discussed as treatment for chlamydial genital infections including LGV in pregnancy contexts |

---

## Conclusion and Next Steps

**Decision: Hold** *(for Rank 1 — Punctate Epithelial Keratoconjunctivitis)*

**Rationale:**
Evidence for erythromycin in punctate epithelial keratoconjunctivitis as a specific diagnostic entity is limited to indirect mechanism-based and contextual literature (L4); no clinical trials and no PEK-directed publications are available.

---

**Decision: Proceed with Guardrails** *(for Rank 4 — Lymphogranuloma Venereum)*

**Rationale:**
Erythromycin is already cited as an alternative treatment for LGV in CDC and WHO sexually transmitted infection treatment guidelines (particularly in pregnancy, where doxycycline is contraindicated), supported by observational studies, historical clinical series, and a completed Phase 4 macrolide-class RCT (L3). The Alberta, Canada surveillance data (PMID 40815293) further confirms ongoing LGV activity in Canadian gbMSM populations, demonstrating local clinical relevance.

---

**To proceed, the following is needed:**

- **Resolve data gaps first:**
  - Query Health Canada Drug Product Database to confirm DIN list and approved indications for erythromycin
  - Download and parse TFDA/Health Canada package insert to extract warnings and contraindications (DG001 — Blocking)
  - Retrieve MOA data from DrugBank API (DG002)

- **For PEK (Rank 1) — before any advancement:**
  - Conduct a focused literature search specifically for erythromycin ophthalmic ointment in PEK or related superficial keratitis
  - Consider a prospective case series as a minimum study design given the established ophthalmic dosage form

- **For LGV (Rank 4) — actionable next steps:**
  - Confirm alignment with current Canadian STI guidelines (PHAC/CATIE) for erythromycin as alternative treatment
  - Evaluate pregnancy population sub-indication (doxycycline-contraindicated patients) as a priority use case
  - Prepare a clinical use recommendation brief citing CDC guideline support and Canadian epidemiological data

- **For Exposure Keratitis (Rank 3):**
  - Review the 8 available publications for direct erythromycin prophylaxis evidence in lagophthalmos-related exposure; erythromycin ointment as a lubricant-antibiotic combination has clinical plausibility worth formalising
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

