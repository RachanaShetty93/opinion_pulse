from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)

# Allow your frontend (Live Server: 127.0.0.1:5500 / localhost:5500) to call this API
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500", "http://localhost:5500"]}})

CORS(app, resources={r"/*": {"origins": "*"}})

# Load saved model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer .pkl')

@app.route('/', methods=['GET'])
def home():
    return "Sentiment Analysis API is running!"

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    # Handle preflight (browser sends this automatically)
    if request.method == 'OPTIONS':
        return ('', 204)

    if not request.is_json:
        return jsonify({"error": "Request must be application/json"}), 415

    data = request.get_json(silent=True) or {}
    text = data.get('text', '').strip()
    if not text:
        return jsonify({"error": "Field 'text' is required"}), 400

    # Vectorize and predict
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    sentiment = "Positive" if pred == 1 else "Negative"

    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
