# Claude Code Instructions for Forjet Migrations

When assisting a user with a Forjet migration from the `forjet-recipes` repository, follow these core principles:

1. **Think in AST, not Regex**
   - Never use simple find-and-replace for migrations. 
   - Analyze the semantic purpose of the code before refactoring.
   - When modifying imports, ensure type definitions and hooks are also updated.

2. **Always Check the Recipe Contract**
   - Read the relevant `why.md` and `preview.md` in the `migration-bible` folder to understand the "Before/After" state.
   - Every migration has a `contract_mutations` section in its `recipe.yaml` — ensure you add/remove the exact Environment Variables specified there.

3. **Specific Migration Rules**
   - **Firebase → Supabase:** Replace `.collection('x').doc('y').get()` with `.from('x').select('*').eq('id', y).single()`. Note that Firebase UIDs are strings, Supabase IDs are UUIDs.
   - **Vercel → Coolify:** Remove `export const runtime = 'edge'` from route handlers as Coolify uses standard Node.js environments.
   - **OpenAI → Ollama:** Swap `gpt-4` for `llama3.2`. Never hardcode models; default to `OLLAMA_MODEL` env var.
   - **PlanetScale → Neon:** Change `mysql2` to `postgres` in drizzle config. Map `tinyint(1)` to `boolean`.
   - **Clerk → Better Auth:** Replace `<ClerkProvider>` with `<SessionProvider>`. Use Better Auth's `useSession()` instead of `useUser()`.
   - **Stripe → LemonSqueezy:** Webhook verification is strictly required using `verifyWebhookSignature`. Replace `priceId` with `variantId`.

4. **Testing and Validation**
   - After a file is migrated, verify that the function signature remains identical (same inputs → same outputs).
   - Prompt the user to run their test suite or type checker (`tsc --noEmit` or `npm run typecheck`) after major transformations.

*Remember: Your goal is to apply the exact transformations defined in the Forjet Migration Bible with 100% precision, minimizing manual plumbing for the developer.*
