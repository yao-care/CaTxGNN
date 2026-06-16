---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Clopidogrel
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

# Clopidogrel: From Acute Coronary Syndrome to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is a P2Y12 ADP receptor antagonist (antiplatelet agent) widely used to prevent atherothrombotic events, including acute coronary syndrome and ischemic stroke/TIA.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** — a neurologically distinct migraine subtype involving brainstem-origin symptoms — with **16 publications** directly supporting this direction.
Notably, the closely related broader indication of **Migraine Disorder** (TxGNN Rank 2, Score 99.43%) is further supported by **8 registered clinical trials** and **20 publications**, together providing a substantial body of converging evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atherothrombotic event prevention (ACS, ischemic stroke/TIA) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Canada Market Status | Not marketed (data verification required — see note below) |
| Number of DINs | 0 (data gap likely) |
| Recommended Decision | Proceed with Guardrails (PFO-associated migraine subgroup) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, Clopidogrel is an irreversible P2Y12 ADP receptor antagonist that blocks platelet activation and aggregation. Its proven efficacy in preventing arterial thrombotic events provides the mechanistic foundation for the migraine repurposing hypothesis.

Migraine with brainstem aura (formerly called basilar-type migraine) is characterized by neurological symptoms originating from the brainstem — such as dysarthria, vertigo, diplopia, or bilateral visual disturbance — occurring before or during the headache phase. A well-established pathophysiological link involves **patent foramen ovale (PFO)**: this cardiac septal defect allows venous microemboli to bypass pulmonary filtration and enter the cerebral circulation directly. When microemboli reach the vertebrobasilar system, they can trigger cortical spreading depression (CSD) in the posterior circulation, precipitating brainstem aura symptoms. By inhibiting P2Y12 receptors, Clopidogrel reduces platelet aggregation and microemboli formation in this vulnerable pathway — making it particularly relevant to the brainstem aura subtype.

Two additional mechanisms reinforce this prediction. First, preclinical evidence (PMID 31722730) demonstrates that P2Y12 receptors are expressed on microglia in the trigeminal nucleus caudalis — a key brainstem pain-processing hub — where P2Y12 inhibition modulates neuroinflammation via the RhoA/ROCK pathway, offering a direct central analgesic effect independent of PFO status. Second, activated platelets release serotonin (5-HT), which triggers cerebral vasoconstriction and may initiate the migraine cascade; antiplatelet therapy reduces 5-HT release and may interrupt this trigger mechanism. The primary target population is most likely **migraineurs with confirmed PFO or right-to-left shunt**, where all three mechanisms are simultaneously active.

---

## Clinical Trial Evidence

Currently no clinical trials are registered specifically for migraine with brainstem aura.

