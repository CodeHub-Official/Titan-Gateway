import time
import os

def display_dashboard():
    print("🎮 [CODEHUB] - TITAN CONTROL PANEL (CP-1)")
    print("========================================")
    print("🔥 [LIVE ACTIVITY]: MONITORING TARGETS...")
    
    # محاكاة عرض الهجمات الحية من ملفات الـ Loot والـ Logs
    try:
        with open("maestro.log", "r") as f:
            lines = f.readlines()
            for line in lines[-5:]:
                print(f"📡 [ATTACK]: {line.strip()}")
    except:
        print("🛰️ [STATUS]: STEALTH TUNNEL OPERATING AT 100%")

    print("\n💰 [VAULT STATUS]: READY FOR BATCH_001")
    print("🛡️ [SHIELD]: GUARD DOG IS ACTIVE")
    print("========================================")

if __name__ == "__main__":
    while True:
        os.system('clear')
        display_dashboard()
        time.sleep(5)
