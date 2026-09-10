---
layout: default
title: Isoflurane
parent: 僅模型預測 (L5)
nav_order: 421
evidence_level: L5
indication_count: 7
---

# Isoflurane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Isoflurane: From General Anesthesia to Migraine Disorder

## One-Sentence Summary

Isoflurane is a halogenated volatile agent used for induction and maintenance of general anesthesia. Among **7 TxGNN-predicted new indications** evaluated for isoflurane, **Migraine Disorder** is the only candidate currently backed by real-world evidence — **13 publications** support a plausible mechanism, though **no clinical trials** have yet tested this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (induction/maintenance) — no Taiwan/Canada license record in evidence pack |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (Research Priority) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for isoflurane is not available from DrugBank in this evidence pack (Data Gap DG002). Based on known pharmacology, isoflurane is a methyl ethyl ether–class volatile anesthetic that potentiates GABA-A receptor–mediated inhibition and modulates NMDA and two-pore-domain potassium channels, producing reversible CNS depression. Its efficacy in general anesthesia is well established.

The link to migraine is mechanistic rather than indication-analogous: multiple studies (PMID 8665587, 27122032, 17267580, 22523186) show that volatile anesthetics, including isoflurane, suppress **cortical spreading depolarization (CSD)** — the electrophysiological process underlying migraine aura and a proposed trigger for headache. A case report (PMID 26323741, duplicated in Portuguese as PMID 26363696) describes isoflurane general anesthesia successfully terminating refractory status migrainosus, consistent with the GABA-A-mediated CSD-suppression hypothesis. However, this remains a single case observation with no controlled trials, and isoflurane's practical use is limited to inpatient/anesthesia settings — not a feasible chronic outpatient migraine therapy as currently evidenced.

### Other TxGNN-Predicted Candidates (Lower Confidence, No Supporting Evidence)

| Disease | TxGNN Score | Evidence Level | Note |
|---------|------------|-----------------|------|
| Prinzmetal angina | 99.67% | L5 | Theoretical coronary vasodilation, but conflicts with known coronary steal risk |
| Tourette syndrome | 99.61% | pending | No mechanistic or literature support found |
| Manic bipolar affective disorder | 99.57% | L5 | Anesthesia-as-ECT-alternative link applies to depression, not mania |
| Trichotillomania | 99.54% | L5 | No plausible mechanistic link |
| Dysthymic disorder | 99.27% | L5 | Isoflurane-as-ECT-alternative hypothesis, no supporting trials/literature |
| Nephrogenic syndrome of inappropriate antidiuresis | 99.09% | L5 | No biological plausibility identified |

All six are pure knowledge-graph associations with zero clinical trials or literature hits, and are not carried forward for further review.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26323741](https://pubmed.ncbi.nlm.nih.gov/26323741/) | 2015 | Case Report | Braz J Anesthesiol | General anesthesia (isoflurane) successfully terminated refractory status migrainosus, theorized to act via sub-GABA-A receptor stimulation |
| [8665587](https://pubmed.ncbi.nlm.nih.gov/8665587/) | 1996 | Mechanistic (Animal) | Cephalalgia | Inhalational anesthetics (incl. isoflurane) inhibit cortical spreading depression, the process implicated in migraine aura |
| [27122032](https://pubmed.ncbi.nlm.nih.gov/27122032/) | 2016 | Mechanistic (Animal) | J Neuroscience | Sensory cortices show intrinsic susceptibility to spreading depolarizations relevant to migraine aura symptoms |
| [17267580](https://pubmed.ncbi.nlm.nih.gov/17267580/) | 2007 | Mechanistic (Animal) | J Pharmacol Exp Ther | NMDA receptor antagonists suppress cortical spreading depression, supporting therapeutic potential for migraine |
| [22523186](https://pubmed.ncbi.nlm.nih.gov/22523186/) | 2012 | Mechanistic (Animal) | Cephalalgia | Chronic topiramate suppresses potassium-induced cortical spreading depression in rats |
| [20974582](https://pubmed.ncbi.nlm.nih.gov/20974582/) | 2011 | Mechanistic (Animal) | Cephalalgia | NO donor infusion increases CGRP/nNOS-immunoreactive neurons in trigeminal ganglion, a migraine-relevant pathway |
| [27091721](https://pubmed.ncbi.nlm.nih.gov/27091721/) | 2016 | Cohort/Translational | Ann Neurol | Chronic migraineurs show upregulated inflammatory gene transcripts in pericranial periosteum |
| [39354357](https://pubmed.ncbi.nlm.nih.gov/39354357/) | 2024 | Animal Study | J Headache Pain | Passive smoking increases susceptibility to cortical spreading depolarization in mice |
| [40764901](https://pubmed.ncbi.nlm.nih.gov/40764901/) | 2025 | Animal Study | J Headache Pain | CGRP antagonist atogepant does not affect CSD susceptibility, suggesting its efficacy is independent of CSD suppression |
| [26363696](https://pubmed.ncbi.nlm.nih.gov/26363696/) | 2015 | Case Report (duplicate/Portuguese) | Rev Bras Anestesiol | Same case as PMID 26323741 — isoflurane general anesthesia used to terminate status migrainosus |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold (Research Priority)**

**Rationale:**
Isoflurane is not currently marketed in Canada (0 DINs), and Blocking-severity safety data (TFDA warnings/contraindications, DG001) is missing, precluding any near-term safety assessment. The migraine hypothesis has a coherent mechanistic basis (CSD suppression) and one supporting case report, but no controlled clinical trials exist, and isoflurane's anesthesia-only delivery profile is impractical for a chronic headache indication. The remaining six predicted indications have no literature or trial support and should stay deprioritized.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph (warnings, contraindications) to close Blocking gap DG001
- Confirmed mechanism of action data from DrugBank (DG002)
- A controlled or pilot clinical study of isoflurane (or a non-anesthetic CSD-suppressing analog) in status migrainosus or refractory migraine
- Feasibility assessment of delivery route, since isoflurane requires anesthesia infrastructure incompatible with routine migraine care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

