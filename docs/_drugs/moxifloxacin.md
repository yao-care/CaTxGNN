---
layout: default
title: Moxifloxacin
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
---

# Moxifloxacin
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

# Moxifloxacin: From Bacterial Infections to Bubonic Plague

## One-Sentence Summary

Moxifloxacin (Avelox®, DB00218) is a fourth-generation fluoroquinolone antibiotic whose detailed MOA data was not captured in this evidence pack; based on well-established pharmacology, it inhibits bacterial DNA gyrase and topoisomerase IV to deliver broad-spectrum bactericidal activity. The TxGNN model identified 10 candidate new indications — predominantly hematological conditions — but **bubonic plague** (TxGNN rank #10) stands apart as the only indication supported by actual evidence: **6 preclinical and observational publications** plus **FDA approval under the Animal Rule (2012)**. All other 9 predicted indications are rated Hold due to absent mechanistic links or active safety contraindications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in data (Fluoroquinolone antibiotic class) |
| Predicted New Indication (Primary) | Bubonic Plague |
| TxGNN Prediction Score | 99.41% (TxGNN Rank #10; Evidence Rank #1 among all predictions) |
| Evidence Level | L3 (Animal efficacy studies + FDA Animal Rule approval) |
| Canada Market Status | Not marketed (0 DINs — likely a data gap; manual verification recommended) |
| Number of DINs | 0 |
| Recommended Decision | **Proceed with Guardrails** (Bubonic Plague) / Hold (all other 9 indications) |

---

## All Predicted Indications — Summary

| TxGNN Rank | Disease | Score | Evidence Level | Recommendation | Key Issue |
|-----------|---------|-------|----------------|----------------|-----------|
| 1 | Polyclonal Hyperviscosity Syndrome | 99.98% | L5 | Hold | No mechanistic link to antibiotic MOA; likely KG neighbourhood effect |
| 2 | Hyperamylasemia | 99.98% | L5 | Hold | ⚠️ Possible reverse causality — moxifloxacin has amylase-elevation ADR |
| 3 | Congenital Analbuminemia | 99.97% | L5 | Hold | 1 case report (PMID 32181025) unrelated to moxifloxacin; false positive |
| 4 | Blood Group Incompatibility | 99.96% | L5 | Hold | Immune-mediated haemolysis; no mechanistic link |
| 5 | Premalignant Hematological Disease | 99.95% | L5 | Hold | No clinical or preclinical evidence |
| 6 | Monoclonal Gammopathy | 99.95% | L4 | Hold | Moxifloxacin treats secondary infections, not the clonal B-cell disease itself |
| 7 | Hematological Disease with Peripheral Neuropathy | 99.94% | L5 | Hold | ⚠️ **Contraindicated** — FDA Black Box Warning for irreversible peripheral neuropathy |
| 8 | Congenital Hematological Disorder | 99.91% | L4 | Hold | Antibiotic supportive role only; ⚠️ QT prolongation risk in cardiac-vulnerable patients |
| 9 | Hematopoietic/Lymphoid Neoplasm | 99.67% | L5 | Hold | No antitumour activity data; topoisomerase selectivity differs from oncology agents |
| **10** | **Bubonic Plague** | **99.41%** | **L3** | **Proceed with Guardrails** | **FDA-approved under Animal Rule; robust preclinical evidence** |

---

## Why is This Prediction Reasonable?

Moxifloxacin belongs to the fourth-generation fluoroquinolone class and exerts its bactericidal effect through dual inhibition of two essential bacterial enzymes: **DNA gyrase (GyrA/GyrB subunits)** and **topoisomerase IV (ParC/ParE subunits)**. Both enzymes are required for bacterial DNA supercoiling, replication, repair, and transcription. By trapping enzyme-DNA cleavage complexes, moxifloxacin causes lethal double-strand DNA breaks. This dual-target mechanism provides broader activity and a higher barrier to resistance than single-target quinolones.

*Yersinia pestis*, the gram-negative bacillus causing bubonic, septicemic, and pneumonic plague, is exquisitely susceptible to moxifloxacin, with minimum inhibitory concentrations (MIC) reported as low as ≤0.03 mg/L. The pharmacokinetic profile of moxifloxacin — high oral bioavailability (~90%), extensive tissue distribution, and a long half-life (~12 hours) — is well-suited for treating this systemic infection.

Because plague is a rare, rapidly fatal disease classified as a **CDC Category A bioterrorism pathogen**, conducting conventional Phase 3 human RCTs is both ethically and practically infeasible. Recognizing this, the US FDA approved moxifloxacin for plague in **2012 under the Animal Rule (21 CFR 314.600)** — a regulatory pathway that accepts animal efficacy data in place of human trials when the condition precludes ethical human testing. Multiple independent animal studies and in vitro pharmacodynamic models provided the scientific basis, and this FDA approval constitutes the highest achievable regulatory validation for this indication. The L3 evidence classification reflects the formal absence of human Phase 2/3 RCT data, not a weakness in the underlying science.

---

## Clinical Trial Evidence

No clinical trials directly investigating moxifloxacin as treatment for bubonic plague were identified in the registry search. This is expected — plague trials in humans are not feasible. The regulatory basis for use rests entirely on the Animal Rule pathway and preclinical data.

> **Note:** Moxifloxacin did appear in trials for related hematological contexts (Ranks #6 and #8), where it served as a standard **QTc-positive control** (NCT07023029) and as prophylactic antibiotic therapy in immunocompromised patients (NCT00324324, NCT00062231) — both roles that confirm its established pharmacological profile rather than supporting the hematological indications themselves.

---

## Literature Evidence (Bubonic Plague)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15555886](https://pubmed.ncbi.nlm.nih.gov/15555886/) | 2004 | Animal Study (in vivo) | Int J Antimicrob Agents | Moxifloxacin 100 mg/kg bid × 7 days provided full protection against systemic plague (challenge up to 6h post-infection) and pneumonic plague (up to 30h post-aerosol) in BALB/c mice; comparable to ciprofloxacin |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Animal Study (in vivo) | Antibiotiki i Khimioterapiia | Moxifloxacin ED50 = 5.5–14.0 mg/kg against both FI+ and FI− *Y. pestis* strains; high susceptibility confirmed for all 20 tested strains |
| [21115791](https://pubmed.ncbi.nlm.nih.gov/21115791/) | 2011 | In vitro PK/PD Model | Antimicrob Agents Chemother | In vitro dynamic model derived optimal moxifloxacin dosing regimen; demonstrated potent bactericidal kill of *Y. pestis* and prevention of resistance emergence |
| [21486959](https://pubmed.ncbi.nlm.nih.gov/21486959/) | 2011 | In vitro Comparative | Antimicrob Agents Chemother | Head-to-head comparison of candidate antibiotics against *Y. pestis*; moxifloxacin compared favourably to streptomycin (gold standard), supporting its role as an alternative where streptomycin is unavailable |
| [29623187](https://pubmed.ncbi.nlm.nih.gov/29623187/) | 2018 | Case Report (ADR) | Ther Adv Drug Saf | Confirms FDA guidance listing plague as a moxifloxacin indication; case documents tinnitus ADR — underscores the need for active safety monitoring |
| [26210091](https://pubmed.ncbi.nlm.nih.gov/26210091/) | 2015 | Case Report | Ticks Tick-Borne Dis | Tularemia (Francisella tularensis; also CDC Category A pathogen) managed with fluoroquinolone class; contextually supports the class's role in bioterrorism-relevant infections |

---

## Canada Market Information

The evidence pack records **0 active DINs (Drug Identification Numbers)** and a market status of **Not marketed** for moxifloxacin in Canada. This is **likely a data collection gap** rather than an accurate regulatory picture — Avelox® (moxifloxacin) is known to be available commercially in numerous countries. A direct lookup in the **Health Canada Drug Product Database** is strongly recommended before making any regulatory or procurement decisions based on this field.

Currently no DIN licence records are available to display.

---

## Safety Considerations

Safety data (warnings, contraindications, drug interactions) was not captured in this evidence pack. However, two **critical safety signals** are identified from the embedded repurposing rationale analysis:

- **QT Prolongation**: Moxifloxacin was used as a **standard QTc-positive control** in NCT07023029, formally confirming its clinically significant QT-prolonging effect. This is a class-wide concern for fluoroquinolones and is particularly relevant in populations with congenital hematological disorders (e.g., sickle cell disease) who may have existing cardiac involvement.
- **Peripheral Neuropathy**: All fluoroquinolones carry an **FDA Black Box Warning** (updated 2013) for the risk of potentially irreversible peripheral neuropathy. Moxifloxacin should be avoided in patients with pre-existing neuropathy — this makes it a functional contraindication for Rank #7 (hematological disease with acquired peripheral neuropathy), one of its own predicted indications.

Please refer to the current Avelox® (moxifloxacin) product monograph or package insert for the complete list of warnings, contraindications, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Bubonic Plague, TxGNN Rank #10)*
**Decision: Hold** *(All other 9 predicted indications, TxGNN Ranks #1–9)*

**Rationale:**
Moxifloxacin's potential for bubonic plague is not speculative — it is already FDA-approved under the Animal Rule, supported by multiple independent animal studies and in vitro PK/PD models, and the L3 classification understates the true regulatory weight of this evidence. By contrast, all other TxGNN-predicted indications (hematological conditions, Ranks 1–9) lack any mechanistic bridge to moxifloxacin's antibiotic MOA, and two of them (Ranks #7 and #8) carry active safety flags that could cause patient harm.

**To proceed, the following is needed:**

- **Verify Canada registration status**: Confirm DIN records via Health Canada's Drug Product Database — the current "not marketed" flag is inconsistent with known international availability and must be resolved before any formulary or supply chain decision
- **Obtain product monograph**: Retrieve the Canadian Avelox® product monograph for complete safety, contraindication, and drug interaction data (flagged as Blocking data gap DG001)
- **MOA documentation**: Complete DrugBank API query to formally capture mechanism of action data (flagged as High data gap DG002)
- **Health Canada / FDA alignment**: Confirm whether Health Canada recognises the FDA Animal Rule approval basis for the plague indication, or whether a separate Canadian submission is required
- **QT monitoring protocol**: Establish cardiac monitoring requirements for any clinical use context, particularly in immunocompromised or haematology patients
- **Exclude Rank #7 indications proactively**: Flag hematological disease with peripheral neuropathy as a contraindicated combination — do not advance to S1 safety review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

