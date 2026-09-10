---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Imiglucerase
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

# Imiglucerase: From Gaucher Disease to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

Imiglucerase is a recombinant glucocerebrosidase enzyme replacement therapy, internationally established for Gaucher disease (Type I/III), but it holds **zero drug licenses in Canada and is not currently marketed**. Of the 10 candidate indications TxGNN generated for this drug, 9 (including the top-ranked Hurler syndrome and Scheie syndrome) are graph-topology artifacts from clustering with other lysosomal storage diseases and carry little or no drug-specific evidence. The one credible signal — **Lysosomal Storage Disease with Skeletal Involvement**, i.e., the bone manifestations of Gaucher disease itself — is backed by **2 clinical trials** and **20 publications**, and mechanistically is simply the drug's own core indication rather than a novel repurposing target.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (Type I/III) — established international indication; not formally captured in the structured `original_indications` field (data gap) |
| Predicted New Indication | Lysosomal Storage Disease with Skeletal Involvement (i.e., skeletal/bone manifestations of Gaucher disease) |
| TxGNN Prediction Score | 98.94% (rank 6 of 10 candidates; score 0.9894, graph rank 17,195) |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on the other 9 candidates:** The single top-scoring prediction (Hurler syndrome, 99.52%) and 8 others (Scheie syndrome, benign adrenal neoplasm, ichthyosis syndrome, cholesteryl ester storage disease, Wolman disease and its subtype, proximal myopathy with extrapyramidal signs, and a GH-insensitivity/immune-dysregulation syndrome) all score **higher or similarly high** but are staged **L4–L5 / Hold** — they lack matching substrate-level mechanism (e.g., Hurler/Scheie need alpha-L-iduronidase, not glucocerebrosidase) and have zero or only generic non-specific literature. High TxGNN scores alone do not indicate strong evidence; only rank 6 has drug-specific clinical and literature support.

## Why is This Prediction Reasonable?

Formal mechanism-of-action data is not populated in the structured record (data gap DG002), but the evidence pack's own literature base makes the mechanism clear: Imiglucerase is a recombinant form of human **glucocerebrosidase (β-glucocerebrosidase)**, administered as enzyme replacement therapy (ERT) to break down accumulated glucosylceramide in patients with Gaucher disease — a deficiency of this exact enzyme.

"Lysosomal storage disease with skeletal involvement," as scored by TxGNN, is not a mechanistically distant new indication — it corresponds directly to the **bone manifestations of Gaucher disease itself** (bone pain, avascular necrosis, lytic lesions, medullary infarction), which is already part of Imiglucerase's established disease biology. This is a direct, on-target mechanistic match, not a cross-mechanism inference, which is why it earns L2 evidence versus the L4/L5 assigned to the other 9 candidates.

