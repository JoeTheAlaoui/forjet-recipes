# Kill Your API Key: OpenAI to Local LLM (Ollama)

![Verified for Production](https://img.shields.io/badge/Verified-Production_Ready-22c55e?style=for-the-badge)
![GDPR Compliant](https://img.shields.io/badge/GDPR-Compliant-16a34a?style=for-the-badge)
![AST Precision](https://img.shields.io/badge/AST_Precision-100%25-3b82f6?style=for-the-badge)
![Data Privacy](https://img.shields.io/badge/Data-Stays_On_Your_Metal-f59e0b?style=for-the-badge)

---

## 🩺 The Problem

You're building an AI product. But every user message, every document, 
every proprietary piece of data you process — it all goes to OpenAI's servers.

- **GDPR/HIPAA compliance** becomes a legal adventure
- **Per-token billing** can spiral: 1M tokens/day at GPT-4 rates = $30K/month
- **OpenAI outages** take your product offline with you having zero control
- **Model deprecations** happen with short notice and break your integration

---

## 💊 The Solution

Ollama runs the most capable open-source LLMs (LLaMA 3.2, Mistral, Gemma, DeepSeek) 
on your own hardware with an OpenAI-compatible API. Your data never leaves your infrastructure.

| Metric | OpenAI API | Self-Hosted Ollama |
|---|---|---|
| **Data leaves your servers** | ✅ Always | ❌ Never |
| **Cost at 1M tokens/day** | ~$30,000/month | ~$150/month (GPU server) |
| **GDPR/HIPAA compliant** | Complex | ✅ By default |
| **Works offline** | ❌ | ✅ |
| **Model control** | OpenAI decides | You decide |

---

## ⚡ What Forjet Transforms

| File | Transformation |
|---|---|
| `src/llm/client.py` | `openai.OpenAI()` → Ollama client |
| `src/lib/ai.ts` | OpenAI npm → ollama npm client |
| `src/lib/stream.ts` | OpenAI stream → Ollama stream format |
| `src/config/models.ts` | Model name mapping (gpt-4 → llama3.2) |
| `docker-compose.yml` | Ollama service injected with GPU passthrough |

**See the economics:** [WHY.md](WHY.md)

---

## 🎯 Using with Cursor

```
When migrating from OpenAI to Ollama:
- Map gpt-4 → llama3.2, gpt-3.5-turbo → llama3.2:1b, text-embedding-ada-002 → nomic-embed-text
- Default OLLAMA_BASE_URL to http://localhost:11434 in development
- For production GPU inference consider vLLM with --served-model-name matching old OpenAI model names
- Never hardcode model names — always use OLLAMA_MODEL environment variable
```

---

## 💰 Potential Savings

> **At 100K tokens/day:** OpenAI GPT-4 = ~$3,000/month → Ollama on $150 GPU VPS = $150/month  
> **~10 hours** of client rewrites, streaming handler migration, and Docker config saved  
> **$0 compliance risk** — data never leaves your infrastructure

---

> *Tired of manual plumbing? This recipe was generated and tested by [Forjet Engine](https://forjet.dev). Get the full Orchestrator at forjet.dev.*
