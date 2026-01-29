import sqlite3, os, re
DB = os.path.expanduser("~/TITAN_HEADQUARTERS/TITAN_CORE.db")
ARC = os.path.expanduser("~/Titan-Lab/Empire_Archive")
def run():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS intelligence_assets (id INTEGER PRIMARY KEY, source TEXT, data TEXT, category TEXT)")
    cur.execute("UPDATE strategic_assets SET status='VALID' WHERE status IS NULL OR status='' LIMIT 10")
    count = 0
    for root, dirs, files in os.walk(ARC):
        for f in files:
            if f.endswith(('.txt', '.csv')):
                with open(os.path.join(root, f), 'r', errors='ignore') as file:
                    items = re.findall(r'[\w\.-]+@[\w\.-]+', file.read())
                    for i in items[:5]:
                        cur.execute("INSERT INTO intelligence_assets (source, data, category) VALUES (?, ?, ?)", (f, i, os.path.basename(root)))
                        count += 1
    conn.commit()
    conn.close()
    print(f"✅ Intelligence Injected: {count} points added to core.")
run()
