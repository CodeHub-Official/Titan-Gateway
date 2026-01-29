from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

def get_real_stats():
    # النمل بيعد الـ IPs الفريدة اللي حاولت تدخل
    try:
        ips = subprocess.getoutput("netstat -tnpa | grep 'python3' | awk '{print $5}' | cut -d: -f1 | sort | uniq | wc -l")
        last_ip = subprocess.getoutput("netstat -tnpa | grep 'python3' | awk '{print $5}' | tail -n 1")
        return {"visitors": ips, "last_geo": last_ip, "sales": "0 (Waiting BTC)"}
    except:
        return {"visitors": "Scanning...", "last_geo": "N/A", "sales": "0"}

@app.route('/dashboard')
def dashboard():
    stats = get_real_stats()
    return f"""
    <body style="background:#000; color:#0f0; font-family:monospace; padding:30px;">
        <h1 style="border-bottom:2px solid #0f0;">🛰️ TITAN REAL-TIME MONITOR</h1>
        <div style="display:flex; gap:20px;">
            <div style="border:1px solid #0f0; padding:20px; flex:1;">
                <h3>ACTIVE CONNECTIONS</h3>
                <p style="font-size:40px;">{stats['visitors']}</p>
                <p>Latest Connection from: <span style="color:white;">{stats['last_geo']}</span></p>
            </div>
            <div style="border:1px solid #f00; padding:20px; flex:1;">
                <h3>WALLET STATUS (BTC)</h3>
                <p style="font-size:40px; color:#f00;">{stats['sales']}</p>
                <p>Target: bc1q...zl48</p>
            </div>
        </div>
        <div style="margin-top:20px; background:#111; padding:10px;">
            <marquee>Ants are verifying blockchain confirmations... Marketing bots active in Panama forums...</marquee>
        </div>
    </body>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
