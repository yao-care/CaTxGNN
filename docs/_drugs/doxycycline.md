---
layout: default
title: Doxycycline
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
---

# Doxycycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Doxycycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Doxycycline is a broad-spectrum tetracycline antibiotic with well-established efficacy against intracellular pathogens including *Chlamydia trachomatis*, *Rickettsia* species, *Borrelia burgdorferi*, and *Mycoplasma* — though no formal original indication is recorded in the current regulatory dataset.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**, a corneal surface condition that can occur as a sequela to chlamydial infection,
with **0 clinical trials** and **1 publication** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in current regulatory dataset (doxycycline is a broad-spectrum antibiotic for bacterial infections) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, doxycycline is a broad-spectrum tetracycline antibiotic with potent activity against *Chlamydia trachomatis* and related intracellular organisms. Its efficacy as a first-line treatment for chlamydial infections — including ocular trachoma and follicular conjunctivitis — is well-established in clinical guidelines, and this antimicrobial backbone forms the core of the model's prediction.

Punctate epithelial keratoconjunctivitis (PEK) is a corneal surface disorder characterized by small fluorescein-staining lesions at multiple levels of the corneal epithelium. The mechanistic link to doxycycline is primarily *indirect*: chlamydial follicular conjunctivitis can resolve while leaving behind persistent residual corneal pathology in the form of PEK. By fully eradicating the underlying *C. trachomatis* infection, doxycycline may prevent progression to or accelerate resolution of this post-infectious corneal sequela. The sole supporting publication (PMID 1424659, 1992) describes precisely this clinical scenario: bilateral gray punctate epithelial lesions persisting after oral tetracycline or doxycycline treatment for chlamydial conjunctivitis.

In addition to its antimicrobial role, doxycycline possesses anti-MMP (matrix metalloproteinase) and anti-inflammatory properties that theoretically could promote corneal epithelial barrier restoration and reduce stromal edema associated with PEK lesions. However, this mechanism remains speculative and extrapolated from periodontal and pulmonary research; it has not been directly validated for corneal disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Series | *Cornea* | Two patients with *Chlamydia trachomatis* follicular conjunctivitis treated with oral tetracycline or doxycycline achieved resolution of follicles, but subsequently developed recurrent bilateral gray punctate epithelial lesions staining with fluorescein, with anterior stromal edema in one case — suggesting PEK as a persistent post-infectious corneal sequela |

---

## Canada Market Information

No regulatory authorizations (DINs) are currently on file for doxycycline in this dataset. The drug is recorded as **not marketed** with zero active licenses.

> **Note:** Doxycycline is a long-established generic antibiotic marketed globally under numerous brand names (e.g., Vibramycin, Doryx, Periostat). The absence of DINs in this dataset likely reflects a data gap rather than true non-availability. Verification via Health Canada's Drug Product Database is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, and drug–drug interactions) are not available in the current evidence pack. Retrieval of the TFDA/Health Canada product monograph is flagged as a **blocking data gap (DG001)** that must be resolved before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The single available publication (a 1992 case series) does not demonstrate that doxycycline *treats* PEK — it describes PEK as a condition that *persists despite* doxycycline treatment of the underlying infection, which actually raises questions about whether the drug is sufficient for this indication. The mechanistic connection is indirect and the evidence base is insufficient to support further development without targeted research.

**To proceed, the following is needed:**

- **Clarify the clinical question:** Distinguish between (a) doxycycline preventing PEK by fully eradicating chlamydial infection vs. (b) doxycycline directly treating established PEK via MMP inhibition or anti-inflammatory effects
- **Safety data:** Retrieve and review TFDA/Health Canada package insert warnings, contraindications, and DDI profile (Blocking data gap DG001)
- **MOA data:** Confirm mechanism of action via DrugBank (High-priority data gap DG002)
- **Regulatory verification:** Confirm actual Canada market availability via Health Canada Drug Product Database
- **Prospective case series:** Design a targeted observational study measuring corneal outcomes (slit-lamp PEK scores, fluorescein staining area) in patients receiving doxycycline for chlamydial conjunctivitis
- **Route compatibility assessment:** Evaluate whether systemic oral dosing or topical ophthalmic doxycycline formulations are more appropriate for this indication
- **Comparative literature review:** Search for studies on tetracycline-class drugs in other forms of infectious keratoconjunctivitis to strengthen mechanistic plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

