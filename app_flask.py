# app_flask.py
from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load model
with open("linear_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    x_val = data.get("x")
    if x_val is None:
        return jsonify({"error": "Missing 'x' value"}), 400

    prediction = model.predict(np.array([[x_val]]))
    return jsonify({"predicted_y": float(prediction[0][0]), "x": x_val})

if __name__ == "__main__":
    app.run(debug=True)
