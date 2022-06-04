from flask import Flask,render_template, request
import pickle
import numpy as np
app = Flask(__name__)

model1 = pickle.load(open('static/heartcancer.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("heartCancer.html")

@app.route('/predictdisease',methods=['POST','GET'])
def predictdisease():
    if request.method == 'POST':

        age = int(request.form['age'])
        gender = int(request.form['gender'])
        chest_pain = int(request.form['chest_pain'])
        resting_bp = int(request.form['resting_bp'])
        cholestrol = int(request.form['cholestrol'])
        fasting_bs = int(request.form['fasting_bs'])
        resting_ecg = int(request.form['resting_ecg'])
        maxHR = int(request.form['maxHR'])
        exercise = int(request.form['exercise'])
        old_peak = float(request.form['old_peak'])
        st_slope = int(request.form['st_slope'])

        data = np.array([[age, gender, chest_pain, resting_bp,cholestrol,fasting_bs,resting_ecg,maxHR,exercise,old_peak,st_slope]])
        my_prediction = model1.predict(data)

        if(my_prediction==1):
            return render_template('heartResult1.html')
        else:
            return render_template('heartResult0.html')

if __name__ == "__main__":
    app.run(debug=True)