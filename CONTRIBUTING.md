# Contributing to The Great Migrations

> Welcome, Software Surgeon. Your scalpel is a YAML file. Your patient is a bloated, vendor-locked codebase.

---

## What We're Building

This is not a collection of tutorials. This is a **machine-readable migration specification library**.
Each recipe is consumed by [Forjet Engine](https://forjet.dev) to perform AST-level, 
deterministic code transformations. The bar is high, and that's the point.

---

## The Three Laws of a Great Migration Recipe

1. **It must solve real pain.** If developers aren't actively complaining about this 
   migration on Reddit and X, it's not a priority. Check the [research report](https://github.com/forjet/forjet-recipes/discussions) before opening a PR.

2. **It must be AST-precise.** No "just search and replace this." Every transformation 
   must target specific AST nodes via `jscodeshift` or `python_ast`. 
   Regex-based migrations are rejected.

3. **It must include the full story.** A `recipe.yaml` without `WHY.md`, `PREVIEW.md`, 
   and a per-recipe `README.md` is an incomplete PR. The human story is as important 
   as the machine spec.

---

## How to Add a New Migration

### Step 1: Choose a Migration Worth Fighting For

Ask yourself: **Is this a migration developers are currently suffering through?**

High-probability signals:
- Active Reddit threads in r/webdev, r/selfhosted, r/node, r/devops
- Trending discussions on X about pricing, lock-in, or deprecation
- Tool announced end-of-free-tier, pricing change, or acquisition

### Step 2: Create the Directory Structure

```bash
mkdir migration-bible/your-tool-to-their-tool
touch migration-bible/your-tool-to-their-tool/recipe.yaml
touch migration-bible/your-tool-to-their-tool/README.md
touch migration-bible/your-tool-to-their-tool/PREVIEW.md
touch migration-bible/your-tool-to-their-tool/WHY.md
```

### Step 3: Write the `recipe.yaml`

Follow the [JSON Schema](schema/recipe-schema.json). Required fields:
- `id` — kebab-case slug, unique across the repo
- `name` — Pain-language name (see existing recipes for inspiration)
- `version` — Start at `"1.0.0"`
- `trigger.required_roles` — At least one role
- `transformations` — At least one AST transformation

**Quality bar for `transformations`:**
- Each `target_file` must be a realistic path in a real project
- Each `codemod` name must correspond to a real jscodeshift codemod concept
- Order transformations logically (dependencies first)
- Comment each transformation with `# N. What this transformation does`

### Step 4: Write `WHY.md` — The Economic Case

Structure:
1. **The Problem** — What pain does this solve? Use real data (Reddit posts, pricing pages).
2. **💰 Potential Savings** — Time saved (hours), money saved ($/month), cognitive load reduced.
3. **What is [Target Tool]?** — Brief, honest description of the alternative.
4. The marketing hook at the bottom (copy from existing recipes).

### Step 5: Write `PREVIEW.md` — The Before/After

This is the most viral part of any recipe. Show real code:
- Use `diff` code blocks with `+` and `-` prefix
- Cover the 3-5 most common patterns developers will encounter
- End with the env var diff — everyone forgets env vars
- The headline: **"⚡ This transformation took 0.2 seconds of AST Surgery."**

### Step 6: Write `README.md` — The Landing Page

Use this structure:
1. **Title** — Same pain-language name as the recipe
2. **Badges** — Copy the badge pattern from `firebase-to-supabase`
3. **The Problem** (2-3 paragraphs of real pain)
4. **The Solution** (comparison table: old tool vs new tool)
5. **What Forjet Does** (link to PREVIEW.md)
6. **What This Recipe Transforms** (table of files and transformations)
7. **Prerequisites**
8. **Using with Forjet** (CLI example)
9. **Using with Cursor** (cursorrules snippet)
10. **💰 Potential Savings** (concrete numbers)
11. **⚠️ Known Caveats** (be honest — this builds trust)
12. **Contributing** link
13. Marketing hook at the bottom

### Step 7: Update `.cursorrules`

Add a section for your migration with 5-8 concrete rules that teach Cursor 
how to assist with this specific migration intelligently.

### Step 8: Update the main `README.md`

Add your migration to the "High-Priority Escapes" table with:
- Name (linked to your recipe folder)
- The pain (one phrase)
- Time saved
- Money saved

---

## Validation

Before opening a PR, validate your recipe against the JSON Schema:

```bash
# Install ajv-cli
npm install -g ajv-cli

# Validate your recipe
ajv validate -s schema/recipe-schema.json -d migration-bible/your-recipe/recipe.yaml
```

---

## PR Checklist

- [ ] `recipe.yaml` validates against `schema/recipe-schema.json`
- [ ] `WHY.md` contains real data (link sources)
- [ ] `PREVIEW.md` shows at least 3 before/after code diffs
- [ ] `README.md` includes the savings calculator section
- [ ] `.cursorrules` updated with migration-specific rules
- [ ] Main `README.md` updated with new entry in the migration table
- [ ] Recipe `id` is unique across the entire repo
- [ ] All `target_file` paths reflect real, common project structures

---

## 🎯 Surgery Wanted (Bounty Board)

Add a high-value migration and get featured as a **Master Surgeon** in our Hall of Fame. We prioritize migrations that actively save startups thousands of dollars.

### The Most Wanted List
- `Datadog → Grafana Stack` (Escape enterprise logging bills)
- `MongoDB Atlas → Neon (FerretDB)` (Escape Atlas pricing tiers)
- `Heroku → Railway/Render` (Escape dormant dyno fees)
- `Auth0 → Better Auth` (Escape B2B enterprise tier pricing)
- `Contentful → Payload CMS` (Escape headless CMS API limits)

### 🏆 Master Surgeon Hall of Fame
*(Be the first to perform a perfect AST migration from the list above and get your GitHub profile featured here forever)*

---

## Community Standards

- Be accurate. Don't inflate savings numbers.
- Be honest about caveats. Every migration has gotchas — document them.
- Be kind. Every contributor here is solving real pain for real developers.

---

> *"A good Software Surgeon leaves no trace — just a healthier codebase and a lighter invoice."*
>
> — Forjet Team
