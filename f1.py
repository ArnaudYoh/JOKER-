from flask import Flask, request, render_template
import
app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template('random.html')
 
@app.route("/echo", methods=['POST'])
def echo(): 
	text =request.form['input']

    return render_template('random.html', script.main(text))
 
 
if __name__ == "__main__":
    app.run(debug=True)