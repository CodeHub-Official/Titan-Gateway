from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <body style="background:#0a0a0a;color:#00ff41;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;">
        <div style="text-align:center;border:1px solid #00ff41;padding:40px;box-shadow:0 0 20px #00ff41;">
            <h1>CODE HUB | TITAN SYSTEM</h1>
            <p style="color:#fff;">Sovereign Lab - Operational</p>
            <div style="margin-top:20px;font-weight:bold;animation:blink 1s infinite;">● SYSTEM: ONLINE</div>
        </div>
        <style>@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }</style>
    </body>
    ''')

# التعديل الجوهري لـ Vercel
main = app

if __name__ == "__main__":
    app.run()
