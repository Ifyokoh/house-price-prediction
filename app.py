from flask import Flask, request, render_template
import pickle
import numpy as np
import json


#loading model from file
model = pickle.load(open('model.pkl', 'rb'))


app = Flask(__name__)


def process_input(request_data: str) -> np.array:
    # a processing function to transform the inputs to expected format
    return np.asarray(json.loads(request.data)["inputs"])


@app.route('/')
def home():
    return render_template('home.html')



@app.route("/predict", methods = ['POST'])
def predict() -> str:
    try:
        input_params = process_input(request.data)
        prediction = model.predict(input_params)
        return json.dumps({"predicted_price": prediction.tolist()})
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 400

    

if __name__ == "__main__":
    app.run(debug=True)