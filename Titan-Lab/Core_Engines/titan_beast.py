import os, re, asyncio, httpx, random
from bs4 import BeautifulSoup

def check_vpn():
    # فحص نفق الاتصال المشفر
    vpn = os.popen("ifconfig").read()
    if "tun0" not in vpn and "ppp0" not in vpn:
        print("!! CRITICAL: VPN DISCONNECTED - SHIELD DOWN !!")
        return False
    print("💎 Shield Active: VPN Tunnel Secured")
    return True

async def titan_hunt():
    if not check_vpn(): return
    
    output_dir = "CodeHub_Leads"
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    
    with open("targets.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    async with httpx.AsyncClient(http2=True, timeout=20, follow_redirects=True) as client:
        for url in urls:
            try:
                print(f"[*] Diving into: {url}")
                resp = await client.get(url, headers={"User-Agent": "Mozilla/5.0"})
                soup = BeautifulSoup(resp.text, 'html.parser')
                
                # استخراج الذهب
                text = soup.get_text()
                emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text))
                phones = set(re.findall(r'(?:\+971|971|00971|05|\+966|966|05|\+20|01)\d{8,11}', text))
                
                # فرز وتخزين فوري للنتائج الملموسة
                with open(f"{output_dir}/WhatsApp_Gold.txt", "a") as f_wa:
                    for p in phones: 
                        if len(p) > 8: f_wa.write(f"https://wa.me/{p.replace('+','')}\n")
                
                with open(f"{output_dir}/Emails_Gold.txt", "a") as f_em:
                    for e in emails: f_em.write(f"{e}\n")
                
                await asyncio.sleep(random.uniform(1, 3))
            except: continue

if __name__ == "__main__":
    asyncio.run(titan_hunt())
