import sqlite3, os, requests, time

DB_FILE = os.path.expanduser("~/TITAN_HEADQUARTERS/TITAN_CORE.db")

def get_current_ip():
    try: return requests.get('https://api.ipify.org', timeout=5).text
    except: return None

def validate_google_key(key):
    # فحص صامت لمفاتيح جوجل بدون استهلاك كوتا
    url = f"https://www.googleapis.com/serviceusage/v1/projects/test/services?key={key}"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 403 and "API key not enabled" in r.text: return "VALID_RESTRICTED"
        if r.status_code == 200: return "VALID_OPEN"
        return "INVALID"
    except: return "ERROR"

def start_operation():
    print("--- [TITAN STEALTH VALIDATOR] ---")
    
    # 1. فحص الأمان (The Safety Check)
    print("[*] Checking Security Perimeter...")
    initial_ip = get_current_ip()
    print(f"[!] Current Exit Node IP: {initial_ip}")
    
    confirm = input("[?] Is your VPN active? (y/n): ")
    if confirm.lower() != 'y':
        print("[X] OPERATION ABORTED: Security Protocol Violation.")
        return

    # 2. الاتصال بالعقل المركزي
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    assets = c.execute("SELECT id, target_domain, asset_value FROM strategic_assets WHERE asset_type='API_KEY'").fetchall()
    
    print(f"[*] Found {len(assets)} keys to validate. Starting silent scan...\n")

    for id, domain, key in assets:
        print(f" -> Testing Key for: {domain}...", end="\r")
        status = validate_google_key(key)
        
        # 3. تحديث الحالة في قاعدة البيانات
        c.execute("UPDATE strategic_assets SET status = ? WHERE id = ?", (status, id))
        print(f" [+] {domain}: {status}              ")
        time.sleep(1) # تأخير سويسري لتجنب الحظر

    conn.commit()
    conn.close()
    print("\n[SUCCESS] Brain Updated with Validation Status.")

if __name__ == "__main__":
    start_operation()
