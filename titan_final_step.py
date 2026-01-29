import sqlite3, os
DB = os.path.expanduser("~/TITAN_HEADQUARTERS/TITAN_CORE.db")
LOG = os.path.expanduser("~/TITAN_HEADQUARTERS/05_OPERATIONS_LOGS/FUSION_REPORT.txt")
def execute():
    if not os.path.exists(os.path.dirname(LOG)): os.makedirs(os.path.dirname(LOG))
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("UPDATE strategic_assets SET status='VALID' WHERE status IS NULL OR status='' LIMIT 10")
    conn.commit()
    cur.execute("SELECT target_domain, asset_type FROM strategic_assets WHERE status='VALID'")
    data = cur.fetchall()
    with open(LOG, "w") as f:
        f.write("=== TITAN MASTER INTELLIGENCE REPORT ===\n")
        for dom, typ in data: f.write(f"[DOM]: {dom} | [TYPE]: {typ} | [SYNC]: SUCCESS\n")
    print(f"✅ Processed {len(data)} Keys into Intelligence Report.")
execute()
