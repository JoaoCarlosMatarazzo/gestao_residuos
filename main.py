import os
from services.api import app

if __name__ == "__main__":
    os.system("python sensors/sensor_simulator.py &")  # Executa o simulador em paralelo
    app.run(debug=True)
