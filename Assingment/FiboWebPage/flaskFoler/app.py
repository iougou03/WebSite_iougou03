from py.fibomethod import fibo
from flask import Flask, render_template
from flask import redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/show',methods=['POST'])
def showfibo():
    number=request.form['number']
    fnum= fibo(int(number))
    return render_template('showfibo.html',number=number,fnum=fnum)

if __name__ == "__main__":
    app.run(debug = True)

