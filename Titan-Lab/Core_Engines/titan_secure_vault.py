import os, re, asyncio, cloudscraper, httpx, random

# CodeHub Secure Tunnel [cite: 2026-01-20]
BOT_TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "7228901951"

# ترسانة المتصفحات للتمويه [cite: 2026-01-11]
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
]

async def send_to_hq(msg):
    # إرسال مشفر عبر قناة تليجرام الآمنة
    async with httpx.AsyncClient(http2=True) as client:
        try:
            await client.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                             data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
        except: pass

async def secure_invasion():
    scraper = cloudscraper.create_scraper()
    print("\033[94m🛡️ CodeHub Secure Tunnel Established. Titan is invisible.\033[0m")
    
    with open("targets.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        try:
            # تمويه الطلب بهوية مختلفة كل مرة [cite: 2026-01-11]
            headers = {'User-Agent': random.choice(USER_AGENTS)}
            resp = scraper.get(url, headers=headers, timeout=15)
            
            if resp.status_code == 200:
                emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', resp.text))
                phones = set(re.findall(r'(?:\+|00)?(?:971|966|20|965|968|973)\d{8,11}', resp.text))
                
                if emails or phones:
                    report = (f"🛡️ **SECURE SEIZURE: {url}**\n"
                              f"📧 Emails: {', '.join(emails) if emails else 'None'}\n"
                              f"📱 Phones: {', '.join(phones) if phones else 'None'}")
                    await send_to_hq(report)
                    print(f"✅ Securely Sent: {url}")
            await asyncio.sleep(random.uniform(2, 4)) # تأخير أمني
        except: continue

if __name__ == "__main__":
    asyncio.run(secure_invasion())
