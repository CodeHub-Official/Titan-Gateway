import sqlite3, os, re

DB_PATH = os.path.expanduser("~/TITAN_HEADQUARTERS/TITAN_CORE.db")
ARCHIVE_PATH = os.path.expanduser("~/Titan-Lab/Empire_Archive")

def feed():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # إنشاء جدول البيانات المستهدفة إذا لم يوجد
    cur.execute("CREATE TABLE IF NOT EXISTS intelligence_assets (id INTEGER PRIMARY KEY, source TEXT, data TEXT, category TEXT)")
    
    count = 0
    # مسح الأرشيف (مصر، السعودية، الإمارات)
    for root, dirs, files in os.walk(ARCHIVE_PATH):
        for file in files:
            if file.endswith(('.txt', '.csv')):
                path = os.path.join(root, file)
                category = os.path.basename(root)
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
                    # استخراج "الذهب": إيميلات أو أرقام كمثال للبيانات
                    found = re.findall(r'[\w\.-]+@[\w\.-]+', content)
                    for item in found[:10]: # أخذ عينة من كل ملف للتغذية
                        cur.execute("INSERT INTO intelligence_assets (source, data, category) VALUES (?, ?, ?)", (file, item, category))
                        count += 1
    conn.commit()
    conn.close()
    print(f"✅ Nucleus Fed: {count} new intelligence points injected.")

if __name__ == "__main__": feed()
