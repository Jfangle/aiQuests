import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template
from calc import Calculator  # Now this should work

app = Flask(__name__)
calculator = Calculator()  # Create a Calculator instance

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/home')
def home():
    print('home page test')
    return 'This is the Home Page'

@app.route('/calculator')
def calculator_view():
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)