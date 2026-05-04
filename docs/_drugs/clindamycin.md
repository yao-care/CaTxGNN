---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 6
---

# Clindamycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic with well-established use in treating serious bacterial infections caused by anaerobic bacteria and gram-positive cocci, including skin and soft tissue infections, pelvic inflammatory disease, and (in combination) toxoplasmosis.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
however **no clinical trials** and **no publications** currently support this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (anaerobic and gram-positive organisms) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this evidence pack. Based on established pharmacological knowledge, Clindamycin is a lincosamide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit, thereby blocking peptide chain elongation. It demonstrates activity against anaerobic bacteria and gram-positive cocci, and is clinically used for serious soft tissue infections, dental infections, pelvic inflammatory disease, bacterial vaginosis, and — in combination therapy — toxoplasmosis and *Pneumocystis* pneumonia.

Punctate epithelial keratoconjunctivitis (PEK) is characterized by diffuse, multifocal superficial corneal epithelial defects. Its etiology is heterogeneous — common causes include herpes simplex virus (HSV), adenoviral infection, dry eye disease, drug toxicity, ultraviolet exposure, and staphylococcal blepharitis. The predominant pathogenic mechanisms are viral or non-infectious in nature, which do not align with Clindamycin's antibacterial mechanism of action targeting bacterial ribosomes.

The TxGNN prediction score of 99.97% is numerically high, but the accompanying repurposing rationale in the evidence pack attributes this to phenotypic and topological proximity between corneal surface diseases within the knowledge graph, rather than a direct pharmacological or mechanistic connection. Without a biologically plausible link between 50S ribosomal inhibition and PEK pathogenesis, this prediction requires substantial mechanistic validation before it can be considered actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Clindamycin is currently **not marketed in Taiwan** (未上市), with no registered drug licenses on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Taiwan TFDA package insert warnings, contraindications, and drug interaction data were not available at the time of this report generation. Retrieval of the official product monograph is required before any safety screening can be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on the TxGNN model output (Evidence Level L5), with no supporting clinical trials or published literature for the specific indication of punctate epithelial keratoconjunctivitis. The predominant etiologies of PEK are viral and non-infectious — mechanisms that fall outside the spectrum of Clindamycin's antibacterial activity — making the biological plausibility of this repurposing pathway low.

**To proceed, the following is needed:**
- Retrieve Clindamycin's detailed mechanism of action (MOA) from DrugBank (DB01190) to support or refute mechanistic relevance
- Obtain the Taiwan TFDA (or equivalent) package insert to complete the mandatory safety screening (currently a blocking data gap)
- Establish a specific mechanistic hypothesis — for example, investigating whether bacterial secondary infections on damaged corneal epithelium could constitute a niche indication — before any further preclinical investment
- Conduct a targeted literature review covering antibacterial agents in corneal surface disease to determine whether any lincosamide-class precedent exists
- Reassess against lower-ranked predictions (e.g., **Exposure Keratitis**, ranked #2, Evidence Level L4) which carry stronger biological rationale for secondary bacterial infection prevention and have existing supportive literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

