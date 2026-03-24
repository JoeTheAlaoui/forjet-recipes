# Stop Paying Per-User Auth Fees: Why Leave Clerk?

## The Problem: Auth Pricing Scales Against You

Clerk is excellent for prototyping. But as you grow, you discover:

- **$0.02/MAU after 10,000 users** — At 50K users: $800/month just for auth
- **Vendor lock-in baked in** — Clerk components, hooks, and middleware are 
  deeply proprietary. Migrating later means rewriting your entire auth layer.
- **Per-seat pricing on teams** — Enterprise plans add per-seat fees on top of MAU costs.
- **Your users are in Clerk's database**, not yours — You don't own the auth store.

---

## 💰 Potential Savings

> **Clerk at 50K MAU:** ~$800/month  
> **Better Auth (self-hosted):** $0/month (just your DB storage cost)  
>
> **Time saved by Forjet:** ~12–20 hours of hook rewrites, middleware migration, 
> provider component replacement, and webhook handler conversion

---

## What is Better Auth?

Better Auth is a fully-featured, TypeScript-native, open-source auth library.
It stores user data in YOUR database (Postgres, SQLite, MySQL), giving you 
complete ownership with zero per-user fees. It supports OAuth, magic links, 
2FA, sessions, and organizations out of the box.

> *"This recipe was generated and tested by Forjet Engine. Get the full Orchestrator at [forjet.dev](https://forjet.dev)."*
