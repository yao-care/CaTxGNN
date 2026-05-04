---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Amoxicillin: From Bacterial Infections to Monoclonal Gammopathy (IPSID Subtype)

## One-Sentence Summary

Amoxicillin is a broad-spectrum penicillin-class antibiotic used to treat a wide range of bacterial infections, including respiratory, urinary, and gastrointestinal tract infections.
The TxGNN model predicts it may be relevant to **Monoclonal Gammopathy** — specifically the immunoproliferative small intestinal disease (IPSID) subtype, where chronic bacterial infection drives B-cell clonal expansion — with **1 clinical trial** and **11 publications** providing the strongest evidence base among all 8 predicted indications in this report.
This prediction is biologically plausible but strictly limited to early-stage IPSID and **cannot be extrapolated to MGUS, multiple myeloma, or Waldenström's macroglobulinemia**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (standard antibiotic use; no regulatory license data available) |
| Predicted New Indication | Monoclonal Gammopathy (IPSID subtype) |
| TxGNN Prediction Score | 99.22% (Rank 6 of 8 in predicted set; highest evidence level) |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed (0 licenses on file) |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

> **Note on prediction selection:** Eight indications were predicted for this candidate (TW-DB01060-multi). Ranks 1–5 and rank 7 all carry L5 evidence with a "Hold" recommendation and no supporting clinical or preclinical data. Rank 6 (Monoclonal Gammopathy) is the highest-evidence prediction (L3) and is the focus of this report. Rank 8 (Septicemic Plague) carries L4 preclinical evidence and is summarised at the end.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Amoxicillin is a β-lactam antibiotic that inhibits bacterial cell wall synthesis by irreversibly binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and triggering autolytic bacterial cell lysis. It provides broad-spectrum bactericidal activity against gram-positive cocci and many gram-negative organisms.

The connection to monoclonal gammopathy rests on a specific and well-characterised biological mechanism applicable **only to IPSID (Immunoproliferative Small Intestinal Disease)**, also known as Mediterranean lymphoma or alpha heavy-chain disease. IPSID is an extranodal marginal zone B-cell lymphoma driven by chronic mucosal bacterial infection — most often *Campylobacter jejuni* and historically *Helicobacter pylori* — in which persistent bacterial antigen stimulation drives polyclonal, then oligoclonal, then monoclonal IgA heavy-chain-secreting B-cell expansion. Eliminating the bacterial antigen driver through antibiotic therapy can deprive the clonal population of its survival signal, enabling tumor regression in early-stage disease.

