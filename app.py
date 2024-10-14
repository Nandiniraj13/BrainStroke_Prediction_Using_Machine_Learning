from flask import Flask,render_template,request
import numpy as np
import sklearn
import pickle
import pandas as pd

app=Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')




@app.route('/predictAction', methods=['POST'])
def predictAction():
    if request.method == 'POST':
        name = request.form['name']
        gender_Male = int(request.form['gender'])
        age = int(request.form['age'])
        heart_disease_1 = int(request.form['disease'])
        ever_married_Yes = int(request.form['married'])
        work = int(request.form['work'])
        Residence_type_Urban = int(request.form['residence'])
        avg_glucose_level = float(request.form['avg_glucose_level'])
        bmi = float(request.form['bmi'])
        smoking = int(request.form['smoking'])
        
        # Blood pressure handling
        bp = request.form['bp']
        systolic, diastolic = map(int, bp.split('/'))
        hypertension_1 = 1 if systolic > 140 or diastolic > 90 else 0

        work_type_Never_worked=0
        work_type_Private=0
        work_type_Self_employed=0
        work_type_children=0
        
        if work == 1:
            work_type_Never_worked = 1
        elif work == 2:
            work_type_Private = 1
        elif work == 3:
            work_type_Self_employed = 1
        elif work == 4:
            work_type_children = 1

        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_smokes = 0
        if smoking == 1:
            smoking_status_formerly_smoked = 1
        elif smoking == 2:
            smoking_status_never_smoked = 1
        elif smoking == 3:
            smoking_status_smokes = 1

        input_features = [
            age, avg_glucose_level, bmi, gender_Male, hypertension_1, 
            heart_disease_1, ever_married_Yes, work_type_Never_worked, 
            work_type_Private, work_type_Self_employed, work_type_children, 
            Residence_type_Urban, smoking_status_formerly_smoked, 
            smoking_status_never_smoked, smoking_status_smokes
        ]

        features_value = [np.array(input_features)]
        features_name = [
            'age', 'avg_glucose_level', 'bmi', 'gender_Male', 'hypertension_1', 
            'heart_disease_1', 'ever_married_Yes', 'work_type_Never_worked', 
            'work_type_Private', 'work_type_Self-employed', 'work_type_children', 
            'Residence_type_Urban', 'smoking_status_formerly smoked', 
            'smoking_status_never smoked', 'smoking_status_smokes'
        ]

        df = pd.DataFrame(features_value, columns=features_name)
        prediction = model.predict(df)[0]
        
        result_message = ""
        if prediction == 1:
            result_message = f"{name}, you might be at risk of having a stroke."
        else:
            result_message = f"{name}, good news! You don't have any risk of stroke."

        return render_template('result.html', a=result_message)



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)