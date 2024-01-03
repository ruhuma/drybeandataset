from flask import Flask, render_template, request

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
        
        print(area)
        return render_template('classification.html',area=area)
    else:
        return render_template('classification.html')

if __name__ == '__main__':
    app.run()
