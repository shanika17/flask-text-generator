#!/usr/bin/env python

from transformers import pipeline
from flask import Flask,render_template,request,redirect, url_for
import pyrebase

app=Flask(__name__)

config = {
    'apiKey': "AIzaSyDljXzWzGdTHV-KjUbpvmja3EpxEJO7OW4",
    'authDomain': "authentication-app-d7812.firebaseapp.com",
    'projectId': "authentication-app-d7812",
    'storageBucket': "authentication-app-d7812.appspot.com",
    'messagingSenderId': "965036005644",
    'appId': "1:965036005644:web:aac30260c0ef9510011129",
    'databaseURL': "https://authentication-app-d7812-default-rtdb.firebaseio.com"

  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'



@app.route('/')
def login():
     return render_template('login.html')
'''
@app.route('/')
def login():
     return render_template('signup.html')
'''
@app.route('/register')
def register():
     return render_template('signup.html')

@app.route('/index')
def index():
     return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    raw_text = request.form['input_text']
    new_text = raw_text + " project"

    generator = pipeline('text-generation', model='gpt2')
    output = generator(new_text, max_length=100, num_return_sequences=1)

    generated_text = output[0]['generated_text'].replace(new_text, '', 5)

    # Redirect the user to the result page
    return redirect(url_for('result', new_text=new_text, generated_text=generated_text))

@app.route('/result')
def result():
    new_text = request.args.get('new_text')
    generated_text = request.args.get('generated_text')

    return render_template('result.html', new_text=new_text, generated_text=generated_text)


@app.route('/logout')
def logout():
     return render_template('login.html')

# if __name__== "__main__":
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
