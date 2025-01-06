from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Initialize Flask app
app = Flask(__name__)

# Load model and tokenizer
model_name = "Milan97/autotrain-9ikup-ih7yd"  # Replace with your model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Define label mapping
labels = {0: "notClickBait", 1: "clickBait"}  # Adjust for your use case

@app.route('/classify', methods=['POST'])
def classify_text():
    try:
        # Get input data from the request
        data = request.json
        text = data.get("text", None)

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Tokenize input text
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

        # Perform inference
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_class = torch.argmax(logits, dim=1).item()
            confidence = torch.softmax(logits, dim=1).max().item()

        # Return response
        return jsonify({
            "text": text,
            "label": labels[predicted_class],
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)