import os
import json
import time

LOOT_PATH = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/Loot/"
SALES_CATALOG = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/Sales_Catalog.txt"

def get_file_sample(path):
    try:
        with open(path, 'r', errors='ignore') as f:
            lines = [f.readline().strip() for _ in range(3)]
            return " | ".join(lines)
    except:
        return "Unreadable Binary Content"

def build_catalog():
    print("🚀 CodeHub Sales Engine: Cataloging Loot...")
    if not os.path.exists(LOOT_PATH):
        print("❌ Vault is empty!")
        return

    assets = os.listdir(LOOT_PATH)
    with open(SALES_CATALOG, "w") as catalog:
        catalog.write(f"=== CODEHUB SALES CATALOG ({time.ctime()}) ===\n")
        catalog.write(f"Total Assets Secured: {len(assets)}\n")
        catalog.write("="*50 + "\n\n")

        for asset in assets:
            full_path = os.path.join(LOOT_PATH, asset)
            size = os.path.getsize(full_path) / 1024 # KB
            
            # Pricing Logic based on file type
            category = "Standard"
            price = "50$"
            if "sql" in asset or ".env" in asset:
                category = "PREMIUM GOLD"
                price = "500$+"
            
            sample = get_file_sample(full_path)
            
            catalog.write(f"💎 PRODUCT: {asset}\n")
            catalog.write(f"   📊 Category: {category}\n")
            catalog.write(f"   📦 Size: {size:.2f} KB\n")
            catalog.write(f"   💰 Est. Value: {price}\n")
            catalog.write(f"   📝 Sample: {sample[:100]}...\n")
            catalog.write("-" * 30 + "\n")

    print(f"✅ Catalog Created! Total items: {len(assets)}")
    print(f"📂 View your products: cat {SALES_CATALOG}")

if __name__ == "__main__":
    build_catalog()
