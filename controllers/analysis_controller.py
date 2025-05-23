from flask import request, jsonify
from services.nlp_service import analyze_text

def analyze():
    data = request.json
    text = data.get("text")

    if not text:
        return jsonify({"error": "Texto não fornecido"}), 400

    result = analyze_text(text)
    return jsonify(result)
