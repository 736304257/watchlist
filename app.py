from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
import os
import click

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    user=User.query.first()
    movies=Movie.query.all()
    return render_template('index.html', user=user, movies=movies)
@app.route('/user/<name>')
def hello(name):
    return '<h1>Hello %s!</h1><img src="http://helloflask.com/totoro.gif">' % name
@app.route('/test')
def test_url_for():
    print(url_for('index'))
    print(url_for('hello',name='zhaozhao'))
    return '测试页面'


#创建数据库模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #主键
    name = db.Column(db.String(20)) #名字

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True) #主键
    title = db.Column(db.String(60)) #电影标题
    year = db.Column(db.String(4)) #电影年份

@app.cli.command()
def forge():
    db.create_all()
    name = "飞浪无心"
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'My Neighbor Totoro', 'year': '1988'}
    ]
    user = User(name=name)
    uu = User.query.first()
    uu.name = user.name
    for m in movies:
       movie = Movie(title=m['title'], year=m['year'])
       db.session.add(movie)

    db.session.commit()
    click.echo('Done.')
