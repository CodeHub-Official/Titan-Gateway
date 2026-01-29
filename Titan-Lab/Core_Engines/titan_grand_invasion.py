import os, re, asyncio, random, cloudscraper, httpx
from bs4 import BeautifulSoup

# CodeHub VIP Execution - Titan V15.4
BOT_TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "7228901951"

async def send_to_telegram(url, country, industry, emails, phones):
    msg = (f"🚀 **CodeHub VIP: NEW SEIZURE**\n"
           f"🌐 **Site:** {url}\n"
           f"📍 **Location:** {country}\n"
           f"💼 **Industry:** {industry}\n"
           f"📧 **Emails:** {', '.join(emails) if emails else 'None'}\n"
           f"📱 **Phones:** {', '.join(phones) if phones else 'None'}\n"
           f"⚡ **Source:** Titan Deep Ant")
    async with httpx.AsyncClient() as client:
        try:
            await client.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                             data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
        except: pass

async def grand_invasion():
    print("\033[92m🚀 CodeHub VIP Bot Linked. Starting Invasion...\033[0m")
    scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'android'})
    if not os.path.exists("targets.txt"): return

    with open("targets.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        try:
            await asyncio.sleep(random.uniform(1, 2))
            resp = scraper.get(url, timeout=10)
            if resp.status_code != 200: continue
            soup = BeautifulSoup(resp.text, 'html.parser')
            content = soup.get_text()

            # Classification Logic
            country = "Egypt" if any(k in url or k in content for k in [".eg", "مصر"]) else "Saudi/UAE/Global"
            industry = "Real_Estate" if any(k in content.lower() for k in ["aqar", "property", "عقارات"]) else "General_Business"
            
            emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content))
            phones = set(re.findall(r'(?:\+|00)?(?:971|966|20|965|968|973)\d{8,11}', content))

            if phones or emails:
                await send_to_telegram(url, country, industry, emails, phones)
                print(f"✅ Seized & Sent to Bot: {url}")
        except: continue

if __name__ == "__main__":
    asyncio.run(grand_invasion())
