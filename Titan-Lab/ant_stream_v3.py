import os, subprocess, time

def ant_pumping():
    print("[🐜] Ant Technology: Syncing 27% Achievement...")
    while True:
        try:
            status = subprocess.check_output(["git", "status", "--porcelain"]).decode()
            if status:
                print("[💎] New Instagram & Google Gold detected! Pumping...")
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", "CodeHub: 27 Percent Sovereignty"], check=True)
                subprocess.run(["git", "push", "origin", "main"], check=True)
                print("[✅] Sync Complete. The Galaxy is ours.")
            else:
                pass
        except Exception:
            pass
        time.sleep(3)

if __name__ == "__main__":
    ant_pumping()
