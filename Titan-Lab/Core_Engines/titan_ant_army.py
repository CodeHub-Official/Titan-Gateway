import asyncio, httpx, os

# إعدادات البوت والدستور
TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
ID = "7228901951"
VAULT_FILE = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/targets.txt"

async def ant_scout(client, url):
    try:
        # جيش النمل بيفحص الموقع بأقصى سرعة
        res = await client.get(url, timeout=4, follow_redirects=True)
        if res.status_code == 200:
            msg = f"🐜 [Ant Army] SUCCESS!\n🎯 URL: {url}\n📦 Status: Captured"
            await client.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={msg}")
            print(f"🐜 Ant captured: {url}")
    except: pass

async def main():
    print("🏗️ CodeHub: Ant Army Tech Initiated...")
    if not os.path.exists(VAULT_FILE):
        print("❌ Waiting for the Supply Line (targets.txt)...")
        return

    while True:
        with open(VAULT_FILE, "r") as f:
            links = list(set([line.strip() for line in f if "http" in line]))
        
        print(f"🌊 Army deploying on {len(links)} targets from our list...")
        
        # تكنولوجيا جيش النمل: 100 هجوم متوازي في نفس اللحظة
        async with httpx.AsyncClient(verify=False, limits=httpx.Limits(max_connections=100)) as client:
            for i in range(0, len(links), 100):
                batch = links[i:i+100]
                await asyncio.gather(*[ant_scout(client, u) for u in batch])
                print(f"✅ Ants finished batch {i//100 + 1}")
        
        print("⏳ Army resting for 60s before next wave...")
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
