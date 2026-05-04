---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Adenosine: From Supraventricular Tachycardia to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Adenosine is an endogenous purine nucleoside used clinically to terminate paroxysmal supraventricular tachycardia (SVT) and as a pharmacological stress agent in cardiac imaging. The TxGNN model's highest-ranked prediction — "obsolete bundle branch block" — is a deprecated ontology term and most likely a knowledge graph topological artifact; the second-ranked prediction, **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**, is mechanistically coherent and is supported by **1 ongoing Phase 2a clinical trial** and **13 publications** spanning case reports, basic science, and clinical reviews.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Supraventricular tachycardia (SVT); pharmacological cardiac stress testing — internationally established use; not currently marketed in Canada |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.42% (Rank 2; Rank 1 is a deprecated disease ontology term and a likely KG artifact) |
| Evidence Level | L3 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

> **Note on Rank 1 ("obsolete bundle branch block"):** The TxGNN score is 99.94% but the "obsolete" prefix indicates this disease node has been retired from current clinical ontologies. Its presence with a high score is consistent with a graph topology artifact caused by an unremoved deprecated node — not a genuine clinical prediction. All substantive analysis in this report focuses on the Rank 2 prediction (CPVT).

---

## Why Is This Prediction Reasonable?

Adenosine acts on **A1 adenosine receptors** on cardiac cells to inhibit adenylyl cyclase, which reduces intracellular cyclic AMP (cAMP). Lower cAMP reduces protein kinase A (PKA) activity, which in turn decreases phosphorylation of the cardiac ryanodine receptor 2 (RyR2). In CPVT patients, RyR2 mutations cause abnormal spontaneous calcium leak from the sarcoplasmic reticulum (SR Ca²⁺ leak), particularly under adrenergic stimulation — this triggers delayed afterdepolarizations (DADs) that can degenerate into life-threatening bidirectional or polymorphic ventricular tachycardia.

