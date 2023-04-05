from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        myGender=request.form['Gender'] 
        myPI = request.form['ParentIncome']
        myIQ = request.form['IQ']
        myPE = request.form['ParentEncouragement']
        model = load('app/CollegeAttend.joblib')
        np_arr = np.array([myGender,myPI, myIQ,myPE])
        predictions = model.predict([np_arr])  
        predictions_to_str = str(predictions)
        #return predictions_to_str
        return render_template('index.html', href2='The suggestion for you (Gender:'+str(myGender)+'Parent Income: '+str(myPI)+'IQ :'+str(myIQ)+'Parent Encouragement:'+str(myPE)+') is:'+predictions_to_str)

