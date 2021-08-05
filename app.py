from flask import Flask, request, render_template
import pickle
import numpy as np
import json
# import requests 


#loading model from file
model = pickle.load(open('model.pkl', 'rb'))


app = Flask(__name__)

# CREATING A PROCESSING FUNCTION TO TRANSFORM INPUTS TO THE 
## EXPECTED FORMAT
def process_input(request_data: str) -> np.array:
    return np.asarray(json.loads(request.data)["inputs"])


@app.route('/')
def home():
    return render_template('home.html')


#creating route for model prediction
@app.route("/predict", methods = ['GET', 'POST'])
def predict() -> str:
    try:
        input_params = process_input(request.data)
        prediction = model.predict(input_params)
        return json.dumps({"predicted_price": prediction.tolist()})
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 400

    

if __name__ == "__main__":
    app.run(debug=True)