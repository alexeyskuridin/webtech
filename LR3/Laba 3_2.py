from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index(): return 'Hello!'

@app.route('/test')
def test(): return 'Just test'

@app.route('/user/<username>')
def show_profile(username):
    return 'Username: ' + str(username)

@app.route('/lab3')
def lab3():
    return render_template('Laba 3_2.html')

app.run()