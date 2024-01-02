from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def Hello():
    return render_template('index.html')

@app.route('/name', methods = ['GET','POST'])
def hey():
    if request.method == 'POST':
        area = request.form['area']
        print(area)

if __name__ == '__main__':
    app.run()