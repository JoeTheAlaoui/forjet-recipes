# Why Run Your Own LLM?

## The Problem: Every Token is a Tax on Your Business

When you build AI features with OpenAI's API:

- **Every user query costs money** — GPT-4 at $0.03/1K tokens adds up fast
- **Your data leaves your servers** — Every prompt, every user message, 
  every document goes to OpenAI's servers. GDPR, HIPAA, SOC 2 compliance becomes complicated.
- **Downtime is their problem, your crisis** — When OpenAI has an outage, 
  your product breaks. You have no SLA guarantee.
- **Model changes break your app** — OpenAI deprecates models with short notice, 
  forcing emergency engineering work.

---

## 💰 Potential Savings

> **API Cost at Scale:**  
> 1M tokens/day at GPT-4 rates = ~$30,000/month  
> Self-hosted LLaMA 3.2 on $150/month GPU server = $150/month  
>
> **Time saved by Forjet:** ~10 hours of Ollama setup, API client rewrites, 
> streaming handler migration, and docker-compose configuration

---

## What is Ollama?

Ollama is the simplest way to run open-source LLMs (LLaMA, Mistral, Gemma, DeepSeek) 
locally or on your own server. It exposes an API compatible with OpenAI's format, 
making migration straightforward at the API contract level — and that's exactly 
what Forjet's AST engine handles.

> *"This recipe was generated and tested by Forjet Engine. Get the full Orchestrator at [forjet.dev](https://forjet.dev)."*
