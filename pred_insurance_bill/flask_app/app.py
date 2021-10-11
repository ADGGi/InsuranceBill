from flask import Flask, request, url_for, redirect, render_template, jsonify
from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = load_model('lr_model')
cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

@app.route('/')
@app.route('/index')
def index() :
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict() :
    age = request.form.get("age")
    sex = request.form.get("sex")
    bmi = request.form.get("bmi")
    children = request.form.get("children")
    smoker = request.form.get("smoker")
    region = request.form.get("region")
    data = ((age, sex, bmi, children, smoker, region))
    data_1 = np.array(data)
    # feature = [x for x in request.form.values()]
    # feature_1 = [np.array(feature)]
    # prediction = model.predict(feature_1)
    # output = round(prediction[0], 2)
    data_unseen = pd.DataFrame([data_1], columns = cols)
    prediction = predict_model(model, data = data_unseen, round = 0)
    prediction = int(prediction.Label[0])
    return render_template('index.html', prediction_text = 'Predicted Bill will be {}$.'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
