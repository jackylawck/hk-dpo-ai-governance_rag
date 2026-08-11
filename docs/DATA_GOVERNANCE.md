# Data Governance & Privacy Architecture / 數據管治與隱私架構

**Document Control / 文檔管控:** V1.0  
**Framework Alignment / 框架對齊:** ISO/IEC 42001:2023 (Annex A.7), GDPR / HK PDPO (Cap. 486)  
**Scope / 適用範圍:** HK DPO AI Governance Local RAG Advisor (地端 RAG 智能顧問)

---

## 1. Data Provenance & Lineage / 數據來源與血統

* **Dynamic Ingestion (動態載入):** Operates strictly on the knowledge base dynamically generated from official PDF documents uploaded by the end-user.  
  完全基於使用者於在地端動態上傳之官方指引 PDF 生成向量知識庫。
* **Zero IP Claim (零版權主張):** The system claims zero intellectual property ownership over ingested regulatory texts.  
  系統對所有載入之法規文本主張零知識產權。

---

## 2. Data Minimization & In-Memory Sandbox / 資料最小化與內存沙盒

* **Zero Persistent Vector Store (零持久化向量庫):** Does not write embeddings to hard drives or external vector cloud databases (Pinecone, Weaviate).  
  絕不將 Embedding 向量寫入硬碟或外部雲端向量資料庫。
* **RAM Isolation (揮發性記憶體隔離):** All document parsing, `FAISS` indexing, and similarity searches occur exclusively within volatile RAM.  
  所有文件解析、`FAISS` 索引與語義比對，完全於 Session RAM 記憶體中執行。
* **Ephemeral Lifecycle (短暫性生命週期):** Upon browser closure or session reset, the entire vector index is instantly destroyed.  
  關閉瀏覽器或重置會話時，所有內存向量索引即刻徹底銷毀。

---

## 3. Embedding & Chunking Specifications / 向量化與切片規範

* **Local Embedding Model (地端向量模型):** Pure local execution using open-source `sentence-transformers`.  
  使用開源地端 `sentence-transformers` 進行向量化，完全不呼叫外部 API。
* **Golden Chunk Size (黃金切片長度):** Configured to ~300 - 400 characters to encapsulate full legal clauses.  
  設定為 300 - 400 字，確保單一條文之完整性。
* **Overlap Buffer (重疊緩衝區):** 50 - 100 character overlap to ensure continuity and prevent breaking legal prerequisites.  
  設定 50 - 100 字重疊，防止斷句時切割法規前提條件。
