import httpx
import asyncio
import os
import re

# --- CodeHub Cloud Master Config ---
API_KEY = "A5421c969a3b500ccfa3d0971f02f79b"
TOKEN = "8290479304:AAEa6o56IPfTNb8KJqSfiFXWLVjfU4DjxS0"
CHAT_ID = "7228901951"
TARGETS_FILE = os.path.expanduser("~/Titan-Lab/Data_Vault/targets.txt")

async def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        try: await client.post(url, data={'chat_id': CHAT_ID, 'text': message})
        except: pass

def extract_price(content, url):
    # Specialized Regex for Cloud Response
    if "amazon" in url:
        m = re.search(r'class="a-price-whole">([\d,.]+)', content)
        if m: return f"{m.group(1)} EGP"
    elif "noon" in url:
        m = re.search(r'"price":\s?([\d.]+)', content)
        if m: return f"{m.group(1)} SAR/EGP"
    
    # Global Patterns
    patt = [r'(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s?(?:EGP|SAR|AED|USD|\$|جنيه|ريال)']
    for p in patt:
        res = re.search(p, content)
        if res: return res.group(0)
    return "Searching..."

async def hunt(url):
    is_hard = any(d in url for d in ["amazon", "noon"])
    # استخدام البروتوكول الآمن https لتخطي الـ 401
    proxy_url = f"https://api.scraperapi.com?api_key={API_KEY}&url={url}&render=true" if is_hard else url
    
    print(f"[*] Target: {url}")
    try:
        async with httpx.AsyncClient(timeout=60.0, follow_redirects=True) as client:
            resp = await client.get(proxy_url)
            if resp.status_code == 200:
                price = extract_price(resp.text, url)
                print(f"[+] Result: {price}")
                await send_telegram(f"☁️ Titan Cloud Update:\n💰 Price: {price}\n🔗 {url}")
            elif resp.status_code == 401:
                print("[!] Error 401: Please verify your email in ScraperAPI!")
            else:
                print(f"[!] Blocked: Status {resp.status_code}")
    except Exception as e:
        print(f"[!] Error: {e}")

async def main():
    if not os.path.exists(TARGETS_FILE): return
    with open(TARGETS_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()][-6:]
    for u in urls:
        await hunt(u)
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
