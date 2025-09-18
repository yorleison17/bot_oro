import os
from flask import Flask, request
import requests

app = Flask(__name__)

# Tu token y chat_id directos
TOKEN = "7581025511:AAEdxP8cPlynjkbfeXTDzKz_9JPjSb5MRN4"
CHAT_ID = "8264626126"

@app.route('/')
def home():
    return "🚀 Bot de alertas activo y funcionando desde Render (versión directa)"

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data.get("message", "⚠️ Alerta sin mensaje")
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    
    r = requests.post(url, json=payload)
    return {"status": "ok", "telegram_response": r.json()}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
