from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CODE HUB | TITAN SYSTEM</title>
        <style>
            body { background-color: #0a0a0a; color: #00ff41; font-family: 'Courier New', monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }
            .container { text-align: center; border: 1px solid #00ff41; padding: 40px; border-radius: 10px; box-shadow: 0 0 20px #00ff41; background: rgba(0, 255, 65, 0.05); }
            h1 { font-size: 3rem; text-shadow: 0 0 10px #00ff41; margin-bottom: 10px; }
            p { font-size: 1.2rem; color: #fff; }
            .status { margin-top: 20px; font-weight: bold; animation: blink 1s infinite; }
            @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
            .btn { margin-top: 30px; display: inline-block; padding: 10px 20px; border: 1px solid #00ff41; color: #00ff41; text-decoration: none; transition: 0.5s; }
            .btn:hover { background: #00ff41; color: #000; box-shadow: 0 0 20px #00ff41; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>CODE HUB</h1>
            <p>Sovereign Security & Data Intelligence</p>
            <div class="status">● SYSTEM: OPERATIONAL</div>
            <a href="#" class="btn">ENTER COMMAND CENTER</a>
        </div>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run()
