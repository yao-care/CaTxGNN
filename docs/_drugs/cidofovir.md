---
layout: default
title: Cidofovir
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 4
---

# Cidofovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Cidofovir: From Antiviral (CMV) to Sclerosing Cholangitis

## One-Sentence Summary

Cidofovir is a broad-spectrum antiviral nucleotide analogue, originally developed for the treatment of cytomegalovirus (CMV) retinitis in immunocompromised patients (including those with HIV/AIDS).
The TxGNN model predicts it may have potential utility in **Sclerosing Cholangitis**,
however, **no clinical trials** and **no direct supporting publications** have been identified for this indication to date.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Canada regulatory record; known use: CMV retinitis in immunocompromised patients |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Cidofovir is a nucleotide analogue antiviral agent. It is phosphorylated intracellularly to its active diphosphate form, which acts as a competitive inhibitor of viral DNA polymerase — particularly that of cytomegalovirus (CMV). This mechanism provides potent suppression of CMV replication and is the pharmacological basis for its established use in CMV retinitis among HIV/AIDS patients.

The proposed mechanistic link between Cidofovir and sclerosing cholangitis is indirect and highly speculative. CMV infection in immunosuppressed individuals is a recognised cause of secondary sclerosing cholangitis (CMV cholangiopathy), in which direct bile duct epithelial infection and periductal inflammation can produce a cholestatic picture mimicking primary sclerosing cholangitis (PSC). The TxGNN knowledge graph likely established this connection through a "CMV infection → biliary tract disease" edge, inferring that an effective anti-CMV agent could be beneficial in CMV-driven biliary pathology.

It is critical to distinguish, however, that the far more prevalent form — primary sclerosing cholangitis (PSC) — is an autoimmune fibroinflammatory condition with no established viral aetiology. Cidofovir's antiviral mechanism offers no known pathway to modulate autoimmune biliary inflammation or fibrosis. The prediction is therefore biologically plausible only within the narrow context of CMV-associated secondary cholangitis, and even then, supporting clinical data are entirely absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Cidofovir has no Drug Identification Numbers (DINs) currently registered in Canada and is not marketed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is classified as **L5** — model prediction only, with no clinical trials or literature directly supporting Cidofovir for sclerosing cholangitis. The mechanistic rationale is biologically coherent only for the rare CMV-associated secondary subtype, and is entirely inapplicable to the much more common autoimmune-driven PSC. The signal most likely reflects an indirect knowledge graph edge rather than a true repurposing opportunity.

**To proceed, the following is needed:**
- Confirmed MOA data from DrugBank to formally document the antiviral mechanism
- Identification of any case reports or retrospective series describing Cidofovir use in CMV-associated cholangitis or CMV cholangiopathy
- Subtype clarification: any future investigation must specify whether the target is PSC (autoimmune, not suitable) or CMV-associated secondary sclerosing cholangitis (potentially suitable)
- Canada package insert safety data, including nephrotoxicity warnings (Cidofovir is known for significant renal toxicity), key contraindications, and drug interactions
- Assessment of Canada regulatory pathway, given zero current DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

