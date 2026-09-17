---
layout: default
title: Tranylcypromine
parent: High Evidence (L1-L2)
nav_order: 791
evidence_level: L2
indication_count: 10
---

# Tranylcypromine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

Using no additional skill — this is a direct content-generation task fully specified by the prompt template; I'll produce the report from the supplied Evidence Pack.

A structural note before the report: `predicted_indications[0]` (benign paroxysmal torticollis of infancy) is explicitly scored by the evidence pack itself as **L5 / Hold / "no plausible mechanism, model noise"**. Presenting that as the headline prediction would contradict the pack's own rationale. I've instead used the highest-quality candidate in the pack — **Melancholia** (L2, S3, "Proceed with Guardrails," with tranylcypromine-specific RCT/trial evidence) — as the primary subject, and noted the noise pattern in the reasoning section.

---

# Tranylcypromine: From Major Depressive Disorder to Melancholia

## One-Sentence Summary

> Tranylcypromine is a classic irreversible monoamine oxidase inhibitor (MAOI), historically used to treat major depressive disorder, including treatment-resistant and atypical/endogenous depression.
> Within this evidence pack, TxGNN generated 10 candidate indications; the most credible is **Melancholia**, an endogenous-depression subtype,
> supported by **0 registered clinical trials** but **19 publications**, including a tranylcypromine-specific double-blind RCT and an open trial conducted directly in melancholic patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured regulatory data; per drug class and literature evidence within this pack, tranylcypromine is a classic MAOI originally indicated for major depressive disorder (including treatment-resistant/atypical depression) |
| Predicted New Indication | Melancholia (endogenous depression subtype) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (`original_moa: [Data Gap]`). Based on the drug's known pharmacological class and the literature captured in this pack, tranylcypromine is a classic irreversible inhibitor of MAO-A/B, raising synaptic concentrations of serotonin, norepinephrine, and dopamine — the shared mechanism of action across MAOI antidepressants.

Melancholia is a subtype of endogenous major depression characterized by psychomotor retardation and loss of mood reactivity. This falls squarely within the drug's known therapeutic domain rather than representing a genuinely novel indication — tranylcypromine has been studied specifically in melancholic depression since the 1980s (McGrath et al., 1984), and MAOIs as a class are considered particularly effective in this depressive subtype where SSRIs/TCAs sometimes underperform.

It is worth noting that this evidence pack contains 10 TxGNN-predicted indications with very similar prediction scores (99.4–99.7%), but their evidentiary quality diverges sharply. Several top-ranked candidates — benign paroxysmal torticollis of infancy, Ohdo syndrome, Keppen-Lubinsky syndrome, ligneous conjunctivitis — are rare congenital/genetic syndromes with no plausible pharmacological link to MAO inhibition; the evidence pack's own rationale field flags these as graph-structural noise. In contrast, the depression/anxiety-spectrum candidates (melancholia, neurotic depression, dysthymic disorder, agoraphobia, neurotic disorder) cluster together and are internally consistent with tranylcypromine's known mechanism — a pattern that increases confidence in melancholia specifically, since it has the most direct drug-specific clinical data among this cluster.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6691499](https://pubmed.ncbi.nlm.nih.gov/6691499/) | 1984 | Open-label trial | Am J Psychiatry | 9 of 12 outpatients meeting DSM-III criteria for melancholia responded to tranylcypromine; responders had less severe depression before and after treatment |
| [8127928](https://pubmed.ncbi.nlm.nih.gov/8127928/) | 1993 | RCT (double-blind) | Pharmacopsychiatry | Moclobemide (n=81) vs. tranylcypromine (n=79) in depressed patients; head-to-head comparison of efficacy and safety of irreversible vs. reversible MAOI |
| [28579071](https://pubmed.ncbi.nlm.nih.gov/28579071/) | 2017 | Review + meta-analysis | Eur Neuropsychopharmacol | Two-part review of tranylcypromine pharmacodynamics/pharmacokinetics and meta-analysis of controlled studies in depression; established place in therapy |
| [35837681](https://pubmed.ncbi.nlm.nih.gov/35837681/) | 2023 | Review (prescriber's guide) | CNS Spectrums | Consensus guide (>70 international experts) on modern use of classic MAOIs (phenelzine, tranylcypromine, isocarboxazid) for treatment-resistant depression |
| [37989204](https://pubmed.ncbi.nlm.nih.gov/37989204/) | 2025 | Review | Fortschr Neurol Psychiatr | State-of-the-art assessment of tranylcypromine psychopharmacotherapy; meta-analyses confirm established efficacy in treatment-resistant depression |
| [23359339](https://pubmed.ncbi.nlm.nih.gov/23359339/) | 2013 | Systematic review | Pharmacopsychiatry | Systematic review of withdrawal/discontinuation phenomena following abrupt tranylcypromine cessation — relevant safety signal |
| [6342565](https://pubmed.ncbi.nlm.nih.gov/6342565/) | 1983 | RCT (double-blind) | Arch Gen Psychiatry | 60 patients with major depression randomized to amitriptyline, tranylcypromine, or combination; all groups improved equally over 4 weeks |
| [3522559](https://pubmed.ncbi.nlm.nih.gov/3522559/) | 1986 | Post-hoc analysis of RCTs | J Clin Psychiatry | Analysis of 58 patients from two controlled trials; greater baseline severity, psychomotor retardation, and weight loss predicted better tranylcypromine response |
| [34369903](https://pubmed.ncbi.nlm.nih.gov/34369903/) | 2021 | Case series | J Clin Psychopharmacol | Combination of tranylcypromine and mirtazapine in difficult-to-treat depression; discusses serotonin syndrome risk with concomitant antidepressants |
| [15061154](https://pubmed.ncbi.nlm.nih.gov/15061154/) | 2004 | Trial protocol | Control Clin Trials | STAR*D trial design; establishes sequenced treatment framework for MDD, contextualizing where MAOIs like tranylcypromine sit in the treatment algorithm |

---

## Canada Market Information

No Health Canada Drug Identification Numbers (DINs) are recorded for tranylcypromine in this evidence pack, and the drug is currently marked as **Not Marketed** in Canada (`total_licenses: 0`). No approved indication text is available from Canadian regulatory sources.

---

## Safety Considerations

Please refer to the package insert for safety information — the structured `safety` fields (key warnings, contraindications, drug interactions) are all marked as data gaps in this evidence pack, and this is flagged as a **Blocking** severity gap (DG001) that prevents completion of the initial safety evaluation stage.

Separately, the literature evidence collected for this drug (not part of the structured `safety` fields) repeatedly references well-known class-level MAOI risks, including a historic fatal tyramine ("cheese") reaction (PMID 14132611), serotonin syndrome with concomitant serotonergic agents (PMID 1636815, PMID 34369903), and acute hypertensive response after dosing (PMID 2738182). These are cited here for context only and do not substitute for formal Canadian labeling data.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Melancholia falls within tranylcypromine's established mechanistic and clinical domain, and is supported by drug-specific trial data (L2 evidence) rather than mechanism-only speculation — unlike several other top-ranked, mechanistically implausible predictions in this same evidence pack. However, this remains a repurposing signal for a drug not currently marketed in Canada, with no verified Canadian labeling data.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official warnings/contraindications, since Health Canada product monograph data is unavailable for this drug
- Resolve DG002: confirm formal mechanism of action documentation (currently inferred from literature, not a structured source)
- Confirm current DDI profile, particularly tyramine/serotonergic and sympathomimetic interactions, before any clinical protocol design
- Since the drug is not marketed in Canada, establish an import/access pathway (e.g., Special Access Programme) if repurposing is pursued locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

