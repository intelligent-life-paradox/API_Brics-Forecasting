import joblib
import os
import pandas as pd

MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')

def load_model(country: str, algorithm: str):
    """
    Carrega um modelo específico com base no país e algoritmo.
    """
    file_name = f"{country}_{algorithm}_final.pkl".replace(" ", "_")
    file_path = os.path.join(MODEL_DIR, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Model not found: {file_name}")

    return joblib.load(file_path)

def predict_weighted_average(country: str, features: dict):
    """
    Carrega dois modelos (XGBoost e GradientBoosting) e retorna a média das previsões.
    """
    algorithms = ["XGBoost", "GradientBoosting"]
    predictions = []

    df = pd.DataFrame([features])  # Transforma em DataFrame para ambos os modelos

    for algo in algorithms:
        model = load_model(country, algo)
        pred = model.predict(df)[0]
        predictions.append(pred)

    # Média simples (poderíamos aplicar pesos, ex: 0.6 e 0.4)
    avg = sum(predictions) / len(predictions)
    return avg
