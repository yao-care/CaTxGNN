---
layout: default
title: Givosiran
parent: 僅模型預測 (L5)
nav_order: 363
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: From Acute Hepatic Porphyria to Porphyria due to ALA Dehydratase Deficiency

## One-Sentence Summary

Givosiran (Givlaari) is a GalNAc-conjugated siRNA therapeutic approved by the FDA (2019) for the prevention of acute attacks in Acute Hepatic Porphyria (AHP), primarily targeting ALAS1 — the first rate-limiting enzyme in hepatic heme biosynthesis.
The TxGNN model generates 10 predictions; ranks 1–8 are assessed as knowledge graph (KG) structural false positives driven by liver-disease node clustering, with no mechanistic basis or clinical evidence.
**Rank 9 — Porphyria due to ALA Dehydratase Deficiency (ALAD porphyria / Doss porphyria)** — is the single prediction with genuine mechanistic plausibility and literature support, backed by **0 dedicated clinical trials** and **8 publications** (including indirect Phase 3 ENVISION data and one critical negative case report).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Hepatic Porphyria (AHP) — FDA approved 2019 (Givlaari) |
| Predicted New Indication | Porphyria due to ALA Dehydratase Deficiency (ALAD porphyria, Rank 9) |
| TxGNN Prediction Score | 99.91% (Rank 9 of 10; Ranks 1–8 assessed as KG false positives) |
| Evidence Level | L3 (indirect Phase 3 data + negative case report; no dedicated ADP trials) |
| Canada Market Status | ✗ Not Marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Hold (Research Question) |

> **Note on ranks 1–8:** Early-onset familial noncirrhotic portal hypertension, primitive portal vein thrombosis, hepatoportal sclerosis, idiopathic copper-associated cirrhosis, hepatopulmonary syndrome, chronic HCV/HBV infection, glycogen storage disease, and phenylalanine metabolism disorder all score 99.93–99.99% but share identical or near-identical TxGNN scores — a hallmark of KG topological clustering around the "hepatic disease" node, not disease-specific pharmacological prediction. None has mechanistic support, clinical trials, or literature. All are assessed as **Hold (L5)** and are not featured in this report.

---

## Why is This Prediction Reasonable?

Givosiran is a subcutaneously administered, GalNAc-conjugated small interfering RNA (siRNA) that is selectively taken up by hepatocytes via the asialoglycoprotein receptor. Inside the liver cell, it silences the mRNA of **ALAS1** (δ-aminolevulinic acid synthase 1), the first and rate-limiting enzyme in the heme biosynthesis pathway. By suppressing ALAS1, givosiran reduces production of the downstream neurotoxic intermediates **δ-aminolevulinic acid (ALA)** and porphobilinogen (PBG) — the metabolites responsible for the acute neurovisceral attacks of AHP.

**ALAD porphyria (Doss porphyria)** is caused by autosomal recessive deficiency of ALA dehydratase (ALAD), the **second enzyme** in the heme biosynthesis pathway. Because ALAD is deficient, ALA cannot be converted to PBG, and ALA accumulates — the same neurotoxic intermediate that drives AHP attacks. In principle, givosiran could reduce this accumulation *upstream* by suppressing ALAS1 and thereby limiting the total ALA entering the pathway. This upstream bypass logic is mechanistically coherent. Notably, the FDA 2019 approval label explicitly includes ADP within the AHP indication umbrella.

However, the picture is complicated. A documented case report (PMID 35991568) recorded a **complete lack of response** to givosiran in an ALAD porphyria patient. The proposed explanation is that in ADP, the metabolic bottleneck lies entirely at the ALAD step itself — meaning that even if ALAS1 produces less ALA, the severely deficient ALAD enzyme cannot clear what remains, and clinical benefit is not achieved. The Phase 3 ENVISION trial enrolled predominantly Acute Intermittent Porphyria (AIP) patients with very few ADP cases, leaving the ADP question statistically unresolved.

---

## Clinical Trial Evidence

No clinical trials specifically targeting givosiran in ALAD porphyria (Doss porphyria) are currently registered on ClinicalTrials.gov or ICTRP.

