import sqlite3, os

db_path = os.path.expanduser('~/TITAN_HEADQUARTERS/TITAN_CORE.db')
catalog_path = 'AUCTION_CATALOG.txt'

try:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT category, data FROM intelligence_assets')
    rows = cur.fetchall()
    
    with open(catalog_path, 'w', encoding='utf-8') as f:
        f.write("="*50 + "\n")
        f.write("   TITAN PRIVATE AUCTION: PREVIEW CATALOG\n")
        f.write("   GENERATED: 2026-01-29 | ASSETS: " + str(len(rows)) + "\n")
        f.write("="*50 + "\n\n")
        
        for row in rows:
            f.write(f"[TARGET: {row[0]:<15}] | [ASSET: {row[1]}]\n")
            
    print(f"\n\033[1;32m[✅] SUCCESS: {len(rows)} Assets extracted to {catalog_path}\033[0m")
    print("\033[1;36m[ℹ️] Type 'cat AUCTION_CATALOG.txt' to view the goods.\033[0m\n")
    conn.close()
except Exception as e:
    print(f"\033[1;31m[!] Error: {e}\033[0m")
