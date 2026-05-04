---
layout: default
title: Caffeine
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Caffeine
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

# Caffeine: From CNS Stimulant to Nasal Cavity Disease

## One-Sentence Summary

Caffeine is a methylxanthine and non-selective adenosine receptor antagonist with well-established use as a CNS stimulant, analgesic adjuvant in combination products, and treatment for apnea of prematurity in neonates.
The TxGNN model's top-ranked prediction identifies **Nasal Cavity Disease** as a potential new indication, supported by **3 publications** — all of which are indirect and do not directly evaluate caffeine as a treatment for nasal pathology.
Across the 10 predicted indications reviewed, evidence quality ranges widely; notably, **Hypnic Headache (rank 9)** carries the strongest evidence base and is the only indication reaching a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CNS stimulant; analgesic adjuvant (combination OTC products); apnea of prematurity |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (Preclinical / Mechanism Studies Only) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data could not be retrieved from DrugBank for this evaluation. Based on established pharmacology, caffeine is a non-selective antagonist of adenosine A1 and A2A receptors, and at higher concentrations also inhibits phosphodiesterase (PDE), thereby raising intracellular cAMP levels. These actions underlie its CNS stimulant effect, analgesic potentiation, and bronchodilatory properties.

For nasal cavity disease specifically, two mechanistic threads emerge. First, adenosine receptors are expressed in nasal mucosal vasculature; caffeine-mediated receptor blockade could theoretically modulate local vasomotor tone and reduce mucosal congestion. Second, bitter taste receptors (TAS2Rs / T2Rs) — known targets of caffeine-related bitter compounds — are expressed in nasal epithelium and airway smooth muscle, and their activation has been linked to antimicrobial peptide secretion and localized airway dilation.

However, neither mechanism has been explored in clinical or human tissue studies for nasal cavity disease. The three retrieved publications address: (1) intranasal caffeine as a *delivery route* for cognitive enhancement rather than a nasal treatment, (2) general bitter taste receptor pharmacology in airways, and (3) lung cancer prevention in a rat model. None constitute direct evidence that caffeine treats nasal cavity pathology. The mechanistic link is speculative, and this prediction is best interpreted as a model-generated hypothesis requiring prospective validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for caffeine in nasal cavity disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Formulation / Preclinical | *Current Drug Delivery* | Intranasal thermo-sensitive caffeine gel developed to enhance cognition after sleep deprivation; the nasal cavity is the drug delivery route, not the therapeutic target |
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | *Pharmacology & Therapeutics* | Comprehensive review of bitter taste receptor (T2R) pharmacology; documents T2R expression in nasal cavity, lungs, and airways — provides indirect mechanistic context for caffeine's potential airway effects |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal Study | *Cancer Research* | Black tea and caffeine reduced NNK-induced lung tumor incidence in F344 rats; focused on lung carcinogenesis prevention, not nasal cavity disease |

---

## Canada Market Information

Caffeine (DrugBank DB00201) currently has **no Health Canada Drug Identification Numbers (DINs)** and is not approved as an independent pharmaceutical product in Canada. It is present as an active ingredient in numerous OTC combination analgesics (e.g., acetaminophen + caffeine preparations) and as a prescription neonatal apnea treatment, but these would be registered under combination or branded products rather than caffeine alone. No standalone product licenses are on record for this DrugBank entry.

---

## Safety Considerations

Formal safety data (package insert warnings and contraindications) was not retrievable for this evaluation. No drug-drug interaction records were identified. Based on established pharmacological knowledge:

- **CNS and cardiovascular effects**: Caffeine at therapeutic doses can cause tachycardia, palpitations, hypertension, anxiety, and insomnia; high doses carry risk of cardiac arrhythmia
- **Caffeine withdrawal**: Abrupt cessation after regular use precipitates rebound headache — clinically important when considering dose tapering protocols
- **Biphasic dose-response**: Caffeine displays opposing effects on several systems depending on dose (e.g., analgesic adjuvant at low doses vs. potential thrombotic trigger at high doses); any new indication must carefully define a therapeutic dose range
- **Local irritation concern**: Caffeine may irritate oral and pharyngeal mucosa; this is particularly relevant for the glossodynia prediction (rank 6), where caffeine use is discouraged
- **Drug interactions**: Caffeine is a CYP1A2 substrate; co-administration with CYP1A2 inhibitors (e.g., ciprofloxacin, fluvoxamine) can substantially elevate plasma levels

Please refer to applicable product monographs and package inserts for complete safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (nasal cavity disease, score 99.91%) is not supported by any direct clinical or human mechanistic evidence. All three retrieved publications address tangentially related topics, and the prediction appears to reflect a mathematical association within the knowledge graph rather than an established biological relationship.

---

**Broader context — Most Actionable Indication Across All Predictions:**

While the report's primary focus follows the top-ranked TxGNN prediction, the **Hypnic Headache (rank 9)** indication merits immediate attention:

| Feature | Detail |
|---------|--------|
| Evidence Level | L3 (Observational studies / Systematic review) |
| Decision Stage | S2 |
| Recommendation | **Proceed with Guardrails** |
| Key references | PMIDs [24942086](https://pubmed.ncbi.nlm.nih.gov/24942086/), [25231430](https://pubmed.ncbi.nlm.nih.gov/25231430/), [23832130](https://pubmed.ncbi.nlm.nih.gov/23832130/) |
| Mechanistic basis | Caffeine blocks nocturnal adenosine accumulation via A1/A2A antagonism, raising the headache threshold during sleep; mechanism is among the clearest of all predicted indications |
| Reported efficacy | Bedtime caffeine (60–100 mg, one cup of strong coffee) documented as first-line therapy with reported response rate >70% across multiple case series |

---

**To proceed with the primary indication (nasal cavity disease), the following is needed:**

- Mechanistic studies directly examining caffeine's effect on nasal mucosal adenosine and T2R signaling pathways
- In vitro or in vivo disease models (rhinitis, chronic sinusitis, nasal polyps) with caffeine intervention
- Clear definition of the disease subtype within the broad "nasal cavity disease" category
- Safety profiling for intranasal caffeine formulations if the intranasal route is explored

**To proceed with hypnic headache (highest-evidence prediction):**

- Design a prospective pilot RCT or structured case series given disease rarity in the elderly population
- Define caffeine dose, timing (within 15 minutes of awakening from headache vs. prophylactic bedtime use), and formulation
- Pre-specify monitoring for sleep quality outcomes, as bedtime caffeine may paradoxically worsen sleep in a subset of patients
- Obtain Health Canada authorization pathway guidance for caffeine as a pharmaceutical product in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

