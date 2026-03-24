# Stop Paying Per-User Auth Fees: Clerk to Better Auth

![Verified for Production](https://img.shields.io/badge/Verified-Production_Ready-22c55e?style=for-the-badge)
![AST Precision](https://img.shields.io/badge/AST_Precision-100%25-3b82f6?style=for-the-badge)
![Your Data](https://img.shields.io/badge/Users_Live_In-Your_Database-f59e0b?style=for-the-badge)
![Time Saved](https://img.shields.io/badge/Time_Saved-~15_Hours-a855f7?style=for-the-badge)

---

## 🩺 The Problem

Clerk is delightful at zero users. At scale, the bill grows against you:

- **$0.02 per MAU after 10,000 users** — 50K users = $800/month just for auth
- **Your users live in Clerk's database**, not yours — you have zero ownership
- **Deep hook coupling** — `useUser()`, `useAuth()`, `<ClerkProvider>`, `clerkMiddleware()` 
  are baked into every layer of your app
- **Proprietary component library** — their `<SignIn>`, `<SignUp>`, `<UserButton>` 
  are impossible to fully customize

---

## 💊 The Solution

Better Auth is a fully TypeScript-native, open-source auth library. Users are stored 
in YOUR database. Zero per-MAU fees. Full customization. Works with any Postgres/SQLite/MySQL.

| Feature | Clerk | Better Auth |
|---|---|---|
| **Pricing** | $0.02/MAU after 10K | $0/month (your DB costs) |
| **User data ownership** | Clerk owns it | You own it |
| **Customization** | Limited | Full — it's your code |
| **TypeScript support** | ✅ | ✅ Best-in-class |
| **OAuth providers** | ✅ | ✅ |
| **2FA / MFA** | ✅ | ✅ |
| **Organizations/Teams** | ✅ (expensive) | ✅ (built-in, free) |
| **Self-hostable** | ❌ | ✅ |

---

## ⚡ What Forjet Transforms

| File | Transformation |
|---|---|
| `src/middleware.ts` | `clerkMiddleware()` → Better Auth session check |
| `src/app/layout.tsx` | `<ClerkProvider>` → `<SessionProvider>` |
| `src/hooks/useAuth.ts` | `useUser()`/`useAuth()` → `useSession()` |
| `src/app/api/auth/route.ts` | Clerk server auth → Better Auth `getSession()` |
| `src/app/(auth)/sign-in/page.tsx` | Clerk components → Better Auth form |
| `src/app/api/**` | `auth().userId` → Better Auth session checks |

**See the economics:** [WHY.md](WHY.md)

---

## 💰 Potential Savings

> **At 50K MAU:** Clerk = $800/month → Better Auth = $0/month  
> **At 100K MAU:** Clerk = $1,800/month → Better Auth = $0/month  
> **~15 hours** of hook rewrites, middleware migration, and webhook conversion saved

---

> *Tired of manual plumbing? This recipe was generated and tested by [Forjet Engine](https://forjet.dev). Get the full Orchestrator at forjet.dev.*
