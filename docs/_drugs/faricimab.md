---
layout: default
title: Faricimab
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 0
---

# Faricimab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Faricimab (DB15303): 資料不足，無法完成老藥新用評估

## One-Sentence Summary

Faricimab（DrugBank ID：DB15303）在本次 Evidence Pack 中**無原適應症記錄**，亦**無 TxGNN 預測結果**。
關鍵資料包括作用機轉（MOA）、安全性資訊及法規核准紀錄均缺失，**本報告目前無法進行有效的老藥新用評估**。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無資料 |
| 預測新適應症 | 無預測結果 |
| TxGNN 預測分數 | N/A |
| 證據等級 | N/A（無預測資料） |
| 市場狀態 | 未上市 |
| 核准許可證數量 | 0 |
| 建議決策 | **Hold** |

---

## 結論與後續步驟

**Decision: Hold**

**理由：**
本次 Evidence Pack 存在多項關鍵資料缺口（見下表），TxGNN 預測管線未產生任何候選適應症，安全性與法規資訊亦均缺失，目前**無法啟動老藥新用評估流程**。

**進入下一階段前，需補齊以下資料：**

| 優先級 | 缺口 ID | 缺少資料 | 修補方式 |
|--------|---------|---------|---------|
| 🔴 Blocking | DG001 | 原廠仿單警語與禁忌 | 從 TFDA 官網下載仿單 PDF 並解析 |
| 🟠 High | DG002 | 作用機轉（MOA） | 查詢 DrugBank API（DB15303） |
| 🟠 High | — | 原始核准適應症（`original_indications` 為空） | 補齊 DrugBank / 藥品仿單中的核准適應症 |
| 🟠 High | — | TxGNN 預測結果（`predicted_indications` 為空陣列） | 確認 FARICIMAB 已納入預測管線並重新執行 |
| 🟡 Medium | — | DDI 資料（查詢無結果） | 確認藥物英文名/別名後重新查詢 |

> **注意**：本報告結果僅供研究參考，不構成醫療建議。任何老藥新用候選均需經過臨床驗證方可應用。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

