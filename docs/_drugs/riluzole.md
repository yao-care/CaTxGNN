---
layout: default
title: Riluzole
parent: High Evidence (L1-L2)
nav_order: 680
evidence_level: L1
indication_count: 10
---

# Riluzole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

Using the report as a direct writing task (no coding/skill needed) — one judgment call worth flagging up front: `predicted_indications[0]` by raw TxGNN score is *bilateral parasagittal parieto-occipital polymicrogyria*, but the evidence pack's own rationale calls this (and ranks #2, #4, #5, #9) likely model noise/false positives with zero evidence and `Hold` status. The only candidate with real evidence (L1, 20 PubMed papers, `Proceed with Guardrails`) is rank #8 — Amyotrophic Lateral Sclerosis, susceptibility to — which is also riluzole's globally established indication. I built the report around that one rather than the noise-flagged top score, and noted the discarded high-score predictions in the summary for transparency.

---

# Riluzole (DB00740): From an Unrecorded Original Indication to Amyotrophic Lateral Sclerosis (Susceptibility)

## One-Sentence Summary

Riluzole's original indication is not recorded in this dataset, but it is globally known as the standard glutamate-modulating therapy for amyotrophic lateral sclerosis (ALS, marketed elsewhere as Rilutek). TxGNN's highest-scoring predictions in this run (polymicrogyria, skeletal dysplasia, mitochondrial myopathy, and others) are flagged by the model's own rationale as likely false positives with no supporting mechanism or evidence. The one prediction with real evidentiary support — **Amyotrophic Lateral Sclerosis, susceptibility to** — is backed by **20 publications** (no dedicated clinical trials registered for this exact term), and effectively confirms the drug's known efficacy rather than identifying a novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset (data gap); riluzole is globally approved for Amyotrophic Lateral Sclerosis |
| Predicted New Indication | Amyotrophic Lateral Sclerosis, susceptibility to |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not on file in the regulatory record for this drug (data gap). However, the evidence pack's own repurposing rationale supplies the mechanistic basis: riluzole inhibits presynaptic glutamate release and blocks voltage-gated sodium channels, reducing glutamate-mediated excitotoxicity in motor neurons — one of the three core pathophysiological mechanisms of ALS (alongside oxidative stress and mitochondrial dysfunction).

Because riluzole is already the internationally approved standard-of-care drug for ALS, this "predicted new indication" is not a novel repurposing signal — it is TxGNN correctly re-identifying the drug's own established use. The "Not marketed / Not marketed" status in this dataset most plausibly reflects that riluzole has not yet obtained a market authorization in this jurisdiction, not an absence of efficacy evidence.

By contrast, the other top-ranked-by-score predictions in this batch (bilateral parasagittal parieto-occipital polymicrogyria, axial spondylometaphyseal dysplasia, trichomegaly-retina pigmentary degeneration-dwarfism syndrome, lethal arthrogryposis-anterior horn cell disease syndrome, autosomal dominant mitochondrial myopathy) involve developmental, skeletal, or metabolic pathology with no known connection to glutamate excitotoxicity or sodium-channel blockade. The evidence pack itself labels these as likely model noise, with zero supporting trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Review | CNS Drugs | Riluzole is the only medication shown to modestly prolong ALS survival; reviews pathophysiology, diagnosis, and management. |
| [8061281](https://pubmed.ncbi.nlm.nih.gov/8061281/) | 1994 | Preclinical | Neuroreport | Riluzole shows neuroprotective effects against ALS patient CSF cytotoxicity mediated by AMPA/kainate receptors, supporting an excitotoxicity-based mechanism. |
| [20942785](https://pubmed.ncbi.nlm.nih.gov/20942785/) | 2010 | Review | CNS Neurol Disord Drug Targets | Notes riluzole is the only available ALS drug, extending lifespan by 2–3 months; reviews genetic determinants as therapeutic targets. |
| [19593125](https://pubmed.ncbi.nlm.nih.gov/19593125/) | 2009 | Review | Curr Opin Neurol | Confirms riluzole remains the only drug with proven efficacy in ALS despite intensive research into disease mechanisms. |
| [22646982](https://pubmed.ncbi.nlm.nih.gov/22646982/) | 2011 | Review (preclinical drug discovery) | Expert Opin Drug Discov | Riluzole is the only approved ALS therapeutic, improving survival by 2–3 months; discusses unmet need for new agents. |
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Review | Journal of Neurology | Details the "glutamate hypothesis" of motor neuron injury in ALS, the mechanistic basis for riluzole's antiglutamatergic action. |
| [16723044](https://pubmed.ncbi.nlm.nih.gov/16723044/) | 2006 | Review | Expert Rev Mol Med | Reviews proposed ALS mechanisms (oxidative stress, excitotoxicity, mitochondrial dysfunction, protein aggregation) and treatment pathways. |
| [20942786](https://pubmed.ncbi.nlm.nih.gov/20942786/) | 2010 | Review | CNS Neurol Disord Drug Targets | Reviews ALS diagnosis, pathogenesis, and therapeutic targets, including glutamate-related approaches. |
| [22763933](https://pubmed.ncbi.nlm.nih.gov/22763933/) | 2012 | Review | Praxis | Reviews ALS diagnosis and treatment, characterizing selective motor neuron degeneration. |
| [31108504](https://pubmed.ncbi.nlm.nih.gov/31108504/) | 2019 | Preclinical | Human Molecular Genetics | iPSC-derived ALS motor neurons show altered calcium dynamics and glutamate receptor properties; notes riluzole minimally extends life expectancy via inhibition of glutamatergic transmission and calcium overload. |

---

## Canada Market Information

Riluzole currently has no marketed products or DINs on file for this jurisdiction (0 licenses recorded; market status: Not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Riluzole's evidence for ALS is L1-level (20 supporting publications, internationally established standard of care), but it is not currently marketed in this jurisdiction and safety-label data is missing, so review should proceed cautiously rather than move straight to a "Go."

**To proceed, the following is needed:**
- Package insert / label warnings and contraindications (flagged as a **Blocking** data gap — currently prevents entry into initial safety review, per meta.data_gaps DG001)
- Mechanism-of-action documentation from DrugBank to formally close the MOA data gap (DG002)
- A dedicated market-authorization assessment, since this is a regulatory/availability gap rather than an efficacy gap
- Independent evaluation (or explicit exclusion) of the five noise-flagged predictions before they are surfaced to reviewers, to avoid diluting confidence in the genuine signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

