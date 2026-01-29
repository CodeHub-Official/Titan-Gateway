import os, re

LOOT_DIR = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/Loot/"
VAULT_FILE = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/The_Vault.txt"

def refine():
    patterns = {
        "EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "DB_PASS": r"(DB_PASSWORD|password|pwd)[\s:=]+['\"]?([a-zA-Z0-9@#$%^&*()_+=-]+)['\"]?",
        "API_KEY": r"(API_KEY|APP_SECRET|token)[\s:=]+['\"]?([a-zA-Z0-9\-_]{20,})['\"]?"
    }
    
    with open(VAULT_FILE, "w") as vault:
        vault.write("🏆 CODEHUB GRAND VAULT - GOLD REPORT 🏆\n" + "="*40 + "\n")
        
        for root, dirs, files in os.walk(LOOT_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                vault.write(f"\n🎯 SOURCE: {file}\n")
                try:
                    with open(file_path, "r", errors="ignore") as f:
                        content = f.read()
                        for label, pattern in patterns.items():
                            matches = re.findall(pattern, content, re.IGNORECASE)
                            for match in set(matches):
                                result = match[1] if isinstance(match, tuple) else match
                                vault.write(f"   ✨ {label}: {result}\n")
                except: pass
    print(f"✅ Refinery Complete! Check your gold at: {VAULT_FILE}")

if __name__ == "__main__":
    refine()
