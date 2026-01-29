import os, shutil, sqlite3, re, time

# --- الإعدادات السويسرية ---
SOURCE_DIR = os.path.expanduser("~/Titan-Lab/Data_Vault/Loot")
HQ_DIR = os.path.expanduser("~/TITAN_HEADQUARTERS")
DB_FILE = os.path.join(HQ_DIR, "TITAN_CORE.db")
MASTER_TXT = os.path.join(HQ_DIR, "ULTIMATE_GOLD.txt")

DIRS = {
    "01_KINGS_KEYS": [".env", "config.php", "wp-config.php", "settings.php"],
    "02_EMPIRE_DATABASES": [".sql", ".db", ".sqlite"],
    "03_GIT_INTELLIGENCE": [".git", ".git_config"],
    "04_RAW_IDENTITIES": ["emails", "phones", "leads", "csv"],
    "05_OPERATIONS_LOGS": [".log", ".txt", ".json"]
}

def setup():
    if not os.path.exists(HQ_DIR): os.makedirs(HQ_DIR)
    for d in DIRS:
        path = os.path.join(HQ_DIR, d)
        if not os.path.exists(path): os.makedirs(path)

def organize():
    print("[*] Stage 1: Swiss Organizing...")
    if not os.path.exists(SOURCE_DIR): return
    files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]
    for f in files:
        if f.endswith(".py") or f.endswith(".sh"): continue
        target = "99_UNCLASSIFIED"
        for folder, keys in DIRS.items():
            if any(k in f.lower() for k in keys): target = folder; break
        try: shutil.move(os.path.join(SOURCE_DIR, f), os.path.join(HQ_DIR, target, f))
        except: pass

def refine_and_inject():
    print("[*] Stage 2 & 3: Refining & Injecting to Core...")
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS strategic_assets (id INTEGER PRIMARY KEY, target_domain TEXT, asset_type TEXT, asset_value TEXT UNIQUE, status TEXT DEFAULT "NEW")')
    
    keys_path = os.path.join(HQ_DIR, "01_KINGS_KEYS")
    patterns = {"API_KEY": r"(API_KEY|api_secret|access_token|auth_token)\s*=\s*['\"]?([^'\"]+)['\"]?",
                "DB_PASS": r"(DB_PASSWORD|DB_PASS|database_password)\s*=\s*['\"]?([^'\"]+)['\"]?"}
    
    found_count = 0
    with open(MASTER_TXT, 'w') as master:
        for f_name in os.listdir(keys_path):
            with open(os.path.join(keys_path, f_name), 'r', errors='ignore') as f:
                content = f.read()
                for label, pat in patterns.items():
                    matches = re.findall(pat, content, re.I)
                    for m in matches:
                        val = m[1].strip()
                        if len(val) > 5:
                            try:
                                c.execute('INSERT INTO strategic_assets (target_domain, asset_type, asset_value) VALUES (?,?,?)', (f_name, label, val))
                                master.write(f"SOURCE: {f_name} | {label}: {val}\n")
                                found_count += 1
                            except: pass
    conn.commit()
    conn.close()
    return found_count

if __name__ == "__main__":
    print("--- TITAN ULTIMATE ENGINE ACTIVATED ---")
    setup()
    organize()
    total = refine_and_inject()
    print("-" * 40)
    print(f"[SUCCESS] Operation Complete.")
    print(f"[*] Total Gold Assets Secured in Core: {total}")
    print(f"[*] Check your HQ: {HQ_DIR}")