This mechanism is directly analogous to the well-established *H. pylori* eradication model for gastric MALT lymphoma, where triple therapy containing Amoxicillin + Clarithromycin + proton pump inhibitor achieves complete remission in up to 80% of early-stage cases. Multiple case reports — including a landmark 1997 *Lancet* publication (PMID 8988128) and a 2010 case series (PMID 20300878) — document IPSID regression following *H. pylori* eradication regimens. A 1996 Japanese case report (PMID 9030995) documents Mediterranean lymphoma treated successfully with antibiotics. This evidence base, while case-level only, provides mechanistic coherence that justifies a "Research Question" designation rather than an outright rejection.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | NA | Terminated | 351 | Oral empirical antibiotic therapy (Amoxicillin/Clavulanic acid + Ciprofloxacin vs. Moxifloxacin monotherapy) for fever in low-risk neutropenic cancer patients. This is a supportive care study — the enrolled population includes hematologic cancer patients but the endpoint is infection control, not monoclonal gammopathy treatment. Trial was terminated early. Not interpretable as evidence for IPSID therapy. Relevance grade: C (peripheral). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8988128](https://pubmed.ncbi.nlm.nih.gov/8988128/) | 1997 | Case Report / Retrospective Review | *Lancet* | **Landmark case:** Regression of IPSID after *H. pylori* eradication — direct evidence that antibiotic-based eradication therapy (Amoxicillin-containing triple therapy) can induce IPSID tumor regression. |
| [9030995](https://pubmed.ncbi.nlm.nih.gov/9030995/) | 1996 | Retrospective Case Series | *Internal Medicine* (Tokyo) | Mediterranean lymphoma (IPSID) treated with antibiotics — a 74-year-old with IgA heavy-chain secreting lymphoplasmacytic infiltration responded to antibiotic treatment; supports the bacterial-antigen-driven model. |
| [20300878](https://pubmed.ncbi.nlm.nih.gov/20300878/) | 2010 | Case Report / Retrospective Review | *Journal of Gastrointestinal Cancer* | Regression of IPSID after *H. pylori* eradication in a 20-year-old with extensive proximal small-bowel thickening and mesenteric lymphadenopathy — achieved remission following eradication therapy. |
| [16253033](https://pubmed.ncbi.nlm.nih.gov/16253033/) | 2005 | Case Report | *Archives of Pathology & Laboratory Medicine* | Nonsecretory variant of IPSID — molecular and immunophenotypic characterisation of an extranodal marginal zone B-cell lymphoma; contextualises disease biology. |
| [21908119](https://pubmed.ncbi.nlm.nih.gov/21908119/) | 2011 | Case Report | *Médecine et Maladies Infectieuses* | Pneumonia and *Rothia dentocariosa* in a haematology patient — Amoxicillin used for secondary bacterial infection; incidental to monoclonal gammopathy. |
| [35619805](https://pubmed.ncbi.nlm.nih.gov/35619805/) | 2022 | Case Report | *Frontiers in Public Health* | Disseminated nocardiosis in a patient with macroglobulinemia — Amoxicillin/clavulanic acid listed as susceptible agent in antimicrobial sensitivity panel; Amoxicillin not used as primary treatment for macroglobulinemia. |
| [20513124](https://pubmed.ncbi.nlm.nih.gov/20513124/) | 2010 | Diagnostic Accuracy Study | *American Journal of Hematology* | High false-positive Aspergillus galactomannan in multiple myeloma — context study in haematological malignancies; no direct Amoxicillin relevance. |
| [18639371](https://pubmed.ncbi.nlm.nih.gov/18639371/) | 2009 | Retrospective Cohort | *British Journal of Oral & Maxillofacial Surgery* | Bisphosphonate-associated osteonecrosis of the jaw (ONJ) — Amoxicillin used as wound prophylaxis in myeloma patients; coincidental use. |
| [20015614](https://pubmed.ncbi.nlm.nih.gov/20015614/) | 2010 | Case Series | *International Journal of Oral and Maxillofacial Surgery* | Surgical management of bisphosphonate-induced ONJ in 40 patients — Amoxicillin part of surgical antimicrobial protocol; not relevant to myeloma biology. |
| [22092390](https://pubmed.ncbi.nlm.nih.gov/22092390/) | 2012 | Retrospective Comparative Cohort | *Journal of Oral Pathology & Medicine* | BRONJ comparison between multiple myeloma and breast cancer — Amoxicillin used as part of standardised ONJ management; no implications for monoclonal gammopathy treatment. |

> **Evidence interpretation note:** Of the 11 publications retrieved, only PMIDs 8988128, 9030995, 20300878, and 16253033 are directly relevant to the IPSID-antibiotic hypothesis. The remaining 7 publications document Amoxicillin used for infectious complications or surgical prophylaxis in patients who coincidentally have haematological malignancies — they do not constitute evidence for repurposing.

---

## Safety Considerations

Safety data for this Evidence Pack has not been retrieved (Data Gap DG001: TFDA/Health Canada package insert warnings and contraindications pending). Please refer to the product package insert for complete prescribing information.

Based on well-established class knowledge:
- **Key Warnings:** Serious and potentially fatal hypersensitivity (anaphylactic) reactions reported in patients receiving penicillin-class antibiotics; cross-reactivity with cephalosporins possible. *Clostridioides difficile*-associated diarrhoea (CDAD) can occur during and after antibiotic use.
- **Contraindications:** History of serious hypersensitivity reaction (anaphylaxis or Stevens–Johnson syndrome) to any β-lactam antibiotic.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
There is a mechanistically coherent and biologically grounded rationale for Amoxicillin (as part of *H. pylori* eradication triple therapy) in early-stage IPSID — a rare bacterial-antigen-driven B-cell lymphoproliferative disorder that closely parallels the established gastric MALT lymphoma eradication model. Landmark publications including a *Lancet* case report document genuine tumour regression. However, all current evidence consists of case reports and small series; no RCTs exist, the indication is narrowly disease-subtype specific, and the evidence does not support use in other monoclonal gammopathy variants.

**To proceed, the following is needed:**

- Retrieve complete MOA data from DrugBank API (Data Gap DG002) to formally document PBP-binding mechanism and confirm no immunomodulatory off-target activity
- Retrieve Health Canada / TFDA package insert for complete warnings and contraindications (Data Gap DG001)
- Verify and correct market authorisation data — Amoxicillin is widely approved globally; the current "Not Marketed / 0 DINs" entry likely reflects a data collection gap
- Commission a systematic review of IPSID antibiotic treatment literature to quantify response rates and identify optimal regimen composition (Amoxicillin alone vs. triple therapy combination)
- Clarify whether the anti-tumour effect in IPSID is attributable to Amoxicillin specifically or to the triple-therapy combination (Amoxicillin + Clarithromycin + PPI)
- Consult current haematology guidelines for IPSID staging criteria (Stage I–II vs. III) to define the patient population most likely to benefit
- Consider prospective registry study or pilot trial in early-stage IPSID patients, particularly in regions of high IPSID prevalence (Middle East, North Africa, and South Asia)
- Formally exclude this indication pathway for MGUS, multiple myeloma, Waldenström's macroglobulinemia, and other non-IPSID monoclonal gammopathy subtypes

---

## Appendix: Summary of All 8 Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Rationale Summary |
|------|---------|------------|---------------|----------------|-------------------|
| 1 | Polyclonal Hyperviscosity Syndrome | 99.63% | L5 | Hold | No mechanistic link; likely topological false positive from blood/infection node clustering in knowledge graph |
| 2 | Hyperamylasemia | 99.63% | L5 | Hold | Laboratory marker, not a treatment target; Amoxicillin can paradoxically *cause* drug-induced pancreatitis |
| 3 | Congenital Analbuminemia | 99.59% | L5 | Hold | Monogenic disease (*ALB* loss-of-function); no biological rationale for antibiotic intervention |
| 4 | Blood Group Incompatibility | 99.40% | L5 | Hold | Sole literature finding (PMID 40350274) is a coincidental *Campylobacter* bacteraemia in an ABO-mismatched HSCT patient — Amoxicillin treated an infection, not the incompatibility |
| 5 | Premalignant Haematological System Disease | 99.29% | L5 | Hold | MDS/CHIP/SMM require targeted or watch-and-wait strategies; no antibiotic mechanism relevant |
| **6** | **Monoclonal Gammopathy (IPSID)** | **99.22%** | **L3** | **Research Question** | **Biologically plausible for IPSID subtype; H. pylori eradication therapy (Amoxicillin-containing) documented to induce IPSID regression — see full report above** |
| 7 | Haematological Disease with Acquired Peripheral Neuropathy | 99.14% | L5 | Hold | Paraprotein/amyloid-driven neuropathies (POEMS, AL) require targeted blood disorder therapy; no antibiotic mechanism |
| 8 | Septicemic Plague | 99.13% | L4 | Research Question | *In vitro* and murine studies show β-lactam activity against *Y. pestis*; however, clinical guidelines recommend aminoglycosides or fluoroquinolones as first-line due to β-lactamase resistance concerns and intracellular penetration limitations |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

