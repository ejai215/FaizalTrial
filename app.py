# -*- coding: utf-8 -*-
#"""
#Created on Mon Aug  3 21:11:12 2020
#
#@author: pattn
#"""


# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
from flask import Flask, request, render_template
import pickle

app = Flask("__name__")



q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/predict", methods=['POST'])
def predict():
    
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']


    model = pickle.load(open("PumpStatusModel.pkl", "rb"))
    
    
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5]]
    new_df = pd.DataFrame(data, columns = ['mean', 'max', 'kurtosis', 'variance','onenorm'])
    
    single = model.predict(new_df)
    probablity = model.predict_proba(new_df)[:,0]
    
    if single==0:
        o1 = "The pump status is health"
        o2 = "Confidence: {}".format(probablity*100)
    elif single==1:
        o1 = "The pump status is severe"
        o2 = "Confidence: {}".format(probablity*100)
    elif single==2:
        o1 = "The pump status is mild"
        o2 = "Confidence: {}".format(probablity*100)
    else:
        o1 = "The pump status is mild2"
        o2 = "Confidence: {}".format(probablity*100)
        
    return render_template('home.html', output1=o1, output2=o2, query1 = request.form['query1'], query2 = request.form['query2'],query3 = request.form['query3'],query4 = request.form['query4'],query5 = request.form['query5'])
    
if __name__ == "__main__":
    app.run()
