import httpx
import asyncio
import os
import re
import random

TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "7228901951"
TARGETS_FILE = os.path.expanduser("~/Titan-Lab/Data_Vault/targets.txt")

async def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        try:
            await client.post(url, data={'chat_id': CHAT_ID, 'text': message})
        except:
            pass

def deep_extract_price(content, url):
    if "amazon" in url:
        match = re.search(r'class="a-price-whole">([\d,.]+)', content)
        if match: return f"{match.group(1)} EGP/USD"
    elif "noon" in url:
        match = re.search(r'"price":\s?([\d.]+)', content)
        if match: return f"{match.group(1)} Currency"
    
    patterns = [r'(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s?(?:EGP|SAR|AED|USD|\$|جنيه|ريال)']
    for p in patterns:
        m = re.search(p, content)
        if m: return m.group(0)
    return "Locked/Not Found"

async def hunt(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com/",
        "DNT": "1"
    }
    
    try:
        async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=20.0) as client:
            print(f"[*] Ghost Scouting: {url}...")
            await asyncio.sleep(random.uniform(2, 5))
            response = await client.get(url)
            if response.status_code == 200:
                price = deep_extract_price(response.text, url)
                print(f"[+] Result: {price}")
                await send_telegram(f"🕵️ Titan Ghost Hunt:\n💰 Price: {price}\n🔗 {url}")
            else:
                print(f"[!] Blocked by {url} (Status: {response.status_code})")
    except Exception as e:
        print(f"[!] Stealth Failure: {e}")

async def main():
    if not os.path.exists(TARGETS_FILE):
        print(f"[-] File not found: {TARGETS_FILE}")
        return
    with open(TARGETS_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    print(f"🚀 Launching Phantom Army on {len(urls)} targets...")
    for url in urls:
        await hunt(url)

if __name__ == "__main__":
    asyncio.run(main())
