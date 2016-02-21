from flask import Flask, request, render_template
from parser import *

app = Flask(__name__)
app.config['STATIC'] = '/static/'
 
@app.route("/")
def hello():
    return render_template('random.html')
 
@app.route("/echo", methods=['POST'])
def echo(): 
	#text =request.form['input']
	data = request.form['input']

    return render_template('random.html', text=request.form['input'])
 
 
if __name__ == "__main__":
    app.run(debug=True)