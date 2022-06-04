from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__)

model1 = pickle.load(open('static/diabetes.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("diabetes.html")

@app.route('/predictdiabetes',methods=['POST','GET'])
def predictdiabetes():
    if request.method == 'POST':

        preg = request.form['pregnancies']
        glucose = request.form['glucose']
        bp = request.form['bp']
        st = request.form['thickness']
        insulin = request.form['insulin']
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = request.form['age']

        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        my_prediction = model1.predict(data)

        if(my_prediction==1):
            return render_template('diabetesResult1.html')
        else:
            return render_template('diabetesResult0.html')


if __name__ == "__main__":
    app.run(debug=True)
