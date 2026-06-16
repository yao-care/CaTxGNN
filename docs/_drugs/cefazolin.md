---
layout: default
title: Cefazolin
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 8
---

# Cefazolin
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

# Cefazolin: From Surgical Prophylaxis to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic widely used as a perioperative surgical prophylaxis agent and for treatment of gram-positive bacterial infections involving skin, soft tissue, and urinary tract.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**, with **1 clinical trial** and **3 publications** currently supporting this direction.
This prediction carries a critical mechanistic caveat: Cefazolin's limited coverage of *Haemophilus influenzae* and *Moraxella catarrhalis* — which together account for approximately 50% of acute otitis media (AOM) pathogens — significantly constrains its role as a broad empiric first-line agent for this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Canadian regulatory data available (Cefazolin is a first-generation cephalosporin used for surgical prophylaxis and gram-positive bacterial infections) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Cefazolin is a first-generation cephalosporin that kills bacteria by irreversibly binding to penicillin-binding proteins (PBPs), thereby blocking cell wall peptidoglycan cross-linking and causing bacterial lysis. This bactericidal mechanism is particularly potent against gram-positive organisms including *Staphylococcus aureus* (MSSA) and *Streptococcus pneumoniae* — both recognized pathogens in acute otitis media. *S. pneumoniae* alone accounts for approximately 30–40% of AOM cases, placing Cefazolin within a pharmacologically plausible range for a subset of infections.

The TxGNN model's prediction likely reflects the structural proximity in its knowledge graph between first-generation cephalosporins and the cluster of otitis media disease nodes. Supporting this, a 2025 case series (PMID 39567876) documents the use of Ceftazidime-Cefazolin combination therapy in pediatric Gradenigo Syndrome — a rare intracranial complication of acute otitis media — representing the most current direct clinical precedent for Cefazolin use in an AOM-related context. A 1982 comparative study (PMID 6752467, captured under suppurative otitis media) also directly compared Cefazolin against cefmetazole in suppurative otitis media with measurable efficacy.

However, the prediction has a critical structural limitation: *H. influenzae* and *M. catarrhalis* together cause approximately 40–50% of AOM episodes, and Cefazolin has intrinsically poor activity against these gram-negative organisms due to susceptibility to their beta-lactamases. This spectral gap disqualifies Cefazolin from broad undifferentiated AOM empiric therapy. Its role, if any, is confined to culture-directed or surgically-contexted scenarios where gram-positive predominance is confirmed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Multicenter, randomized, double-blind, placebo-controlled RCT comparing 5-day vs. 10-day antibiotic courses in children aged 6–23 months with AOM, targeting antimicrobial resistance reduction. Trial was terminated early; reason undisclosed — no positive efficacy conclusion can be drawn. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Review | Southern Medical Journal | Review of cephalosporin class efficacy in pediatric infections including otitis media; highlights high inhibitory activity against gram-positive cocci and utility in penicillin-hypersensitive patients. Cefazolin specifically noted. |
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case Series | Annals of Otology, Rhinology & Laryngology | Ceftazidime-Cefazolin empiric combination used in pediatric Gradenigo Syndrome (petrous apicitis as a complication of acute otitis media); provides the most recent and direct evidence of Cefazolin being used in the AOM complication spectrum. |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Case Review | Clinical Pharmacy | Stevens-Johnson syndrome case in a child treated for otitis media; IV Cefazolin appears as part of the treatment course — indirect evidence only, not a primary efficacy study. |

---

## Canada Market Information

Cefazolin (DB01327) has no recorded product licenses in the Canadian regulatory database at the time of this report (data cutoff: 2026-06-15). No Drug Identification Numbers (DINs) are currently listed.

> **Note for verification:** Cefazolin is a widely available generic antibiotic in many jurisdictions. The absence of DINs in this dataset warrants direct confirmation against the Health Canada Drug Product Database, as data collection gaps may account for this finding.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data including key warnings, contraindications, and drug interactions were not available in this evidence pack (Data Gap DG001: TFDA package insert not yet retrieved). This is classified as a **Blocking** gap that must be resolved before any clinical safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole registered clinical trial (NCT01511107) was terminated before completion, yielding no positive efficacy conclusions, and the three available publications provide only indirect or case-level support for the top predicted indication (infectious otitis media). More critically, Cefazolin's inherent spectrum gap against *H. influenzae* and *M. catarrhalis* — the cause of ~50% of AOM cases — makes a broad claim for this indication pharmacologically untenable at this time.

**Stronger signal identified in adjacent indication:**
The rank 3 prediction — **Middle Ear Disease** (specifically perioperative surgical prophylaxis) — carries **L2 evidence** with a **"Proceed with Guardrails"** recommendation. Two clinical trials (including an active Phase 4 RCT, NCT03014687) and 11 publications support Cefazolin's well-established role as a gold-standard perioperative antibiotic for ear canal and mastoid surgeries. This sub-indication warrants a separate, prioritized evaluation.

**To proceed with either indication, the following is needed:**

- **Safety data (Blocking):** Retrieve and parse the Health Canada/TFDA package insert to obtain warnings, contraindications, and drug interaction information (Data Gap DG001)
- **MOA documentation (High priority):** Query DrugBank API for formal mechanism of action to complete the mechanistic rationale (Data Gap DG002)
- **Regulatory verification:** Confirm Cefazolin's actual Canadian DIN status directly against the Health Canada Drug Product Database — the current "Not Marketed" flag may reflect a data gap rather than genuine absence from the market
- **Target population definition:** For infectious otitis media, identify gram-positive-dominant AOM subpopulations (e.g., post-surgical otitis, culture-confirmed MSSA, penicillin-allergic patients requiring IV therapy) where Cefazolin's narrow spectrum is clinically appropriate
- **MRSA prevalence assessment:** Cefazolin is inactive against MRSA; local epidemiological data for target patient populations must be reviewed before any surgical prophylaxis protocol is designed
- **Separate report for middle ear disease:** Given the superior evidence profile (L2, Phase 4 RCT), a dedicated evaluation focused on perioperative prophylaxis in otologic surgery is recommended as the higher-priority next step
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

