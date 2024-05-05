from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
from pickle import load

myData = pd.read_csv('myData.csv')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('html_template.html')


@app.route('/', methods=["POST"])
def get_details():
    age = request.form['age']
    myData.loc[0,'age'] = int(age)
    Diabetes = request.form['Diabetes']
    diab_val = 'Diabetes_'+Diabetes
    myData.loc[0,diab_val] = 1
    Triglyceride = request.form['Triglyceride']
    tri_val = 'Triglyceride_'+Triglyceride
    myData.loc[0,tri_val] = 1
    hemoglobin_sorted = request.form['hemoglobin']
    hemo_val = 'hemoglobin_sorted_'+hemoglobin_sorted
    myData.loc[0,hemo_val] = 1
    Kidney = request.form['Kidney']
    kid_val = 'Kidney_'+Kidney
    myData.loc[0,kid_val] = 1
    Liver = request.form['Liver']
    liv_val = 'Liver_'+Liver
    myData.loc[0,liv_val] = 1
    myData.fillna(0,inplace=True)
    print(age, Diabetes, Triglyceride, hemoglobin_sorted, Kidney, Liver)
    print(myData)
    myData.to_csv('newData.csv')
    ypred=[]
    if(Triglyceride==hemoglobin_sorted==Kidney==Liver=='Normal') and Diabetes=='No':
        ypred.append('Congratulations!! You are living a normal life')
    else:
        print("im here")
        model = load(open('SupervisedModelFinal.pkl', 'rb'))
        ypred = model.predict(myData)
    print(ypred[0])

    return render_template('pass2.html',PredictedAge=ypred[0])
    #return render_template('pass2.html', a=age, d=Diabetes, T=Triglyceride, h=hemoglobin_sorted, kid=Kidney, l=Liver ,PredictedAge=ypred)


if __name__ == '__main__':
    app.run(debug=True)
