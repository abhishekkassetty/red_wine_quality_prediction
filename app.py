from flask import Flask,render_template,url_for,request,jsonify
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

file_name = "model_classification.pkl"
load_model = pickle.load(open("model/"+file_name,"rb"))
classification_predictions = load_model

file_name1 = "model_regression.pkl"
load_model = pickle.load(open("model/"+file_name1,"rb"))
regression_predictions = load_model

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods = ["POST"])
def predict():

    data = [request.form['fixed acidity'],
            request.form['volatile acidity'],
            request.form['citric acid'],
            request.form['residual sugar'],
            request.form['chlorides'],
            request.form['free sulfur dioxide'],
            request.form['total sulfur dioxide'],
            request.form['density'],
            request.form['pH'],
            request.form['sulphates'],
            request.form['alcohol']
        ]

    print(data)
    data = np.array([np.asarray(data)],dtype=float)
    print(data)
    pred_regression = regression_predictions.predict(data)

    if classification_predictions.predict(data) == 0:
        pred_classification = "NOT GOOD"
    else:
        pred_classification = "GOOD"



    return render_template('index.html' , pred_c  = pred_classification, pred_r = pred_regression)




if __name__=="__main__":
    app.run(debug=True)