By suppressing the β-adrenergic/cAMP/PKA signalling cascade, adenosine directly counteracts the molecular trigger responsible for CPVT arrhythmias. This pathway is not merely theoretical: PMID 23747301 demonstrates that ATP (adenosine's metabolic precursor) physically interacts with the RyR2 central domain at CPVT mutation hotspots, and PMID 18313614 reports a clinical case in which intravenous ATP successfully terminated bidirectional ventricular tachycardia in a confirmed CPVT patient.

The connection to adenosine's established indication in SVT is direct: both SVT and CPVT are supraventricular or ventricular arrhythmias in structurally normal hearts, and adenosine's antiarrhythmic mechanism — blunting catecholamine-driven electrical instability — is applicable across both contexts. The existence of an ongoing Phase 2a trial (NCT07263139) investigating AGP100, a compound targeting the same adenosine receptor pathway, further validates the mechanistic hypothesis even though the trial uses a derivative rather than native adenosine.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT07263139](https://clinicaltrials.gov/study/NCT07263139) | Phase 2a | Recruiting | 10 | Investigates AGP100 (an adenosine receptor pathway agent) for safety, tolerability, and exploratory efficacy in CPVT. Current treatments often fail to prevent exercise/stress-induced arrhythmias; this trial targets that unmet need. Note: AGP100 is not native adenosine — it may be an A1/A2 receptor agonist or adenosine prodrug; drug identity parity requires verification. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case Report | *Heart Rhythm* | **Most direct evidence.** Intravenous ATP terminated bidirectional ventricular tachycardia in a confirmed CPVT patient, providing clinical proof-of-concept that the adenosine/purinergic pathway can acutely suppress CPVT-type arrhythmias. |
| [23747301](https://pubmed.ncbi.nlm.nih.gov/23747301/) | 2013 | Basic Science | *Biochim Biophys Acta* | ATP directly binds the RyR2 central domain at sites harbouring CPVT-causative mutations, providing a molecular-level mechanistic explanation for adenosine's relevance in CPVT. |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Consensus Statement | *Europace* | ESC/HRS/APHRS multi-society consensus on pharmacological provocation testing in cardiac electrophysiology, covering diagnosis of CPVT and related inherited arrhythmia syndromes where adenosine-type agents are referenced. |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Clinical Observational | *Heart Rhythm* | Demonstrates that electrophysiological studies in RyR2-mutation CPVT have limited diagnostic value, highlighting the need for pharmacological (including purinergic) approaches. |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | In Vitro / Organoid | *J Physiology* | Using cardiac-neural microtissues, shows CPVT pathology involves sympathetic neurons in addition to cardiomyocytes — reinforcing that agents dampening adrenergic/cAMP signalling (such as adenosine) may have broader therapeutic targets. |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Preclinical | *Cardiovascular Research* | PDE2A/PDE4B gene therapy prevents heart failure and arrhythmias by improving subcellular cAMP compartmentation — indirectly validates adenosine's anti-arrhythmic mechanism via cAMP suppression in cardiomyocytes. |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Basic Science | *Communications Biology* | Characterises TECRL-deficiency CPVT, revealing mitochondrial dysfunction and calcium dysregulation — contextualises the complexity of CPVT pathophysiology beyond classic RyR2 mutations. |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Preclinical | *Science Translational Medicine* | SR Ca²⁺ leak via RyR2 contributes mechanistically to arrhythmia in pressure-overload and MI models; stabilising RyR2 (or reducing PKA-driven phosphorylation as adenosine does) reduces arrhythmia risk. |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Review / Clinical Guidance | *Paediatric Anaesthesia* | Reviews management of paediatric arrhythmias including CPVT, noting adenosine's role in differential diagnosis and acute management of narrow and wide complex tachycardias. |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | *J Assoc Physicians India* | Classifies and reviews idiopathic ventricular tachycardias in structurally normal hearts; adenosine responsiveness is cited as a diagnostic and therapeutic criterion for specific VT subtypes. |

---

## Canada Market Information

Adenosine currently has **no Drug Identification Numbers (DINs) issued in Canada**. The drug is not commercially marketed in Canada under any dosage form or brand name at this time.

Adenosine is approved and widely marketed in other major jurisdictions (e.g., the United States — Adenocard® for SVT; Adenoscan® for cardiac stress imaging), suggesting that regulatory precedent exists for a Canadian filing if a new indication were pursued.

---

## Safety Considerations

Detailed Canadian labelling data (warnings, contraindications) are not available in this evidence pack.

> Please refer to international package inserts and Health Canada drug product databases for complete safety information. Clinically, adenosine is known to cause transient bradycardia, AV block, flushing, and bronchospasm — factors that would require specific risk mitigation in any CPVT indication given the patient population (including paediatrics and young adults).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for adenosine in CPVT is biologically coherent and supported by one pivotal case report (PMID 18313614) and basic science demonstrating direct ATP-RyR2 interaction; however, no completed clinical trial using native adenosine or a validated analogue exists, and the single ongoing Phase 2a trial (NCT07263139) uses AGP100 — a compound whose relationship to adenosine itself requires clarification. Evidence is currently at L3 (observational/mechanistic), which is insufficient to recommend proceeding to formulation or indication development without further data.

**To proceed, the following is needed:**

- **Confirm drug identity of AGP100**: Determine whether AGP100 is an adenosine prodrug, A1 receptor agonist, or a structurally distinct compound — this is critical to assess whether NCT07263139 results are transferable to native adenosine.
- **Retrieve adenosine MOA from DrugBank** (DG002): Formal MOA data should replace the current data gap to support mechanistic dossier submission.
- **Obtain Health Canada/TFDA labelling data** (DG001): Warnings and contraindications are needed before any safety evaluation stage (S1) can be initiated.
- **Monitor NCT07263139 outcomes**: Projected completion June 2027; Phase 2a results will critically determine whether adenosine pathway agents show dose-response efficacy and acceptable safety in CPVT.
- **Conduct a targeted literature review for adenosine + CPVT**: Search specifically for any completed pilot studies, compassionate use reports, or electrophysiology lab case series beyond PMID 18313614.
- **Assess formulation feasibility**: Native adenosine has an extremely short plasma half-life (<10 seconds IV); a CPVT indication would likely require a sustained-release, oral prodrug, or subcutaneous delivery strategy — this is a significant pharmaceutical development consideration.

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

