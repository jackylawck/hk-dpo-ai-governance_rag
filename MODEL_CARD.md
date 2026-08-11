# Model Card: Pure Python Local RAG Engine (ISO 42001 Cryptographic Consultation Workstation)
# 模型卡片：純 Python 地端 RAG 引擎（ISO 42001 密碼學諮詢工作站）

> **ISO 42001 Compliance Statement:** This Model Card documents system capabilities, privacy guardrails, and cryptographic lineage tracking for the local RAG engine under ISO/IEC 42001:2023 guidelines.
> **ISO 42001 合規聲明：** 本模型卡片依據 ISO/IEC 42001:2023 指引編寫，記錄本純地端 RAG 引擎之系統能力、隱私護欄及密碼學血統追溯機制。

---

## 1. System Overview & Intended Use (系統概述與預期用途)

* **Model Name / 模型名稱:** HK DPO AI Governance Local RAG Advisor (香港數字辦 AI 管治地端 RAG 顧問)
* **Version / 系統版本:** 1.1 (Local In-Memory RAG Instance / 本地內存 RAG 實例)
* **Type / 模型類型:** Zero-Dependency, Pure Python Local Retrieval-Augmented Generation (RAG) Engine (零外部 API 依賴、純 Python 本地檢索增強生成引擎)
* **Target Audience / 目標受眾:** Compliance Officers, Legal Counsel, Enterprise IT Management, External Auditors (合規官、法務顧問、企業 IT 管理層、外部審計師)。
* **Intended Use / 預期用途:** Localized, privacy-preserving semantic search and consultation against uploaded regulatory guidelines, specifically the HK DPO Generative AI Guideline V1.1 (針對使用者上傳之監管指引——特別是香港數字辦《生成式人工智能技術及應用指引》V1.1——提供在地化、具隱私保護之語義檢索與法規諮詢)。
* **Out-of-Scope Use / 禁用範疇:** Explicitly blocks redirection of corporate confidential PDFs to external cloud vector databases or unencrypted third-party APIs (嚴禁將企業機密 PDF 重定向至外部雲端向量庫或未加密之第三方 API)。

---

## 2. Technical Stack & Embedding Specifications (技術棧與向量規範)

* **Vectorization Engine / 向量化引擎:** Local open-source `sentence-transformers` for semantic embedding (採用開源地端 `sentence-transformers` 進行語義嵌入)。
* **Vector Indexing / 向量索引:** `FAISS` / Pure Python vector similarity computation held strictly within session RAM (`FAISS` 與純 Python 向量相似度計算，完全限制於 Session RAM 內存中)。
* **Chunking Strategy / 切片策略:** ~300 - 400 characters per chunk with an overlapping buffer to preserve regulatory semantic integrity (每區塊約 300 - 400 字，配備重疊緩衝區以保留法規語義完整性)。
* **Deployment Model / 部署模式:** Ephemeral, zero-data-at-rest sandbox. Uploaded documents are destroyed immediately upon session reset or browser closure (短暫性內存沙盒，資料不落地。上傳文件於會話重置或瀏覽器關閉時即刻銷毀)。

---

## 3. Cryptographic Audit Trail & Privacy Safeguards (密碼學審計軌跡與隱私護欄)

* **SHA-256 Lineage / SHA-256 血統:** Generates a unique cryptographic hash ID for every retrieved text chunk to ensure auditability and non-repudiation (為每個被檢索之文本切片生成唯一 SHA-256 哈希值，確保可審計性與不可否認性)。
* **Copyright & Data Protection / 版權與數據保護:** The repository DOES NOT store or distribute official guideline PDFs. End-users upload official documents locally, avoiding copyright infringement and PII leakage (本倉庫絕對不預存或分發官方指引 PDF。使用者於在地端自行上傳，徹底杜絕侵權與個人資料外洩)。
* **Zero Hallucination Control / 零幻覺控制:** Enforces strict "retrieve-first" context matching. Queries without grounding in the uploaded document are flagged with explicit confidence limits (強制執行「先檢索後回應」語境匹配。缺乏上傳文件依據之查詢，將被硬性標記信任度限制)。

---

## 4. ISO 42001 Control Mapping (ISO 42001 控制措施對齊)

* **A.7.3 (Transparency & Explainability / 透明度與可解釋性):** Provides exact source text chunks and section references for every regulatory answer generated (為產出之每項法規解答提供精確原始文本區塊與條文引述)。
* **A.7.5 (AI System Traceability / AI 系統可追溯性):** Implements SHA-256 hash logging for full verification of regulatory retrieval inputs and outputs (實作 SHA-256 哈希值紀錄，實現法規檢索輸入與輸出之完整查驗)。
* **A.8.3 (Data Protection & Privacy / 數據保護與私隱):** Local RAM execution guarantees zero external data leakage or unauthorised data recycling for LLM training (地端 RAM 運算確保零外部數據外洩，亦不被挪用於 LLM 模型訓練)。

---

## 5. Contact & Accountability (問責與聯絡人)

* **System Owner / 系統負責人:** Jacky Law
* **LinkedIn / 專業人脈:** [https://www.linkedin.com/in/jackylawck](https://www.linkedin.com/in/jackylawck)
