---
layout: default
title: Methotrimeprazine
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 7
---

# Methotrimeprazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Methotrimeprazine: From Psychiatric Agitation / Psychosis to Manic Bipolar Affective Disorder

## One-Sentence Summary

Methotrimeprazine (levomepromazine) is a first-generation phenothiazine antipsychotic with documented use in acute psychiatric agitation and psychotic disorders, though no current marketing authorization (DIN) is on record in Canada in this dataset.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, currently supported by **0 clinical trials** and **20 publications** — the majority of which are indirect, historical, or describe broad psychiatric agitation rather than confirmed bipolar mania.
The mechanistic rationale is plausible given its D2 antagonism, but direct evidence for this specific indication remains at the preclinical/mechanistic level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal Canada DIN on record; known pharmacological use in psychotic disorders and palliative sedation |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this dataset. Based on known pharmacological properties, methotrimeprazine is a phenothiazine derivative with broad receptor-blocking activity: it acts primarily as a D2 dopamine receptor antagonist, placing it in the same therapeutic class as haloperidol, chlorpromazine, and other first-generation antipsychotics. It also possesses significant H1 antihistamine and α1 adrenergic blocking activity, which account for its pronounced sedative and anxiolytic profile — a characteristic that distinguishes it within its class.

Manic bipolar affective disorder (acute mania) is conventionally managed with D2 antagonists, including both typical antipsychotics (haloperidol) and atypical agents (olanzapine, quetiapine, aripiprazole). The pharmacological overlap is therefore mechanistically coherent: the same D2 blockade that underlies these approved antimanic treatments is present in methotrimeprazine. The added sedative burden from H1 and α1 blockade may offer an adjunctive advantage in controlling acute manic agitation, particularly in inpatient settings.

