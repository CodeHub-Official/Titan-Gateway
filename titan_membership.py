from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CODE HUB | SOVEREIGN SHIELD</title>
        <style>
            body { background: #050505; color: #e0e0e0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }
            .container { background: rgba(20, 20, 20, 0.8); backdrop-filter: blur(10px); border: 1px solid rgba(0, 255, 127, 0.2); padding: 40px; border-radius: 20px; box-shadow: 0 0 50px rgba(0, 255, 127, 0.1); text-align: center; max-width: 500px; width: 90%; }
            h1 { color: #00ff7f; letter-spacing: 5px; text-transform: uppercase; font-size: 1.5rem; margin-bottom: 10px; }
            .status-bar { background: #111; padding: 10px; border-radius: 10px; margin: 20px 0; border-left: 4px solid #00ff7f; font-size: 0.8rem; }
            .pulse { animation: pulse-animation 2s infinite; color: #00ff7f; font-weight: bold; }
            @keyframes pulse-animation { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
            .btn { background: #00ff7f; color: #000; border: none; padding: 15px 30px; border-radius: 30px; font-weight: bold; cursor: pointer; transition: 0.3s; text-decoration: none; display: inline-block; margin-top: 20px; }
            .btn:hover { background: #fff; transform: scale(1.05); }
            .footer { margin-top: 30px; font-size: 0.7rem; color: #555; letter-spacing: 2px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>CODE HUB</h1>
            <p style="color: #888;">Titan AI Security Nucleus</p>
            <div class="status-bar">
                SYSTEM STATUS: <span class="pulse">ONLINE & DEFENDING</span><br>
                <small>Ant-Army Active Nodes: 4,102</small>
            </div>
            <p>Our autonomous intelligence has detected a vulnerability in your infrastructure. Secure your assets immediately.</p>
            <a href="#" class="btn">REQUEST SECURITY AUDIT</a>
            <div class="footer">POWERED BY TITAN SOVEREIGN SYSTEMS © 2026</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