The Phase 3 ENVISION trial (NCT03338816) is the pivotal study for givosiran across AHP subtypes, but ALAD porphyria patients were not the primary enrollment target. No dedicated ADP trial has been launched.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | 2022 | RCT | J Intern Med | Givosiran significantly reduces AHP attack rates; primary AIP population, ADP subgroup not separately reported |
| [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/) | 2022 | Phase 3 Clinical Data | Orphanet J Rare Dis | Phase 3 ENVISION post-hoc analysis; quantifies AHP disease burden; ADP included in AHP definition but not individually analyzed |
| [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/) | 2022 | Case Report (NEGATIVE) | Front Genet | **Critical negative finding**: a documented ALAD porphyria (Doss porphyria) patient showed no response to givosiran; authors hypothesize ADP metabolic bottleneck is not at ALAS1 |
| [35734365](https://pubmed.ncbi.nlm.nih.gov/35734365/) | 2022 | Review / Drug Development Analysis | Drug Des Dev Ther | Comprehensive review of givosiran siRNA mechanism and clinical development for AHP; discusses AHP subtype spectrum including ADP |
| [37027823](https://pubmed.ncbi.nlm.nih.gov/37027823/) | 2023 | Review | Blood | RNA interference in AHPs; covers ALAS1 biology and givosiran mechanism; contextualizes ADP within the porphyria therapeutic landscape |
| [39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/) | 2024 | Clinical Practice Review | Rev Clin Esp | Therapeutic approach to acute hepatic porphyria crises; classifies ADP alongside AIP as an AHP subtype treatable with givosiran |
| [40312531](https://pubmed.ncbi.nlm.nih.gov/40312531/) | 2025 | Phase 3 Subgroup | Sci Rep | Givosiran expanded access in 10 Japanese AHP patients; confirms subcutaneous monthly dosing (2.5 mg/kg) is safe and effective; AHP subtypes not individually broken down |
| [36883675](https://pubmed.ncbi.nlm.nih.gov/36883675/) | 2023 | PK/PD Modeling | CPT Pharmacometr Syst Pharmacol | Semimechanistic PK/PD model of urinary ALA reduction across Phase I–III trials; informs dosing rationale for reducing ALA in AHP broadly |

---

## Canada Market Information

Givosiran (brand name: Givlaari, Alnylam Pharmaceuticals) is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) have been issued by Health Canada as of the data cutoff (2026-06-21).

Givosiran holds FDA approval (USA, 2019) and EMA approval (Europe, 2020) for acute hepatic porphyria in adults. A Health Canada submission has not been identified in the public record.

---

## Safety Considerations

Package insert safety data was not available in the current evidence pack (Data Gap: TFDA/Health Canada label not retrieved). Based on published clinical trial reports and the FDA prescribing information:

- **Key Warnings**: Hepatotoxicity (elevated alanine aminotransferase observed in Phase 3 ENVISION; monitor liver function); anaphylaxis risk (post-marketing reports)
- **Drug Interactions**: Givosiran inhibits CYP1A2 and CYP2D6 — concomitant use of sensitive CYP1A2 substrates (e.g., theophylline, tizanidine) and CYP2D6 substrates (e.g., tamoxifen, some antidepressants) requires dose reduction or avoidance

For complete safety information, please refer to the **Givlaari (givosiran) FDA package insert** (Alnylam Pharmaceuticals, 2021 revision).

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Although ALAD porphyria falls within givosiran's FDA-approved AHP indication umbrella, the only documented clinical case of givosiran use specifically in ALAD porphyria showed no response — directly undermining the upstream ALAS1-suppression rationale. Phase 3 ENVISION evidence cannot be extrapolated to ADP without dedicated subgroup data. This is best classified as an open research question, not an actionable repurposing candidate, until the mechanism of treatment failure is resolved.

**To proceed, the following is needed:**
- Prospective case series or dedicated expanded access program enrolling ALAD porphyria patients with systematic urinary ALA/PBG biomarker monitoring
- Investigation into why the documented case showed no response: residual ALAD activity assay, ALA kinetics pre- and post-givosiran dosing
- Reassessment of whether upstream ALAS1 suppression can meaningfully reduce intracellular ALA when the ALAD step is severely impaired
- Health Canada regulatory review: ADP is mechanistically distinct from AIP and may require a separate indication filing despite being listed in the FDA label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