However, the specificity of existing evidence is critically low. Most publications in this dataset were produced in the 1960s–1990s and describe broad psychiatric agitation, depressive conditions, or unspecified psychosis rather than confirmed bipolar mania. The TxGNN model's high prediction score most likely reflects class-level D2 pharmacological overlap with approved antimanic agents in the knowledge graph — not a validated efficacy signal derived from bipolar mania studies. An important safety flag also appears in this indication context: a case report (PMID 990658) documents fatal pancytopenia in a manic patient receiving levomepromazine combined with lithium and diazepam, which is directly relevant to typical co-medication scenarios in bipolar management.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for methotrimeprazine in manic bipolar affective disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [14129294](https://pubmed.ncbi.nlm.nih.gov/14129294/) | 1964 | Clinical Case Series | Am J Psychiatry | Methotrimeprazine used to control acutely disturbed psychiatric patients; describes sedative and antipsychotic effects in acute agitation contexts |
| [14112288](https://pubmed.ncbi.nlm.nih.gov/14112288/) | 1963 | Systematic Pharmacological Study | J Neuropsychiatry | Broad systematic studies of levomepromazine across psychiatric indications; foundational pharmacological characterization |
| [990658](https://pubmed.ncbi.nlm.nih.gov/990658/) | 1976 | Case Report (Safety) | Br J Psychiatry | Fatal pancytopenia in a manic patient treated with levomepromazine + lithium + diazepam; critical safety signal for bipolar co-treatment scenarios |
| [1355693](https://pubmed.ncbi.nlm.nih.gov/1355693/) | 1992 | Prospective Safety Study | Br J Psychiatry | Prospective NMS risk study in 223 psychiatric inpatients; overall NMS incidence 2.2%; levomepromazine among implicated neuroleptics |
| [2404521](https://pubmed.ncbi.nlm.nih.gov/2404521/) | 1990 | Clinical Study (indirect) | Biol Psychiatry | RS-86 in manic disorder; indirect pharmacological comparator study in a bipolar mania population |
| [991806](https://pubmed.ncbi.nlm.nih.gov/991806/) | 1976 | Clinical Study (indirect) | L'Encéphale | Sequential neuroleptic–viloxazine association for melancholic/manic-depressive psychosis; neuroleptic used for manic state control |
| [14116226](https://pubmed.ncbi.nlm.nih.gov/14116226/) | 1964 | Pharmacological Interaction Study | Compr Psychiatry | Phenothiazine potentiation by nylidrin; class-level mechanistic data applicable to methotrimeprazine |
| [6127880](https://pubmed.ncbi.nlm.nih.gov/6127880/) | 1982 | Biomarker Study (indirect) | Acta Psychiatr Scand | Diurnal MHPG variation in bipolar vs unipolar depressives; noradrenergic context relevant to drug class effects in mood disorders |
| [4773193](https://pubmed.ncbi.nlm.nih.gov/4773193/) | 1973 | Clinical Study (indirect) | Curr Med Res Opin | Lorazepam for severe anxiety and psychotic conditions; levomepromazine appears as comparator agent in psychotic agitation management |
| [13711471](https://pubmed.ncbi.nlm.nih.gov/13711471/) | 1961 | Clinical Study | Orvosi Hetilap | Historical levomepromazine use in depressive states; earliest clinical series establishing use across mood-spectrum presentations |

---

## Canada Market Information

No marketing authorizations for methotrimeprazine are on record in this dataset for Canada (0 DINs). The drug is not currently marketed.

> **Note:** The repurposing rationale for the schizophrenia indication (Rank 4) references prior Canadian approval (alongside UK BNF listing and EU authorization). Any regulatory pathway analysis should verify whether historical DINs exist under the brand name Nozinan® or equivalent, as current database status may reflect voluntary market withdrawal rather than a lack of prior approval.

---

## Safety Considerations

**Key safety signals identified from literature (no formal package insert data available for this dataset):**

- **Neuroleptic Malignant Syndrome (NMS):** A prospective study (PMID 1355693, n=223) documented a 2.2% NMS incidence in psychiatric inpatients treated with various neuroleptics including levomepromazine. NMS risk is a class-wide concern for all D2 antagonists and requires monitoring for hyperthermia, rigidity, altered consciousness, and autonomic instability.
- **Fatal Pancytopenia:** A case report (PMID 990658) describes fatal pancytopenia in a manic patient receiving levomepromazine combined with lithium carbonate and diazepam. This is a directly relevant safety signal for the manic bipolar indication, where lithium co-administration is standard of care.
- **Corneal Deposits and Lens Opacities:** Long-term phenothiazine use has been associated with anterior corneal and lens deposits (PMID 21060765), as confirmed in schizophrenia patients on extended methotrimeprazine therapy.
- **Retrograde Ejaculation:** Reported as an adverse effect in male patients (PMID 22450639), relevant to shared prescribing decisions.

Please refer to the package insert (currently not available in this dataset) for the full list of warnings, contraindications, and drug interactions. Health Canada product monograph review is required before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
While the D2 antagonist mechanism of methotrimeprazine provides a theoretically coherent basis for antimanic activity, there are no registered clinical trials and no direct prospective studies addressing manic bipolar affective disorder. The 20 PubMed publications are predominantly historical (pre-1980s), methodologically weak, and address broad psychiatric agitation rather than confirmed bipolar mania. A specific safety signal — fatal pancytopenia with levomepromazine + lithium — directly relevant to this indication's standard co-treatment adds a Blocking concern. The drug is also not currently marketed in Canada.

**To proceed, the following is needed:**

- **MOA clarification:** Query DrugBank API for receptor binding profile (D2, H1, α1, M1 affinity constants) to formally establish mechanistic link
- **Safety data retrieval:** Download and parse the Health Canada product monograph (or equivalent international SPC, e.g., UK Nozinan® SmPC or French Nozinan® RCP) to identify formal contraindications, warnings, and DDI profile
- **Literature audit:** Screen all 20 PubMed records for studies specifically enrolling DSM/ICD-confirmed bipolar I manic patients (vs. broad psychotic agitation) to reassess effective evidence count
- **Lithium interaction assessment:** Formally evaluate the levomepromazine + lithium pancytopenia risk given lithium's central role in bipolar maintenance therapy
- **Regulatory pathway review:** Confirm whether any historical Canadian DINs existed (e.g., Nozinan®) and whether a label extension pathway is viable vs. a new drug submission requirement
- **Comparative positioning:** Consider whether the schizophrenia indication (Rank 4, L2 evidence, two Cochrane systematic reviews) offers a more viable initial regulatory target before pursuing the bipolar mania expansion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

