---
layout: default
title: Rimegepant
parent: 僅模型預測 (L5)
nav_order: 681
evidence_level: L5
indication_count: 6
---

# Rimegepant
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

# Rimegepant: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Rimegepant is a small-molecule CGRP receptor antagonist ("gepant"), internationally approved for acute treatment of migraine (with or without aura) and prevention of episodic migraine, though it is **not yet marketed in Canada**. The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura**, a rare migraine subtype in which vasoconstrictive drugs (triptans) are traditionally contraindicated. Currently **0 clinical trials** specifically target this subtype, but **14 publications** on rimegepant's general migraine efficacy and safety profile support the mechanistic direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established via Canadian licensing (no DIN on file); internationally approved for acute treatment of migraine (± aura) and prevention of episodic migraine |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (data gap, item DG002). Based on the supporting literature, rimegepant is a small-molecule, highly selective calcitonin gene-related peptide (CGRP) receptor antagonist — a "gepant" — approved for acute and preventive treatment of migraine. Unlike triptans, gepants act without causing vasoconstriction.

Migraine with brainstem aura (formerly "basilar-type migraine") is a subtype in which triptans are relatively or absolutely contraindicated because of their vasoconstrictive action on the vertebrobasilar circulation. Since rimegepant's CGRP-antagonist mechanism does not rely on vasoconstriction, there is a plausible theoretical rationale for its use in this population as a safer alternative acute/preventive option. A 2026 longitudinal MRA study (PMID 41574090) directly examined rimegepant's effect on cerebral and extracerebral arteries during migraine attacks, framing it explicitly as a "non-vasoconstrictive alternative" to triptans — this is the closest mechanistic bridge to the brainstem-aura population in the current evidence.

However, none of the 14 available publications enrolled or specifically analyzed patients with migraine with brainstem aura; all efficacy and safety data (Phase 3 open-label study, Phase 4 dosing study, network meta-analysis, PK studies) come from general migraine populations. The prediction is therefore mechanistically plausible but not yet directly evidenced for this specific subtype.

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for migraine with brainstem aura.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41574090](https://pubmed.ncbi.nlm.nih.gov/41574090/) | 2026 | Longitudinal MRA study | Brain Communications | Directly examines rimegepant's non-vasoconstrictive vascular effects during spontaneous migraine attacks — most mechanistically relevant to the brainstem-aura rationale |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network meta-analysis | The Journal of Headache and Pain | Compares relative efficacy of lasmiditan vs. rimegepant vs. ubrogepant for acute migraine treatment |
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Phase 3 open-label, long-term safety | Cephalalgia | Long-term safety/effectiveness of rimegepant 75mg ODT in Chinese adults with moderate-to-severe migraine |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Phase 4 open-label safety/tolerability | The Journal of Headache and Pain | 24-week safety/tolerability of once-daily 75mg rimegepant for episodic migraine prevention |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review (gepant class) | Handbook of Clinical Neurology | Overview of CGRP receptor antagonists (gepants) as a drug class, including rimegepant |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Review | CNS Drugs | Comprehensive review of rimegepant in acute and preventive migraine treatment; superior to placebo in Phase 3 trials |
| [36808268](https://pubmed.ncbi.nlm.nih.gov/36808268/) | 2023 | Phase 1 PK/safety | Clinical Pharmacology in Drug Development | PK and safety of single/multiple-dose rimegepant ODT in healthy Chinese adults |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | Pain Management | Overview of rimegepant within the new wave of acute migraine treatments (vs. lasmiditan, ubrogepant) |
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Regulatory approval review | Drugs | First-approval summary of rimegepant ODT (NURTEC ODT) for acute migraine treatment |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | Retrospective analysis | Headache | Off-label tolerability/effectiveness of rimegepant for acute migraine in adolescents |

## Canada Market Information

Rimegepant is **not currently marketed in Canada** — no Health Canada Drug Identification Number (DIN) is on file, and no licensed products or approved indication text are available for this drug.

## Safety Considerations

Please refer to the package insert for safety information. Health Canada/TFDA-level warnings, contraindications, and drug interaction data are not currently available (data gap, item DG001 — classified as Blocking, as it prevents completion of the S1 safety review stage).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap on regulatory safety labelling (warnings/contraindications) prevents this candidate from completing the S1 safety review stage. In addition, while the CGRP-antagonist mechanism offers a plausible rationale for avoiding the vasoconstriction risk associated with triptans in migraine with brainstem aura, no clinical trial or literature directly evaluates rimegepant in this specific subtype — all current evidence (L3: reviews, a network meta-analysis, and open-label safety studies) is extrapolated from general migraine populations.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph data: key warnings, contraindications, and drug-drug interactions
- Confirmed mechanism of action (MOA) data via DrugBank API query
- Targeted search for any case series, registry data, or subgroup analyses specific to migraine with brainstem aura
- Canadian market entry status confirmation (currently 0 DINs on file)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

