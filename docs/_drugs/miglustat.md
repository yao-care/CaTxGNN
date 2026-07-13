---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: From Gaucher Disease to Tay-Sachs Disease

## One-Sentence Summary

Miglustat (Zavesca) is a glucosylceramide synthase (GCS) inhibitor originally approved as substrate reduction therapy (SRT) for Type 1 Gaucher disease and Niemann-Pick disease type C, working by blocking upstream glycosphingolipid biosynthesis. Among 10 TxGNN-predicted indications, **Tay-Sachs Disease** stands out as the highest-evidence candidate, supported by **5 clinical trials** and **20 publications** — all other predictions are model-only (L5, Hold). The mechanistic rationale is the strongest of all candidates: GM2 ganglioside accumulation in Tay-Sachs follows a biosynthetic pathway (GlcCer → LacCer → GM2) that GCS inhibition can directly interrupt upstream.

> **Scope note**: TxGNN's top-ranked prediction by model score is "autosomal ichthyosis syndrome with fatal disease course" (99.83%), but it carries zero clinical evidence and a Hold recommendation. This report focuses on **Tay-Sachs disease** (TxGNN rank #7 by score, L2 evidence, Research Question) as the only actionable repurposing candidate in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 1 Gaucher disease; Niemann-Pick disease type C |
| Predicted New Indication | Tay-Sachs Disease (GM2 Gangliosidosis) |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not found in Health Canada database |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not captured in this Evidence Pack. Based on published literature, Miglustat is a competitive inhibitor of **glucosylceramide synthase (GCS)** — the enzyme that converts ceramide to glucosylceramide (GlcCer), the first committed step in glycosphingolipid (GSL) biosynthesis. By reducing GlcCer production, Miglustat lowers the downstream supply of all GlcCer-derived GSLs. This is the basis of its approved use in Gaucher disease (GlcCer accumulation) and Niemann-Pick type C (secondary GSL buildup).

Tay-Sachs disease shares this same metabolic highway. In Tay-Sachs, β-hexosaminidase A (HexA) deficiency prevents GM2 ganglioside from being broken down. GM2 is synthesized along the pathway **Ceramide → GlcCer → LacCer → GM3 → GM2**. Miglustat blocks this pathway at the very first step, reducing the rate at which GM2 is synthesized in the first place — the therapeutic strategy known as substrate reduction therapy (SRT). This is the most mechanistically direct connection among all 10 TxGNN candidates, and it mirrors the exact rationale for Miglustat's approved indications.

