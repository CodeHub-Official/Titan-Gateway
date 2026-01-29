import asyncio, httpx, re, os
VAULT = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/targets.txt"
async def deep_scrape():
    # البحث في محركات بحث متعددة بكلمات مفتاحية خطيرة
    queries = ["php?id=", "wp-config.php.bak", "index+of+admin+passwords", ".env+DB_PASSWORD"]
    headers = {"User-Agent": "Mozilla/5.0"}
    async with httpx.AsyncClient(headers=headers, verify=False) as client:
        for q in queries:
            try:
                r = await client.get(f"https://www.google.com/search?q={q}&num=100")
                links = re.findall(r'https?://[^\s<>"]+', r.text)
                with open(VAULT, "a") as f:
                    for l in links: 
                        if "google" not in l: f.write(l + "\n")
                print(f"🔥 Sniper: Flooding Vault with {len(links)} new leads!")
            except: pass
async def main():
    while True:
        await deep_scrape()
        await asyncio.sleep(5) # سرعة جنونية كل 5 ثواني
if __name__ == "__main__": asyncio.run(main())
