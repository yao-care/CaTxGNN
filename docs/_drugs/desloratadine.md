---
layout: default
title: Desloratadine
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 6
---

# Desloratadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Desloratadine: From Allergic Rhinitis/Urticaria to Cold Urticaria

## One-Sentence Summary

Desloratadine is a second-generation, non-sedating H1 antihistamine used globally for allergic rhinitis and chronic urticaria, though it currently holds no active Drug Identification Numbers (DINs) in Canada.
The TxGNN model predicts it may be effective for **Cold Urticaria**, with **3 completed clinical trials** and **7 publications** currently supporting this direction.
The evidence level is rated **L1**, underpinned by multiple randomized controlled and dose-escalation studies directly evaluating desloratadine in this population.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No active Canadian license; globally approved for allergic rhinitis and chronic urticaria |
| Predicted New Indication | Cold Urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Desloratadine is a selective, long-acting H1 receptor antagonist and the pharmacologically active metabolite of loratadine. It competitively blocks peripheral histamine H1 receptors, thereby reducing the vascular and sensory consequences of histamine release. Beyond simple receptor blockade, desloratadine also exerts mild anti-inflammatory effects — including inhibition of pro-inflammatory cytokine and mediator release from mast cells and basophils — which further distinguishes it from older first-generation antihistamines.

Cold urticaria (acquired cold urticaria, ACU) is triggered by cold stimuli that cause mast cell degranulation, releasing large amounts of histamine that bind to cutaneous H1 receptors, producing wheals, angioedema, and pruritus. Desloratadine directly interrupts this pathway by blocking H1 receptors before histamine can exert its vascular and sensory effects. Critically, dose-escalation studies have shown that higher-than-standard doses (10–20 mg vs. the usual 5 mg) can raise the critical temperature threshold measured by TempTest — meaning patients can tolerate colder stimuli before a reaction is triggered.

The mechanistic link between desloratadine and cold urticaria is therefore strong and direct: cold urticaria is fundamentally a histamine-mediated condition, and H1 antagonism addresses the core effector pathway. Current European Academy of Allergology and Clinical Immunology (EAACI) guidelines already recommend second-generation H1 antihistamines as first-line treatment, with dose escalation up to fourfold for inadequate responders. The TxGNN prediction aligns tightly with established clinical practice, and the model's top-ranked score of 99.94% reflects this robust pharmacological rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized, double-blind, placebo-controlled crossover study comparing 5 mg vs. 20 mg desloratadine in ACU patients; assessed wheal reduction via thermography, volumetry, and digital time-lapse photography — direct dose comparison for cold urticaria management |
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Multi-centre, double-blind, dose-escalating trial (5 mg / 10 mg / 20 mg) in ACU patients; establishes dose-response relationship and identifies the minimum effective dose to inhibit cold urticaria symptoms |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Head-to-head comparison of 5 antihistamines (including desloratadine) in urticaria patients in tropical Latin America; large-sample pharmacokinetic and pharmacodynamic study providing relative efficacy positioning |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | High-dose desloratadine (20 mg) significantly decreases wheal volume and raises cold provocation thresholds compared to standard dose (5 mg) and placebo in ACU; randomized, placebo-controlled, crossover design — foundational dose optimization evidence |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Dose-escalation RCT measuring critical temperature threshold in cold urticaria; demonstrates that H1 antihistamine dose escalation produces measurable clinical benefit and that individual patient response is variable, supporting personalized dosing strategies |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | Clinical Trial | J Dermatol Treat | Proof-of-concept study: 5 mg desloratadine for 4 days significantly inhibited cold urticaria responses in 12 patients using ice-cube provocation testing — early evidence establishing efficacy in this indication |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Comprehensive review of chronic urticaria aetiology and management; positions H1 antihistamines as cornerstone therapy and discusses their role across physical urticaria subtypes including cold urticaria |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Comparative Review | Allergy | Comparative review of second-generation antihistamines in allergic rhinitis and chronic urticaria; contextualizes the safety and efficacy profile of desloratadine relative to other H1 blockers |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Case Series | J Allergy Clin Immunol Pract | Food-dependent cold urticaria case series describing a novel physical urticaria variant; discusses antihistamine management considerations for atypical cold urticaria presentations |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case Report | Qatar Med J | First reported case of cold-induced urticaria following black ant bite–induced anaphylaxis; documents desloratadine use in a post-anaphylaxis cold urticaria context, extending the clinical spectrum of the indication |

---

## Canada Market Information

Desloratadine currently has **no active Drug Identification Numbers (DINs)** registered with Health Canada and is not marketed in Canada under any product license.

> For context, desloratadine is approved in the United States (Clarinex®), the European Union, and numerous other jurisdictions for allergic rhinitis and chronic idiopathic urticaria. The absence of Canadian DINs is a regulatory gap that would need to be addressed for any local market entry or clinical program in Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No safety data (key warnings, contraindications, or drug interactions) was available in this Evidence Pack. Based on its broad global approval history, desloratadine is generally considered to have a favorable tolerability profile with low sedation risk; however, the formal Canadian product monograph should be reviewed before any clinical application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed randomized controlled trials and dose-escalation studies directly demonstrate desloratadine's efficacy in cold urticaria, current EAACI guidelines already endorse second-generation H1 antihistamines as first-line treatment for this condition, and the mechanistic link (H1 blockade → histamine pathway inhibition) is well-established and direct.

**To proceed, the following is needed:**

- **Health Canada regulatory pathway**: No active DINs exist; a New Drug Submission (NDS) or comparable regulatory filing would be required for Canadian market authorization in the cold urticaria indication
- **Full safety dossier**: Formal product monograph data covering contraindications, warnings, precautions, and drug interactions must be obtained and reviewed before clinical implementation
- **Mechanism of action documentation**: Formal DrugBank/pharmacology records to complete the mechanistic analysis dossier (currently a data gap)
- **Optimal dosing protocol for Canada**: Determine whether standard 5 mg or updosed (10–20 mg) regimens are appropriate based on available dose-response evidence and local treatment guidelines
- **Special population data**: Confirm safety and dosing for pediatric patients, pregnant/lactating women, and renally/hepatically impaired patients in the Canadian context
- **TFDA package insert review** (if applicable): Download and parse the product monograph for full contraindication and warning mapping to complete the safety assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

