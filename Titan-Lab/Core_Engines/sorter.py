import os, re

def organize_leads():
    # إنشاء المجلدات لو مش موجودة
    folders = ['Real_Estate_Leads', 'Business_Leads']
    for folder in folders:
        if not os.path.exists(folder): os.makedirs(folder)

    # الملف اللي فيه مخرجات تايتان (titan_out.txt)
    if not os.path.exists('titan_out.txt'):
        print("!! الملف لسه مكنش فيه داتا !!")
        return

    with open('titan_out.txt', 'r') as f:
        content = f.read()
        
    # نملة التصنيف العقاري
    re_patterns = ['nakheel', 'emaar', 'aldar', 'property', 'realestate', 'meraas', 'عقارات']
    
    blocks = content.split('💎 DEEP GOLD FOUND')
    for block in blocks:
        if not block.strip(): continue
        
        is_re = any(kw in block.lower() for kw in re_patterns)
        target_folder = 'Real_Estate_Leads' if is_re else 'Business_Leads'
        
        # استخراج واتساب
        phones = re.findall(r'wa.me/(\d+)', block)
        # استخراج إيميلات
        emails = re.findall(r'📧: ([\w\.-]+@[\w\.-]+)', block)
        
        with open(f"{target_folder}/clean_list.txt", "a") as out:
            for p in phones: out.write(f"WhatsApp: https://wa.me/{p}\n")
            for e in emails: out.write(f"Email: {e}\n")
            out.write("-" * 20 + "\n")

    print("✅ تم تنظيم الـ 50 شركة في المجلدات يا شريكي.")

if __name__ == "__main__":
    organize_leads()