The apparent "repurposing opportunity" here is therefore less about discovering a new disease-drug pairing and more about a **market-access gap**: Imiglucerase's efficacy in Gaucher disease (including skeletal disease) is well established internationally, yet the drug currently has no Canadian market authorization (0 DINs). The other 9 TxGNN candidates, by contrast, cluster near Gaucher disease in the knowledge graph purely because they are also lysosomal storage diseases (e.g., Hurler/Scheie need alpha-L-iduronidase, Wolman disease/CESD need lysosomal acid lipase) — a category-level proximity, not a substrate-level one — and should not be advanced without independent, drug-specific evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04656600](https://clinicaltrials.gov/study/NCT04656600) | Phase 4 | Completed | 12 | Evaluated efficacy and safety of imiglucerase at the maximum labeled Chinese dose (60 U/kg IV biweekly) in Chinese patients with Gaucher disease Type III, assessing hematologic, visceral, and bone-disease outcomes. |
| [NCT01842841](https://clinicaltrials.gov/study/NCT01842841) | Phase 3 | Completed | 5 | Open-label extension study of **velaglucerase alfa** (a related but distinct glucocerebrosidase ERT, not imiglucerase itself) in Japanese Gaucher disease patients — indirect, class-level supporting evidence only. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17539908](https://pubmed.ncbi.nlm.nih.gov/17539908/) | 2007 | Cohort | Clinical Genetics | Imiglucerase (Cerezyme) improved health-related quality of life in Type 1 Gaucher disease patients with skeletal manifestations (bone pain, infarctions, avascular necrosis, lytic lesions). |
| [9453101](https://pubmed.ncbi.nlm.nih.gov/9453101/) | 1997 | Cohort | Skeletal Radiology | MRI-based assessment of skeletal involvement in Type 1 Gaucher disease and therapeutic response to enzyme replacement. |
| [8931951](https://pubmed.ncbi.nlm.nih.gov/8931951/) | 1996 | Cohort | Blood Cells Mol Dis | Low-dose ERT improved bone-related complications in 14 adult Type I Gaucher disease patients with severe skeletal involvement. |
| [20055531](https://pubmed.ncbi.nlm.nih.gov/20055531/) | 2010 | Review | BioDrugs | Overview of recombinant glucocerebrosidase (imiglucerase) as ERT for Gaucher disease, including dosing regimens. |
| [21889384](https://pubmed.ncbi.nlm.nih.gov/21889384/) | 2011 | Review | Mol Genet Metab | Past, present, and future therapeutic approaches to bone pathology in Gaucher disease, highlighting ERT's impact on skeletal manifestations. |
| [18553043](https://pubmed.ncbi.nlm.nih.gov/18553043/) | 2008 | Case series | Calcif Tissue Int | Bone metabolism changes in 7 Gaucher disease patients treated consecutively with imiglucerase and miglustat. |
| [22640238](https://pubmed.ncbi.nlm.nih.gov/22640238/) | 2012 | Case series | Br J Haematol | ICGG Registry analysis (n=1016) of persistent thrombocytopenia in Type 1 Gaucher disease despite 4–5 years of continuous imiglucerase therapy. |
| [27441734](https://pubmed.ncbi.nlm.nih.gov/27441734/) | 2016 | Biomarker study | Am J Hematol | Plasma glucosylsphingosine (lyso-GL1) as a biomarker of Gaucher disease and its response to therapy. |
| [12803930](https://pubmed.ncbi.nlm.nih.gov/12803930/) | 2003 | Review | Phil Trans R Soc Lond B | Clinical experience with substrate reduction therapy in Gaucher disease, contextualizing ERT's role and limitations (e.g., no CNS penetration). |
| [9050375](https://pubmed.ncbi.nlm.nih.gov/9050375/) | 1997 | Review | Curr Opin Hematol | General review of Gaucher disease genetics, natural history, and enzyme replacement. |

*(10 of 20 available publications shown, prioritized by direct clinical/cohort evidence over general reviews.)*

## Canada Market Information

Imiglucerase currently holds **no Health Canada drug licenses (0 DINs)** and is **not marketed** in Canada. No product listings are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. Structured safety fields (key warnings, contraindications, drug interactions) are not yet populated in this evidence pack.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The only clinically credible signal in this prediction set is the drug's already-established mechanism — glucocerebrosidase replacement for Gaucher disease, including its skeletal manifestations — supported by 2 trials and 20 publications (L2). This is closer to a **Canadian market-access question** than a novel indication discovery, so guardrails are warranted pending regulatory documentation rather than pending new efficacy proof. The remaining 9 TxGNN candidates (including the top-ranked Hurler syndrome) should stay at **Hold**: they arise from lysosomal-storage-disease graph clustering rather than substrate-matching mechanism, and none have drug-specific clinical evidence.

**To proceed, the following is needed:**
- Official TFDA/Health Canada product label to resolve the blocking safety data gap (DG001) before any S1 safety assessment
- Formal DrugBank/regulatory confirmation of mechanism of action (DG002)
- Clarification of the regulatory pathway for Canadian market authorization, given 0 current DINs
- Determination of whether "skeletal involvement" needs a distinct label claim or is already covered under a general Gaucher disease indication
- No further action on the other 9 candidate indications unless independent, drug-specific mechanistic or trial evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

