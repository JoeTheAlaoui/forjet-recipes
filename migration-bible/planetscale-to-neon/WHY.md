# PlanetScale Killed the Free Tier. Here's Your Escape.

## The Problem: The Free Lunch is Over

In April 2024, PlanetScale discontinued its free tier with ~10 days notice.
Thousands of developers woke up to an email forcing them to pay $39/month 
or watch their databases get deleted.

Beyond the pricing shock, PlanetScale has other fundamental issues:
- **It's MySQL under the hood (Vitess)** — all MySQL's quirks, none of SQL's full power
- **No foreign keys in production** — PlanetScale's branching model means FK constraints 
  don't work as expected, requiring application-level data integrity
- **MySQL-specific types everywhere** — `TINYINT(1)` for booleans, signed/unsigned 
  madness — your schema becomes MySQL-specific over time

---

## 💰 Potential Savings

> **PlanetScale Hobby:** removed (was free)  
> **PlanetScale Scaler:** $39/month  
> **Neon Free Tier:** $0/month (permanent, 0.5GB, branching included)  
> **Neon Pro:** $19/month  
>
> **Time saved by Forjet:** ~15 hours of MySQL → Postgres type migration, 
> client library swap, and Drizzle/Prisma dialect reconfiguration

> *"This recipe was generated and tested by Forjet Engine. Get the full Orchestrator at [forjet.dev](https://forjet.dev)."*
