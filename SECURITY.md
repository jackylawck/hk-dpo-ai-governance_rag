# Security Policy

## Supported Versions

We take the security of this Local RAG Engine seriously. Currently, only the latest release on the `main` branch deployed via Streamlit Community Cloud is actively supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| V1.1.x  | :white_check_mark: |
| < V1.1  | :x:                |

## Security Architecture & Data Protection

This RAG repository maintains a strict **Zero Data At Rest (資料不落地)** policy:
1. **Local Embedding Only:** The application does not make external API calls to proprietary models (e.g., OpenAI, Anthropic) for embeddings. All vectorization runs locally.
2. **Volatile Memory Vector Store:** The `FAISS` index is stored exclusively in RAM. No `.index` files are saved to the server's hard drive.
3. **Automated Dependency Scanning:** GitHub Actions (Dependency Review & Bandit) are integrated to continuously scan `requirements.txt` for known CVEs in `sentence-transformers`, `FAISS`, and other libraries.

## Reporting a Vulnerability

If you discover any security vulnerability, library exploit, or data-leakage flaw within the RAG pipeline, please DO NOT report it through public GitHub issues.

Instead, please report the vulnerability directly via LinkedIn direct message to the System Owner:
👉 **[Jacky Law CK - LinkedIn Profile](https://www.linkedin.com/in/jackylawck)**

Please include:
* A detailed description of the vulnerability.
* Steps to reproduce the exploit.
* Potential impact on local memory or document privacy.

You should expect a response within 48 hours. Validated security issues will be patched and deployed immediately.
