---
layout: default
title: Dostarlimab
parent: Model Prediction Only (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Dostarlimab
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

# Dostarlimab: From dMMR Endometrial Cancer to Cervical Adenofibroma

## One-Sentence Summary

Dostarlimab (brand name JEMPERLI) is a PD-1 blocking antibody. Its rationale text describes an approval in mismatch-repair-deficient endometrial cancer. The TxGNN model predicts it may be effective for **cervical adenofibroma**, but **no clinical trials and no publications** currently support this. The prediction is weak and looks like a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometrial cancer, mismatch-repair-deficient (taken from the rationale text; the licence record has no indication text) |
| Predicted New Indication | Cervical adenofibroma |
| TxGNN Prediction Score | 50.0% (all 10 predictions for this drug share this score, so it does not discriminate between them) |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Dostarlimab is known to be a PD-1 blocking antibody. It releases the brake on T cells so the immune system can attack tumours that depend on the PD-1/PD-L1 pathway.

Cervical adenofibroma is a benign tumour with no established dependence on PD-1/PD-L1 signalling. Immune checkpoint blockade is aimed at malignant tumours, and benign lesions like this are usually managed by other means. The mechanistic rationale is therefore weak.

The score of 0.5 is uninformative, and the disease match is probably driven by the drug's association with gynaecologic cancers in the knowledge graph. This indication should not be treated as a credible repurposing lead without new evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications with Some Signal

The other nine predictions have little or no evidence. These four are the only ones with a possible lead or a safety signal:

| Predicted Indication | Evidence | Assessment |
|------|------|------|
| Bladder clear cell adenocarcinoma | [NCT04779151](https://clinicaltrials.gov/study/NCT04779151): Phase 2 basket trial of niraparib plus dostarlimab in DNA repair-deficient or platinum-sensitive solid tumours; terminated; 51 participants | Research question (L3). Basket enrolment does not establish disease-specific efficacy. The eligible tumour types and any posted results need checking. |
| Fallopian tube papillary adenocarcinoma | None supplied | Research question. A related Müllerian tract cancer, so testing dMMR/MSI-high status could make a hypothesis. This is by analogy only. |
| Vulvar alveolar soft part sarcoma | None supplied | Research question. PD-1 blockade is biologically plausible for this sarcoma, but the vulvar primary site is very rare. |
| LAMA5-related multisystemic syndrome | [PMID 40642102](https://pubmed.ncbi.nlm.nih.gov/40642102/) (2025, Gynecologic Oncology Reports): checkpoint inhibitor exacerbated paraneoplastic cerebellar degeneration in endometrial cancer, inferred to be a case report | Hold. This is a safety signal for immune-related neurological adverse events, not efficacy evidence. The disease match looks spurious. |

For the autoimmune liver overlap syndrome, PD-1 blockade could worsen autoimmunity, so the mechanistic direction argues against benefit.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2523434 | JEMPERLI |

The licence record has no dosage form or approved indication text.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-1 blocking antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

Checkpoint inhibitors as a class are known to cause immune-related adverse events, including immune-mediated hepatitis. One case report (PMID 40642102) describes a neurological event.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials, no literature and a non-discriminating model score, and the mechanism is weak for a benign tumour. No further work is justified on cervical adenofibroma.

**To proceed, the following is needed:**
- The Health Canada package insert, for warnings, contraindications and approved indications. This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- For the higher-plausibility questions (fallopian tube adenocarcinoma, vulvar alveolar soft part sarcoma, bladder clear cell adenocarcinoma), dedicated literature and trial searches. These should include the full NCT04779151 record and dMMR/MSI-high status.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