> **Broader migraine evidence (Rank 2 — Migraine Disorder, TxGNN Score 99.43%):** The closely related indication of migraine disorder has 8 registered clinical trials sharing the same mechanistic basis. The most relevant trials are summarized below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | CANOA study: Clopidogrel + aspirin vs aspirin alone after transcatheter ASD closure — directly evaluates Clopidogrel for new-onset migraine prevention post-cardiac procedure |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Prospective trial specifically evaluating Clopidogrel to relieve migraine with right-to-left shunt — the most directly relevant trial; status and results require confirmation |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1,000 | COMPETE trial: head-to-head comparison of anticoagulation vs antiplatelet (including Clopidogrel) vs standard migraine therapy in PFO-associated migraine; large, well-designed trial with pending results |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Active, not recruiting | 440 | SPRING trial: PFO closure vs medication (possibly including Clopidogrel) for migraine — ongoing Phase 3 multicenter RCT with results due 2025 |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Large PFO closure vs antiplatelet vs anticoagulant RCT (CLOSE); primary endpoint is stroke prevention with migraine as secondary outcome |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A | Terminated | 7 | GORE CARDIOFORM device trial for migraine — terminated early (n=7); Clopidogrel was standard post-procedure medication, not the investigational agent |
| [NCT02777359](https://clinicaltrials.gov/study/NCT02777359) | Phase 2 | Unknown | 100 | PFO closure for migraine — device-focused; Clopidogrel used as standard post-procedure antiplatelet, not primary intervention |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | Enrolling by invitation | 3,300 | General neurology pragmatic registry; Clopidogrel-migraine association is indirect |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Comprehensive systematic review of antithrombotic drugs (including Clopidogrel) as migraine preventive medication; highest-tier synthesis of current evidence |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Systematic Review | Indian J Thorac Cardiovasc Surg | Systematic review of new-onset headache/migraine after ASD closure; management strategies including antiplatelet therapy reviewed |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: percutaneous PFO closure in migraine with aura — establishes PFO-migraine mechanistic link and context for antiplatelet approaches |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | Cephalalgia | Direct pilot randomised trial of Clopidogrel as prophylactic treatment for migraine; foundational controlled evidence for the repurposing hypothesis |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | Comparative Study | JAMA Cardiology | CANOA 1-year results: effect of Clopidogrel + aspirin vs aspirin alone on migraine after ASD closure; assesses durability after Clopidogrel cessation at 3 months |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | Comparative Study | JAMA | CANOA primary results: Clopidogrel + aspirin significantly reduces new-onset migraine attacks after transcatheter ASD closure vs aspirin alone |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Clinical Study | J Investigative Medicine | Clopidogrel 75 mg/day added to regimen of drug-refractory migraineurs with confirmed PFO; 56.8% had PFO; improvement documented at 3 and 6 months |
| [31722730](https://pubmed.ncbi.nlm.nih.gov/31722730/) | 2019 | Basic Science | J Neuroinflammation | P2Y12 receptor on microglia in the trigeminal nucleus caudalis mediates microglial activation via RhoA/ROCK in chronic migraine mouse model — direct mechanistic evidence |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label Pilot | Neurology | TRACTOR study: ticagrelor (non-thienopyridine P2Y12 inhibitor) evaluated after observation that thienopyridines including Clopidogrel reduced migraine in PFO patients |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective Review | Cephalalgia | Clopidogrel as primary therapy in migraineurs with right-to-left shunt; establishes paradoxical embolization as mechanistic link |

---

## Canada Market Information

No Health Canada Drug Identification Numbers (DINs) are recorded in the current dataset for Clopidogrel. This almost certainly reflects a **data gap**: Clopidogrel (Plavix® and multiple generic formulations) is widely available in Canada as an approved prescription antiplatelet agent. Verification against the Health Canada Drug Product Database (DPD) is recommended before using this field for regulatory decisions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The CANOA Phase 4 RCT (n=220, published in JAMA 2015 and JAMA Cardiology 2021) provides direct evidence that Clopidogrel + aspirin significantly reduces new-onset migraine after cardiac septal defect procedures, and multiple retrospective studies and a pilot RCT confirm the antiplatelet-migraine connection in PFO-positive patients. Migraine with brainstem aura shares the same posterior-circulation microembolism pathway and likely represents the subgroup with the highest probability of benefit, making cautious clinical exploration appropriate.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm Clopidogrel's actual Canadian DIN status via the Health Canada Drug Product Database — current data showing "未上市" (not marketed) is inconsistent with known market availability and requires correction
- **Safety review:** Obtain and review the full package insert for approved warnings, contraindications (especially active bleeding disorders and hypersensitivity), and drug-drug interactions (notably PPIs via CYP2C19 competition, NSAIDs, anticoagulants)
- **Pharmacogenomics:** CYP2C19 genotyping is clinically significant — poor metabolizers (~15–30% of East Asians, 2–5% of Europeans) show substantially reduced Clopidogrel activation; efficacy in migraine may be genotype-dependent
- **Patient selection criteria:** Define the target subpopulation — patients with **confirmed PFO or right-to-left shunt** and **migraine with brainstem aura refractory to ≥2 standard preventive agents** represent the most evidence-backed candidates
- **Pending trial outcomes:** Confirm publication status of NCT02938182 (prospective Clopidogrel/RLS migraine trial, n=50) and await results of NCT05546320 (COMPETE, n=1,000) and NCT04946734 (SPRING Phase 3, n=440) — these will provide decisive evidence for or against first-line use
- **Mechanistic study:** Commission or identify direct research on P2Y12 expression in the brainstem of migraine with brainstem aura patients to strengthen disease-specific mechanistic rationale beyond PFO-mediated embolism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

