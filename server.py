from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

shape_seconds = ["40","30","20"]
shape_level = 1
shape_process = 0
letter_process = 0
letter_level = 1 

@app.route('/index')
def log_in():
    return render_template('log_in.html') 

@app.route("/status")
def status():
    user_id = request.args.get('user_id')
    return render_template("status.html",user_id=user_id,letter_process=letter_process,shape_process=shape_process)

@app.route("/before_shape")
def before_shape():
    return render_template("before_shape.html",level = shape_level,seconds=shape_seconds[int(shape_level)-1])

@app.route("/before_letter")
def before_letter():
    return render_template("before_letter.html",level = letter_level)

@app.route("/flip_card/<seconds>")
def flip_card(seconds):
    return render_template("flip_card.html",seconds=seconds)

@app.route("/after_shape")
def after_shape():
    return render_template("after_shape.html")

@app.route("/after_letter")
def after_letter():
    return render_template("after_letter.html")

@app.route("/update_process",methods=["POST"])
def update_process():
    global shape_level
    global shape_process
    global letter_process
    global letter_level
    json_data = request.get_json()
    
    json_data["rank"] = count_rank
    data.append(json_data)
    result = {}
    result["url"] = "http://127.0.0.1:5000/Item/"+str(count_rank)
    return json.dumps(result)
    
if __name__ == '__main__':
   app.run(debug = True)