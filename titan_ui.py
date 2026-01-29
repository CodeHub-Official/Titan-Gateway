from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# واجهة مستوحاة من أنظمة Google Cloud المركزية
HTML_UI = """
<body style="background:#0a0a0a; color:#00ff00; font-family:monospace; padding:20px;">
    <h2>👑 TITAN CORE: SOVEREIGN INTERFACE</h2>
    <div id="chat" style="border:1px solid #333; height:300px; overflow-y:scroll; padding:10px; background:#000;">
        <p>[SYSTEM]: النواة جاهزة. ليفل الذكاء: 9.4</p>
    </div>
    <input type="text" id="cmd" style="width:80%; background:#000; color:#00ff00; border:1px solid #00ff00; padding:10px; margin-top:10px;" placeholder="اطلب من الوحش...">
    <button onclick="send()" style="padding:10px; background:#00ff00; color:#000; border:none; cursor:pointer;">إرسال</button>
    <script>
        function send() {
            let cmd = document.getElementById('cmd').value;
            document.getElementById('chat').innerHTML += '<p style="color:#fff;">[YOU]: ' + cmd + '</p>';
            // هنا يتم الربط مع النواة لاحقاً
        }
    </script>
</body>
"""

@app.route('/')
def index(): return render_template_string(HTML_UI)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
