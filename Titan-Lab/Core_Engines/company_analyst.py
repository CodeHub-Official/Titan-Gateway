import os, time

def analyze_gold():
    print("🚀 CodeHub Data Miner: Extracting Business Intelligence...")
    tunnels_file = "/data/data/com.termux/files/home/Titan-Lab/Data_Vault/codehub_tunnels.log"
    if os.path.exists(tunnels_file):
        with open(tunnels_file, "r") as f:
            lines = f.readlines()
            print(f"📊 Total Targets Captured: {len(lines)}")
            for line in lines[-5:]: # عرض آخر 5 صيدات
                print(f"💎 Found Potential Client: {line.strip()}")
    else:
        print("⏳ Waiting for the Infiltrator to bring gold...")

if __name__ == "__main__":
    while True:
        os.system('clear')
        analyze_gold()
        time.sleep(30)
