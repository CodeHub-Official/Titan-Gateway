import sqlite3, os
DB = os.path.expanduser('~/TITAN_HEADQUARTERS/TITAN_CORE.db')
try:
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('SELECT category, data FROM intelligence_assets LIMIT 20')
    rows = cur.fetchall()
    print("\n\033[1;33m[⚖️] --- PRIVATE AUCTION LEDGER (TOP 20 ASSETS) ---\033[0m")
    print(f"{'CATEGORY':<20} | {'EXTRACTED INTELLIGENCE':<30}")
    print("-" * 55)
    for row in rows:
        print(f"{row[0]:<20} | {row[1]:<30}")
    conn.close()
except Exception as e:
    print(f"Error accessing core: {e}")
