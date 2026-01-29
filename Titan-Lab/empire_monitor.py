import time
import os

def monitor_beast():
    print("🖥️ [CODEHUB] - EMPIRE LIVE MONITORING")
    print("📡 SCANNING CHANNELS FOR BATCH_001...")
    
    # تفقد آخر العمليات في سجل المايسترو
    if os.path.exists("maestro.log"):
        with open("maestro.log", "r") as f:
            lines = f.readlines()
            for line in lines[-10:]:
                print(f"🔥 [ACTIVITY]: {line.strip()}")
    else:
        print("🔕 [STATUS]: SILENT BUT ACTIVE. WAITING FOR NEW DATA FLOW.")

if __name__ == "__main__":
    monitor_beast()