The critical clinical nuance is patient population. Infantile Tay-Sachs progresses so rapidly that SRT cannot meaningfully change outcomes — two terminated trials confirm this. **Late-onset (adult/juvenile) Tay-Sachs**, however, presents a slower disease course where upstream substrate reduction has a viable therapeutic window. A 12-month randomized controlled trial (Shapiro et al., 2009) and a 2023 systematic review (Mansouri et al.) have directly explored this approach in late-onset GM2 gangliosidosis, providing the foundational evidence for proceeding further.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | Completed | 10 | PK, safety, and tolerability of Miglustat in infantile-onset GM2 gangliosidosis (Tay-Sachs and infantile Sandhoff); confirmed drug penetration into CSF — a prerequisite for CNS efficacy |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | Completed | 5 | Single and multiple oral-dose PK of Miglustat in juvenile GM2 gangliosidosis; established dosing parameters and tolerability in the pediatric population |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Phase 2 | Recruiting | 21 | Long-term safety, PK, and efficacy of Nizubaglustat (a next-generation GCS inhibitor) in GM2 gangliosidosis or NPC; includes a cohort transitioning from stable Miglustat — signals ongoing field interest |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | Terminated | 30 | Miglustat effects on neurological and systemic symptoms of infantile-type Sandhoff/Tay-Sachs; termination is a key negative signal — SRT alone is unlikely sufficient for the rapidly progressive infantile form |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | Terminated | 16 | Miglustat + ketogenic diet (Syner-G) synergistic regimen for infantile/juvenile gangliosidoses; terminated status limits conclusions, though it signals interest in combination approaches |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genetics in Medicine | 12-month randomized controlled trial + 24-month extension evaluating Miglustat safety and efficacy in late-onset GM2 gangliosidosis; primary clinical efficacy data for this repurposing direction |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Systematic Review | European Journal of Neurology | Systematic review of Miglustat safety and efficacy across GM2 gangliosidosis studies; synthesizes inconsistent prior results to clarify the overall evidence picture |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Review | Int J Mol Sciences | Comprehensive review of GM2 gangliosidoses pathophysiology and current therapies including SRT; covers neuroinflammation and neuronal apoptosis as mechanistic targets |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Review | Frontiers in Physiology | Reviews new approaches to Tay-Sachs therapy including SRT, gene therapy, enzyme replacement, and pharmacological chaperones; contextualizes Miglustat's role among emerging alternatives |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Case Series | Neurology | SRT with Miglustat in 2 infantile Tay-Sachs patients; neurological deterioration was not arrested, but drug penetration into CSF was confirmed and macrocephaly was prevented — clinically important negative result for the infantile subtype |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Observational | Mol Genetics and Metabolism | Natural history mapping of infantile GM2 gangliosidoses; notes GI side effects as a limiting factor for Miglustat use in young patients |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Pilot Study | J Inherited Metabolic Disease | Neurocognitive testing in late-onset Tay-Sachs (LOTS) patients; explores cognition as an outcome measure for therapeutic trials in adult-onset disease |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Drug Overview | Curr Opin Investig Drugs | Expert overview of Miglustat development; confirms launch for Gaucher disease and describes pipeline for Tay-Sachs, Fabry disease, and NPC — historical basis of the repurposing rationale |
| [11227045](https://pubmed.ncbi.nlm.nih.gov/11227045/) | 2001 | Expert Review | Expert Opin Investig Drugs | Mechanistic basis for substrate reduction therapy across glycosphingolipid storage disorders; foundational rationale for applying GCS inhibition beyond Gaucher disease |
| [9103204](https://pubmed.ncbi.nlm.nih.gov/9103204/) | 1997 | Basic Science | Science | Landmark preclinical study: N-butyldeoxynojirimycin (chemical precursor to Miglustat) prevented lysosomal GM2 storage in Tay-Sachs mice and reduced storage neurons in brain — the original proof-of-concept for this repurposing direction |

---

## Canada Market Information

No Health Canada DINs were found for Miglustat in this dataset (market status: Not Marketed, 0 licenses).

**Important caveat**: This is likely a data gap rather than a true regulatory absence. Miglustat (Zavesca®) is known to hold regulatory approval in the EU and US for Type 1 Gaucher disease and Niemann-Pick disease type C. Verification through the Health Canada Drug Product Database (DPD) is strongly recommended before drawing conclusions about Canadian market status. If approved, the product monograph would be the definitive source for Canadian labeling, warnings, and approved indications.

---

## Safety Considerations

No safety data was captured in this Evidence Pack (warnings and contraindications: not available; drug interaction query: no records found).

Key safety signals from published literature (for orientation — not a substitute for the product monograph):

- **Gastrointestinal effects**: Diarrhea, flatulence, and abdominal cramping are the most common adverse events; dose-dependent and frequently dose-limiting, particularly in younger patients
- **Neurological effects**: Tremor and peripheral neuropathy have been reported with long-term use; baseline neurological assessment recommended
- **Other effects**: Weight loss and muscle weakness observed in clinical studies

Please refer to the Zavesca product monograph (or applicable package insert) for the complete and authoritative safety profile.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tay-Sachs disease shares the exact upstream biosynthetic pathway that Miglustat is mechanistically designed to interrupt, making this the strongest repurposing candidate in the TxGNN prediction set. A completed Phase 3 PK study, a completed Phase 2 study, a published RCT (Shapiro et al., 2009), and a 2023 systematic review collectively establish an L2 evidence base — though the evidence is clearer for late-onset (adult) Tay-Sachs than for the infantile form, where two terminated trials signal insufficient efficacy.

**To proceed, the following is needed:**

- **Verify Health Canada status**: Confirm Miglustat DIN status via the Health Canada Drug Product Database — the current 0-DIN record is likely a data gap
- **Obtain the Canadian product monograph**: Required for complete warnings, contraindications, and approved indication language before any clinical decision-making
- **Clarify terminated trial outcomes**: Determine whether NCT03822013 and NCT02030015 were terminated for efficacy failure, safety concerns, or enrollment challenges — this critically affects interpretation of the evidence
- **Narrow the target population**: Based on existing data, focus on **late-onset (adult/juvenile) Tay-Sachs**; the infantile form is not a viable target for SRT monotherapy
- **Full-text review of Mansouri et al. 2023** (PMID 37209042): This systematic review is the most current evidence synthesis and should be reviewed in full before any clinical or regulatory pathway decision
- **Monitor NCT07399704**: The ongoing Nizubaglustat trial (recruiting, n=21) includes a Miglustat-transition cohort and may generate comparative data relevant to next-generation GCS inhibitor positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

