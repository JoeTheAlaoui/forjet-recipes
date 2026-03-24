# The $800 Bill Migration: Vercel to Coolify

![Verified for Production](https://img.shields.io/badge/Verified-Production_Ready-22c55e?style=for-the-badge)
![AST Precision](https://img.shields.io/badge/AST_Precision-100%25-3b82f6?style=for-the-badge)
![Time Saved](https://img.shields.io/badge/Time_Saved-~8_Hours-a855f7?style=for-the-badge)
![Monthly Savings](https://img.shields.io/badge/Monthly_Savings-~$600-f59e0b?style=for-the-badge)

---

## 🩺 The Problem

Your Vercel bill arrived. It wasn't $80. It was $800.

Bandwidth overages ($40/100GB), serverless function executions, build minutes, team seats — 
Vercel's usage-based pricing model punishes success. Developers across Reddit 
share the same horror story: traffic spike → invoice shock → panic.

**The system is designed to make leaving feel impossible.** Next.js Edge Functions, 
ISR, and Middleware all work "optimally" only on Vercel's infrastructure.

---

## 💊 The Solution

Coolify is an open-source PaaS that runs on any $6/month VPS.
You get the same git-push-to-deploy experience, automatic SSL, and preview 
branches — for a flat monthly fee that never changes when your traffic spikes.

| Feature | Vercel | Coolify (on Hetzner VPS) |
|---|---|---|
| **Monthly Cost** | $80–$800+ (usage-based) | $6–$20/month flat |
| **Deploy on git push** | ✅ | ✅ |
| **Automatic SSL** | ✅ | ✅ |
| **Preview branches** | ✅ | ✅ |
| **Bandwidth overages** | $40/100GB | ❌ (your VPS bandwidth) |
| **Vendor lock-in** | High (Next.js coupling) | None |

---

## ⚡ What Forjet Transforms

| File | Transformation |
|---|---|
| `vercel.json` | → `docker-compose.yml` + Coolify config |
| `src/middleware.ts` | Edge runtime → standard Node.js middleware |
| `next.config.js` | Vercel-specific settings → standard Next.js config |
| `.github/workflows/deploy.yml` | Vercel CI → Coolify webhook trigger |

**See the economics:** [WHY.md](WHY.md)

---

## 🎯 Using with Cursor

```
When migrating from Vercel to Coolify:
- Remove `export const runtime = 'edge'` from route handlers
- Replace Vercel-specific next.config.js options with standard equivalents
- Add Dockerfile and docker-compose.yml for local/production parity
- Use Coolify webhook for CI/CD instead of Vercel GitHub integration
```

---

## 💰 Potential Savings

> **~8 hours** of Docker, Nginx, and CI/CD configuration saved  
> **~$600/month** average savings (Vercel Pro + usage vs VPS flat rate)  
> **$7,200/year** for a team that hit Vercel's usage ceiling

---

> *Tired of manual plumbing? This recipe was generated and tested by [Forjet Engine](https://forjet.dev). Get the full Orchestrator at forjet.dev.*
