import os, subprocess, time

def secure_push():
    print("[🛡️] CodeHub Steel Pump: Online & Active")
    print("[🛰️] Tunnel Status: Encrypted SSH Enabled")
    
    while True:
        try:
            # التحقق من وجود "ذهب" جديد لم يرفع بعد
            check = subprocess.check_output(["git", "status", "--porcelain"]).decode()
            if check:
                print("[💎] Ant Army captured new data! Syncing to Cloud...")
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", "Empire Sync: Continuous Flow"], check=True)
                # الرفع عبر النفق الآمن
                subprocess.run(["git", "push", "origin", "main"], check=True)
                print("[✅] Vault Updated Successfully.")
            else:
                pass 
        except Exception as e:
            print(f"[⚠️] Waiting for Handshake: {e}")
        
        time.sleep(5) # فحص كل 5 ثواني لضمان التدفق

if __name__ == "__main__":
    secure_push()
