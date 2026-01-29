import os, re

def ant_army():
    root_path = os.path.expanduser('~/')
    targets = ['Titan-Lab', 'TITAN_HEADQUARTERS']
    patterns = {
        'Phone': r'\+?\d{10,15}',
        'Email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        'Database': r'\.db$|\.sql$|\.titan$'
    }
    
    results = {'Phones': 0, 'Emails': 0, 'Files': 0, 'Total_Size_MB': 0}
    
    print("\033[1;35m[🐜] ANT ARMY RELEASED... DEEP MINING IN PROGRESS...\033[0m")
    
    for target in targets:
        for root, dirs, files in os.walk(os.path.join(root_path, target)):
            for file in files:
                results['Files'] += 1
                file_path = os.path.join(root, file)
                results['Total_Size_MB'] += os.path.getsize(file_path) / (1024*1024)
                
                # قراءة الملفات بعمق (حتى الثنائية منها)
                try:
                    with open(file_path, 'r', errors='ignore') as f:
                        content = f.read()
                        results['Phones'] += len(re.findall(patterns['Phone'], content))
                        results['Emails'] += len(re.findall(patterns['Email'], content))
                except:
                    continue

    print("\n\033[1;32m[🏆] SCAN COMPLETE: THE TREASURE REVEALED\033[0m")
    print(f"-------------------------------------------")
    print(f"📦 Total Files Scanned: {results['Files']}")
    print(f"💾 Total Data Size:     {results['Total_Size_MB']:.2f} MB")
    print(f"📱 Potential Numbers:   {results['Phones']}")
    print(f"📧 Potential Emails:    {results['Emails']}")
    print(f"-------------------------------------------")
    
    # تقدير القيمة
    value = (results['Phones'] * 5) + (results['Emails'] * 1)
    print(f"\033[1;33m[💰] ESTIMATED BLACK-MARKET VALUE: ${value:,}\033[0m")

ant_army()
