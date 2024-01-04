from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd

app = Flask(__name__)
@app.route('/')
def Hello():
    return render_template('index.html')

@app.route('/classification', methods = ['GET','POST'])
def hey():
    if request.method == 'POST':
        area = request.form['area']
        aspectration = request.form['aspectratio']
        eccentricity = request.form['eccentricity']
        extent = request.form['extent']
        solidity = request.form['solidity']
        roundness = request.form['roundness']
        compactness = request.form['compactness']
        sf1 = request.form['sf1']
        sf2 = request.form['sf2']
        sf4 = request.form['sf4']
        #input = np.array([[area,aspectration,eccentricity,extent,solidity,roundness,compactness,sf1,sf2,sf4]]).astype(np.float64)
        #sscaler = StandardScaler()
        input_data = np.array([[39188.0,1.132879,0.588252,0.781313,0.989960,0.951599,0.939219,0.006806,0.003267,0.999349]])
        feature_names = ['Area','AspectRation','Eccentricity','Extent','Solidity','roundness','Compactness','ShapeFactor1','ShapeFactor2','ShapeFactor4']
        print(input_data)
        model = pickle.load(open('best_svm_model.pkl','rb'))
               
        scaler = joblib.load('stdscaler.pkl')

        input_scaled = scaler.fit_transform(input_data)
        
        print(input_scaled)
        
        drybeanclassified = model.predict(input_scaled)

        print(drybeanclassified)
        if drybeanclassified == 0:
            classification = 'BARBUNYA'
        elif drybeanclassified== 1:
            classification = 'BOMBAY'
        elif drybeanclassified== 2:
            classification = 'CALI'
        elif drybeanclassified== 3:
            classification = 'DERMASON'
        elif drybeanclassified== 4:
            classification = 'HOROZ'
        elif drybeanclassified== 5:
            classification = 'SEKER'
        else :
            classification = 'SIRA'
        return render_template('classification.html',area=classification)
    else:
        return render_template('classification.html')

if __name__ == '__main__':
    app.run()
