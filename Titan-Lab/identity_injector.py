import os
import re

LOOT_PATH = "Data_Vault/Loot/"
SHIELD_FILE = "Data_Vault/shield_identity.txt"

def harvest_identities():
    """استخراج الهويات الحقيقية من ملفات الـ Loot"""
    if not os.path.exists(LOOT_PATH): return
    
    identities = set()
    # البحث عن User-Agents أو Token داخل الملفات المسحوبة
    for filename in os.listdir(LOOT_PATH):
        try:
            with open(os.path.join(LOOT_PATH, filename), 'r', errors='ignore') as f:
                content = f.read()
                # سحب أي بصمة رقمية حقيقية
                found = re.findall(r'User-Agent: (.*)', content)
                for item in found: identities.add(item.strip())
        except: continue
    
    if identities:
        with open(SHIELD_FILE, "w") as f:
            for identity in identities: f.write(identity + "\n")
        print(f"[✅] Injected {len(identities)} Real Identities into Titan's Brain.")
    else:
        print("[!] No real identities found yet. Waiting for more loot...")

if __name__ == "__main__":
    harvest_identities()
