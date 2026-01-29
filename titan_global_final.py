from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# محفظتك لاستقبال الأرباح (يتم تغييرها لمحفظتك الحقيقية)
MY_WALLET = "bc1qvvda5vuas24ervsvd7m6gn7ts975re7uzlzl48" 

@app.route('/pay')
def payment_gateway():
    order_id = str(uuid.uuid4())[:8]
    return f"""
    <div style="background:#000; color:#0f0; padding:20px; border:1px solid #0f0;">
        <h3>Secure Checkout</h3>
        <p>Order ID: {order_id}</p>
        <p>Send 500 USDT to: <b>{MY_WALLET}</b></p>
        <p style="color:red;">[Waiting for Blockchain Confirmation...]</p>
    </div>
    """

if __name__ == "__main__":
    # تشغيل على بورت دولي بتمويه عالٍ
    app.run(host='0.0.0.0', port=8888)
