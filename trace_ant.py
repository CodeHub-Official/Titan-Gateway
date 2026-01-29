import sqlite3, os
db_path = os.path.expanduser('~/TITAN_HEADQUARTERS/TITAN_CORE.db')
try:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # معرفة أسماء الجداول اللي النملة أنشأتها
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print("\033[1;35m[🐜] ANT ANALYST STORAGE SCAN...\033[0m")
    
    for table in tables:
        t_name = table[0]
        # فحص عدد السطور في كل جدول
        cur.execute(f"SELECT COUNT(*) FROM {t_name}")
        count = cur.fetchone()[0]
        print(f"\033[1;36m[#] Table: {t_name} | Entries: {count}\033[0m")
        
        # عرض عينة من أي جدول فيه بيانات كتير (زي الـ 1000 رقم)
        if count > 0:
            cur.execute(f"PRAGMA table_info({t_name})")
            cols = [col[1] for col in cur.fetchall()]
            print(f"    Columns: {cols}")
            cur.execute(f"SELECT * FROM {t_name} LIMIT 3")
            for row in cur.fetchall():
                print(f"    Data Sample: {row}")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
