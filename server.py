from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

shape_seconds = ["40","35","30"]
letter_number=["5","7","10"]
letter_max_score = [5,7,10]
shape_level = 1
shape_process = 0
letter_process = 0
letter_level = 1 
user_id=[]

json_file = open('./static/gifs/answer.json',"r")  
answer = json.load(json_file)
json_file.close()

@app.route('/index')
def log_in():
    return render_template('log_in.html') 

@app.route("/status")
def status():
    global user_id
    if not user_id:
        user_id.append(request.args.get('user_id'))
    
    return render_template("status.html",user_id=user_id[0],shape_level=shape_level,letter_level=letter_level,letter_process=letter_process,shape_process=shape_process)

@app.route("/before_shape")
def before_shape():
    return render_template("before_shape.html",level = shape_level,seconds=shape_seconds[shape_level-1])

@app.route("/before_letter")
def before_letter():
    return render_template("before_letter.html",level = letter_level,number=letter_number[letter_level-1])

@app.route("/flip_card/<seconds>")
def flip_card(seconds):
    return render_template("flip_card.html",seconds=seconds)

@app.route("/letter/<level>")
def letter(level):
    return render_template("letter.html",level=level,answer=answer)

@app.route("/after_shape/<score>")
def after_shape(score):
    return render_template("after_shape.html",score=score,seconds=shape_seconds[shape_level-1])

@app.route("/after_letter/<score>/<answer>")
def after_letter(score,answer):
    return render_template("after_letter.html",answer=answer,score=score,level = letter_level,number=letter_number[letter_level-1])

@app.route("/update_process",methods=["POST"])
def update_process():
    global shape_level
    global shape_process
    global letter_process
    global letter_level
    json_data = request.get_json()
    score = int(json_data["score"])
    result = {}
    if json_data["type"]=="shape":
        increased_amount = shape_level*15*score/16
        if shape_process + increased_amount >= 100:
            result["increase"] = 100 - shape_process
            shape_process = 100
        else:
            result["increase"] = increased_amount
            shape_process += increased_amount

        if score >= 14:
            if shape_level != 3:
                shape_level += 1
                result["level"] = "u"+str(shape_level)
            else:
                result["level"] = "m"
        else:
            result["level"] = "n"
    else:
        increased_amount = letter_level*15*score/letter_max_score[letter_level-1]
        if letter_process + increased_amount >= 100:
            result["increase"] = 100 - letter_process
            letter_process = 100
        else:
            result["increase"] = increased_amount
            letter_process = increased_amount

        if score > letter_max_score[letter_level-1]-2:
            if letter_level != 3:
                letter_level += 1
                result["level"] = "u"+str(letter_level)
            else:
                result["level"] = "m"
        else:
            result["level"] = "n"

    return json.dumps(result)

if __name__ == '__main__':
   app.run(debug = True)