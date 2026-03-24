# The Great Migrations

> *The Bible of Modern Software Migrations — community-powered, AST-precision, vendor-free.*

[![Migration Count](https://img.shields.io/badge/Migrations-6_Proven_Escapes-22c55e?style=for-the-badge&logo=switchbot)](migration-bible/)
[![Powered by Forjet](https://img.shields.io/badge/Powered_by-Forjet_Engine-6366f1?style=for-the-badge&logo=abstract)](https://forjet.dev)
[![Cursor Ready](https://img.shields.io/badge/Cursor-Rules_Included-f59e0b?style=for-the-badge&logo=cursor)](/.cursorrules)
[![Claude Ready](https://img.shields.io/badge/Claude-Instructions_Included-d97757?style=for-the-badge)](/CLAUDE.md)
[![Windsurf Ready](https://img.shields.io/badge/Windsurf-Rules_Included-0ea5e9?style=for-the-badge)](/.windsurfrules)
[![Opencode Ready](https://img.shields.io/badge/Opencode-Workflow_Included-10b981?style=for-the-badge)](/.agents/workflows/forjet_migration.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

---

## The Developer's Escape Manual

Every year, thousands of developers get trapped:
- **The $800 Vercel bill** they never saw coming
- **The Firebase pricing spike** after a product goes viral  
- **The PlanetScale free tier** that disappeared overnight  
- **The Clerk invoice** that scales against their success  

This repository is the antidote. Every entry is not just documentation — it's a 
machine-readable recipe that **[Forjet Engine](https://forjet.dev)** executes 
as AST-level surgery on your actual codebase. No find-and-replace. No regex.
No "just follow these 47 steps manually."

---

## 🌍 The Global Migration Impact

If 1,000 developers run these 6 migrations using Forjet, here is the collective impact on the ecosystem:

| Migration Escape | Collective Time Saved | Collective Wealth Saved (Annual) |
|---|---|---|
| **Firebase → Supabase** | 30,000 Hours | $2,400,000 |
| **Vercel → Coolify** | 8,000 Hours | $7,200,000 |
| **OpenAI → Ollama** | 10,000 Hours | $36,000,000+ |
| **PlanetScale → Neon** | 15,000 Hours | $468,000 |
| **Clerk → Better Auth** | 15,000 Hours | $9,600,000 |
| **Stripe → LemonSqueezy** | 10,000 Hours | $5,000,000+ |
| **TOTAL IMPACT** | **88,000 Hours** | **~$60,668,000 / Year** |

*Stop letting vendors capture your margins. The Great Migrations is the wealth-transfer protocol back to the developers.*

---

## 📖 The Migration Bible

Each migration includes:
- **`recipe.yaml`** — Machine-readable AST transformation spec (Forjet Engine input)
- **`README.md`** — Problem/Solution/Result with real savings numbers
- **`PREVIEW.md`** — Exact before/after code diffs
- **`WHY.md`** — Economic and technical justification

### 🔥 High-Priority Escapes

| Migration | The Pain | Time Saved | Money Saved |
|---|---|---|---|
| 🔥 [**Fire Firebase. Hire Supabase.**](migration-bible/firebase-to-supabase/) | Per-read pricing, vendor lock-in, no JOINs | ~30 hrs | ~$200/mo |
| 🔥 [**The $800 Bill Migration: Vercel → Coolify**](migration-bible/vercel-to-coolify/) | Usage-based billing horror stories | ~8 hrs | ~$600/mo |
| 🔥 [**Kill Your API Key: OpenAI → Ollama**](migration-bible/openai-to-ollama/) | Per-token cost, data privacy, compliance | ~10 hrs | $0–$29,850/mo |
| 🔥 [**PlanetScale Killed the Free Tier. Neon Didn't.**](migration-bible/planetscale-to-neon/) | Free tier deleted with 10-day notice | ~15 hrs | $39/mo |
| 🔥 [**Stop Paying Per-User Auth Fees: Clerk → Better Auth**](migration-bible/clerk-to-better-auth/) | $0.02/MAU after 10K users | ~15 hrs | $800/mo at 50K users |
| 🔥 [**Stop Filing Taxes in 47 Countries: Stripe → LemonSqueezy**](migration-bible/stripe-to-lemonsqueezy/) | Global VAT hell | ~10 hrs | $5K+/yr in accounting |

---

## 🏗️ Golden Stacks (Starters)

Skip the boilerplate. Launch with a battle-tested stack from day one.

| Starter | Stack |
|---|---|
| [The Indie Hacker's Stack](starters/nextjs-supabase-stripe-starter.yaml) | Next.js + Supabase + Stripe + Shadcn |
| [The AI Backend Stack](starters/fastapi-pgvector-langchain-starter.yaml) | FastAPI + pgvector + LangChain + Ollama |

---

## ⚡ Using with Forjet Engine

```bash
# Run a migration recipe on your codebase
forjet migrate --recipe firebase-to-supabase --repo ./my-app

# Or scaffold from a starter
forjet scaffold --starter nextjs-supabase-stripe --output ./my-new-app
```

Configure in your bundle manifest:
```yaml
overrides:
  backend: supabase      # triggers firebase-to-supabase
  deploy: coolify        # triggers vercel-to-coolify
  llm_provider: ollama   # triggers openai-to-ollama
```

---

## 🎯 Multi-Agent Integration

This repository is built to be consumed by AI. It ships with native rules and workflows for the most popular Agentic IDEs and CLI tools:

- **Cursor AI:** Drop [`.cursorrules`](.cursorrules) into your project root.
- **Claude Code:** Uses `CLAUDE.md`. The Claude CLI will automatically read it.
- **Windsurf:** A native [`.windsurfrules`](.windsurfrules) is included.
- **Antigravity / Opencode:** Native agent workflow in [`.agents/workflows/forjet_migration.md`](.agents/workflows/forjet_migration.md).

These rules teach the AI how to apply the recipes via precise AST logic instead of regex find-and-replace.

---

## 📐 Recipe Format

Every recipe follows a strict schema validated against [`schema/recipe-schema.json`](schema/recipe-schema.json):

```yaml
id: recipe-slug
name: "Human-readable name with emotion"
version: "1.0.0"
description: >
  What does this recipe do and when does it activate?

trigger:
  required_roles: [backend]
  overrides:
    backend: supabase

transformations:
  - target_file: src/lib/auth.ts
    engine: jscodeshift        # or python_ast
    codemod: firebase_auth_to_supabase

contract_mutations:
  - action: remove_env
    var: FIREBASE_API_KEY
    component_role: backend
  - action: add_env
    var: SUPABASE_URL
    component_role: backend
```

---

## 🩺 Become a Software Surgeon

Think you can add a migration the community needs? Read [CONTRIBUTING.md](CONTRIBUTING.md).

The most-wanted missing recipes (open issues welcome):
- [ ] `Datadog → Grafana Stack` — monitoring bills that make CFOs cry
- [ ] `MongoDB Atlas → Neon (FerretDB)` — Atlas free tier limits
- [ ] `Heroku → Railway/Render` — the original dev trauma
- [ ] `Prisma → Drizzle` — stop paying the abstraction tax (in `recipes/` already, needs migration-bible treatment)

---

## 🏛️ Project Structure

```
forjet-recipes/
├── 📂 migration-bible/       ← The Great Migrations (each is a story + a spec)
│   ├── 📂 firebase-to-supabase/
│   │   ├── recipe.yaml       ← Machine-readable AST spec
│   │   ├── README.md         ← Problem/Solution/Result
│   │   ├── PREVIEW.md        ← Before/After code diffs
│   │   └── WHY.md            ← Economic justification
│   ├── 📂 vercel-to-coolify/
│   ├── 📂 openai-to-ollama/
│   ├── 📂 planetscale-to-neon/
│   ├── 📂 clerk-to-better-auth/
│   └── 📂 stripe-to-lemonsqueezy/
├── 📂 starters/              ← Golden Stack bootstrappers
│   ├── nextjs-supabase-stripe-starter.yaml
│   └── fastapi-pgvector-langchain-starter.yaml
├── 📂 recipes/               ← Original v0.1 recipe format (legacy, still valid)
├── 📂 schema/                ← JSON Schema for recipe validation
├── 📜 .cursorrules           ← Cursor AI integration
├── 📜 .windsurfrules         ← Windsurf IDE integration
├── 📜 CLAUDE.md              ← Claude Code integration
├── 📂 .agents/               ← Opencode / Antigravity workflows
├── 📜 README.md              ← You are here
└── 📜 CONTRIBUTING.md        ← How to become a Software Surgeon
```

---

## License

[MIT](LICENSE) — Copyright 2026 Forjet

---

> **Tired of manual plumbing?** These recipes were generated and tested by 
> [Forjet Engine](https://forjet.dev). Get the full Orchestrator to automate 
> migrations at scale, with preview diffs, rollback support, and CI integration.
