#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
"""
    RPi_Robot
    ~~~~~~

    A robot website application written with
    Flask.

    :copyright: (c) TEOTW by Jailman.
    :license: Nonsense.
"""

'''##########Import modules##########'''
# from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from time import sleep
from datetime import timedelta
#import dirvers
# from Modules import driver
# from Modules import servo

'''##########App & config setup##########'''
# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='SeriouslydevelopedbyJailman',
    USERNAME='admin',
    PASSWORD='111'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.permanent_session_lifetime = timedelta(hours=24)



'''##########Login & error & command pages##########'''
#error handler
@app.errorhandler(401)
def forbidden(error):
    title = 'Error 401'
    return render_template('401.html', title=title), 401

@app.errorhandler(404)
def page_not_found(error):
    title = 'Error 404'
    return render_template('404.html', title=title), 404

@app.errorhandler(503)
def page_not_found(error):
    title = 'Error 503'
    return render_template('503.html', title=title), 503


#command page
@app.route('/command')
def show_entries():
    title = 'Command'
    if not session.get('logged_in'):
        abort(401)
    return render_template('command.html', title=title)


#login page
@app.route('/', methods=['GET', 'POST'])
def login():
    title = 'Login'
    # flash('You wanna damn log in, son?')
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            abort(401)
        elif request.form['password'] != app.config['PASSWORD']:
            abort(401)
        else:
            session['logged_in'] = True
            # flash('You were logged in, fucker!')
            return redirect(url_for('index'))
    return render_template('login.html', title=title)


#logout page
# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('You were logged out, fucker?')
#     return redirect(url_for('login'))



'''##########Pi Pages##########'''
#raspberrypi pages
@app.route('/index')
def index():
    session.permanent = True
    if not session.get('logged_in'):
        abort(401)
    return render_template('index.html')

@app.route('/Patrol_Monitor')
def Patrol_Monitor():
    if not session.get('logged_in'):
        abort(401)
    return render_template('Patrol_Monitor.html')

@app.route('/Sensor_Graph')
def Sensor_Graph():
    if not session.get('logged_in'):
        abort(401)
    return render_template('Sensor_Graph.html')

@app.route('/Home_Automation')
def Home_Automation():
    if not session.get('logged_in'):
        abort(401)
    return render_template('Home_Automation.html')

@app.route('/Amaze_Me')
def Amaze_Me():
    if not session.get('logged_in'):
        abort(401)
    return render_template('Amaze_Me.html')



'''##########CGI drivers##########'''

'''##########Servo drivers##########'''
# @app.route('/servo/<float:post_value>')
# def servo_ctrl(post_value):
#     servo.somefunc(post_value)


'''##########Wheel drivers##########'''
# @app.route('/wheel/<direction>')
# def wheel_ctrl(direction):
#     driver.somefunc(direction)





if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=80
        )
