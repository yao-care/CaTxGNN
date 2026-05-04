---
layout: default
title: Chlorpromazine
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
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

# Chlorpromazine: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Chlorpromazine (DB00477) is the first antipsychotic drug ever used in clinical medicine, historically approved for schizophrenia and related psychotic disorders since 1954.
The TxGNN model assigns it the highest prediction rank for **Retinal Dystrophy with or without Extraocular Anomalies** (score: 99.95%), yet **0 clinical trials** and **15 publications** have been identified — and critically, the available evidence does not support a therapeutic role, with the most directly relevant literature describing chlorpromazine as a *cause* of retinal toxicity rather than a treatment.
The overall evidence level is **L5** (model prediction only), and the current recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia / psychotic disorders (historical global use; no current Taiwan/Canada approvals on file) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Currently Marketed (Largactil historically available in Canada; now discontinued) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Chlorpromazine is a first-generation (typical) antipsychotic belonging to the phenothiazine class. Its primary mechanism is post-synaptic dopamine D2 receptor antagonism (Ki ≈ 1 nM), with additional blockade of histamine H1, muscarinic M1, and α1-adrenergic receptors. This multi-receptor profile explains its broad sedative, antiemetic, and antipsychotic effects, and underlies both its clinical utility and its characteristic adverse-effect burden (extrapyramidal symptoms, tardive dyskinesia, anticholinergic effects).

Retinal dystrophy with or without extraocular anomalies is a hereditary group of conditions driven by progressive photoreceptor degeneration — caused by mutations in genes such as *RPGR*, *PRPF31*, or *CEP290*. The fundamental pathology is structural and genetic, not one of dopaminergic or histaminergic dysregulation. There is no established pharmacological bridge between chlorpromazine's receptor targets and the retinal degeneration cascade.

**Importantly, the evidence points in the opposite direction.** Long-term use of chlorpromazine and other phenothiazines is a recognised cause of drug-induced retinopathy (pigmentary changes, photoreceptor damage), as documented in the literature returned by this query (PMID 5647013: *Phenothiazine-retinopathy*). The TxGNN model's high prediction score most likely reflects topological proximity within the knowledge graph — shared intermediate nodes related to ocular phenotypes — rather than a genuine therapeutic opportunity. This candidate should be treated as a **knowledge-graph artefact** rather than a biologically grounded repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 15 retrieved publications were identified through the broad query term "retinal dystrophy with or without extraocular anomalies." None describe chlorpromazine as a treatment for this condition. The most directly relevant paper (PMID 5647013) documents retinal toxicity *caused* by the phenothiazine drug class. The remainder cover general ocular/orbital developmental conditions and carry no mechanistic link to chlorpromazine.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [5647013](https://pubmed.ncbi.nlm.nih.gov/5647013/) | 1968 | Case/Report | *Ophthalmologica* | Describes phenothiazine-induced retinopathy — drug class causes pigmentary retinal toxicity; directly contradicts therapeutic repurposing |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | *Documenta Ophthalmologica* | Wagner-Stickler vitreoretinal degeneration complex: myopia, cataract, retinal detachment; genetic aetiology, no pharmacological intervention discussed |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | *Pediatric Radiology* | Differential diagnosis and imaging of paediatric ocular pathologies including congenital/developmental lesions; no chlorpromazine content |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Research Article | *Int J Mol Sci* | Optic nerve head and retinal abnormalities in congenital fibrosis of extraocular muscles (CFEOM; KIF21A/TUBB3 mutations); genetic developmental disorder |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | *Taiwan J Ophthalmol* | Congenital lens shape anomalies and anterior segment dysgenesis; structural/developmental, not pharmacological |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | *Am J Ophthalmol* | Pathogenesis and treatment of maculopathy associated with cavitary optic disc anomalies; surgical/vitreoretinal management focus |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | *J Binocular Vis Ocul Motility* | Congenital cranial dysinnervation disorders (CCDDs); diagnosis framework for ophthalmoplegia subtypes |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | *Klin Monbl Augenheilkd* | Congenital ptosis: levator muscle dystrophy and fibrosis; surgical management |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | *Am J Ophthalmol* | Unilateral cryptophthalmia: absent globe and optic nerve; describes anatomical anomalies in two patients |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review/Case Series | *Semin Ultrasound CT MR* | Orbital infections and sinusitis-related complications; no relevance to retinal dystrophy or chlorpromazine |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** A specific safety concern relevant to this repurposing candidate is that chlorpromazine is a documented cause of **drug-induced retinopathy** (phenothiazine retinopathy). Pursuing chlorpromazine in any retinal indication would require a robust ophthalmological monitoring plan and careful risk-benefit justification.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.95%), but all other evidence indicators point against pursuing this candidate: there are no supporting clinical trials, the retrieved literature includes evidence that chlorpromazine *causes* retinal toxicity, and the mechanistic rationale is absent — retinal dystrophy is a genetic photoreceptor disease with no known link to dopamine/histamine receptor pharmacology. The high TxGNN rank is likely a knowledge-graph topological artefact.

**To reconsider, the following would be needed:**

- A credible mechanistic hypothesis explaining how D2/H1/M1 antagonism could modify photoreceptor degeneration pathways (e.g., neuroprotective signalling via dopamine in the retinal circuitry)
- Preclinical evidence (in vitro or animal models of retinal dystrophy) demonstrating protective, rather than toxic, effects of chlorpromazine or phenothiazine congeners at the relevant doses
- Resolution of the known safety conflict: phenothiazine retinopathy is a class-wide adverse effect that would need to be addressed before any ocular indication development
- Formal MOA data from DrugBank and package insert review (currently both flagged as data gaps)
- At minimum, advancement of evidence level from L5 to L4 (preclinical data) before any further investment

---

> ⚠️ *This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

