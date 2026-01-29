import asyncio, httpx, os
TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
ID = "7228901951"
VAULT = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/targets.txt"

async def attack(client, url):
    try:
        # محاكاة هجوم سريع للتأكد من استجابة السيرفر
        res = await client.get(url, timeout=5)
        if res.status_code == 200:
            msg = f"🚀 [CodeHub] TARGET HIT!\n🎯 URL: {url}\n🛡️ Status: ACCESSIBLE"
            await client.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={msg}")
            print(f"✅ Alert Sent for {url}")
    except: pass

async def main():
    print("⚔️ Army of Ants Deployed... Expecting Telegram Spam!")
    async with httpx.AsyncClient(verify=False) as client:
        while True:
            if os.path.exists(VAULT):
                with open(VAULT, "r") as f:
                    urls = f.readlines()[-20:] # هجوم على آخر 20 رابط وصلوا
                tasks = [attack(client, u.strip()) for u in urls]
                await asyncio.gather(*tasks)
            await asyncio.sleep(10)

if __name__ == "__main__": asyncio.run(main())
