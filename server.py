from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

    
@app.route('/index')
def log_in():
    return render_template('log_in.html') 

@app.route("/status")
def status():
    user_id = request.args.get('user_id')
    shape_process = request.args.get('shape_process')
    letter_process = request.args.get('letter_process')
    print(shape_process)
    print(letter_process)
    return render_template("status.html",user_id=user_id,letter_process=letter_process,shape_process=shape_process)

@app.route("/before_shape")
def before_shape():
    return render_template("before_shape.html")

@app.route("/after_shape")
def after_shape():
    return render_template("after_shape.html")

if __name__ == '__main__':
   app.run(debug = True)