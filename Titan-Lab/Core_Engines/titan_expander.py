import asyncio, httpx, re, os

VAULT_FILE = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/targets.txt"

async def expand_list(client, url):
    try:
        # الدخول للموقع اللي جيش النمل نجح فيه وسحب كل الروابط اللي جواه
        r = await client.get(url, timeout=5)
        new_links = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', r.text)
        
        # تنقية الروابط (عشان ميسحبش فيسبوك ويوتيوب)
        valid_links = [l for l in set(new_links) if any(x in l for x in [".com", ".net", ".org", ".gov"])]
        
        if valid_links:
            with open(VAULT_FILE, "a") as f:
                for link in valid_links:
                    f.write(link + "\n")
            print(f"📈 Expander: Added {len(valid_links)} new potential targets from {url}")
    except: pass

async def main():
    print("🧬 CodeHub Expander: Doubling the Arsenal...")
    async with httpx.AsyncClient(verify=False, follow_redirects=True) as client:
        while True:
            if os.path.exists(VAULT_FILE):
                with open(VAULT_FILE, "r") as f:
                    # قراءة آخر 50 رابط اشتغل عليهم جيش النمل
                    seeds = f.readlines()[-50:]
                
                tasks = [expand_list(client, s.strip()) for s in seeds if "http" in s]
                await asyncio.gather(*tasks)
            
            print("⏳ Expander resting for 30s to avoid detection...")
            await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(main())
