---
layout: default
title: Cerliponase Alfa
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
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

# Cerliponase alfa: From CLN2 Disease (Batten Disease) to Scheie Syndrome

## One-Sentence Summary

Cerliponase alfa (Brineura) is a recombinant human TPP1 (tripeptidyl peptidase 1) enzyme replacement therapy approved for CLN2 disease — a rare, fatal lysosomal storage disorder causing progressive neurodegeneration in children.
The TxGNN model predicts it may be effective for **Scheie Syndrome**, scoring **99.98%** in the prediction model.
However, there are **no clinical trials** and **no supporting literature** for this specific indication, making this a model-only prediction with very limited biological rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CLN2 Disease (Neuronal Ceroid Lipofuscinosis Type 2 / Batten Disease) |
| Predicted New Indication | Scheie Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, cerliponase alfa is a recombinant form of human TPP1 (tripeptidyl peptidase 1), a lysosomal serine protease. It is administered via intracerebroventricular (ICV) infusion directly into the brain ventricles to replace deficient TPP1 enzyme in patients with CLN2 disease (a form of Batten disease). Without TPP1, lysosomal waste proteins accumulate in neurons, causing rapid neurodegeneration, seizures, and death in early childhood.

Scheie Syndrome (MPS I-S) is the attenuated form of Mucopolysaccharidosis Type I, caused by a deficiency of **alpha-L-iduronidase (IDUA)** — an entirely different lysosomal enzyme that degrades glycosaminoglycans (heparan sulfate and dermatan sulfate). The two diseases share only a broad categorical label as "lysosomal storage diseases" (LSDs), but the deficient enzymes, their substrates, and their downstream disease manifestations are completely distinct. An approved enzyme replacement therapy, laronidase (Aldurazyme), already exists for MPS I.

The TxGNN model's high prediction score almost certainly reflects **graph-topology similarity** within the knowledge graph — both diseases occupy nodes in the LSD cluster — rather than any true biological or mechanistic transferability. The ICV route of cerliponase alfa delivery further limits systemic reach, making it unsuitable for the skeletal and connective tissue manifestations that characterise Scheie Syndrome. In summary, while the prediction is computationally high-confidence, the mechanistic link is not biologically supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cerliponase alfa in Scheie Syndrome.

---

## Literature Evidence

Currently no related literature available for cerliponase alfa in Scheie Syndrome.

---

## Canada Market Information

Cerliponase alfa is not currently marketed in Canada. No DINs have been issued.

> **Note:** Cerliponase alfa (Brineura®) holds FDA approval (United States, 2017) and EMA approval (European Union) for CLN2 disease. Regulatory submission to Health Canada has not been confirmed based on available data.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack.

> Clinicians should be aware that cerliponase alfa is administered via a surgically implanted intracerebroventricular (ICV) access device, which carries inherent procedural and infection risks. These delivery-route considerations are particularly relevant when evaluating any potential repurposing application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's prediction is driven by shared lysosomal storage disease ontology rather than mechanistic similarity — cerliponase alfa replaces TPP1, while Scheie Syndrome requires IDUA replacement (already served by laronidase). There is zero clinical trial evidence and zero relevant literature to support this repurposing hypothesis. The ICV-only delivery route further limits applicability for a disease with prominent systemic and musculoskeletal features.

**To proceed, the following would be needed:**

- Basic science evidence demonstrating any functional overlap between TPP1 enzyme activity and alpha-L-iduronidase (IDUA) deficiency pathology
- Preclinical (animal model) data showing cerliponase alfa benefit in an MPS I model
- Mechanistic rationale explaining how ICV delivery could address the systemic manifestations of Scheie Syndrome
- Review of full safety profile (TFDA/Health Canada package insert) to complete S1 safety screening
- Regulatory status clarification for cerliponase alfa in Canada

> ⚠️ **Research Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

