---
layout: default
title: Elvitegravir
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 3
---

# Elvitegravir
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

# Elvitegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Elvitegravir is a human immunodeficiency virus integrase strand transfer inhibitor (INSTI), originally developed as part of combination antiretroviral therapy for the treatment of HIV-1 infection in adults.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (Feline AIDS)**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (integrase strand transfer inhibitor, combination ART) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on known pharmacological classification, elvitegravir is an integrase strand transfer inhibitor (INSTI) that blocks HIV-1 replication by preventing the strand transfer step — the covalent insertion of reverse-transcribed viral DNA into the host cell genome. This mechanism is specific to lentiviral integrase enzymes.

Feline Acquired Immunodeficiency Syndrome is caused by Feline Immunodeficiency Virus (FIV), a lentivirus belonging to the same *Retroviridae* family as HIV-1. Because both FIV and HIV-1 encode a structurally related integrase enzyme, there is a theoretical basis for cross-species INSTI activity — the knowledge graph underlying TxGNN likely captures this shared lentiviral biology as an association signal.

However, this link remains at the level of structural analogy and graph topology inference. No in vitro studies, animal experiments, or clinical data have verified elvitegravir's actual inhibitory activity or effective concentrations against FIV. In contrast, the second-ranked TxGNN prediction — Simian Immunodeficiency Virus (SIV) infection — carries 7 supporting publications documenting direct INSTI activity against SIV strains, making that indication far better characterized. The feline AIDS prediction should currently be treated as a hypothesis requiring primary biological validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note:** For the second-ranked prediction (Simian Immunodeficiency Virus infection, TxGNN score 99.89%, Evidence Level L3), 7 preclinical publications are available, including NHP macaque models and in vitro resistance mapping studies. If the clinical focus shifts toward SIV-related veterinary or translational research, that evidence base should be reviewed separately.

---

## Canada Market Information

Elvitegravir is not currently authorized for sale in Canada. No Drug Identification Numbers (DINs) have been issued by Health Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, and drug interactions) were not retrieved in this Evidence Pack. Full prescribing information should be consulted before any clinical or research application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based solely on the TxGNN model with no supporting clinical trials or published preclinical data specific to FIV, and elvitegravir has no market authorization in Canada — making clinical translation premature at this stage.

**To proceed, the following is needed:**
- In vitro studies confirming elvitegravir's antiviral activity against FIV integrase (EC₅₀ against FIV strains)
- Species-specific pharmacokinetic data in cats, including oral bioavailability and CNS penetration
- Safety and tolerability assessment in feline species (hepatic/renal metabolism differs substantially from humans)
- Identification of an appropriate veterinary dosage form and administration route
- Retrieval of complete mechanism of action data from DrugBank (currently pending — DG002)
- Full safety profile from the Health Canada or FDA package insert (currently pending — DG001)
- Cross-review of the SIV infection evidence base (L3, 7 publications) to determine whether the non-human primate model provides a relevant mechanistic bridge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

