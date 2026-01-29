import re, os

def extract_all():
    # الأنماط الجينية للبيانات
    phone_pattern = r'\+?[0-9]{10,15}'
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    files_to_scan = ['FINAL_BANKING_AUCTION.txt', 'FINAL_TECH_EXCHANGE.txt', 'IMPERIAL_KNOWLEDGE_BASE.txt']
    
    phones = set()
    emails = set()

    print("\033[1;33m[🚜] HARVESTING EVERY BIT OF DATA...\033[0m")

    for file in files_to_scan:
        if os.path.exists(file):
            with open(file, 'r', errors='ignore') as f:
                content = f.read()
                phones.update(re.findall(phone_pattern, content))
                emails.update(re.findall(email_pattern, content))

    # حفظ النتائج في "خزائن" منفصلة
    with open('PURE_GOLD_PHONES.txt', 'w') as pf:
        pf.write('\n'.join(phones))
    with open('PURE_GOLD_EMAILS.txt', 'w') as ef:
        ef.write('\n'.join(emails))

    print(f"\033[1;32m[💎] HARVEST COMPLETE!")
    print(f"📱 Unique Phones Extracted: {len(phones)}")
    print(f"📧 Unique Emails Extracted: {len(emails)}\033[0m")

extract_all()
