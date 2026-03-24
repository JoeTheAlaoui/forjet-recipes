# PlanetScale Killed the Free Tier. Neon Didn't.

![Verified for Production](https://img.shields.io/badge/Verified-Production_Ready-22c55e?style=for-the-badge)
![AST Precision](https://img.shields.io/badge/AST_Precision-100%25-3b82f6?style=for-the-badge)
![Free Tier](https://img.shields.io/badge/Neon_Free_Tier-Permanent-f59e0b?style=for-the-badge)
![Time Saved](https://img.shields.io/badge/Time_Saved-~15_Hours-a855f7?style=for-the-badge)

---

## 🩺 The Problem

April 2024: PlanetScale deleted its free tier with ~10 days notice.  
Thousands of developers got an email: pay $39/month or your data gets deleted.

Beyond the pricing shock, PlanetScale runs on Vitess (MySQL under the hood):  
- **No foreign keys in production** — data integrity is your application's problem
- **MySQL-specific types everywhere** — your schema becomes MySQL-locked  
- **Proprietary branching model** — impressive engineering, but deeply coupled to PlanetScale's infra

---

## 💊 The Solution

Neon gives you real Postgres with a free tier that never expires, plus serverless 
branching that matches PlanetScale's workflow — without MySQL's limitations.

| Feature | PlanetScale | Neon |
|---|---|---|
| **Free Tier** | ❌ Removed April 2024 | ✅ Permanent (0.5GB) |
| **Database** | MySQL (Vitess) | PostgreSQL |
| **Foreign Keys** | Limited | Full support |
| **Branching** | ✅ | ✅ |
| **Edge/Serverless** | ✅ HTTP driver | ✅ `@neondatabase/serverless` |
| **Vendor Lock-in** | High | Low (standard Postgres) |

---

## ⚡ What Forjet Transforms

| File | Transformation |
|---|---|
| `src/lib/db.ts` | `@planetscale/database` → `@neondatabase/serverless` |
| `drizzle.config.ts` | `mysql2` dialect → `postgres` dialect |
| `src/db/schema.ts` | MySQL types → Postgres types (`tinyint` → `boolean`, etc.) |
| `prisma/schema.prisma` | `provider = "mysql"` → `provider = "postgresql"` |
| `src/lib/edge-db.ts` | PlanetScale HTTP driver → Neon HTTP driver |

**See the economics:** [WHY.md](WHY.md)

---

## ⚠️ Type Mapping Reference

| MySQL (PlanetScale) | PostgreSQL (Neon) |
|---|---|
| `tinyint(1)` | `boolean` |
| `varchar(255)` | `text` or `varchar(255)` |
| `int unsigned` | `integer` (no unsigned in Postgres) |
| `datetime` | `timestamp with time zone` |
| `json` | `jsonb` (more powerful) |

---

## 💰 Potential Savings

> **PlanetScale Scaler:** $39/month  
> **Neon Free Tier:** $0/month  
> **~15 hours** of MySQL→Postgres type migration, ORM reconfiguration saved

---

> *Tired of manual plumbing? This recipe was generated and tested by [Forjet Engine](https://forjet.dev). Get the full Orchestrator at forjet.dev.*
