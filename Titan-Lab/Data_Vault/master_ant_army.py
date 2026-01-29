import asyncio, httpx, os, time, random
from bs4 import BeautifulSoup

# مصادر البيانات (القديم والجديد)
SOURCES = [
    "targets.txt",
    "../Empire_Archive/archived_targets_v1.txt",
    "../Logs/seen_links.log",
    "titan_harvest.log"
]
REPORT_FILE = "codehub_global_intelligence.txt"

def merge_assets():
    all_links = set()
    for src in SOURCES:
        full_path = os.path.expanduser(src)
        if os.path.exists(full_path):
            with open(full_path, "r") as f:
                for line in f:
                    if "http" in line:
                        # استخراج الرابط فقط من السطر
                        link = [w for w in line.split() if "http" in w][0].strip("|")
                        all_links.add(link)
    return list(all_links)

async def analyze_site(client, url):
    try:
        start = time.time()
        res = await client.get(url, timeout=12, follow_redirects=True)
        duration = time.time() - start
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # استخراج هوك البيع (Sales Hooks)
        hooks = []
        if duration > 3: hooks.append("Slow Load Speed")
        if not url.startswith('https'): hooks.append("No SSL Security")
        if "wp-content" in res.text: hooks.append("WordPress Legacy")
        if not soup.find('meta', attrs={'name': 'viewport'}): hooks.append("Not Mobile Friendly")
        
        status = "CRITICAL OPPORTUNITY" if len(hooks) > 1 else "HEALTHY"
        return f"TARGET: {url}\nSTATUS: {status}\nHOOKS: {', '.join(hooks) if hooks else 'Optimized'}\n{'-'*40}\n"
    except:
        return f"TARGET: {url}\nSTATUS: SHIELDED/OFFLINE\n{'-'*40}\n"

async def main():
    links = merge_assets()
    print(f"[🛡️] CodeHub Assets United: {len(links)} Unique Targets Found.")
    
    async with httpx.AsyncClient(verify=False, http2=True) as client:
        print("[🚀] Shadow Army is launching the Global Audit...")
        tasks = [analyze_site(client, url) for url in links]
        results = await asyncio.gather(*tasks)
        
        with open(REPORT_FILE, "w") as f:
            f.write(f"CODEHUB GLOBAL INTELLIGENCE REPORT - {time.strftime('%Y-%m-%d')}\n")
            f.writelines(results)
    print(f"[🏆] Audit Complete! Report: {REPORT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
