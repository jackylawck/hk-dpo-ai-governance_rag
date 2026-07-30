# Model Card: Pure Python Local RAG Engine (ISO 42001 Cryptographic Consultation Workstation)

> **ISO 42001 Compliance Statement:** This Model Card documents the system capabilities, privacy guardrails, and cryptographic lineage tracking for the local RAG engine under ISO/IEC 42001:2023 guidelines.

---

## 1. System Overview & Intended Use (系統概述與預期用途)

* **Model Name:** HK DPO AI Governance Local RAG Advisor
* **Version:** 1.1 (Local In-Memory RAG Instance)
* **Type:** Zero-Dependency, Pure Python Local Retrieval-Augmented Generation (RAG) Engine
* **Target Audience:** Compliance Officers, Legal Counsel, Enterprise IT Management, External Auditors.
* **Intended Use:** Localized, privacy-preserving semantic search and consultation against uploaded regulatory guidelines (e.g., HK DPO Generative AI Guideline V1.1)[cite: 1].
* **Out-of-Scope Use:** Redirection of corporate confidential PDFs to external cloud vector databases or unencrypted third-party APIs.

---

## 2. Technical Stack & Embedding Specifications (技術棧與向量規範)

* **Vectorization Engine:** Local open-source `sentence-transformers` for semantic embedding.
* **Vector Indexing:** `FAISS` / Pure Python vector similarity computation held strictly within session RAM.
* **Chunking Strategy:** ~300 - 400 characters per chunk with overlapping buffer to preserve regulatory semantic integrity[cite: 1].
* **Deployment Model:** Ephemeral, zero-data-at-rest sandbox. Uploaded documents are destroyed immediately upon session reset or browser closure.

---

## 3. Cryptographic Audit Trail & Privacy Safeguards (密碼學審計軌跡與隱私護欄)

* **SHA-256 Lineage:** Generates a unique cryptographic hash ID for every retrieved text chunk to ensure auditability and non-repudiation.
* **Copyright & Data Protection:** The repository DOES NOT store or distribute official guideline PDFs. End-users upload official documents locally, avoiding copyright infringement and PII leakage.
* **Zero Hallucination Control:** Enforces strict "retrieve-first" context matching. Queries without grounding in the uploaded document are flagged with explicit confidence limits.

---

## 4. ISO 42001 Control Mapping (ISO 42001 控制措施對齊)

* **A.7.3 (Transparency & Explainability):** Provides exact source text chunks and section references for every regulatory answer generated[cite: 1].
* **A.7.5 (AI System Traceability):** Implements SHA-256 hash logging for full verification of regulatory retrieval inputs and outputs.
* **A.8.3 (Data Protection & Privacy):** Local RAM execution guarantees zero external data leakage or unauthorised data recycling for LLM training.

---

## 5. Contact & Accountability (問責與聯絡人)

* **System Owner:** Jacky Law CK (ISO 42001 Lead Auditor Track / AI Governance Professional)
* **LinkedIn:** [https://www.linkedin.com/in/jackylawck](https://www.linkedin.com/in/jackylawck)
