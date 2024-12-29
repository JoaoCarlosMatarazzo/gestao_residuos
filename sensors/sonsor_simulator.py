import random
import json
import time

def generate_sensor_data(num_bins=10):
    sensor_data = []
    for bin_id in range(1, num_bins + 1):
        sensor_data.append({
            "bin_id": bin_id,
            "level": random.randint(0, 100),  # 0 to 100% full
            "last_updated": time.time()
        })
    return sensor_data

def save_sensor_data_to_file(data, file_path="data/sensor_data.json"):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    while True:
        data = generate_sensor_data()
        save_sensor_data_to_file(data)
        print(f"Sensor data updated at {time.ctime()}")
        time.sleep(60)  # Update every minute
