from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os


# Load model
with open("linear_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Flask PKL API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    x_val = data.get("x")
    if x_val is None:
        return jsonify({"error": "Missing 'x' value"}), 400

    prediction = model.predict(np.array([[x_val]]))
    return jsonify({"predicted_y": float(prediction[0][0]), "x": x_val})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Dynamic port for Railway
    app.run(host="0.0.0.0", port=port, debug=True)
