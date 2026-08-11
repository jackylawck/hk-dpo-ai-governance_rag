# Enterprise AI Risk Assessment Report / 企業 AI 風險評估報告

**Document Control / 文檔管控:** V1.0  
**Framework Alignment / 框架對齊:** ISO/IEC 42001:2023 (Annex A.6.1), EU AI Act (Article 9), NIST AI RMF (MAP & MEASURE)  
**Scope / 適用範圍:** HK DPO AI Governance Local RAG Advisor (地端 RAG 智能顧問)

---

## 1. System Risk Categorization / 系統風險分類

Based on the EU AI Act risk classification framework, the Local RAG Advisor is classified as a **Minimal Risk (極低風險)** system.
依據歐盟人工智能法案 (EU AI Act) 風險分類框架，本純地端 RAG 顧問被歸類為**極低風險 (Minimal Risk)** 系統。

* **Search & Consultation Tool / 檢索與諮詢工具:** Deployed strictly as a local decision-support tool for compliance reading (僅作為合規閱讀與檢索之在地化決策支援工具)。
* **No ADM or Biometrics / 無自動化決策或生物識別:** Does not profile individuals, conduct automated employment decisions, or process biometric data (不進行個人畫像、自動化僱傭決策，亦不處理生物識別數據)。

---

## 2. Risk Identification & Mitigation Matrix / 風險識別與控制矩陣

| Identified Risk (識別風險) | Impact (影響) | Likelihood (概率) | Mitigation Control (緩解控制措施) | Residual Risk (殘餘風險) |
| :--- | :--- | :--- | :--- | :--- |
| **Generative Hallucination<br>(生成式幻覺)** | High (高) | Low (低) | **Context-Grounded Search:** Bypasses LLM creative layers. Enforces strict context matching against uploaded PDFs.<br>**語境對齊檢索：** 繞過 LLM 隨機創作層，強制與上傳 PDF 進行硬性語境比對。 | Minimal (極低) |
| **Semantic Drift<br>(語義檢索遺漏/漂移)** | Medium (中) | Low (低) | **Overlapping Chunking:** 300-400 character chunks with 50-100 character buffer prevent boundary context loss.<br>**重疊切片機制：** 300-400 字切片配備 50-100 字緩衝區，防止邊界語境丟失。 | Minimal (極低) |
| **Copyright Infringement<br>(版權侵犯風險)** | Medium (中) | Low (低) | **No PDF Redistribution:** The repository DOES NOT host or distribute official PDFs. Users upload authorized PDFs locally.<br>**不預存官方 PDF：** 倉庫絕對不分發官方原文，由使用者於在地端載入獲授權文件。 | Minimal (極低) |
| **Data Privacy Leakage<br>(數據隱私洩漏)** | High (高) | Low (低) | **100% In-Memory Sandbox:** Local execution only. Zero data transmitted to external vector cloud APIs.<br>**100% 內存沙盒：** 純本地運算，絕不上傳數據至外部雲端向量 API。 | Minimal (極低) |

---

## 3. Approval & Accountability / 審批與問責

The residual risks are deemed acceptable. The local-only execution model effectively neutralizes standard cloud-based LLM privacy risks.  
經評估，殘餘風險均處於極低水平。純地端運算模式已有效化解傳統雲端 LLM 數據隱私風險。
