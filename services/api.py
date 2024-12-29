from flask import Flask, jsonify
from data_processing import bins_to_empty
from models.optimization import optimize_route

app = Flask(__name__)

@app.route("/bins")
def get_bins():
    bins = bins_to_empty()
    return jsonify(bins)

@app.route("/optimize-route")
def get_optimized_route():
    bins = bins_to_empty()
    route, distance = optimize_route(bins, "data/city_map.json")
    return jsonify({"route": route, "distance": distance})

if __name__ == "__main__":
    app.run(debug=True)
