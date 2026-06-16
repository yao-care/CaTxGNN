---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir (DrugBank DB00442) is a first-line oral antiviral for chronic hepatitis B virus (HBV) infection, acting as a potent inhibitor of HBV DNA polymerase.
The TxGNN model assigns a prediction score of **99.98%** for **chronic hepatitis C virus (HCV) infection** — placing it at Rank #1 among repurposing candidates —
however, this signal appears to be a **knowledge graph topology artifact**: no clinical trial has evaluated entecavir as an HCV treatment, and its pharmacological target (HBV DNA polymerase) is structurally and functionally distinct from HCV's NS5B RNA-dependent RNA polymerase.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus (HBV) infection |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, entecavir is a cyclopentyl deoxyguanosine analogue that competitively inhibits HBV DNA polymerase through three distinct activities: reverse transcriptase priming, DNA-dependent DNA synthesis of the negative strand, and RNase H activity. This mechanism is highly specific to HBV's reverse-transcribing replication cycle and has been the basis for its approved clinical use.

Hepatitis C virus, by contrast, is a positive-sense single-stranded RNA virus that replicates through NS5B RNA-dependent RNA polymerase (RdRp) — a structurally and enzymatically different target from HBV DNA polymerase. No in vitro or in vivo data in the retrieved literature demonstrates that entecavir inhibits HCV NS5B or suppresses HCV RNA replication.

The high TxGNN prediction score reflects graph topology rather than biological plausibility. In the TxGNN knowledge graph, HBV and HCV occupy neighboring disease nodes due to shared clinical contexts: both cause chronic hepatitis, cirrhosis, and hepatocellular carcinoma; both are managed in co-infection scenarios; and both appear frequently in the same clinical guidelines and patient populations. This proximity generates a high prediction score, but does not constitute mechanistic evidence. ⚠️ In HBV/HCV co-infected patients, entecavir is routinely co-administered with direct-acting antivirals (DAAs) — but exclusively as an **HBV suppressor**, not as an anti-HCV agent. This prediction is most accurately classified as a **false positive driven by disease-node proximity** in the knowledge graph.

---

## Clinical Trial Evidence

All retrieved clinical trials involve entecavir in HBV or HBV/HCV co-infection management. No trial has evaluated entecavir as a direct treatment for HCV infection.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of DAA-based treatment for chronic HCV/HBV co-infected patients; monitored HBV reactivation incidence and risk factors during anti-HCV therapy; entecavir used as HBV suppressor background, not as HCV treatment |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Three-arm RCT evaluating prophylactic nucleoside analogue timing (12-week vs. 24-week prophylaxis) to prevent HBV clinical reactivation in HCV/HBV co-infected patients receiving DAA therapy for chronic hepatitis C |
| [NCT06566248](https://clinicaltrials.gov/study/NCT06566248) | Phase 2 | Recruiting | 90 | Phase IIa evaluation of TQA3810 tablets combined with or without nucleoside analogues in primary/treated HBV patients; entecavir serves as active comparator background |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | Cohort of 66 anti-HCV-antibody-positive chronic hepatitis B patients receiving nucleoside analogue therapy; HCV reactivation was observed; ETV role is HBV suppression, not HCV treatment |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Treatment advances for HBV/HCV co-infection; entecavir recommended for HBV component; HCV managed with interferon-based or DAA regimens; no cross-activity reported |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | Antiviral drugs for chronic HBV and HCV infection and renal effects; entecavir classified as HBV-specific nucleoside analogue; HCV requires separate agent class |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review | Clinics and Research in Hepatology and Gastroenterology | HBV/HCV co-infection as therapeutic challenge; dual infection accelerates liver disease; entecavir manages the HBV component alongside IFN-based HCV regimens |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clinics and Research in Hepatology and Gastroenterology | Pediatric management of viral hepatitis B and C; ETV is first-line for HBV in children; HCV managed separately; no shared treatment agent described |

---

## Canada Market Information

Entecavir is currently **not registered in Canada**. Health Canada records show zero Drug Identification Numbers (DINs), and no licensed entecavir products are available through the standard Canadian approval pathway. Patients or researchers seeking access would need to apply through Health Canada's Special Access Program.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.98% for chronic HCV infection is driven by knowledge graph topology — HBV and HCV nodes are neighbors due to shared clinical context — rather than mechanistic or clinical evidence. Entecavir has no established pharmacological activity against HCV NS5B RNA-dependent RNA polymerase, and every retrieved clinical trial involves ETV exclusively as an HBV suppressor. Furthermore, entecavir is not marketed in Canada, adding a regulatory access barrier.

**To proceed, the following is needed:**
- Formal in vitro screening of entecavir against HCV NS5B RdRp to rule out off-target antiviral activity
- Knowledge graph interpretability analysis (edge attribution) to confirm that the high TxGNN score for HCV is attributable to disease-node proximity rather than drug-specific evidence
- If any in vitro HCV activity is detected: HCV replicon assay profiling and pharmacokinetic assessment before any clinical consideration
- Regulatory pathway assessment via Health Canada Special Access Program for any Canadian clinical use

> **Research note:** The TxGNN Rank #2 prediction — hepatitis B virus infection (score 99.85%, L1 evidence, decision: Proceed with Guardrails) — corresponds to entecavir's established approved indication and is supported by multiple completed Phase 3 RCTs and meta-analyses. This internal consistency confirms the model's sensitivity, while the HCV Rank #1 result highlights the importance of mechanistic validation before acting on graph-based predictions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

