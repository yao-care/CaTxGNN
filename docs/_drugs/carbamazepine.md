---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Carbamazepine
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

# Carbamazepine: From Trigeminal Neuralgia to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Carbamazepine (CBZ) is one of medicine's most established anticonvulsant and analgesic drugs, globally recognized as the first-line pharmacological treatment for trigeminal neuralgia through its blockade of voltage-gated sodium channels (Nav1.x) to suppress pathological nerve firing.
The TxGNN model predicts it may be effective for **Trigeminal Nerve Neoplasm** — a biologically plausible extrapolation given that tumors compressing the trigeminal nerve commonly produce secondary neuralgia with the same pain mechanism as primary trigeminal neuralgia.
Current evidence search identified **1 clinical trial** and **20 publications**, though virtually all address tumor-associated secondary neuralgia rather than any direct anti-tumor activity of CBZ.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Trigeminal neuralgia; epilepsy (established global approvals; no Health Canada DIN found in this dataset — see note below) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.9976% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (no DINs found in this dataset) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Data Note**: Carbamazepine (e.g., Tegretol®) is a well-established Schedule F prescription drug sold in Canada. The absence of DIN records in this dataset most likely reflects a data collection gap rather than actual non-availability. Verification against the Health Canada Drug Product Database is recommended before drawing regulatory conclusions.

---

## Why is This Prediction Reasonable?

Carbamazepine exerts its therapeutic effect primarily by blocking voltage-gated sodium channels (Nav1.x), stabilizing the resting membrane potential of neurons and suppressing high-frequency repetitive firing. This mechanism underlies its decades-long status as the gold-standard first-line drug for primary trigeminal neuralgia (TN) — a condition in which aberrant ectopic discharge from the demyelinated trigeminal nerve root produces excruciating paroxysmal facial pain. The same sodium-channel mechanism also explains CBZ's broad anticonvulsant efficacy across focal and generalized seizure types.

Trigeminal nerve neoplasms — including schwannomas, meningiomas, lymphomas, melanomas, and other masses in or near Meckel's cave, the trigeminal ganglion, or the nerve root entry zone — frequently cause **secondary TN** through mechanical compression, nerve invasion, or post-radiation injury. The resulting demyelination and ectopic sodium-channel hyperactivity are pathophysiologically identical to primary TN. Multiple case reports in this evidence pack document exactly this scenario: patients whose trigeminal nerve neoplasms initially presented with neuralgia-type pain for which CBZ was the first pharmacological agent tried (PMIDs 30741017, 25433061, 15235745). Preclinical data (PMID 3181365) further confirm that CBZ dose-dependently suppresses ectopic discharges from experimental neuromas, directly supporting a neuroma-suppression mechanism applicable to neoplasm-adjacent nerve irritation.

