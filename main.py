from api.vanderSentiment import analysisSentiment
from flask import Flask, request, render_template, jsonify
import database.db as db

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def agiim_users():
    return jsonify(db.get_users())


@app.route('/register', methods=['GET'])
def show_register():
    return jsonify({
        'name': 'Pedro',
        'email': 'pedro.net@com',
        'msg': '',
        'pos': 0,
        'neu': 0,
        'neg': 0,
        'correctFell': True
    })

@app.route('/register', methods=['POST'])
def my_msg_register():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        name = json['name']
        email = json['email']
        val = (name, email)
        db.add(val, 'users')
        return json
    else:
        return 'Content-Type not supported!'

@app.route('/')
def my_home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_home_post():
    name = request.form['name']
    email = request.form['email']
    #val = (name, email)
    #db.add(val, "users")
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