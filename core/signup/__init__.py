import flask
from flask import render_template, request
from core import pokedb

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def pokemail_index():
    return render_template('index.html')

@app.route('/signup',methods=['POST'])
def pokemail_signup():
    form = request.form['email']
    # Create the object that will be submitted.
    pokedb.insert_user_email({'Email':form})
    return 'You are signed up for Pokemail! Check your email everyday to see what Pokemon you have discovered.'


def start_server():
    app.run(host='localhost',port=8080, debug=True)