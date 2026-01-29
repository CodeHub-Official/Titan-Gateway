import os, time, re

LOOT_DIR = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/Loot/"

def extract_secrets(file_path):
    secrets = []
    patterns = [r"DB_.*", r".*PASSWORD.*", r".*SECRET.*", r".*KEY.*", r".*USER.*"]
    try:
        with open(file_path, "r", errors="ignore") as f:
            content = f.readlines()
            for line in content:
                if any(re.match(p, line, re.IGNORECASE) for p in patterns):
                    secrets.append(line.strip())
    except: pass
    return secrets

print("🧐 CodeHub Analyst: Scanning Loot for Gold...")
processed_files = set()

while True:
    if os.path.exists(LOOT_DIR):
        current_files = set(os.listdir(LOOT_DIR))
        new_files = current_files - processed_files
        
        for file_name in new_files:
            print(f"\n📂 Analyzing: {file_name}")
            findings = extract_secrets(os.path.join(LOOT_DIR, file_name))
            if findings:
                print("💰 [GOLD FOUND]:")
                for secret in findings:
                    print(f"   ✨ {secret}")
            processed_files.add(file_name)
    
    time.sleep(10)
