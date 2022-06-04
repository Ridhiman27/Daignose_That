from flask import Flask,render_template,request
import pickle
import os
import numpy as np
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from werkzeug.utils import secure_filename
app = Flask(__name__)

model1 = load_model('static/Alzheimers_ridhi2.h5');
# model1._make_predict_function()  

@app.route('/')
def hello_world():
    return render_template("alziemer.html")

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(300,300))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    print(preds)
    return preds

@app.route('/predictbrain',methods=['POST','GET'])
def predictbrain():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        my_prediction = model_predict(file_path, model1)
        # pred_class = decode_predictions(my_prediction, top=1)
        # result = str(pred_class[0][0][1])   
        if(my_prediction==1):
            return render_template('alziemerresult1.html')
        else:
            return render_template('alziemerresult0.html')

if __name__ == "__main__":
    app.run(debug=True)
