---
layout: default
title: Treprostinil
parent: Model Prediction Only (L5)
nav_order: 939
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Treprostinil: predicted new indication Top-ranked by TxGNN: pulmonary arteriovenous malformation . Best-supp… (evidence level L5). Approved use: Pulmonary arterial hypertension"
monitor_inn: "TREPROSTINIL"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "pulmonary arterial hypertension associated with schistosomiasis", "pulmonary arterial hypertension associated with HIV infection", "pulmonary arterial hypertension associated with chronic hemolytic anemia", "pulmonary arterial hypertension associated with connective tissue disease", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "malformation syndrome with odontal and/or periodontal component", "Ambras type hypertrichosis universalis congenita"]
---

# Treprostinil
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

# Treprostinil: From Pulmonary Arterial Hypertension to PAH Associated with Connective Tissue Disease

## One-Sentence Summary

Treprostinil is a prostacyclin analogue originally used to treat pulmonary arterial hypertension (PAH).
The TxGNN model's top-ranked prediction is pulmonary arteriovenous malformation, but that prediction has no supporting evidence and a weak mechanistic rationale. The best-supported prediction is **PAH associated with connective tissue disease (CTD-PAH)**, which has **no registered clinical trials** but **19 publications**, including a placebo-controlled subcutaneous treprostinil trial and a 2024 systematic review. This report therefore focuses on CTD-PAH, with congenital heart disease-associated PAH as a second candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (Health Canada indication text is not available; taken from the knowledge-graph indication) |
| Predicted New Indication | Top-ranked by TxGNN: pulmonary arteriovenous malformation (not supported by evidence). Best-supported: PAH associated with connective tissue disease |
| TxGNN Prediction Score | 99.70% (top-ranked, pulmonary arteriovenous malformation); 99.55% (CTD-PAH) |
| Evidence Level | L3 for CTD-PAH (reviews, a meta-analysis, and cohort data; no completed Phase 3 RCT in the data) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Proceed with Guardrails (CTD-PAH, as a research question); Hold for the top-ranked prediction |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, treprostinil is a prostacyclin analogue that widens pulmonary and systemic blood vessels, inhibits platelet aggregation, and limits smooth muscle proliferation. Its efficacy in PAH has been established.

CTD-PAH, which occurs mainly in systemic sclerosis and lupus, is a Group 1 PAH subtype. It shares the pulmonary vascular remodeling and vasoconstriction of other PAH forms, so the prostacyclin pathway is mechanistically applicable. The literature includes a subcutaneous treprostinil study in CTD patients (2004) and a 2024 systematic review of CTD-PAH treatment.

It is worth noting that the predicted "new" indication is closely related to the original one. CTD-PAH is a PAH subgroup, so this is more an extension within the existing class-level indication than a distant repurposing.

