import os
import re

# --- إعدادات المصفاة ---
SOURCE_DIR = os.path.expanduser("~/TITAN_HEADQUARTERS/01_KINGS_KEYS")
OUTPUT_FILE = os.path.expanduser("~/TITAN_HEADQUARTERS/MASTER_KEYS.txt")

# الكلمات المفتاحية التي نبحث عنها (الذهب)
PATTERNS = {
    "DB_PASSWORD": re.compile(r"(DB_PASSWORD|DB_PASS|database_password)\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE),
    "API_KEY": re.compile(r"(API_KEY|api_secret|access_token|auth_token)\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE),
    "AWS_KEY": re.compile(r"(AWS_ACCESS_KEY_ID|AWS_SECRET_ACCESS_KEY)\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE),
    "MAIL_PASS": re.compile(r"(MAIL_PASSWORD|SMTP_PASS)\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE),
    "APP_SECRET": re.compile(r"(APP_SECRET|APP_KEY|secret_key)\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE)
}

def refine_gold():
    print(f"[*] بدء تشغيل المصفاة في: {SOURCE_DIR}")
    print(f"[*] يتم البحث عن الأنماط: {list(PATTERNS.keys())}")
    
    results = []
    files_scanned = 0
    secrets_found = 0

    if not os.path.exists(SOURCE_DIR):
        print("[!] خطأ: مجلد المفاتيح غير موجود!")
        return

    # فحص الملفات
    for filename in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                file_hits = []
                
                for key_name, pattern in PATTERNS.items():
                    matches = pattern.findall(content)
                    for match in matches:
                        # تنظيف النتيجة
                        clean_value = match[1] if isinstance(match, tuple) else match
                        if len(clean_value) > 3: # تجاهل القيم القصيرة جداً
                            file_hits.append(f"  [+] {key_name}: {clean_value}")
                
                if file_hits:
                    results.append(f"\n=== SOURCE: {filename} ===")
                    results.extend(file_hits)
                    secrets_found += len(file_hits)
                    print(f" -> تم استخراج {len(file_hits)} سر من: {filename}")
        
        except Exception as e:
            pass
        
        files_scanned += 1

    # حفظ التقرير النهائي
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"--- TITAN REFINERY REPORT ---\n")
        f.write(f"DATE: {os.popen('date').read().strip()}\n")
        f.write(f"FILES SCANNED: {files_scanned}\n")
        f.write(f"SECRETS FOUND: {secrets_found}\n")
        f.write("-" * 40 + "\n")
        f.write("\n".join(results))

    print("-" * 50)
    print(f"[SUCCESS] انتهت العملية.")
    print(f"[*] تم مسح {files_scanned} ملف.")
    print(f"[*] تم العثور على {secrets_found} مفتاح/كلمة سر.")
    print(f"[*] التقرير محفوظ في: {OUTPUT_FILE}")

if __name__ == "__main__":
    refine_gold()

