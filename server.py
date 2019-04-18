from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

    
@app.route('/index')
def log_in():
    return render_template('log_in.html') 


if __name__ == '__main__':
   app.run(debug = True)