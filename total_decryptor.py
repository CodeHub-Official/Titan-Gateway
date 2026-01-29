import os, re, zlib, base64

def deep_crack():
    vault_paths = [os.path.expanduser('~/TITAN_HEADQUARTERS'), os.path.expanduser('~/Titan-Lab')]
    
    # محرك الاستخراج العميق
    patterns = {
        'API_Keys': r'(?i)(api[_-]?key|secret|token)[^a-zA-Z0-9]([a-zA-Z0-9]{32,})',
        'IBAN_Accounts': r'[A-Z]{2}\d{2}[A-Z0-9]{11,30}',
        'Private_Keys': r'-----BEGIN [A-Z ]+ PRIVATE KEY-----',
        'Endpoints': r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s\续]*'
    }

    print("\033[1;31m[🌪️] LAUNCHING TOTAL DECRYPTION ENGINE...\033[0m")

    for v_path in vault_paths:
        for root, dirs, files in os.walk(v_path):
            for file in files:
                f_path = os.path.join(root, file)
                if file.endswith(('.py', '.txt', '.log', '.titan', '.codehub', '.gz')):
                    print(f"\n\033[1;34m[🔓] Deep Scanning: {file}\033[0m")
                    try:
                        with open(f_path, 'rb') as f:
                            data = f.read()
                        
                        # محاولة فك الضغط إذا كان الملف مضغوطاً (Gzip)
                        try: 
                            content = zlib.decompress(data, 16+zlib.MAX_WBITS).decode('utf-8', errors='ignore')
                            print(f"  \033[1;32m[!] Gzip Compression Cracked!\033[0m")
                        except:
                            content = data.decode('utf-8', errors='ignore')

                        # التنقيب عن الكنوز (IBANs, Keys, Endpoints)
                        for label, pattern in patterns.items():
                            matches = re.findall(pattern, content)
                            if matches:
                                print(f"  \033[1;33m[+] Found {len(matches)} {label}\033[0m")
                                # تغذية الوحش فوراً بالنتائج
                                with open('IMPERIAL_KNOWLEDGE_BASE.txt', 'a') as kb:
                                    for m in matches: kb.write(f"TYPE:{label} | DATA:{m}\n")
                                    
                    except Exception as e:
                        continue

deep_crack()
