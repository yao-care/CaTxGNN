---
layout: default
title: Magnesium Sulfate
parent: Model Prediction Only (L5)
nav_order: 571
evidence_level: L5
indication_count: 8
monitor_inn: "MAGNESIUM SULFATE"
predicted_indications: ["thrombotic disease", "pharyngitis", "nasal cavity disease", "psychotic disorder", "acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia", "treatment-refractory schizophrenia"]
last_modified_at: 2026-11-03
description: "Magnesium Sulfate: predicted new indication Thrombotic disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Magnesium Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Magnesium Sulfate: Thrombotic disease
{: .text-alpha }

## One-Sentence Summary

Magnesium sulfate is an injectable magnesium salt that is marketed in Canada under several licences.
The TxGNN model predicts it may be useful for **thrombotic disease**.
Support is limited: **one Phase 3 trial** in a specific thrombotic condition (thrombotic thrombocytopenic purpura) with an unknown status and no results, plus mostly animal and small human studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 8 of 8) |
| Number of DINs | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the retrieved literature, magnesium is a calcium antagonist that may reduce platelet aggregation and deposition. Animal studies show that magnesium sulfate reduced platelet deposition and thrombus formation after arterial injury. In one rat study it also impaired coagulation.

This gives a plausible biological link to thrombosis, but the link rests mainly on preclinical work. The only registered trial studies thrombotic thrombocytopenic purpura (TTP), a specific microangiopathy caused by ADAMTS13 deficiency. It does not test thrombotic disease in general. The strength of the link is therefore uncertain, and the prediction should be treated as a research question rather than an actionable indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03237819](https://clinicaltrials.gov/study/NCT03237819) | Phase 3 | Unknown | 74 | Multicentre randomized trial of magnesium sulfate in TTP in intensive care. No results available and status unverified. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11816720](https://pubmed.ncbi.nlm.nih.gov/11816720/) | 2001 | Preclinical | Thrombosis and Haemostasis | IV magnesium prevented or delayed FeCl3-induced carotid thrombosis in rats, with impaired coagulation in vivo. |
| [3441141](https://pubmed.ncbi.nlm.nih.gov/3441141/) | 1987 | Preclinical | Magnesium | Antithrombogenic effect at sites of endothelial damage after partial coronary and carotid constriction in dogs and rabbits. |
| [7368083](https://pubmed.ncbi.nlm.nih.gov/7368083/) | 1980 | Preclinical | Surgery | Reduced platelet deposition in rabbit arteries after temporary clip occlusion. |
| [14506544](https://pubmed.ncbi.nlm.nih.gov/14506544/) | 2003 | Pilot study (non-randomized) | J Cardiovasc Pharmacol Ther | Feasibility of magnesium administration in patients undergoing non-acute coronary intervention with stent implantation. |
| [3724238](https://pubmed.ncbi.nlm.nih.gov/3724238/) | 1986 | Clinical study | Magnesium | In 15 patients with Prinzmetal's angina, magnesium terminated and prevented cold-induced vasoconstriction. This concerns vasospasm rather than thrombosis. |
| [8024163](https://pubmed.ncbi.nlm.nih.gov/8024163/) | 1994 | Clinical study | Angiology | Magnesium infusion and noradrenaline levels in primary Raynaud's phenomenon (vascular, not thrombotic). |
| [14168822](https://pubmed.ncbi.nlm.nih.gov/14168822/) | 1964 | Historical report | The Practitioner | Parenteral magnesium sulphate in arterial disease. No abstract available. |
| [27749350](https://pubmed.ncbi.nlm.nih.gov/27749350/) | 2016 | Systematic review | Anesthesia & Analgesia | Review of interventions to reduce blood loss in spine surgery. Only tangentially related. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02139499 | Magnesium Sulfate Injection, USP |
| 02513161 | Magnesium Sulfate Injection, BP 49.3% |
| 02542153 | Magnesium Sulfate in Water for Injection |
| 00392618 | Magnesium Sulfate Injection USP |

Eight licences are listed in total, all valid. Dosage form and indication text are not recorded in the local data.

## Safety Considerations

- **Drug Interactions**: 92 interactions are recorded. Major-level interactions include dolutegravir, amikacin and bictegravir. Moderate-level interactions include nifedipine, amlodipine, doxycycline, tetracycline, ciprofloxacin, cisatracurium, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), bisphosphonates (alendronic acid, risedronic acid, ibandronate), and vitamin D forms (cholecalciferol, calcifediol, calcitriol).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No cited study directly addresses thrombotic disease as a whole. The only trial concerns TTP, has an unknown status and no results, and the rest of the evidence is largely animal studies or off-target. The model score is high (0.9990), but it is not backed by clinical evidence for this indication.

**To proceed, the following is needed:**
- Results or status confirmation for NCT03237819, and a decision on which thrombotic condition to target
- Mechanism of action data and a defined thrombotic indication
- Human efficacy data in the chosen thrombotic condition, including dose and route
- Package insert warnings and contraindications, with a bleeding and interaction review given the recorded interactions

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

