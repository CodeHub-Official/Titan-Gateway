import asyncio
import httpx
from bs4 import BeautifulSoup
import os
import random

TARGET_FILE = os.path.expanduser("~/Titan-Lab/targets.txt")

async def ant_scout(client, query):
    """نملة واحدة تسحب روابط بحث واحد بسرعة"""
    try:
        url = f"https://www.bing.com/search?q={query}&count=50"
        resp = await client.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = []
        for a in soup.find_all('a', href=True):
            link = a['href']
            if "http" in link and "bing" not in link and "microsoft" not in link:
                links.append(link)
        return links
    except: return []

async def run_swarm():
    # جيش الكلمات الدليلية (يمكن توسيعه لآلاف الكلمات)
    locations = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Al Ain"]
    sectors = ["Real Estate", "Clinic", "Construction", "Law Firm", "Ecommerce", "Logistics"]
    
    queries = [f'site:.ae "{s}" {l}' for s in sectors for l in locations]
    all_targets = set()

    print(f"--- 🐜 HANNIBAL SWARM STARTING: {len(queries)} SCOUTS ---")
    
    async with httpx.AsyncClient(headers={"User-Agent": "Mozilla/5.0"}, http2=True) as client:
        tasks = [ant_scout(client, q) for q in queries]
        results = await asyncio.gather(*tasks)
        
        for r in results:
            all_targets.update(r)

    with open(TARGET_FILE, "a") as f:
        for link in all_targets:
            f.write(link + "\n")
            
    print(f"[✅] Swarm returned! {len(all_targets)} new links added to targets.txt")

if __name__ == "__main__":
    asyncio.run(run_swarm())
