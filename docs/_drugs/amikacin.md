---
layout: default
title: Amikacin
parent: Model Prediction Only (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Amikacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Amikacin: From Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Amikacin is an aminoglycoside antibacterial, and the Health Canada license records provided do not state its approved indications.
The TxGNN model predicts it may be effective for **paratyphoid fever**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on model output and drug class alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license records; amikacin is an aminoglycoside antibacterial (bacterial infections) |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Amikacin belongs to the aminoglycoside class, which is active against Gram-negative bacteria. *Salmonella*, the cause of paratyphoid fever, is Gram-negative, so in vitro activity is biologically plausible.

The link is weak in clinical practice. Aminoglycosides penetrate poorly into host cells, where *Salmonella* persists, and they are not standard therapy for enteric fever. Fluoroquinolones, azithromycin and third-generation cephalosporins are the established agents. The 99.82% score is a model output, not clinical evidence, and the connection is inferred from drug class only.

The other top-ranked predictions show the same pattern. Typhoid fever, salmonellosis, meningococcemia and epiglottitis are bacterial infections with a generic antibacterial rationale, but amikacin is not a standard agent for any of them. Diffuse scleroderma, congenital analbuminemia, polyclonal hyperviscosity syndrome and hyperamylasemia have no plausible mechanistic link and are likely knowledge-graph artifacts. Punctate epithelial keratoconjunctivitis is often viral or inflammatory, and topical aminoglycosides can themselves cause epithelial toxicity. None of the ten predictions has trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2242971 | AMIKACIN SULFATE INJECTION USP |
| 2486717 | AMIKACIN SULFATE INJECTION |
| 2529459 | AMIKACIN SULFATE INJECTION |
| 2481073 | AMIKACIN SULFATE INJECTION USP |
| 2525909 | AMIKACIN SULFATE INJECTION |

Dosage form, manufacturer and approved indication text were not included in the records provided.

---

## Safety Considerations

Please refer to the package insert for safety information.

Aminoglycosides carry a known risk of nephrotoxicity, which is a particular concern in populations at risk of renal disease, such as those with scleroderma renal involvement.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it (L5, model prediction only). Clinical practice also argues against it, because aminoglycosides are unreliable against intracellular *Salmonella* and effective alternatives already exist.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Approved indication text for the Canadian licenses, to confirm the original indication
- Any supporting clinical or preclinical evidence for amikacin in paratyphoid fever or typhoid fever, including comparison against current standard agents
- Route compatibility assessment, since the required and available routes are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

