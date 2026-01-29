from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <body style="background:#0a0a0a;color:#00ff41;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;">
        <div style="text-align:center;border:1px solid #00ff41;padding:40px;box-shadow:0 0 20px #00ff41;border-radius:15px;">
            <h1 style="font-size:2.5rem;text-shadow: 0 0 10px #00ff41;">CODE HUB</h1>
            <p style="color:#fff;font-size:1.2rem;">SYSTEM OPERATIONAL: SECURE</p>
            <div style="margin-top:20px;font-weight:bold;color:#00ff41;animation:blink 1.5s infinite;">● LINK ESTABLISHED</div>
        </div>
        <style>@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.2; } }</style>
    </body>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
