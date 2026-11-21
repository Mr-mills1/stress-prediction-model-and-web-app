# build an interface for model testing
# import the necessary libraries
from flask import Flask, request, jsonify, render_template
import pickle
from pathlib import Path

# load the model
with (Path(__file__).resolve().parent / 'stress_model.pkl').open('rb') as f:
    model = pickle.load(f)

# create the flask app
app = Flask(__name__)

# define the home route
@app.route('/')
def home():
    return render_template('index.html')

# define the predict route
@app.route('/predict', methods=['POST'])
def predict():
    # get the input data from the request
    text = request.form.get('text', '').strip()
    if not text:
        return jsonify({'error': 'Please enter some text to analyze.'}), 400

    # make a prediction using the model
    prediction = model.predict([text])[0]

    # return the prediction as a JSON response
    return jsonify({'prediction': str(prediction)})

# run the app
if __name__ == '__main__':
    app.run(debug=True)