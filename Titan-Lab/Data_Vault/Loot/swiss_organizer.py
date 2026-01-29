import os
import shutil
import time

# --- إعدادات المسارات (الطريقة السويسرية) ---
SOURCE_DIR = os.path.expanduser("~/Titan-Lab/Data_Vault/Loot")
BASE_DEST = os.path.expanduser("~/TITAN_HEADQUARTERS")

# هيكلة الخزائن
DIRS = {
    "01_KINGS_KEYS": [".env", "config.php", "wp-config.php", "settings.php", "conf.php"],
    "02_EMPIRE_DATABASES": [".sql", ".db", ".sqlite", ".dump"],
    "03_GIT_INTELLIGENCE": [".git", ".git_config", ".gitignore"],
    "04_RAW_IDENTITIES": ["emails", "phones", "leads", "contacts", ".csv", ".xlsx"],
    "05_OPERATIONS_LOGS": [".log", ".txt", ".json"],
    "99_UNCLASSIFIED": [] # للباقي
}

def setup_infrastructure():
    """بناء الهيكل التنظيمي الجديد"""
    print(f"[*] جاري بناء البنية التحتية في: {BASE_DEST}")
    if not os.path.exists(BASE_DEST):
        os.makedirs(BASE_DEST)
    
    for folder in DIRS:
        path = os.path.join(BASE_DEST, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"    [+] تم إنشاء الخزنة: {folder}")

def classify_file(filename):
    """تحديد هوية الملف بدقة"""
    filename_lower = filename.lower()
    
    for folder, keywords in DIRS.items():
        for key in keywords:
            if key in filename_lower:
                return folder
    return "99_UNCLASSIFIED"

def execute_swiss_sort():
    """تنفيذ عملية الفرز والنقل"""
    setup_infrastructure()
    
    print("\n[*] بدء عملية الفرز الدقيق...")
    files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]
    
    moved_count = 0
    
    for file in files:
        # استثناء السكربتات التشغيلية (لا ننقل ملفات بايثون)
        if file.endswith(".py") or file.endswith(".sh"):
            continue
            
        src_path = os.path.join(SOURCE_DIR, file)
        target_folder = classify_file(file)
        dest_path = os.path.join(BASE_DEST, target_folder, file)
        
        try:
            shutil.move(src_path, dest_path)
            print(f" -> تم نقل: {file} \t>>\t {target_folder}")
            moved_count += 1
        except Exception as e:
            print(f" [!] خطأ في نقل {file}: {str(e)}")

    print("-" * 50)
    print(f"[SUCCESS] تمت العملية بنجاح. تم تنظيم {moved_count} ملف.")
    print(f"[*] موقع الملفات الجديد: {BASE_DEST}")

if __name__ == "__main__":
    if os.path.exists(SOURCE_DIR):
        execute_swiss_sort()
    else:
        print(f"[ERROR] المجلد المصدر غير موجود: {SOURCE_DIR}")

