# Stress Text Classifier

A small Flask application for testing a trained text-classification model. Enter text in the browser interface to receive the model's prediction.

## Requirements

- Python 3.9 or newer
- The packages listed in `requirements.txt`
- The trained model file `stress_model.pkl` in the project root

The model is loaded when the application starts. Keep the scikit-learn version compatible with the version used to create the model file.

## Setup

From the project directory, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

```powershell
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Prediction endpoint

`POST /predict` accepts form data with a `text` field and returns JSON:

```json
{"prediction": "model output"}
```

An empty or whitespace-only `text` field returns HTTP 400 with a JSON error message.

> **Note:** This project is for model experimentation only. Predictions are not a clinical assessment or diagnosis. Only load model files from trusted sources; Python pickle files can execute code when loaded.
