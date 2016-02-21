from flask import Flask, request, render_template
from ourparser import parseProgram

app = Flask(__name__)
app.config['STATIC'] = '/static/'
 
@app.route("/")
def hello():
    return render_template('random.html')
 
@app.route("/echo", methods=['POST'])
def echo(): 
	#text =request.form['input']
    data = request.form['input']
    try:
    	result = parseProgram(data)
    except:
    	print("lol it didn't work")
    	result=3
    return render_template('random.html', result=result)
 
 
if __name__ == "__main__":
    app.run(debug=True)