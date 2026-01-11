from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5000/health"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form.get("url")
        try:
            response = requests.post(BACKEND_URL, json={"url": url})
            result = response.json()
        except Exception:
            result = {"status": "DOWN", "error": "Backend not reachable"}
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
