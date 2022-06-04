from flask import Flask,render_template, request
import pickle
import numpy as np
app = Flask(__name__)

model1 = pickle.load(open('static/urinarydisease.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("urinary_disease.html")

@app.route('/predicturinary',methods=['POST','GET'])
def predicturinary():
    if request.method == 'POST':

        temp = float(request.form['temperature'])
        nausea = int(request.form['nausea'])
        pain = int(request.form['pain'])
        urinate = int(request.form['urinate'])
        abdomen = int(request.form['abdomen'])
        burning = int(request.form['burning'])

        data = np.array([[temp,nausea, pain, urinate, abdomen, burning]])
        my_prediction = model1.predict(data)

        if(my_prediction==1):
            return render_template('urinaryresult1.html')
        else:
            return render_template('urinaryresult0.html')


if __name__ == "__main__":
    app.run(debug=True)