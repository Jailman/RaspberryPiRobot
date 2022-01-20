#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, Response, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config.update(
    SECRET_KEY='SeriouslydevelopedbyJailman',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
)


db = SQLAlchemy(app)
# db.init_app(app)
# #define egine
# engine = db.create_engine('sqlite:///test.db')
# #bind metadata
# metadata = db.MetaData(engine)
# metadata.create_all(engine)
# #get db connected
# conn = engine.connect()


login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
#login_manager.init_app(app)


class User(db.Model, UserMixin):
    __tablename__ = 'pilot'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(255))


    def __init__(self, name, fullname, email, password_hash):
        self.name = name
        self.fullname = fullname
        self.email = email
        self.password_hash = password_hash


    def verify_password(self, password):
        return check_password_hash(generate_password_hash(self.password_hash), password)


    def __repr__(self):
       return "%s/%s/%s" % (self.name, self.fullname, self.email)


class Air(db.Model):
    __tablename__ = 'air'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    infaredetector = db.Column(db.Boolean)


class Joystick(db.Model):
    __tablename__ = 'joystick'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gpio = db.Column(db.Integer)
    function = db.Column(db.String(255))
    device = db.Column(db.String(255))


@login_manager.user_loader
def load_user(userid):
   return User.query.get(int(userid))


db.create_all()
try:
    admin1 = User('buc', 'buc les', 'buc@xy.ti', 'buz')
    admin2 = User('zac', 'zac tol', 'zac@xy.ti', 'zab')
    db.session.add(admin1)
    db.session.add(admin2)
    db.session.commit()
except:
    pass

# users = User.query.all()
# print users


# some protected url
@app.route('/')
@login_required
def home():
    return Response('Hello World!<br> <a href="/logout">logout</a>')


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(name=username).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 80,
        debug = True
    )