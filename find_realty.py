import sqlite3, os
db_path = os.path.expanduser('~/TITAN_HEADQUARTERS/TITAN_CORE.db')
try:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # البحث عن أي جدول يحتوي على كلمات "عقارات" أو "أرقام" أو "RealEstate"
    print("\033[1;34m[🔎] SCANNING DATABASE FOR REAL ESTATE ASSETS...\033[0m")
    
    # محاولة استخراج البيانات من كل الجداول المحتملة
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    
    for table in tables:
        t_name = table[0]
        cur.execute(f"SELECT COUNT(*) FROM {t_name} WHERE category LIKE '%Real%' OR data LIKE '%+%' OR category LIKE '%عقارات%'")
        count = cur.fetchone()[0]
        if count > 0:
            print(f"\033[1;32m[🎯] FOUND {count} ASSETS IN TABLE: {t_name}\033[0m")
            cur.execute(f"SELECT category, data FROM {t_name} LIMIT 5")
            for row in cur.fetchall():
                print(f" -> Sample: {row[1][:30]}...")
                
    conn.close()
except Exception as e:
    print(f"Error: {e}")
