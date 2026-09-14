---
layout: default
title: Selinexor
parent: 僅模型預測 (L5)
nav_order: 709
evidence_level: L5
indication_count: 1
---

# Selinexor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Selinexor: From Multiple Myeloma to Drug-Induced Osteoporosis

## One-Sentence Summary

> Selinexor（DB11942）為選擇性核輸出抑制劑（XPO1/CRM1 inhibitor），目前於國際上核准用於多發性骨髓瘤與瀰漫性大 B 細胞淋巴瘤，加拿大尚未取得藥證。
> TxGNN 模型預測其可能對 **Drug-Induced Osteoporosis（藥物性骨質疏鬆症）** 有效，
> 但目前**無任何臨床試驗、無任何文獻**支持此方向，證據等級為 L5，且機轉分析認為此預測極可能是假陽性。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Myeloma / DLBCL（國際核准適應症，非加拿大官方藥證資料，加拿大未上市） |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| Canada Market Status | 未上市 |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

目前 `original_moa` 欄位缺乏正式 DrugBank 機轉資料（Data Gap，見 DG002）。根據 evidence pack 中的機轉關聯分析，Selinexor 是選擇性核輸出抑制劑（SINE），標靶 XPO1/CRM1，透過抑制腫瘤抑制蛋白（p53、FOXO 等）的核外輸出來發揮抗腫瘤作用，目前核准用於多發性骨髓瘤與瀰漫性大 B 細胞淋巴瘤。

然而此機轉與骨代謝調控（RANKL/OPG、Wnt 訊號路徑、蝕骨細胞活性抑制等）**無已知直接關聯**，也未見文獻支持 XPO1 抑制對藥物性骨質疏鬆症具保護或治療效果。反而 Selinexor 臨床上常伴隨體重下降、厭食、疲勞等全身性副作用，理論上可能**加重**而非改善骨質流失風險。

綜合判斷，此適應症僅為 TxGNN 知識圖譜的關聯評分，缺乏機轉支持證據，**極可能為假陽性預測**，不建議在現階段投入進一步驗證資源。

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Selinexor 目前於加拿大**未取得藥證**（0 個 DIN），無可用授權資料可供列表。

---

## Cytotoxicity

Selinexor 屬於抗腫瘤藥物（XPO1/CRM1 標靶抑制劑），故列出本節。

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy（SINE, XPO1/CRM1 抑制劑） |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

（註：`safety.key_warnings`、`contraindications` 及 DDI 查詢結果均為 Data Gap，其中「產品仿單警語/禁忌」被標記為 **Blocking** 等級缺口，在補齊前無法進行 S1 安全性初評。）

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
此預測證據等級僅為 L5（無臨床試驗、無文獻支持），且機轉分析明確指出 XPO1 抑制與骨代謝保護無已知關聯、甚至可能因全身性副作用加重骨質流失，判斷為極可能的假陽性。此外藥品於加拿大尚未上市，安全性資料（仿單警語、禁忌症）為 Blocking 等級缺口，尚無法進入下一階段評估。

**To proceed, the following is needed:**
- 補齊 DrugBank MOA 正式資料（DG002）
- 取得官方產品仿單/藥品標籤中的警語與禁忌症資料（DG001，Blocking）
- 尋找 XPO1 抑制劑與骨代謝相關的臨床前/機轉研究，以驗證或排除此關聯
- 若無法找到支持性證據，建議標記此候選適應症為低優先級並關閉追蹤
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

