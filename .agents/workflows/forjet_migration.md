---
description: Run a Forjet Migration Recipe using Antigravity/Opencode
---

# Forjet Migration Workflow

This workflow guides you through executing a Forjet Migration Recipe from the `forjet-recipes` repository. 

**When to use this workflow:**
When the user asks to migrate their tech stack (e.g., Firebase to Supabase, Vercel to Coolify) using a Forjet recipe.

## Steps

1. **Identify the Target Recipe**
   - Ask the user which migration they want to perform if not specified.
   - Available recipes in the Migration Bible:
     - `firebase-to-supabase`
     - `vercel-to-coolify`
     - `openai-to-ollama`
     - `planetscale-to-neon`
     - `clerk-to-better-auth`
     - `stripe-to-lemonsqueezy`

2. **Read the Recipe Specifications**
   - Use `view_file` to read the `README.md`, `PREVIEW.md`, and `recipe.yaml` of the chosen recipe inside the `forjet-recipes/migration-bible/[recipe]` directory.
   - Understand the `contract_mutations` (Env vars to add/remove) and `transformations` required.

3. **Analyze the User's Codebase**
   - Use `grep_search` or `find_by_name` to locate the files relevant to the old stack (e.g., searching for `firebase/auth`, `@clerk/nextjs`, or `vercel.json`).
   - Create a list of files that need to be modified.

4. **Execute AST-Level Transformations**
   - For each file identified, use `replace_file_content` or `multi_replace_file_content` to apply the changes exactly as outlined in the `PREVIEW.md` of the recipe.
   - Ensure you are doing semantic transformations (preserving types, inputs, and outputs), not blind regex replacements.

5. **Update Environment Variables**
   - Locate the `.env`, `.env.local`, or `.env.example` file.
   - Add and remove the variables as specified in the `contract_mutations` section of the `recipe.yaml`.

6. **Validate the Migration**
   - Run the project's type checker (e.g., `npm run typecheck` or `npx tsc --noEmit`).
   - If there are lint/type errors caused by the migration, fix them.

7. **Notify the User**
   - Once complete, notify the user that the migration has been applied. Provide a summary of the files changed, the env vars updated, and the expected savings (reference the `WHY.md`).
