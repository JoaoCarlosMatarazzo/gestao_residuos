import numpy as np
from sklearn.linear_model import LinearRegression
import json
from datetime import datetime, timedelta

# Função para carregar dados de sensores
def load_sensor_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Função para prever os níveis de resíduos futuros
def predict_full_bins(sensor_data, threshold=90):
    """
    Prever quais lixeiras ultrapassarão o nível de resíduos especificado.

    Args:
        sensor_data (list): Dados atuais das lixeiras.
        threshold (int): Nível de preenchimento considerado como cheio.

    Returns:
        list: Lista de lixeiras que estarão cheias em breve.
    """
    full_bins = []

    # Preparar dados para o modelo de previsão
    for bin_data in sensor_data:
        bin_id = bin_data["bin_id"]
        level = bin_data["level"]
        last_updated = datetime.strptime(bin_data["last_updated"], "%Y-%m-%dT%H:%M:%S")

        # Simular dados históricos baseados no nível atual (mock)
        timestamps = [last_updated - timedelta(hours=i) for i in range(5, 0, -1)]
        levels = [level - i * 5 if level - i * 5 > 0 else 0 for i in range(5)]

        # Converter para formato numpy para o modelo
        X = np.array([(ts - timestamps[0]).total_seconds() / 3600 for ts in timestamps]).reshape(-1, 1)
        y = np.array(levels).reshape(-1, 1)

        # Treinar o modelo de regressão linear
        model = LinearRegression()
        model.fit(X, y)

        # Prever o nível nas próximas 6 horas
        future_time = np.array([(6 * 3600) / 3600]).reshape(-1, 1)
        predicted_level = model.predict(future_time)[0][0]

        # Verificar se o nível ultrapassará o limite
        if predicted_level >= threshold:
            full_bins.append(bin_id)

    return full_bins

# Função principal para previsão
if __name__ == "__main__":
    # Carregar dados dos sensores
    sensor_data_path = "data/sensor_data.json"
    sensor_data = load_sensor_data(sensor_data_path)

    # Prever lixeiras que estarão cheias em breve
    bins_to_empty = predict_full_bins(sensor_data)

    # Exibir resultados
    if bins_to_empty:
        print(f"As seguintes lixeiras precisarão ser esvaziadas em breve: {bins_to_empty}")
    else:
        print("Nenhuma lixeira está prevista para encher em breve.")
