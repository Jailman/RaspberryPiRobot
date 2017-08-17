#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    RPi_Robot
    ~~~~~~

    A robot website application written with
    Flask.

    :copyright: (c) TEOTW by Jailman.
    :license: Apache 2.0.
"""

#global unicode declearation
import sys
reload(sys)
sys.setdefaultencoding('utf8')

'''##########Import modules##########'''
import platform
osdist = platform.platform().split('-')[0]
# from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, Response, \
     render_template, flash
from flask_login import LoginManager, login_required, login_user, UserMixin, \
     logout_user 
from time import sleep
from datetime import timedelta
#import dirvers
# from Modules import driver
# from Modules import servo

'''##########App & config setup##########'''
# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(
    SECRET_KEY='SeriouslydevelopedbyJailman',
    USERNAME='admin1',
    PASSWORD='111'
)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.permanent_session_lifetime = timedelta(hours=5)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

'''##########Simple user model##########'''
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "admin" + str(id)
        self.password = "111"
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)
#create uers
# users = [User(id) for id in range(1, 21)]
users = [User(1)]

'''##########Login & error & command pages##########'''
#error handler
@app.errorhandler(403)
def forbidden(error):
    title = 'Error 403'
    return render_template('403.html', title=title), 403

@app.errorhandler(404)
def page_not_found(error):
    title = 'Error 404'
    return render_template('404.html', title=title), 404

@app.errorhandler(500)
def server_error(error):
    title = 'Error 503'
    return render_template('503.html', title=title), 500

#command page
@app.route('/command', methods=['GET', 'POST'])
@login_required
def command():
    from os import popen as p
    title = 'Command'
    if request.method == 'POST':
        cmd = request.form['command']
        if cmd.strip() != "":
            try:
                if osdist == 'Windows':
                    #windows cmd result needs to be transformed
                    result = p(cmd).read().decode('gbk').encode('utf8')
                else:
                    result = p(cmd).read()
                for line in result.split('\n'):
                    flash(line)
                return render_template('command.html', title=title)
            except:
                flash("Execution Error!")
                return render_template('command.html', title=title)
        flash("Input error!")
        return render_template('command.html', title=title)
    else:
        flash("Here shows the result!")
        return render_template('command.html', title=title)


#login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Login'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != app.config['USERNAME']:
            abort(403)
        elif password != app.config['PASSWORD']:
            abort(403)
        else:
            session['logged_in'] = True
            id = username.split('admin')[1]
            user = User(id)
            login_user(user)
            # return redirect(request.args.get("next"))
            return redirect(url_for('index'))
    return render_template('login.html', title=title)

#logout page
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    logout_user()
    flash('Warning: You were logged out!')
    return redirect(url_for('login'))

# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)



'''##########Pi Pages##########'''
#raspberrypi pages
@app.route('/')
@app.route('/index')
@login_required
def index():
    # return Response("Hello World!")
    return render_template('index.html')

@app.route('/Patrol_Monitor')
@login_required
def Patrol_Monitor():
    return render_template('Patrol_Monitor.html')

@app.route('/Sensor_Graph')
@login_required
def Sensor_Graph():
    return render_template('Sensor_Graph.html')

@app.route('/Home_Automation')
@login_required
def Home_Automation():
    return render_template('Home_Automation.html')

@app.route('/Amaze_Me')
@login_required
def Amaze_Me():
    return render_template('Amaze_Me.html')

'''##########Charts Demo##########'''
@app.route('/get_temperature')
@login_required
def get_temperature():
    return '[30.1, 30.1, 30.1, 30.1, 30.1, 30.1, 30.1, 30.1, 30.1, 30.1, 30.1, 30.1]'

@app.route('/get_humidity')
@login_required
def get_humidity():
    return '[32.3, 32.5, 32.1, 32.6, 30.8, 30.9, 31.1, 31.5, 32.1, 31.9, 31.7, 31.5]'

@app.route('/get_time')
@login_required
def get_time():
    return "['2:00', '2:05', '2:10', '2:15', '2:20', '2:25', '2:30', '2:35', '2:40', '2:45', '2:50', '2:55']"

'''##########Pi Power Control##########'''
# from Modules.gpiostat import gpio_status

@app.route('/power')
@login_required
def query():
    # querystatus
    return "on"
    # GPIO_PIN = 12
    # return gpio_status(GPIO_PIN)

@app.route('/power/<control>')
@login_required
def switch(control):
    if control == "on":
        # switchon
        return "on"
    if control == "off":
        # switchoff
        return "off"


'''##########Robot drivers##########'''

@app.route('/driver/<control>')
@login_required
def robot_driver(control):
    from Modules import driver as d
    d.init_driver()
    if control == "forward":
        d.forward()
    if control == "backward":
        d.backward()
    if control == "stop":
        d.stop()
    if control == "left":
        d.left()
    if control == "right":
        d.right()

'''##########Servo drivers##########'''
# @app.route('/servo/<float:post_value>')
# def servo_ctrl(post_value):
#     servo.somefunc(post_value)








if __name__ == '__main__':
    app.run(
        debug = True,
        host='0.0.0.0',
        port=80
        )
