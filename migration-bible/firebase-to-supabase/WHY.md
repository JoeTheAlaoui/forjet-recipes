# Why Migrate from Firebase to Supabase?

## The Problem: You're Renting a Black Box

Firebase is brilliant for getting started. But as you scale, you discover you've
been building on top of a proprietary, opaque system that:

- **Bills you based on reads, writes, and deletes** — not just storage or compute.
  A single UI mistake (infinite query loop) can generate a $2,000 bill overnight.
- **Locks your data in a NoSQL format** that's hard to query, join, or analyze.
- **Requires Google's SDK everywhere** — your app is now deeply coupled to Firebase's 
  proprietary auth system, security rules DSL, and API patterns.
- **Makes debugging hard** — Firestore security rules fail silently, and query 
  performance is a black box.

---

## The Solution: Supabase (Open-Source Firebase Alternative)

Supabase gives you a real PostgreSQL database with a Firebase-like developer experience:

| Feature | Firebase | Supabase |
|---|---|---|
| **Database** | NoSQL (Firestore) | Postgres (SQL) |
| **Pricing** | Per read/write, unpredictable | Flat-rate, predictable |
| **Vendor Lock-in** | High (proprietary SDK) | Low (open-source, self-hostable) |
| **Query Power** | Limited (no joins) | Full SQL, JOINs, aggregations |
| **Auth** | Firebase Auth | GoTrue (open-source) |
| **Storage** | Firebase Storage | S3-compatible (open-source) |
| **Real-time** | All-or-nothing | Granular Postgres CDC |
| **Self-hosting** | ❌ | ✅ |

---

## 💰 Potential Savings

> **Time Saved:** ~20–40 hours of manual migration work (SDK rewrites, data model transformation, security rules → RLS migration).
>
> **Money Saved:** Firebase's Blaze plan can cost $50–$500+/month for mid-size apps. Supabase's equivalent tier: $25/month flat.
>
> **Cognitive Savings:** No more Firestore security rules hell. SQL and RLS are well-documented, learnable, and debuggable.

---

## What Forjet Does in 0.2 Seconds vs. What You'd Do Manually

**Manually:** You'd spend days:
1. Exporting all Firestore documents to JSON
2. Designing a relational schema from scratch
3. Writing data migration scripts
4. Rewriting every `firebase.auth()` call
5. Rewriting every `db.collection('x').doc('y').get()` call
6. Translating Firebase Security Rules to Postgres RLS policies
7. Migrating Firebase Storage to Supabase Storage
8. Handling UID string → UUID mismatch at the application layer

**Forjet:** Performs AST-level surgery on your source code. No find-and-replace.
No regex. Your code's semantic structure is preserved while the vendor-specific 
calls are replaced with Supabase equivalents. The contract mutations update your
`.env` automatically.

---

> *"This recipe was generated and tested by Forjet Engine. Get the full Orchestrator at [forjet.dev](https://forjet.dev)."*
