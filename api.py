# api.py

from flask import Flask, request, jsonify
from core.detector import analyze_link
from core.auto_block import take_action
from core.predictive import predict_threat

app = Flask(__name__)

@app.route("/scan", methods=["POST"])
def scan():
    data = request.json
    link = data.get("link")

    result = analyze_link(link)
    action = take_action(result, link)
    prediction = predict_threat(link)

    return jsonify({
        "result": result,
        "action": action,
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(port=5001)
