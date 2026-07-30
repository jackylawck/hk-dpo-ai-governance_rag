# Data Governance & Privacy Architecture (數據管治與隱私架構)

**Document Control:** V1.0
**Framework Alignment:** ISO/IEC 42001:2023 (Annex A.7), GDPR / HK PDPO
**Scope:** HK DPO AI Governance Local RAG Advisor

## 1. Data Provenance & Lineage (數據來源與血統)

* **User-Supplied Knowledge Base:** The system operates strictly on the dynamic knowledge base generated from the official PDF documents (e.g., HK DPO Generative AI Guideline V1.1) uploaded by the end-user[cite: 1].
* **Zero Intellectual Property Claim:** The system claims zero ownership over the ingested regulatory texts.

## 2. Data Minimization & In-Memory Sandbox (資料最小化與內存沙盒)

* **Zero Persistent Vector Store:** The system does not write embeddings to disk or external vector databases (e.g., Pinecone, Weaviate). 
* **RAM Isolation:** All document parsing, `FAISS` vector indexing, and semantic searches occur entirely within the volatile memory (RAM) of the local Streamlit session.
* **Ephemeral Lifecycle:** Upon browser closure, session timeout, or page refresh, the entire vector database and document cache are instantly destroyed, completely eliminating data retention risks.

## 3. Embedding & Chunking Specifications (向量化與切片規範)

* **Model Dependency:** Pure local execution using open-source `sentence-transformers`.
* **Chunk Size:** Configured to ~300 - 400 characters to encapsulate full regulatory clauses[cite: 1].
* **Chunk Overlap:** Configured to 50 - 100 characters to ensure logical continuity and prevent splitting critical legal prerequisites[cite: 1].
