import os
import subprocess

def send_alert(message, title="⚠️ TITAN EMERGENCY"):
    try:
        subprocess.run(["termux-notification", "-t", title, "-c", message, "--priority", "high", "--sound"])
    except:
        print(f"ALERT: {message}")

if __name__ == "__main__":
    send_alert("Titan Guard is now patrolling your system.", "🏛️ CODEHUB SECURE")
