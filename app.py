from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd
import os

app = Flask(__name__)
@app.route('/')
def Hello():
    return render_template('index.html')

@app.route('/classification', methods = ['GET','POST'])
def hey():
    try:
        if request.method == 'POST':
            area = float(request.form['area'])
            aspectration = float(request.form['aspectratio'])
            eccentricity = float(request.form['eccentricity'])
            extent = float(request.form['extent'])
            solidity = float(request.form['solidity'])
            roundness = float(request.form['roundness'])
            compactness = float(request.form['compactness'])
            sf1 = float(request.form['sf1'])
            sf2 = float(request.form['sf2'])
            sf4 = float(request.form['sf4'])
            input_array = np.array([[area,aspectration,eccentricity,extent,solidity,roundness,compactness,sf1,sf2,sf4]]).astype(np.float64)
            #input =[[41487.0,1.688753,0.805826,0.689176,0.976555,0.783156,0.768550,0.007208,0.001551,0.997493]]                       
            model = pickle.load(open('best_svm_model.pkl','rb'))
                
            #scaler = joblib.load('stdscaler.pkl')
            #scaler = StandardScaler()
            #input_scaled = scaler.fit_transform(input_array)
            #X_data = pd.DataFrame(input_scaled,columns=['Area','AspectRation','Eccentricity','Extent','Solidity','roundness','Compactness','ShapeFactor1','ShapeFactor2','ShapeFactor4'])
            #input_scaled = scaler.fit_transform(X_data)
            
            # Load the scaler from the pickled file
            scaler = joblib.load("stdscaler_G.pkl")
            input_scaled_G = scaler.transform(input_array)
            print('Input scaled',input_scaled_G)
                    
            drybeanclassified = model.predict(input_scaled_G)
            print('Input Array',input)
            print('Scaled Array',input_scaled_G)

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
    except ValueError:
        # Handle the case where the input is not a valid float
        return "Invalid input. Please enter a valid value in the  fields."

if __name__ == '__main__':
    app.run()