It is important to be transparent about the ceiling of this prediction: **CBZ has no known mechanism to treat the neoplasm itself**. It targets neuronal excitability, not tumor biology. The TxGNN model most likely captures the symptom-management bridge — CBZ controlling secondary TN pain — rather than any direct oncologic activity. A critical clinical signal worth noting is that CBZ *failure* to control pain in a suspected TN patient (as seen in PMIDs 30741017 and 15235745) should itself prompt imaging workup for an underlying neoplasm, since tumor-compression pain often requires definitive tumor treatment to resolve.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | Not Yet Recruiting | 120 | MRI-based study of brain network dynamics and microstructural changes in trigeminal *neuralgia* patients; evaluates neuroimaging biomarkers and blood-brain barrier permeability. Not a CBZ treatment trial and not specific to trigeminal nerve neoplasm — provides indirect neuroimaging context only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | British Journal of Neurosurgery | Primary malignant lymphoma of the trigeminal nerve presenting as facial pain; CBZ was initially prescribed but pain did not improve; MRI then revealed nerve swelling and a Meckel's cave mass. The most direct case in this dataset linking CBZ use to trigeminal nerve neoplasm. |
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clinica Croatica | Comprehensive review of TN treatment options; explicitly notes that TN can be caused by vascular compression *or* a tumor process; CBZ is established as first-line medical therapy regardless of etiology. |
| [9109911](https://pubmed.ncbi.nlm.nih.gov/9109911/) | 1997 | Case Report | Neurology | Post-irradiation neuromyotonia in bilateral facial and trigeminal nerve distribution; neuromyotonic discharges — a radiation-induced nerve lesion — responded to CBZ therapy, supporting CBZ efficacy in radiation-related trigeminal nerve pathology. |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | In-depth review of TN treatments covering etiology (vascular compression, focal demyelination) and CBZ as first-line drug; also discusses MRI detection of neurovascular conflict, relevant to distinguishing neoplastic from vascular causes. |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case Report | No Shinkei Geka | TN caused by cerebellopontine angle lipoma; CBZ was used initially but adequate pain control failed due to side effects, ultimately requiring surgical resection. Illustrates the role of CBZ as a bridge therapy in mass-lesion-associated TN. |
| [32454201](https://pubmed.ncbi.nlm.nih.gov/32454201/) | 2020 | Case Report | World Neurosurgery | Endoscopic endonasal resection of schwannoma in the pterygopalatine fossa; provides management context for trigeminal nerve tumors with facial symptoms, where pre-operative CBZ analgesia is standard. |
| [25968963](https://pubmed.ncbi.nlm.nih.gov/25968963/) | 2015 | Case Report/Review | World Neurosurgery | TN caused by venous angioma; reviews the pathophysiology of TN from structural lesions; CBZ described as typical first-line medical management pending definitive treatment. |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Survey/Cohort | British Journal of Oral & Maxillofacial Surgery | Survey of 254 UK oral surgeons on TN management; highlights CBZ as universal standard treatment and discusses controversies around screening for secondary TN (including tumor-related causes). |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case Report | Arquivos de Neuro-Psiquiatria | Primary melanoma of Meckel's cave presenting as TN with a normal initial MRI; CBZ did not relieve pain; decompression surgery failed; repeat MRI revealed the mass. CBZ non-response serves as a key diagnostic signal for neoplastic TN. |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Preclinical | Experimental Neurology | CBZ dose-dependently inhibits spontaneous ectopic discharges from saphenous neuromas in rats; IV CBZ suppressed A-α/β and A-δ fiber activity at clinically relevant serum levels — mechanistic foundation for CBZ use in neoplasm-adjacent nerve irritation. |

---

## Canada Market Information

No Health Canada DIN registrations were identified for Carbamazepine in this dataset (market status: not marketed, 0 DINs). This is inconsistent with Carbamazepine's known global availability — the drug is marketed in most countries under names such as Tegretol® and generic equivalents — and likely reflects a data retrieval gap for this specific Evidence Pack.

**Action required**: Query the Health Canada Drug Product Database directly at https://health-products.canada.ca/dpd-bdpp/ to retrieve current DIN registrations, approved indications, and product monograph information before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Formal safety data (Health Canada product warnings, contraindications, and drug interaction records) could not be retrieved for this analysis. Carbamazepine is well-known to carry clinically significant safety considerations including serious dermatological reactions (Stevens-Johnson Syndrome, particularly in patients with HLA-B\*1502 allele), agranulocytosis, aplastic anemia, teratogenicity, and extensive CYP450-based drug interactions. A full safety review against the current Health Canada product monograph and the patient's medication list is mandatory before any clinical application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CBZ's Nav1.x sodium-channel blockade mechanism is directly applicable to the secondary trigeminal neuralgia pain caused by trigeminal nerve neoplasms, and its use in this symptomatic context is supported by published case reports and established clinical practice — making it biologically and clinically plausible as an analgesic adjunct in neoplasm management. However, CBZ exerts no anti-tumor effect, and no RCT evidence exists for trigeminal nerve neoplasm as a primary indication; the evidence is indirect (L4), warranting careful framing of its role as palliative pain control rather than disease-modifying treatment.

**To proceed, the following is needed:**

- **Clarify the intended clinical role**: Symptomatic pain management (secondary TN analgesia) is supported; direct oncologic treatment is not — these must be clearly differentiated in any clinical protocol
- **Health Canada database verification**: Retrieve current DIN list, approved indications, and official product monograph from https://health-products.canada.ca/dpd-bdpp/
- **Full safety review**: Obtain current product monograph warnings and contraindications; assess HLA-B\*1502 screening requirement for relevant ethnic populations; review patient medication list for CYP3A4/CYP2C8 drug interactions
- **Pharmacogenomic assessment**: Consider HLA-B\*1502 testing per Health Canada guidance before initiating CBZ in patients of Asian descent
- **Prospective case documentation**: Establish a registry or case series specifically tracking CBZ analgesic efficacy and adverse events in confirmed trigeminal nerve neoplasm patients, stratified by neoplasm type
- **Diagnostic safeguard protocol**: Define a CBZ non-response threshold that should trigger immediate advanced neuroimaging, as failure of CBZ to control trigeminal pain is itself a clinical red flag for underlying neoplasm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

