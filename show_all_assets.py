import os

def scan_realty():
    paths = [
        '~/Titan-Lab/Empire_Archive/Egypt/Real_Estate',
        '~/Titan-Lab/Empire_Archive/UAE/Real_Estate',
        '~/Titan-Lab/Empire_Archive/KSA/Real_Estate'
    ]
    all_contacts = []
    print("\033[1;33m[🕵️] SCANNING REAL ESTATE DATA SOURCES...\033[0m")
    
    for p in paths:
        full_p = os.path.expanduser(p)
        if os.path.exists(full_p):
            for file in os.listdir(full_p):
                with open(os.path.join(full_p, file), 'r', errors='ignore') as f:
                    lines = f.readlines()
                    for line in lines:
                        if len(line.strip()) > 5: # تجنب السطور الفارغة
                            all_contacts.append(f"[{p.split('/')[-2]}] {line.strip()}")
    
    # عرض أول 50 رقم كعينة قوية
    print(f"\n\033[1;32m[🎯] TOTAL NUMBERS FOUND: {len(all_contacts)}\033[0m")
    print("\033[1;36m--- PREVIEWING TOP 50 ENTRIES FOR AUCTION ---\033[0m")
    for contact in all_contacts[:50]:
        print(contact)
    
    if len(all_contacts) > 50:
        print(f"\n\033[1;33m... and {len(all_contacts)-50} more entries ready in the vault.\033[0m")

scan_realty()
