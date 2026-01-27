import asyncio, httpx, os, time

# --- إعدادات القيادة ---
LOG_FILE = "codehub_tunnels.log"
REPORTS_FILE = "vulnerability_reports.txt"
TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "7228901951"

async def send_report(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        try: await client.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"})
        except: pass

async def analyze_site(url):
    report = f"<b>🔍 [CodeHub Audit] Analysis for:</b>\n<code>{url}</code>\n\n"
    vulnerabilities = []
    
    try:
        async with httpx.AsyncClient(timeout=10, verify=False) as client:
            res = await client.get(url)
            # 1. فحص إصدار الخادم (Server Version)
            server = res.headers.get("Server", "Unknown")
            if "PHP" in server or "Apache" in server:
                vulnerabilities.append(f"• <b>Issue:</b> Server Header Exposure ({server})\n  <b>Fix:</b> Disable 'ServerTokens' in config.")

            # 2. فحص أمان الـ Headers
            if "X-Frame-Options" not in res.headers:
                vulnerabilities.append("• <b>Issue:</b> Missing X-Frame-Options (Clickjacking Risk)\n  <b>Fix:</b> Add 'X-Frame-Options: SAMEORIGIN'.")
            
            # 3. فحص ملفات حساسة
            base_url = "/".join(url.split("/")[:3])
            check_git = await client.get(f"{base_url}/.git/config")
            if check_git.status_code == 200:
                vulnerabilities.append("• <b>CRITICAL:</b> Exposed .git directory!\n  <b>Fix:</b> Block access to hidden files.")

        if vulnerabilities:
            final_msg = report + "\n".join(vulnerabilities) + "\n\n✅ <i>Report ready for sale preparation.</i>"
            await send_report(final_msg)
            with open(REPORTS_FILE, "a") as f:
                f.write(f"--- {url} ---\n" + "\n".join(vulnerabilities) + "\n\n")
            return True
    except: pass
    return False

async def main():
    print("🛡️ Auditor is watching for new successful tunnels...")
    processed = set()
    
    while True:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                for line in f:
                    if "|" in line:
                        url = line.split("|")[1].strip()
                        if url not in processed:
                            print(f"[🔬] Analyzing: {url}")
                            await analyze_site(url)
                            processed.add(url)
        await asyncio.sleep(10) # فحص الملف كل 10 ثوانٍ

if __name__ == "__main__":
    asyncio.run(main())
