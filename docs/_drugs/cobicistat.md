---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 3
---

# Cobicistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# COBICISTAT: From HIV-1 Treatment (Pharmacokinetic Booster) to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Cobicistat is a selective CYP3A inhibitor used as a pharmacokinetic (PK) booster within combination antiretroviral regimens for HIV-1 infection — it has no intrinsic antiviral activity of its own.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This high-scoring prediction appears to reflect graph-based proximity between HIV-1 and SIV in the knowledge graph rather than any direct pharmacological evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (as a PK booster in combination antiretroviral therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, cobicistat is a mechanism-based, selective inhibitor of CYP3A4 and CYP3A5. It does not possess intrinsic antiviral activity; rather, it functions purely as a pharmacokinetic enhancer — slowing the hepatic and intestinal metabolism of co-administered antiretroviral drugs (such as protease inhibitors and integrase strand transfer inhibitors) to increase their plasma exposure. It is approved as a component of fixed-dose combinations including elvitegravir/cobicistat/emtricitabine/tenofovir (Stribild, Genvoya) and darunavir/cobicistat (Prezcobix, Symtuza).

Simian Immunodeficiency Virus (SIV) is a lentivirus infecting non-human primates and is evolutionarily closely related to HIV-1, sharing the same viral family (Retroviridae: Lentivirus), CD4+ T cell tropism, and reverse transcriptase-dependent replication pathway. In the TxGNN knowledge graph, SIV and HIV-1 therefore share multiple high-weight neighboring nodes, which likely explains why the model assigns cobicistat a high prediction score for SIV — the graph proximity algorithm propagates cobicistat's HIV-1 association directly to SIV through these shared nodes.

However, this mechanistic link is indirect and structurally weak. Cobicistat's entire therapeutic rationale rests on human hepatic CYP3A pharmacokinetics; whether CYP3A inhibition provides analogous PK boosting in non-human primate species — whose CYP enzyme profiles differ meaningfully from humans — has not been established. Furthermore, SIV infection is a veterinary and preclinical animal-model disease, not a human clinical target, making direct clinical translation uncertain at best.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Cobicistat is not currently marketed in Canada as a standalone product (0 DINs on record). No Health Canada drug identification numbers are registered for cobicistat in this dataset. Note that cobicistat-containing fixed-dose combination products (e.g., Stribild, Genvoya, Prezcobix) may hold separate DINs under their combination brand names, which are not captured here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score (99.92%), this prediction is an artefact of graph-based proximity between HIV-1 and SIV rather than a genuine pharmacological signal — cobicistat has no antiviral activity, SIV is an animal disease rather than a human clinical indication, and there is zero supporting clinical or literature evidence.

**To proceed, the following is needed:**
- **Mechanistic clarification**: Determine whether any SIV-active antiviral agents are CYP3A substrates that could plausibly benefit from cobicistat-mediated PK boosting in non-human primates
- **Non-human primate PK data**: Assess whether CYP3A inhibition by cobicistat translates to meaningful exposure enhancement in macaque or other relevant species
- **MOA data retrieval**: Obtain full DrugBank MOA record (currently unavailable) to enable complete mechanism-based evaluation
- **Regulatory pathway assessment**: Cobicistat is not marketed in Canada; any standalone regulatory submission pathway would need to be scoped before clinical application could be considered
- **Reconsideration of indication target**: Given cobicistat's role as a booster, repurposing evaluation should focus on human diseases where CYP3A substrate drugs are underexposed, rather than novel disease indications driven solely by graph proximity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

