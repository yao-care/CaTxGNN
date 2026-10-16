---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 642
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Naproxen: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout…"
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Naproxen: From Inflammatory and Musculoskeletal Pain Conditions to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) originally used for conditions such as rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout, tendinitis, bursitis, and migraine.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout, tendinitis, bursitis, migraine and headache disorders (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, naproxen belongs to the NSAID class, which reduces inflammation and pain by inhibiting prostaglandin synthesis. Its established use is in symptomatic relief of inflammatory and degenerative joint and soft-tissue conditions.

Brachydactyly-syndactyly syndromes are congenital limb malformations of developmental and genetic origin. Blocking prostaglandin production is not expected to change the underlying cause of such conditions. No mechanistic link is supported by the available data.

The high score (0.994) most likely reflects network proximity in the knowledge graph, for example shared connections to skeletal and musculoskeletal nodes, rather than a biological rationale. The same pattern appears in the other top-ranked predictions (colobomatous microphthalmia-rhizomelic dysplasia syndrome, acromesomelic dysplasia Hunter-Thompson type, brachyolmia-amelogenesis imperfecta syndrome). All are rare congenital syndromes with no trial or literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Naproxen is widely marketed in Canada, with 20 valid single-ingredient licences and none cancelled. Dosage form and approved indication text were not available for these products. The five main authorizations are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02162423 | NAPROSYN | Not available | Not available |
| 02162725 | ANAPROX | Not available | Not available |
| 02162717 | ANAPROX DS | Not available | Not available |
| 02361795 | ALEVE LIQUID GELS | Not available | Not available |
| 02436337 | ALEVE BACK AND BODY PAIN | Not available | Not available |

Other licences include APO-NAPROXEN, APO-NAPROXEN EC, TEVA-NAPROXEN, TEVA-NAPROXEN EC, TEVA-NAPROXEN SODIUM, PRO-NAPROXEN EC, and MAXIDOL LIQUID GELS.

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):**
The knowledge graph links naproxen to contraindications or cautions in the following groups:
- **Cardiovascular:** hypertension, congestive heart failure, coronary artery disease, coronary atherosclerosis, myocardial infarction, coronary thrombosis, stroke, cerebrovascular disorder, cerebral infarction
- **Liver and kidney:** liver failure, liver disease, kidney disease, gallbladder disease
- **Blood:** blood coagulation disease, anemia (including macrocytic anemia), hemoglobinopathy
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, obesity, osteoporosis (including postmenopausal)
- **Other:** epilepsy, benign prostatic hyperplasia, pyoureter, substance abuse/dependence

**Drug Interactions:**
The interaction query returned 100 records. The 20 shown are all rated Moderate. Main examples:
- **Corticosteroids:** hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
- **Other NSAIDs and anti-inflammatories:** acetylsalicylic acid, mesalazine, balsalazide
- **Acid-suppressing drugs:** famotidine, ranitidine, cimetidine, rabeprazole, dexlansoprazole
- **Antidiabetic drugs:** metformin, chlorpropamide
- **Others:** aprepitant, potassium citrate, potassium bicarbonate, picosulfuric acid, polyethylene glycol with electrolytes

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no literature, and no plausible mechanistic link. Brachydactyly-syndactyly syndrome is a congenital developmental disorder that an NSAID is not expected to modify.

**To proceed, the following is needed:**
- Detailed mechanism of action data from DrugBank
- A biological rationale connecting prostaglandin or COX pathways to the disease
- Preclinical or mechanistic studies, or relevant literature
- Health Canada package insert warnings and contraindications, to allow safety screening
- Route and dosage-form compatibility assessment
- Review of whether the other predicted indications offer a more plausible repurposing path
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

