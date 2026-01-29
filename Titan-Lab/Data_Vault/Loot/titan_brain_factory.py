import sqlite3, os, re
INPUT_FILE = os.path.expanduser("~/TITAN_HEADQUARTERS/MASTER_KEYS.txt")
DB_FILE = os.path.expanduser("~/TITAN_HEADQUARTERS/TITAN_CORE.db")
def run():
    if not os.path.exists(os.path.dirname(DB_FILE)): os.makedirs(os.path.dirname(DB_FILE))
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS strategic_assets (id INTEGER PRIMARY KEY AUTOINCREMENT, target_domain TEXT, asset_type TEXT, asset_value TEXT UNIQUE, source_file TEXT, status TEXT DEFAULT "NEW", captured_at DATETIME DEFAULT CURRENT_TIMESTAMP)')
    if not os.path.exists(INPUT_FILE): return print("No Master Keys found!")
    with open(INPUT_FILE, 'r') as f:
        data = f.read()
        sources = re.findall(r"===\s*SOURCE:\s*(.*?)\s*===(.*?)(?==== SOURCE:|\Z)", data, re.DOTALL)
        for src, content in sources:
            keys = re.findall(r"\[\+\]\s*(.*?):\s*(.*)", content)
            for k_type, k_val in keys:
                try:
                    c.execute('INSERT INTO strategic_assets (target_domain, asset_type, asset_value, source_file) VALUES (?, ?, ?, ?)', (src, k_type.strip(), k_val.strip(), src))
                except: pass
    conn.commit()
    print(f"[*] Done! Total Assets Secured: {c.execute('SELECT count(*) FROM strategic_assets').fetchone()[0]}")
    conn.close()
if __name__ == "__main__": run()
