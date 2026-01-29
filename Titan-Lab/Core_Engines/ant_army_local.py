import httpx
import asyncio
import os
import re
import time
import random

# --- CodeHub Deep Data Mining Config ---
TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "7228901951"
TARGETS_FILE = os.path.expanduser("~/Titan-Lab/Data_Vault/targets.txt")
ARCHIVE_LOG = os.path.expanduser("~/Titan-Lab/Empire_Archive/deep_mining.csv")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1"
]

os.makedirs(os.path.dirname(ARCHIVE_LOG), exist_ok=True)

async def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    async with httpx.AsyncClient(verify=False) as client:
        try: await client.post(url, data={'chat_id': CHAT_ID, 'text': message})
        except: pass

def smart_parser(content):
    # البحث عن أي معلومات قيمة: أسعار، هواتف، أو عناوين بريد إلكتروني
    data_found = []
    
    # 1. البحث عن الأسعار
    price = re.search(r'(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s?(?:EGP|USD|SAR|جنيه|\$)', content)
    if price: data_found.append(f"Price: {price.group(0)}")
    
    # 2. البحث عن أرقام الهواتف (نمط دولي ومحلي)
    phones = re.findall(r'(\+?\d{10,14})', content)
    if phones: data_found.append(f"Phone: {phones[0]}")
    
    # 3. البحث عن الإيميلات
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
    if emails: data_found.append(f"Email: {emails[0]}")
    
    return " | ".join(data_found) if data_found else "No Data Found"

async def local_hunt(url, index, total):
    headers = {"User-Agent": random.choice(USER_AGENTS), "Referer": "https://www.google.com/"}
    
    print(f"[{index}/{total}] ⛏️ Deep Mining: {url}")
    try:
        async with httpx.AsyncClient(headers=headers, timeout=15.0, follow_redirects=True, verify=False) as client:
            response = await client.get(url)
            if response.status_code == 200:
                extracted_info = smart_parser(response.text)
                
                # حفظ كل المعلومات في الأرشيف الإمبراطوري
                with open(ARCHIVE_LOG, "a") as f:
                    f.write(f"{time.strftime('%Y-%m-%d')},{url},{extracted_info}\n")
                
                # إرسال البيانات الدسمة فقط لتيليجرام
                if extracted_info != "No Data Found":
                    await send_telegram(f"💎 Titan Deep Mining:\n🛰️ Site: {url}\n📝 Info: {extracted_info}")
            else:
                print(f"[!] Skip {response.status_code}")
    except Exception:
        print(f"[!] Bypass Success")

async def main():
    if not os.path.exists(TARGETS_FILE): return
    with open(TARGETS_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    
    print(f"🚀 TITAN MINER UNLEASHED: Extracting from {len(urls)} links...")
    for i, url in enumerate(urls, 1):
        await local_hunt(url, i, len(urls))
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())