The top-ranked prediction, pulmonary arteriovenous malformation, has a weak rationale. These are structural vascular shunts, and vasodilation could plausibly worsen shunting or hypoxaemia. The high score likely reflects network proximity to pulmonary vascular disease rather than a true therapeutic link. The hair and developmental disorders ranked 7 to 10 (hypotrichosis simplex of the scalp, congenital hypotrichosis milia, a malformation syndrome with odontal and/or periodontal component, and Ambras-type hypertrichosis) have no identified mechanism and are not supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Selected publications for CTD-PAH (listed by study type, with the data's own classification):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic review / meta-analysis | Internal and Emergency Medicine | Meta-analysis of RCT subgroups on functional class, survival, 6-minute walk distance and clinical worsening in CTD-PAH |
| [11897647](https://pubmed.ncbi.nlm.nih.gov/11897647/) | 2002 | Double-blind, placebo-controlled trial | Am J Respir Crit Care Med | 12-week trial of continuous subcutaneous treprostinil in PAH, avoiding central-catheter risks |
| [15302727](https://pubmed.ncbi.nlm.nih.gov/15302727/) | 2004 | Subgroup analysis | Chest | Efficacy and safety of subcutaneous treprostinil in PAH patients with connective tissue disease |
| [41594679](https://pubmed.ncbi.nlm.nih.gov/41594679/) | 2026 | Review | Biomolecules | Current therapeutic strategies and future prospects for CTD-PAH |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals | Recent advances in treating PAH in connective tissue diseases |
| [22291467](https://pubmed.ncbi.nlm.nih.gov/22291467/) | 2012 | Review | Drug Des Devel Ther | Inhaled treprostinil: 64–72% bioavailability relative to parenteral delivery |
| [34462153](https://pubmed.ncbi.nlm.nih.gov/34462153/) | 2021 | Retrospective study | Rev Med Interne | Characteristics and outcomes of CTD-PAH patients treated with prostanoids |
| [41201625](https://pubmed.ncbi.nlm.nih.gov/41201625/) | 2026 | Registry analysis | J Heart Lung Transplant | COMPERA registry: add-on parenteral prostacyclin analogues in 495 pretreated PAH patients, including CTD-PAH |
| [40566626](https://pubmed.ncbi.nlm.nih.gov/40566626/) | 2025 | Case series | Life (Basel) | Selexipag (another prostacyclin-pathway agent) in CTD-PAH with interstitial lung disease |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | Treatment of PAH in connective tissue disease |

For the second candidate, PAH associated with congenital heart disease, relevant publications include a cohort study of subcutaneous treprostinil ([29436381](https://pubmed.ncbi.nlm.nih.gov/29436381/), Heart, 2018), a small cohort of long-term continuous prostacyclin therapy ([23890862](https://pubmed.ncbi.nlm.nih.gov/23890862/), Int J Cardiol, 2013), and a case report in trisomy 21 ([35000655](https://pubmed.ncbi.nlm.nih.gov/35000655/), Cardiol Young, 2022). Several other items retrieved for this indication are loosely matched (for example sotatercept and bosentan studies).

For HIV-associated PAH, only general prostanoid reviews were found, with no HIV-specific data.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02246552 | REMODULIN | Not specified | Not specified |
| 02246553 | REMODULIN | Not specified | Not specified |
| 02246554 | REMODULIN | Not specified | Not specified |
| 02246555 | REMODULIN | Not specified | Not specified |

All four authorizations are valid single-ingredient products; none are cancelled.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these are graph associations, not package-insert text): kidney disease, pyoureter, liver disease, gallbladder disease, hypotensive disorder, blood coagulation disease, lung disease, and one obsolete rare pulmonary disease entry.

**Drug interactions:** The interaction screen returned 100 interacting drugs. Moderate-level interactions listed include:
- Epinephrine, ephedrine (including nasal), papaverine
- Acetylsalicylic acid (aspirin)
- SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
- Mannitol, glycerin
- Fenfluramine, dexfenfluramine, sibutramine

Several others have an unknown interaction level, including pantoprazole, omeprazole, lansoprazole, prednisone, simvastatin and potassium chloride.

Treprostinil's own vasodilatory and antiplatelet effects are consistent with the hypotension and coagulation flags above. Please refer to the package insert for warnings and contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (CTD-PAH and CHD-PAH as research questions); Hold for all other predictions**

**Rationale:**
- CTD-PAH has a plausible mechanism and a body of supporting literature, including a placebo-controlled subcutaneous trial and a 2024 systematic review. However, it is a subgroup of an existing PAH indication, and there is no dedicated CTD-specific Phase 3 RCT or registered trial in the data, so the evidence stays at L3.
- PAH associated with congenital heart disease is supported by observational data, but concerns about worsening right-to-left shunting remain.
- The top-ranked prediction (pulmonary arteriovenous malformation) and the hair and developmental disorders have no evidence (L5) and a weak or absent mechanism, so they should be held.
- Schistosomiasis-associated and chronic haemolytic anaemia-associated PAH are prediction-only (L5); HIV-associated PAH has only indirect class-level reviews (L4).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and are a blocking gap for safety screening
- Approved indication text and dosage forms for the four REMODULIN DINs
- Detailed mechanism of action data from DrugBank
- Confirmation of whether CTD-PAH is already covered by the current Canadian label, which would make this an extension of an existing indication rather than a new one
- A review of the CTD-PAH and CHD-PAH literature for CTD- or CHD-specific outcomes, and a safety monitoring plan for populations at risk (for example shunt physiology and interstitial lung disease)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

