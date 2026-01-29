import asyncio
import random
import time
import sys
import httpx
from bs4 import BeautifulSoup

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/114.0 Firefox/114.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
]

async def check_vpn():
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get("https://ipapi.co/json/")
            data = response.json()
            print(f"[🛡️] VPN ACTIVE: {data.get('org')} ({data.get('country_name')})")
            return True
    except:
        print("[🚨] SECURITY ALERT: VPN IS OFF OR NO INTERNET! ABORTING.")
        return False

async def harvest(client, url):
    try:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        # Security Delay
        await asyncio.sleep(random.uniform(1, 3))
        
        response = await client.get(url, headers=headers, follow_redirects=True, timeout=20)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string.strip() if soup.title else "No Title"
            print(f"[✅] {time.strftime('%H:%M:%S')} | Collected: {url} | {title}")
            with open("titan_harvest.log", "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {url} | {title}\n")
        else:
            print(f"[⚠️] HTTP {response.status_code}: {url}")
            
    except Exception as e:
        print(f"[❌] Target Shielded: {url}")

async def run_titan():
    if not await check_vpn(): sys.exit()
    
    # Using HTTP2 for maximum speed and stealth
    async with httpx.AsyncClient(http2=True, verify=False) as client:
        print("[🚀] Titan Lite Engine Online. Monitoring 5000 targets...")
        while True:
            try:
                with open("targets.txt", "r") as f:
                    targets = [line.strip() for line in f.readlines() if line.strip()]
                
                random.shuffle(targets)
                
                for target in targets:
                    if not target.startswith('http'):
                        target = 'https://' + target
                    await harvest(client, target)
                    await asyncio.sleep(random.uniform(2, 5))
            except FileNotFoundError:
                print("[🚨] Error: targets.txt not found!")
                break
            except Exception as e:
                print(f"[!] Cycle Error: {e}")
                await asyncio.sleep(10)

if __name__ == "__main__":
    try:
        asyncio.run(run_titan())
    except KeyboardInterrupt:
        print("\n[!] Titan Halted by Commander.")
