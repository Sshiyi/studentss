from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask import Flask, request, render_template, redirect
import os

BASE_DIR = os.path.dirname((os.path.abspath(__name__)))
UPLOAD_DIR = os.path.join(BASE_DIR, 'static', 'upload')

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/sh1907'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


@app.route('/')
def score_list():
    student = User.query.all()
    order_condition = db.desc(User.chinese + User.math)
    users = User.query.order_by(order_condition).limit(5)
    return render_template('desclist.html', student=student,users=users)


@app.route('/set_list/', methods=('GET', 'POST'))
def set_list():
    if request.method == 'POST':
        id = request.form['id']
        user = User.query.get(int(id))
        user.gender = request.form['gender']
        user.chinese = request.form['chinese']
        user.math = request.form['math']

        uplpad_img = request.files['avatar']
        filepath = os.path.join(UPLOAD_DIR, user.name)
        uplpad_img.save(filepath)

        return redirect('/')
    else:
        id = request.args['id']
        return render_template('set_student.html', user=User.query.get(int(id)))


class User(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True)
    gender = db.Column(db.String(20))
    chinese = db.Column(db.Float, default=0.0)
    math = db.Column(db.Float, default=0.0)
    english = db.Column(db.Float)


@app.route('/info')
def info():
    id = int(request.args['id'])
    user = User.query.get(id)
    return render_template('info.html', user=user)



if __name__ == '__main__':
    app.debug = True
    app.run()
