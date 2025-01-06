# CBD: Clickbait Detective

**CBD (Clickbait Detective)** is a Python-based project that uses a custom-trained transformer model to classify text titles as **clickbait** or **not clickbait**. This project leverages Hugging Face's `transformers` library and provides a Flask-based API for easy integration into other applications.

---

## Features

- **Custom Model**: Trained specifically for detecting clickbait titles using a dataset curated for this purpose.
- **API Integration**: Exposes the model through a REST API for easy interaction.
- **Confidence Score**: Returns the classification result along with a confidence score.
- **Docker Support**: Fully containerized for seamless deployment.

---

## Model Details

The model used in this project is fine-tuned from a pre-trained transformer model using Hugging Face AutoTrain.

- **Model Repository**: [Clickbait Detection Model](https://huggingface.co/Milan97/ClickbaitDetectionModel)
- **Base Model**: [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)
- **Training Metrics**:
    - **Accuracy**: 1.0
    - **F1 Score**: 1.0
    - **Precision**: 1.0
    - **Recall**: 1.0
    - **Loss**: 0.0029

---

## Installation

### Prerequisites
- Python 3.7 or later
- `pip` package manager

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/CBD.git
   cd CBD
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API**
   ```bash
   python app.py
   ```

The API will start at `http://0.0.0.0:5000`.

---

## API Usage

### Endpoint
**POST** `/classify`

### Request Format
Send a JSON object with the text you want to classify:
```json
{
  "text": "You won’t believe what happened next!"
}
```

### Response Format
The API returns the predicted label and confidence score:
```json
{
  "text": "You won’t believe what happened next!",
  "label": "clickBait",
  "confidence": 0.98
}
```

### Example Request
Using `curl`:
```bash
curl -X POST -H "Content-Type: application/json" \\
-d '{"text": "10 Tips to Boost Productivity"}' \\
http://127.0.0.1:5000/classify
```

---

## Docker Deployment

### Build Docker Image
```bash
docker build -t cbd-api .
```

### Run the Container
```bash
docker run -p 5000:5000 cbd-api
```

---

## File Structure

```
CBD/
├── app.py                # Flask application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker setup
└── README.md             # Project documentation
```

---

## How It Works

1. **Input**: The user sends a text (e.g., a title) to the API.
2. **Processing**: The text is tokenized and passed through the model.
3. **Output**: The API returns a classification label (`clickBait` or `notClickBait`) along with a confidence score.

---

## Applications

- **Content Moderation**: Identify and flag clickbait content on platforms.
- **User Experience**: Improve user trust by filtering misleading titles.
- **Social Media Analytics**: Analyze trends in clickbait content.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [Hugging Face](https://huggingface.co) for their powerful transformers library.
- [Sentence Transformers](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) for the base model.