---
layout: default
title: Sunitinib
parent: High Evidence (L1-L2)
nav_order: 742
evidence_level: L2
indication_count: 10
---

# Sunitinib
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

Using this task's own fully-specified template — it's a direct content-generation task, not one needing brainstorming/debugging skills — I'll generate the report as instructed.

---

# Sunitinib: From Renal Cell Carcinoma / GIST to Liposarcoma

## One-Sentence Summary

Sunitinib is an oral multi-targeted receptor tyrosine kinase inhibitor globally established for gastrointestinal stromal tumour (GIST) and advanced/metastatic renal cell carcinoma (RCC) — though this evidence pack contains no Canadian licensing record, meaning it is currently **not marketed in Canada**. The TxGNN model's top-ranked prediction is that sunitinib may be effective for **Liposarcoma**, with **3 clinical trials** and **9 publications** currently informing this direction, though the evidence specific to this indication is still preliminary (**L2**).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this evidence pack (0 Canadian licenses). Globally, sunitinib is approved for GIST and advanced renal cell carcinoma. |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as data gap DG002). Based on publicly known pharmacology, sunitinib is a multi-targeted tyrosine kinase inhibitor acting on VEGFR1-3, PDGFRα/β, KIT, RET, and FLT3, and it was originally developed for tumours driven by these same targets — namely GIST (KIT/PDGFRA-driven) and RCC (VEGF-pathway-driven angiogenesis).

The repurposing rationale for liposarcoma, as captured in the evidence pack, notes: *"Angiogenesis in sarcoma tissue and PDGFR expression in certain histological subtypes provide the pharmacological basis for sunitinib targeting; however, liposarcoma is a highly heterogeneous disease group not dominated by a single molecular mechanism."* This is a meaningfully weaker mechanistic case than, for example, the DFSP (rank 6) or renal carcinoma (rank 9) candidates in the same pack, where a single dominant driver (COL1A1-PDGFB fusion; VEGF-pathway dependence) is well characterized.

In short, the biological plausibility rests on sunitinib's established anti-angiogenic/anti-PDGFR activity extending from its approved sarcoma-adjacent and vascular-tumour indications into liposarcoma — but because liposarcoma itself is molecularly heterogeneous, the mechanistic link is directional rather than definitive.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Open-label single-site Phase II study identifying a promising sunitinib dose in unresectable/metastatic soft tissue sarcoma, cohort including liposarcoma, leiomyosarcoma, fibrosarcoma, and MFH. |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Multicenter Phase II continuous-dosing sunitinib study in non-GIST sarcomas (metastatic/locally advanced/recurrent), directly covering liposarcoma patients (highest-relevance trial, Grade A). |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 basket protocol primarily testing **regorafenib** (not sunitinib) across selected sarcoma subtypes; sunitinib referenced only as prior-agent precedent — low direct relevance (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | RCT (Phase 2) | International Journal of Cancer | Single-institution Phase II study of sunitinib in relapsed/refractory soft tissue sarcoma, focused on leiomyosarcoma, liposarcoma, and MFH; reports safety/efficacy by subtype. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven review of STS therapy; notes exceptionally high trabectedin activity specifically in myxoid liposarcoma (context for angiogenesis/target-driven agents). |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case Report | Anticancer Research | Long-lasting clinical benefit of sunitinib in a heavily pre-treated patient with metastatic liposarcoma. |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Pending classification | Cancers | Reviews genetic, epigenetic, and transcriptomic alterations in liposarcoma relevant to targeted-therapy selection. |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Pending classification | Expert Review of Anticancer Therapy | Overview of emerging therapies for adult soft tissue sarcoma. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Pending classification | Magyar Onkologia | Medical treatment of soft tissue sarcomas stratified by histological subtype. |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Pending classification | Oncotarget | Next-generation sequencing of extraskeletal myxoid chondrosarcoma; evaluates sunitinib activity in a subset of patients. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Pending classification | BMC Cancer | REGOSARC trial protocol (regorafenib in advanced STS); sunitinib referenced as a prior comparator agent. |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Pending classification | American Journal of Surgical Pathology | Clinicopathologic series on myxoid inflammatory myofibroblastic sarcoma — a distinct sarcoma entity with limited direct relevance to liposarcoma. |

---

## Canada Market Information

No Canadian drug licenses are on file for sunitinib in this evidence pack (`total_licenses = 0`, market status: Not Marketed). No DIN-level product table is available to display.

---

## Cytotoxicity

Sunitinib is an antineoplastic agent (targeted small-molecule multi-kinase inhibitor), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted receptor tyrosine kinase inhibitor: VEGFR1-3, PDGFRα/β, KIT, RET, FLT3) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

*Note: Drug-specific toxicity/warning data is a flagged blocking data gap (DG001) in this evidence pack — see Conclusion below.*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
- The mechanistic link for liposarcoma is plausible but non-specific (liposarcoma is molecularly heterogeneous, and only 1 of 3 trials was directly and strongly on-target). Evidence level is L2, decision stage S2 — this warrants further targeted investigation rather than immediate advancement.
- Critically, **DG001 (TFDA/Canada product warnings and contraindications) is a Blocking data gap** — the evidence pack explicitly states this prevents entry into the S1 safety pre-screen, so no safety-based go/no-go call can be made yet regardless of efficacy evidence.

**To proceed, the following is needed:**
- Resolve DG001: obtain Canadian product monograph / regulatory warnings and contraindications (Blocking priority)
- Resolve DG002: obtain confirmed MOA data from DrugBank
- Since sunitinib holds zero Canadian licenses, clarify the intended regulatory pathway (e.g., Health Canada Special Access, new submission, or cross-reference to an existing international monograph)
- Liposarcoma-specific: seek subtype-level trial data (myxoid/round-cell vs. dedifferentiated vs. pleomorphic), as current trials are basket-designed across multiple sarcoma histologies rather than liposarcoma-specific

**Note for internal prioritization:** within this same evidence pack, the rank-9 candidate (**renal carcinoma**) shows substantially stronger evidence — L1, decision stage S3, "Proceed with Guardrails," with dozens of Phase 2/3 trials including registrational-grade studies. That candidate likely warrants a separate, higher-priority evaluation alongside this liposarcoma report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

