---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 3
---

# Galcanezumab
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

# Galcanezumab: From Migraine Prevention to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Galcanezumab (Emgality) is a humanized anti-CGRP monoclonal antibody approved internationally for the preventive treatment of migraine and episodic cluster headache. The TxGNN model predicts it may be effective for **Heparin Cofactor 2 Deficiency**, with **0 clinical trials** and **0 publications** currently supporting this direction. The mechanistic link between CGRP blockade and coagulation pathway disorders remains highly indirect and biologically contradictory.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine prevention; episodic cluster headache (not marketed in Canada) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Galcanezumab is a humanized IgG4 monoclonal antibody that selectively binds calcitonin gene-related peptide (CGRP), a vasoactive neuropeptide released from trigeminal nerve endings during migraine attacks. By preventing CGRP from binding to its receptor on cranial blood vessels, galcanezumab reduces neurogenic vasodilation and inflammation — the mechanism underlying migraine prevention. Its pharmacological action is highly selective to the trigeminovascular system with no established role in haemostasis or coagulation.

Heparin Cofactor II (HCII, encoded by SERPIND1) is a serine protease inhibitor that inactivates thrombin in the presence of heparin or dermatan sulphate. Deficiency of HCII theoretically impairs the auxiliary anticoagulant pathway, increasing thrombotic risk. The knowledge graph analysis proposes an indirect linkage through the sequence CGRP → vascular endothelial function → coagulation regulation; however, this is a three-or-more-step indirect connection for which no experimental or clinical evidence exists. Furthermore, there is a fundamental directional problem: galcanezumab *blocks* CGRP, whose physiological role includes vasodilation and mild inhibition of platelet aggregation — the net effect of CGRP blockade could theoretically be mildly pro-thrombotic, which would be contraindicated in a patient population already at higher thrombotic risk.

The same directional contradiction applies to the second (antithrombin deficiency type 2) and third (factor 5 excess with spontaneous thrombosis) ranked predictions, both of which involve pro-coagulant or anti-anticoagulant states. The TxGNN high scores in all three cases most likely reflect shared network topology within the knowledge graph — adjacency to vascular and endothelial nodes — rather than genuine therapeutic relevance. These predictions are best treated as graph artefacts until mechanistic or empirical evidence emerges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications involve rare coagulation disorders, and the mechanism by which CGRP blockade could benefit any of these conditions is not only unsubstantiated but directionally contradictory — blocking a vasodilatory, mildly antithrombotic peptide in patients predisposed to thrombosis raises a theoretical safety concern rather than a treatment opportunity. With zero supporting clinical trials or publications (Evidence Level L5), there is insufficient basis to proceed.

**To proceed, the following would be needed:**
- Formal MOA characterisation: Confirm whether galcanezumab has any off-target effects on coagulation factors, thrombin activity, or endothelial haemostatic function (in-vitro or preclinical data).
- Mechanistic hypothesis validation: Identify a plausible, direct biological pathway — not merely a graph-adjacency path — linking CGRP antagonism to HCII, antithrombin, or Factor V regulation.
- Safety signal review: Screen pharmacovigilance databases (FDA FAERS, EudraVigilance) for any reported thrombotic adverse events associated with galcanezumab or other anti-CGRP agents (erenumab, fremanezumab, eptinezumab), which would further inform whether CGRP blockade carries prothrombotic risk.
- Canada regulatory filing: Galcanezumab currently holds no DINs in Canada; any repurposing development would require a de-novo regulatory pathway. Confirm whether Health Canada has received any investigational submissions for galcanezumab to date.
- Evidence re-evaluation: If future mechanistic data reveals a plausible link, reassign to a new evidence-gathering cycle targeting these specific coagulation indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

