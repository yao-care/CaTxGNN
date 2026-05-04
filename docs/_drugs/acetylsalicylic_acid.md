---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 9
---

# Acetylsalicylic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Acetylsalicylic Acid (Aspirin): From Cardiovascular Thrombosis Prevention to Migraine with Brainstem Aura

---

## One-Sentence Summary

Acetylsalicylic acid (ASA, aspirin) is one of the world's most established medications, widely used as an analgesic, antipyretic, and antiplatelet agent for cardiovascular disease prevention. The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (formerly known as basilar-type migraine), with **0 registered clinical trials** and **19 publications** currently providing supporting context for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No licensed product data on file (0 registered authorizations in current dataset) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed (data gap — see note below) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on market status:** Aspirin is globally available as an OTC drug and is listed in Health Canada's licensed products database. The "Not Marketed / 0 DINs" result likely reflects a data completeness issue in the current dataset and should be cross-verified against Health Canada's Drug Product Database before drawing regulatory conclusions.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on well-established pharmacology, acetylsalicylic acid irreversibly inhibits cyclooxygenase enzymes (COX-1 and COX-2). Its antiplatelet effect derives from permanent COX-1 blockade in platelets — preventing thromboxane A2 (TXA2) synthesis for the entire platelet lifespan. Its analgesic and anti-inflammatory effects arise from reduced prostaglandin synthesis across peripheral and central tissues.

Migraine with brainstem aura (MBA, ICHD-3 code 1.2.2) is characterized by fully reversible brainstem-originating aura symptoms — such as vertigo, dysarthria, diplopia, tinnitus, and ataxia — preceding or accompanying headache. The underlying pathophysiology involves cortical spreading depression (CSD), trigeminovascular activation, and platelet-dependent neurogenic inflammation. ASA addresses this axis through two complementary mechanisms: inhibiting TXA2-driven platelet aggregation that may trigger or amplify CSD events, and suppressing prostaglandin-mediated sensitization of trigeminal pain pathways.

A critical therapeutic advantage in this specific subtype is that triptans — the standard acute migraine treatment — carry theoretical contraindication in MBA due to potential brainstem vasoconstriction. ASA's complete absence of vasoconstrictive activity makes it a mechanistically safer candidate. A 2014 retrospective study (PMID 25729594) directly assessed low-dose ASA for prophylaxis in migraine with aura, and a 2025 systematic review (PMID 39989443) examined antithrombotic agents more broadly as migraine preventives. The antiplatelet link is further reinforced by observational data showing that clopidogrel — another antiplatelet agent — reduced migraine with aura after transcatheter PFO closure (PMID 16103551), supporting the platelet-aura mechanistic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Acetylsalicylic Acid specifically in Migraine with Brainstem Aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Study | Current Health Sciences Journal | Evaluated low-dose ASA prophylaxis in 203 patients with migraine with aura (ICHD-II criteria); 95 patients (46.8%) received ASA, compared to other standard prophylactic therapies over ≥4 months |
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | RCT | Cephalalgia | Double-blind multicenter RCT (n=278); IV lysine acetylsalicylate 1.8 g vs sumatriptan 6 mg s.c. vs placebo in acute migraine with/without aura — direct head-to-head comparison |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Explores evidence for antithrombotic drugs (including ASA) as migraine preventive medication; most current comprehensive synthesis |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline / Evidence Assessment | Headache | American Headache Society updated evidence assessment of acute migraine pharmacotherapies, including ASA-based and combination analgesic regimens |
| [2701286](https://pubmed.ncbi.nlm.nih.gov/2701286/) | 1989 | Review | Biomedicine & Pharmacotherapy | 10-year retrospective on the platelet hypothesis of migraine; supports the role of platelet dysfunction in migraine pathogenesis, underpinning ASA's mechanistic rationale |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observational Study | Heart | Clopidogrel (antiplatelet) reduced migraine with aura after transcatheter PFO/ASD closure — indirect evidence supporting antiplatelet mechanisms in aura-type migraine |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Narrative Review | Revue Neurologique | Comprehensive review of migraine with aura, including CSD mechanism, ICHD-III diagnostic criteria, and pathophysiological basis for treatment |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Comparative Review | Current Pain and Headache Reports | Reviews pathophysiologic, epidemiologic, and clinical differences between migraine with and without aura, including distinct risk profiles and management implications |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurology International | Reviews acute migraine treatments; positions ASA and NSAIDs as first-line agents for mild-to-moderate attacks, contextualizing ASA's established role |
| [35006660](https://pubmed.ncbi.nlm.nih.gov/35006660/) | 2022 | Guideline / Systematic Review | FP Essentials | AHA/ASA primary stroke prevention guidelines; relevant because MBA carries elevated stroke risk, and ASA's antiplatelet role in stroke prevention overlaps with this population |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The biological plausibility for ASA in migraine with brainstem aura is substantiated by its dual antiplatelet and anti-inflammatory mechanisms addressing the platelet-CSD-trigeminovascular axis, and its lack of vasoconstrictive effects provides a theoretical safety advantage over triptans specifically in this brainstem-involving subtype. However, current evidence is limited to observational/retrospective studies and secondary literature — no dedicated Phase 2/3 RCT for MBA exists — warranting cautious advancement rather than a definitive go decision.

**To proceed, the following is needed:**
- **Safety data retrieval:** Obtain the full ASA product monograph to complete key warnings, contraindications (e.g., reye's syndrome, GI bleeding, anticoagulant interactions), and DDI assessment — currently a blocking data gap
- **MOA confirmation:** Query DrugBank API (DB00945) to formally document COX-1/COX-2 inhibition profile for the mechanistic rationale section
- **Canada market status verification:** Cross-check Health Canada Drug Product Database to resolve the 0-DIN discrepancy — ASA is expected to be a widely licensed OTC product
- **Proof-of-concept study:** Design a prospective observational cohort or Phase 2 RCT in patients meeting strict ICHD-3 criteria for Migraine with Brainstem Aura (1.2.2), comparing low-dose ASA (81–325 mg) to placebo for attack frequency reduction over 3–6 months
- **Dose and formulation protocol:** Clarify whether the target use is acute treatment (effervescent/IV formulation, higher dose ~900 mg) or prophylaxis (low-dose 81–150 mg daily), as mechanistic rationale and evidence differ substantially between these approaches
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

