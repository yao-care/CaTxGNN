---
layout: default
title: Metoclopramide
parent: Model Prediction Only (L5)
nav_order: 602
evidence_level: L5
indication_count: 5
---

# Metoclopramide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metoclopramide: From Antiemetic and Gastric Prokinetic Use to Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a dopamine antagonist that is used as an antiemetic and to speed gastric emptying.
The TxGNN model predicts it may be useful for **gastric ulcer**, but the prediction is supported by only **2 registered clinical trials** (one indirect, one unrelated) and **20 publications** (mostly reviews and animal studies), so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records provided. The literature describes use as an antiemetic and gastrointestinal prokinetic. |
| Predicted New Indication | Gastric ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this drug is not available in the input. The literature does describe metoclopramide as a dopamine antagonist. It acts on the chemoreceptor trigger zone in the brain, which explains its antiemetic effect. It also stimulates gastrointestinal smooth muscle, which speeds gastric emptying. The evidence pack also lists 5-HT4 agonism.

The link between its known uses and gastric ulcer is indirect. Metoclopramide has no established acid-suppressing or ulcer-healing mechanism, and a 1981 double-blind crossover study in 12 healthy men found no change in gastrin levels or acid secretion. Two animal studies (rat and guinea pig) reported protection against experimentally induced ulcers. The guinea pig authors suggested the effect comes from better gastric drainage and less pyloric reflux, not from lowering acid.

The high TxGNN score reflects proximity in the knowledge graph, not therapeutic proof. Any real benefit would probably be adjunctive or symptomatic, such as easing reflux or delayed gastric emptying around an ulcer. It would not replace standard care (acid suppression and *H. pylori* eradication).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Double-blind randomized trial of metoclopramide premedication in upper GI bleeding. It tests whether the drug reduces repeat endoscopy, radiology intervention or surgery, and improves visualization. This is indirect evidence because it does not measure ulcer healing. |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Pharmacist and data-driven quality improvement programme for prescribing safety in primary care. It is not a drug-efficacy trial and has no demonstrated link to gastric ulcer. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT | Yonsei Med J | IV metoclopramide plus ranitidine before anaesthesia (n=40) was tested for effects on preoperative gastric contents in day-case surgery. It is not an ulcer study. |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal study | Arch Int Pharmacodyn Ther | Metoclopramide protected against aspirin-induced and pylorus-ligated gastric ulcers in rats, compared with ranitidine. |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Animal study | Indian J Physiol Pharmacol | Protection against three ulcer models in guinea pigs without changing gastric acidity, probably through better gastric drainage. |
| [28652516](https://pubmed.ncbi.nlm.nih.gov/28652516/) | 2017 | Animal study | J Smooth Muscle Res | Effects of ulcer location and prokinetic drugs on gastric emptying in rats with acetic acid ulcers. |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Randomized double-blind crossover | MMW Munch Med Wochenschr | In 12 healthy men, neither domperidone nor metoclopramide significantly changed serum gastrin or gastric acid secretion. |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Ann Intern Med | Pharmacology of metoclopramide: dopamine antagonism, antiemetic action and stimulation of GI smooth muscle. |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | Overview of drug treatment for gastric and duodenal ulcer. No abstract is available. |
| [797497](https://pubmed.ncbi.nlm.nih.gov/797497/) | 1976 | Review | Clin Pharmacokinet | Drugs and diseases (including gastric ulcer) that alter gastric emptying and thereby affect oral drug absorption. |
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | Not classified | Curr Med Res Opin | Effect of smoking, metoclopramide and carbenoxolone on bile reflux in gastric ulcer. No abstract is available. |
| [775822](https://pubmed.ncbi.nlm.nih.gov/775822/) | 1976 | Not classified | ZFA (Stuttgart) | Therapy of gastric and duodenal ulcer with metoclopramide. No abstract is available, so the findings cannot be assessed. |

Two recent RCTs, published in 2024 and 2026 and retrieved for the related prediction gastroduodenitis, examined metoclopramide for endoscopic visualization in active upper GI bleeding (PMIDs 38059896 and 42259699). This is a procedural aid, not ulcer treatment.

---

## Canada Market Information

Nine DINs are listed. The records provided do not include dosage form or approved indication text. Five are shown below.

| DIN | Product Name |
|---------|------|
| 02185431 | Metoclopramide Hydrochloride Injection |
| 02548755 | PRZ-Metoclopramide |
| 02230431 | PMS-Metoclopramide Tablets |
| 02510790 | PMS-Metoclopramide Hydrochloride Injection |
| 02230433 | PMS-Metoclopramide Oral Solution |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the input.

Signals from the retrieved literature and evidence pack:
- **Neurotoxicity**: A 1988 safety report describes metoclopramide neurotoxicity (PMID 3059051), a concern for chronic or high-dose use.
- **Perforation, haemorrhage and obstruction**: The evidence pack notes that stimulating GI motility is generally considered unsafe in suspected perforation, haemorrhage or obstruction, and describes this as a standard labelling contraindication. This must be checked against the Canadian label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests mainly on graph proximity. The only clinical signal is an indirect trial in upper GI bleeding, and the ulcer-specific evidence is animal work and older reviews. There is no evidence that metoclopramide heals ulcers or prevents recurrence, and standard acid suppression and *H. pylori* eradication remain first-line.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Results or status of NCT05746377, and a clinical trial with ulcer-specific endpoints (healing, recurrence) if pursued
- A defined role for the drug (adjunctive or symptomatic) with a safety review for chronic or high-dose use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

