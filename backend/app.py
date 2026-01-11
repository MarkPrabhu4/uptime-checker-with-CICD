from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/health", methods=["POST"])
def check_health():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        response = requests.get(url, timeout=5)
        return jsonify({
            "url": url,
            "status_code": response.status_code,
            "status": "UP" if response.status_code == 200 else "DOWN"
        })
    except requests.exceptions.RequestException:
        return jsonify({
            "url": url,
            "status": "DOWN",
            "error": "Request failed"
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
