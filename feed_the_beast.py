import sqlite3, os

db_path = os.path.expanduser('~/TITAN_HEADQUARTERS/TITAN_CORE.db')
list_path = 'REAL_ESTATE_MASTER_LIST.txt'

try:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # إنشاء جدول "المعرفة العميقة"
    cur.execute('CREATE TABLE IF NOT EXISTS deep_knowledge (id INTEGER PRIMARY KEY, data TEXT, type TEXT)')
    
    with open(list_path, 'r') as f:
        contacts = list(set(f.readlines())) # إزالة المكرر لضمان جودة التغذية
        
    print(f"\033[1;34m[⚡] FEEDING {len(contacts)} UNIQUE NEURONS TO THE BEAST...\033[0m")
    
    # حقن البيانات (Batch Processing لسرعة التنفيذ)
    cur.executemany('INSERT INTO deep_knowledge (data, type) VALUES (?, ?)', 
                   [(c.strip(), 'CONTACT') for c in contacts])
    
    conn.commit()
    print("\033[1;32m[🏆] FEEDING COMPLETE. THE BEAST IS NOW SMARTER.\033[0m")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
