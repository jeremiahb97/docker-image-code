from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "It works!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # ✅ dynamic and Cloud Run–friendly
    app.run(host="0.0.0.0", port=port)
