from api.vanderSentiment import analysisSentiment
from flask import Flask, request, render_template, redirect
from database import db

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_home_post():
    name = request.form['name']
    email = request.form['email']
    val = (name, email)
    db.add(val, "users")
    return render_template('text.html', name=name, email=email)

@app.route('/message')
def my_form():
    return render_template('text.html')

@app.route('/message', methods=['POST'])
def my_form_post():
    text = request.form['text']
    msgUser = analysisSentiment(text)
    score = msgUser.englishSentiment()
    pos = score["pos"]
    neg = score["neg"]
    neu = score["neu"]
    return render_template('satisfation.html', pos=pos, neg=neg, neu=neu ) #"The positivity is " + str(pos) + "<br>The negativity is " + str(neg)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') #app.run(debug=True, host='0.0.0.0', port=3000)