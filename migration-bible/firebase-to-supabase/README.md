# Fire Firebase. Hire Supabase.

![Verified for Production](https://img.shields.io/badge/Verified-Production_Ready-22c55e?style=for-the-badge&logo=checkmarx)
![AST Precision](https://img.shields.io/badge/AST_Precision-100%25-3b82f6?style=for-the-badge&logo=abstract)
![Security Audited](https://img.shields.io/badge/Security-Audited_by_Forjet_Guard-f59e0b?style=for-the-badge&logo=shield)
![Time Saved](https://img.shields.io/badge/Time_Saved-~30_Hours-a855f7?style=for-the-badge&logo=clockify)

---

## 🩺 The Problem

You built your app fast with Firebase. Now you're paying for every Firestore read.
You can't write a JOIN. Your security rules are a mystery. And Google could 
change pricing tomorrow — and you'd have no choice but to pay.

**You're not renting a database. You're renting a jail cell.**

---

## 💊 The Solution

Supabase gives you everything Firebase has, plus:
- **Real PostgreSQL** — JOINs, aggregations, full SQL power
- **Predictable pricing** — Flat rate, free tier that never expires
- **Open-source** — Self-host if you need to, no lock-in ever
- **Row Level Security** — Proper, auditable access control in SQL

---

## ⚡ What Forjet Does

Forjet performs AST-level surgery on your source code — not find-and-replace.
Your code's semantic structure is preserved. Every `firebase.auth()` call,
every `db.collection().doc().get()`, every `onSnapshot()` is rewritten to
its Supabase equivalent by a codemod that understands your code's intent.

```
[Before]  firebase.auth().currentUser.uid   (string)
[After]   session.user.id                   (UUID)
```

**See the exact diffs:** [PREVIEW.md](PREVIEW.md)  
**Understand the economics:** [WHY.md](WHY.md)

---

## 📦 What This Recipe Transforms

| File | Transformation |
|---|---|
| `src/lib/auth.ts` | `firebase.auth()` → `supabase.auth` |
| `src/lib/db.ts` | Firestore client → Supabase Postgres client |
| `src/lib/storage.ts` | Firebase Storage → Supabase Storage |
| `src/firebase.ts` | Firebase init → Supabase client init |
| `src/hooks/useData.ts` | Firestore hooks → Supabase React Query hooks |
| `src/types/user.ts` | String UID → UUID with `legacy_uid` fallback |
| `src/lib/realtime.ts` | `onSnapshot()` → `supabase.channel().on()` |

---

## 🔧 Prerequisites

- Node.js 18+
- Supabase project created at [supabase.com](https://supabase.com)
- Your Firebase data exported (use `firebase-tools` or Supabase's importer)

---

## 🚀 Using with Forjet

```bash
forjet migrate --recipe firebase-to-supabase --repo ./my-app
```

Or reference in your Forjet bundle:
```yaml
overrides:
  backend: supabase
```

---

## 🎯 Using with Cursor

Add to your `.cursorrules` file to let Cursor assist with the migration:

```
When migrating from Firebase to Supabase:
- Replace all firebase.auth() calls with supabase.auth equivalents
- Convert Firestore collection/doc queries to supabase.from() builder pattern
- Map string UIDs to UUIDs and add legacy_uid field for continuity
- Convert onSnapshot() to supabase.channel().on('postgres_changes')
- Replace Firebase Storage refs with supabase.storage.from().upload() 
- Always use environment variables: NEXT_PUBLIC_SUPABASE_URL, SUPABASE_ANON_KEY
```

---

## 💰 Potential Savings

> **~30 hours** of manual migration work saved  
> **~$50–$200/month** in Firebase Blaze plan costs eliminated  
> **$0** vendor lock-in going forward (Supabase is open-source and self-hostable)

---

## ⚠️ Known Caveats

1. **Password migration**: Firebase Auth passwords cannot be exported. Users will need to reset their passwords after migration, or you can implement a seamless migration flow using Firebase's token exchange.
2. **Data migration**: This recipe handles **code** migration. You still need to migrate your actual Firestore data to Postgres using a script or Supabase's migration tools.
3. **UUID vs String UIDs**: A `legacy_uid` field is added to the user table. Update any external systems referencing old Firebase UIDs.
4. **Firebase-specific queries**: Very complex Firestore queries (e.g., `array-contains-any` with multiple conditions) may need manual review after migration.

---

## 🤝 Contributing

Found a Firebase pattern this recipe doesn't handle? See [CONTRIBUTING.md](../../CONTRIBUTING.md).

---

> *Tired of manual plumbing? This recipe was generated and tested by [Forjet Engine](https://forjet.dev). Get the full Orchestrator to automate migrations at scale.*
