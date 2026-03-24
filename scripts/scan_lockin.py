import os
import json
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

# Defined Vendor Traps mapping to Forjet Migrations
VENDORS = {
    "firebase": {
        "keywords": ["firebase", "firebase-admin", "FIREBASE_"],
        "migration": "Firebase → Supabase",
        "savings": "~$200/mo & ~30 hours",
        "recipe": "firebase-to-supabase"
    },
    "vercel": {
        "keywords": ["vercel", "@vercel/kv", "VERCEL_"],
        "migration": "Vercel → Coolify",
        "savings": "~$600/mo & ~8 hours",
        "recipe": "vercel-to-coolify"
    },
    "openai": {
        "keywords": ["openai", "OPENAI_API_KEY"],
        "migration": "OpenAI → Ollama",
        "savings": "Up to $30k/mo & Data Privacy",
        "recipe": "openai-to-ollama"
    },
    "planetscale": {
        "keywords": ["@planetscale/database", "PLANETSCALE_"],
        "migration": "PlanetScale → Neon",
        "savings": "Restore Free Tier & ~15 hours",
        "recipe": "planetscale-to-neon"
    },
    "clerk": {
        "keywords": ["@clerk/nextjs", "clerk", "CLERK_"],
        "migration": "Clerk → Better Auth",
        "savings": "~$800/mo at 50K MAU & ~15 hours",
        "recipe": "clerk-to-better-auth"
    },
    "stripe": {
        "keywords": ["stripe", "STRIPE_"],
        "migration": "Stripe → LemonSqueezy",
        "savings": "$5K+/yr in Tax Compliance & ~10 hours",
        "recipe": "stripe-to-lemonsqueezy"
    }
}

def scan_file(filepath, vendors_found):
    if not os.path.exists(filepath):
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            
            for vendor_id, vendor_data in VENDORS.items():
                if vendor_id in vendors_found:
                    continue
                for kw in vendor_data["keywords"]:
                    if kw.lower() in content:
                        vendors_found.add(vendor_id)
                        break
    except Exception:
        pass

def main():
    console.print(Panel.fit(
        "[bold cyan]Forjet Dependency Lock-in Scanner[/bold cyan] 🕵️\n"
        "Scanning your codebase for expensive vendor traps...",
        border_style="cyan"
    ))

    # Identify project root
    cwd = os.getcwd()
    vendors_found = set()

    # Scan package.json
    scan_file(os.path.join(cwd, "package.json"), vendors_found)
    
    # Scan requirements.txt
    scan_file(os.path.join(cwd, "requirements.txt"), vendors_found)
    
    # Scan .env
    scan_file(os.path.join(cwd, ".env"), vendors_found)
    scan_file(os.path.join(cwd, ".env.local"), vendors_found)

    if not vendors_found:
        console.print("[bold green]✅ No high-cost vendor lock-ins detected in your top-level manifests![/bold green]")
        return

    console.print("\n[bold red]🚨 Vendor Lock-in Detected![/bold red]")
    console.print("We found dependencies that typically scale against you. Here are the available escapes:\n")

    table = Table(box=box.SIMPLE_HEAVY, header_style="bold magenta")
    table.add_column("Detected Tool", style="dim")
    table.add_column("Available Migration Escape", style="bold cyan")
    table.add_column("Potential Savings", justify="right", style="green")

    for vendor_id in vendors_found:
        data = VENDORS[vendor_id]
        table.add_row(
            vendor_id.capitalize(),
            data["migration"],
            data["savings"]
        )

    console.print(table)
    
    console.print("\n[dim]💡 To run a migration automatically with AST precision, use Forjet Engine:[/dim]")
    
    for vendor_id in vendors_found:
        recipe = VENDORS[vendor_id]["recipe"]
        console.print(f"  [bold yellow]forjet migrate --recipe {recipe} --repo .[/bold yellow]")

    console.print("\n[italic]View the full Migration Bible at: github.com/forjet/forjet-recipes[/italic]\n")

if __name__ == "__main__":
    main()
