# Stop Filing Taxes in 47 Countries: Stripe to LemonSqueezy

![Verified for Production](https://img.shields.io/badge/Verified-Production_Ready-22c55e?style=for-the-badge)
![AST Precision](https://img.shields.io/badge/AST_Precision-100%25-3b82f6?style=for-the-badge)
![MoR Compliant](https://img.shields.io/badge/Tax_Compliance-47_Countries-f59e0b?style=for-the-badge)
![Time Saved](https://img.shields.io/badge/Time_Saved-~10_Hours-a855f7?style=for-the-badge)

---

## 🩺 The Problem

Stripe is excellent. But if you sell globally without a US entity, you discover the hidden cost:

- **VAT registration** required in EU, UK, Australia, and more once you hit thresholds
- **US Sales Tax Nexus** — sell enough in a US state and you must register and remit
- **Chargeback management** — your responsibility, your loss
- **Accountant bills** for cross-border compliance: $5,000–$20,000+ per year

This is an invisible tax on every indie hacker and small team selling globally.

---

## 💊 The Solution

LemonSqueezy is a **Merchant of Record**. They become the legal seller on your behalf 
in every country. You integrate once and they handle all tax compliance automatically.

| Feature | Stripe | LemonSqueezy |
|---|---|---|
| **Global Tax Handling** | Your problem | ✅ Automatic (47+ countries) |
| **VAT Registration** | You handle it | ✅ LemonSqueezy's entity |
| **Chargebacks** | Your loss | Shared risk |
| **Fee** | 2.9% + $0.30 | ~3.5% + $0.50 (MoR fee included) |
| **Subscription Management** | Full-featured | Full-featured |
| **Best for** | US-entity companies | Global indie hackers |

---

## ⚡ What Forjet Transforms

| File | Transformation |
|---|---|
| `src/lib/payments.ts` | Stripe client → LemonSqueezy client |
| `src/app/api/checkout/route.ts` | Checkout session → LemonSqueezy checkout URL |
| `src/app/api/webhooks/stripe/route.ts` | Stripe events → LemonSqueezy events |
| `src/lib/subscriptions.ts` | Stripe subscription API → LS subscription API |
| `src/app/api/portal/route.ts` | Stripe portal → LemonSqueezy customer portal |

**See the economics:** [WHY.md](WHY.md)

---

## ⚠️ Key API Differences

| Stripe | LemonSqueezy |
|---|---|
| `checkout.session.create()` | Pre-generated checkout URL |
| `payment_intent.succeeded` | `order_created` |
| `customer.subscription.updated` | `subscription_updated` |
| `priceId` | `variantId` |

---

## 💰 Potential Savings

> **Annual accounting costs for global VAT compliance:** $5,000–$20,000+  
> **LemonSqueezy's extra MoR fee at $100K ARR:** ~$600/year  
> **Net savings:** $4,400–$19,400/year  
> **~10 hours** of webhook handler rewrites and client migration saved by Forjet

---

> *Tired of manual plumbing? This recipe was generated and tested by [Forjet Engine](https://forjet.dev). Get the full Orchestrator at forjet.dev.*
