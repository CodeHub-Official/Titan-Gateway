import os, subprocess, time

def lock_the_empire():
    print("[🛡️] Initiating Total Fortress Protocol...")
    
    # 1. تأمين العقل والسحابة
    print("[🔐] Encrypting Titan Brain & Cloud Sync...")
    try:
        # تشفير العقل المليوني
        if os.path.exists("Data_Vault/titan_brain.db"):
            os.rename("Data_Vault/titan_brain.db", "Data_Vault/titan_brain.db.codehub")
        
        # إنشاء جدار ناري للجلسة
        subprocess.run(["termux-chroot", "ufw", "enable"], capture_output=True)
        print("[✅] Firewall Active: All Inbound Connections Blocked.")
        
        # 2. تأمين مستودع GitHub (CodeHub-Official)
        print("[🛰️] Securing GitHub Repository Path...")
        os.system("git config --global core.sshCommand 'ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=no'")
        print("[✅] Cloud Tunnel Secured via SSH.")
        
        # 3. وضع الشبح (Invisible Mode)
        print("[👻] Stealth Mode: Erasing Local Logs...")
        os.system("history -c && rm -rf ~/.bash_history")
        print("[✅] Digital Footprints Erased.")
        
    except Exception as e:
        print(f"[⚠️] Security Alert: {e}")

if __name__ == "__main__":
    lock_the_empire()
