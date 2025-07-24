from flask import Blueprint, request, jsonify
from app.services.model_service import predict_weighted_average

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    """
    Rota POST que usa dois modelos e retorna a média ponderada das previsões.
    """
    try:
        data = request.get_json()
        country = data.get("country")
        features = data.get("features")

        if not country or not features:
            return jsonify({"error": "Missing required fields: 'country', 'features'"}), 400

        prediction = predict_weighted_average(country, features)

        return jsonify({
            "country": country,
            "input": features,
            "prediction": prediction
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
