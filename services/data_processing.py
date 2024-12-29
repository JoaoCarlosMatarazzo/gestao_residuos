import json

def load_sensor_data(file_path="data/sensor_data.json"):
    with open(file_path, 'r') as file:
        return json.load(file)

def bins_to_empty(threshold=75):
    data = load_sensor_data()
    return [bin_data for bin_data in data if bin_data['level'] >= threshold]

if __name__ == "__main__":
    bins = bins_to_empty()
    print(f"Lixeiras para esvaziar: {bins}")
