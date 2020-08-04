from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def home():
    return'昭昭的第一个页面'
@app.route('/user/<name>')
def hello(name):
    return '<h1>Hello %s!</h1><img src="http://helloflask.com/totoro.gif">' % name
@app.route('/test')
def test_url_for():
    print(url_for('home'))
    print(url_for('hello',name='zhaozhao'))
    return '测试页面'
