from api.vanderSentiment import analysisSentiment
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('text.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    msgUser = analysisSentiment(text)
    score = msgUser.englishSentiment()
    pos = score["pos"]
    neg = score["neg"]
    neu = score["neu"]
    return "The positivity is " + str(pos) + "<br>The negativity is " + str(neg)

if __name__ == "__main__":
    app.run(debug=True, host ='0.0.0.0')