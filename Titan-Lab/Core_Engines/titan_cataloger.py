import os, json, time

LOOT_DIR = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/Loot/"
CATALOG_FILE = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/CodeHub_Sales_Catalog.json"

def generate_catalog():
    catalog = {"timestamp": time.ctime(), "assets": []}
    
    if not os.path.exists(LOOT_DIR):
        print("❌ Loot directory not found!")
        return

    for file_name in os.listdir(LOOT_DIR):
        file_path = os.path.join(LOOT_DIR, file_name)
        size = os.path.getsize(file_path)
        
        # تصنيف الأهمية بناءً على نوع الملف
        priority = "Low"
        if any(x in file_name for x in [".env", "config", "sql"]):
            priority = "High 🔥"
        
        asset = {
            "domain": file_name.split("_")[0],
            "file": file_name,
            "size_kb": round(size / 1024, 2),
            "priority": priority,
            "status": "Ready for Sale"
        }
        catalog["assets"].append(asset)

    with open(CATALOG_FILE, "w") as f:
        json.dump(catalog, f, indent=4)
    
    print(f"✅ Catalog Generated with {len(catalog['assets'])} items.")
    print(f"📂 Location: {CATALOG_FILE}")

if __name__ == "__main__":
    generate_catalog()
