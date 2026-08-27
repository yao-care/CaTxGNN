---
layout: default
title: Moclobemide
parent: 僅模型預測 (L5)
nav_order: 434
evidence_level: L5
indication_count: 2
---

# Moclobemide
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

# Moclobemide: From Social Anxiety Disorder to Agoraphobia

## One-Sentence Summary

Moclobemide is a reversible, selective monoamine oxidase-A inhibitor (RIMA), approved in multiple international markets for depression and social anxiety disorder.
The TxGNN model predicts it may be effective for **Agoraphobia**,
with **0 clinical trials** and **12 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Social Anxiety Disorder / Depression (European approved indications; no Canadian registration on file) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published literature, Moclobemide belongs to the RIMA (Reversible Inhibitor of Monoamine Oxidase-A) class. It acts by selectively and reversibly inhibiting MAO-A, thereby reducing the degradation of serotonin, norepinephrine, and dopamine. This upregulates monoaminergic tone in anxiety-relevant brain regions — including the amygdala, hippocampus, and prefrontal cortex — producing anxiolytic and antidepressant effects. Moclobemide's approval in Europe for social anxiety disorder directly establishes its utility in modulating the anxiety neural circuit.

Agoraphobia and panic disorder share a deeply overlapping clinical and neurobiological profile. Under DSM-III/IV, the combined diagnosis "panic disorder with agoraphobia" was standard practice, and most published trials enrolled patients under this combined label. Critically, both RCTs identified in this evidence pack (PMID 10448444; PMID 10361962) specifically studied patients with panic disorder *with agoraphobia* — meaning the existing clinical evidence directly addresses the comorbid population rather than panic disorder alone.

The same cortico-limbic anxiety circuits implicated in agoraphobia are targeted by moclobemide's RIMA mechanism, which has already demonstrated efficacy across multiple anxiety phenotypes: social anxiety disorder (European approval), panic disorder (RCT evidence), and mixed anxiety-depression. Reviews spanning from 1990 to 2020 consistently confirm the MAOI/RIMA class as active across the anxiety disorder spectrum. This mechanistic and phenotypic overlap strongly supports the biological plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10448444](https://pubmed.ncbi.nlm.nih.gov/10448444/) | 1999 | RCT | Br J Psychiatry | Placebo-controlled RCT directly comparing moclobemide, CBT, and their combination in panic disorder **with agoraphobia**; establishes moclobemide as an efficacious pharmacological option in this population |
| [10361962](https://pubmed.ncbi.nlm.nih.gov/10361962/) | 1999 | RCT | Eur Arch Psychiatry Clin Neurosci | Multicenter double-blind RCT (n=135): moclobemide 450 mg/day vs clomipramine 150 mg/day in DSM-III-R panic disorder with/without agoraphobia; comparable efficacy with favourable tolerability |
| [32002937](https://pubmed.ncbi.nlm.nih.gov/32002937/) | 2020 | Review | Adv Exp Med Biol | Comprehensive evidence-based review of pharmacotherapy for anxiety disorders (panic disorder/agoraphobia, GAD, SAD) grounded in meta-analyses and systematic reviews of randomised controlled studies |
| [28867934](https://pubmed.ncbi.nlm.nih.gov/28867934/) | 2017 | Review | Dialogues Clin Neurosci | Guideline-based review of anxiety disorder management including panic disorder/agoraphobia; addresses treatment gaps in primary care and catalogues pharmacological options |
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Review | Acta Psychiatr Scand Suppl | Meta-analysis confirms moclobemide's antidepressant and anxiolytic activity vs multiple comparators (TCAs, SSRIs, other MAOIs) across depressive and anxiety disorders |
| [2248064](https://pubmed.ncbi.nlm.nih.gov/2248064/) | 1990 | Review | Acta Psychiatr Scand Suppl | MAOIs demonstrated effective in controlled studies of panic disorder with agoraphobia, social phobia, PTSD, and mixed anxiety-depression; reviews clinical evidence for irreversible and reversible agents |
| [8313401](https://pubmed.ncbi.nlm.nih.gov/8313401/) | 1993 | Clinical Study | Clin Neuropharmacol | Randomised double-blind 8-week trial in panic disorder evaluating RIMA class (brofaromine); confirms better tolerability vs clomipramine without dietary restrictions — contextualises moclobemide class advantages |
| [16850261](https://pubmed.ncbi.nlm.nih.gov/16850261/) | 2006 | Neuroimaging Study | Metab Brain Dis | SPECT neuroimaging compares citalopram and moclobemide effects on resting brain perfusion in social anxiety disorder; supports shared cortico-limbic mechanism across anxiety phenotypes |
| [12006898](https://pubmed.ncbi.nlm.nih.gov/12006898/) | 2002 | Clinical Analysis | J Clin Psychopharmacol | Pharmacodynamic modelling of moclobemide treatment response in panic disorder; regression-slope analysis examines baseline severity–treatment interaction, informing patient selection |
| [7954487](https://pubmed.ncbi.nlm.nih.gov/7954487/) | 1994 | Open-label Study | Clin Neuropharmacol | 12-week open-label pilot (n=35): moclobemide 300–600 mg/day in social phobia; consistent improvement in both fear and avoidance components with good tolerability |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two RCTs from 1999 directly tested moclobemide in patients with panic disorder with agoraphobia, and the RIMA mechanism is already approved for social anxiety disorder in Europe — together these provide both clinical and mechanistic grounding for this repurposing direction. However, the evidence base is dated, no trials are currently registered for standalone agoraphobia, and safety documentation is unavailable in the current data pack, preventing a full risk-benefit evaluation.

**To proceed, the following is needed:**
- Full prescribing information (package insert / SmPC) to complete the safety, contraindication, and drug interaction assessment
- MOA documentation from DrugBank to formalise the mechanistic rationale
- Verification of current Canadian regulatory status via Health Canada's Drug Product Database (DPD)
- A systematic review or meta-analysis specifically targeting moclobemide in agoraphobia under DSM-5 criteria (standalone diagnosis), to address the gap between the older combined panic/agoraphobia trials and current diagnostic standards
- Comparative effectiveness data against current first-line therapies (SSRIs, SNRIs, CBT) to establish the clinical positioning of moclobemide in an agoraphobia-specific treatment pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

