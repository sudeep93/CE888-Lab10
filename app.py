# This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
import pickle
# import logging
# from logging import Formatter, FileHandler

# import pandas as pd
# log.Fatal(http.ListenAndServe(":" + os.Getenv("PORT"), router))
print("Test")
print("Test 2")
print(os.getcwd())
path = os.getcwd()

# object = pd.read_pickle(r'/Users/abhaymamadapur/Desktop/CE888-Lab10-master/Models/Pickle_RF_Model.pkl')
with open('./Models/Pickle_RF_Model.pkl', 'rb') as f:
    test = pickle.load(f)
#
# Index(['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
#        'exang', 'oldpeak', 'slope', 'ca', 'thal'],
# print("jsnjnj")


def get_predictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    mylist = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

    return test.predict(vals)[0]


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['Chest_Pain_Type']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['Fasting_Blood_Sugar']
        restecg = request.form['ECG_Results']
        thalach = request.form['thalach']
        exang = request.form['Exercise_induced_agine']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']

        target = get_predictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

        if target == 1:
            heart_disease = 'Heart Disease Present'
        else:
            heart_disease = 'Heart Disease Absent'

        return render_template('home.html', target=target, heart_disease=heart_disease)
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run()
