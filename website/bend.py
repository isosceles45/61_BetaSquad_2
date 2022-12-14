from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('randomforrest2.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("agrigo.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    data=[np.array(int_features)]
    print(int_features)
    print(data)
   ##prediction=randomforrest2.predict_proba(data)

prediction=model.predict(data)


    
    return render_template('agrigo.html',pred='Best suitable Tree for you is {}'.prediciton)



        if __name__ == '__main__':
    app.run(debug=True)