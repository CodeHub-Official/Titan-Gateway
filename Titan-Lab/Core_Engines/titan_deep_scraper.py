import os, re, asyncio, cloudscraper, httpx
from bs4 import BeautifulSoup

# CodeHub VIP Auth [cite: 2026-01-20]
BOT_TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "7228901951"

async def send_report(url, emails, phones):
    status = "💰 GOLD FOUND" if (emails or phones) else "🔍 SITE SCOUTED"
    msg = (f"🚀 **CodeHub VIP: {status}**\n"
           f"🌐 **Site:** {url}\n"
           f"📧 **Emails:** {', '.join(emails) if emails else 'N/A'}\n"
           f"📱 **Phones:** {', '.join(phones) if phones else 'N/A'}")
    async with httpx.AsyncClient() as client:
        try:
            await client.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                             data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
        except: pass

async def deep_hunt():
    scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'android'})
    with open("targets.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    
    print("🕷️ Titan Deep Scraper Active... No target will be missed.")
    for url in urls:
        try:
            resp = scraper.get(url, timeout=15)
            soup = BeautifulSoup(resp.text, 'html.parser')
            text = soup.get_text()
            # البحث عن إيميلات وأرقام حتى في الـ Source Code المستخبي
            emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', resp.text))
            phones = set(re.findall(r'(?:\+|00)?(?:971|966|20|965|968|973)\d{8,11}', resp.text))
            
            # إرسال تقرير عن كل موقع مهما كانت النتيجة عشان شريكي يطمن
            await send_report(url, emails, phones)
            print(f"✅ Reported: {url}")
            await asyncio.sleep(1)
        except: continue

if __name__ == "__main__":
    asyncio.run(deep_hunt())
