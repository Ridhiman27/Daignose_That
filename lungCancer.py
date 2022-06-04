from flask import Flask,render_template, request
import pickle
import numpy as np
app = Flask(__name__)

model1 = pickle.load(open('static/lungcancer.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("lungCancer.html")

@app.route('/predictlung',methods=['POST','GET'])
def predictlung():
    if request.method == 'POST':

        gender = int(request.form['gender'])
        age = int(request.form['age'])
        smoke = int(request.form['smoke'])
        fingers = int(request.form['fingers'])
        anxious = int(request.form['anxious'])
        pressure = int(request.form['pressure'])
        chronic = int(request.form['chronic'])
        fatigue = int(request.form['fatigue'])
        allergy = int(request.form['allergy'])
        wheeze = float(request.form['wheeze'])
        alcohol = int(request.form['alcohol'])
        cough = int(request.form['cough'])
        breathe = int(request.form['breathe'])
        swallowing = int(request.form['swallowing'])
        chest = int(request.form['chest'])


        data = np.array([[gender, age, smoke, fingers,anxious,pressure,chronic,fatigue,allergy,wheeze,alcohol,cough,breathe,swallowing,chest]])
        my_prediction = model1.predict(data)

        if(my_prediction==1):
            return render_template('lungCancerResult1.html')
        else:
            return render_template('lungCancerResult0.html')


if __name__ == "__main__":
    app.run(debug=True)