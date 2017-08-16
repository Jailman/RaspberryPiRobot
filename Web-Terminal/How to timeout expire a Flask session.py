# On this example we are going to increment a counter on each
# page load. On normal conditions the session wouldn't expire
# until the user closed the browser, so the counter will never
# get reset to 0, but we are going to set a timeout for the
# session, so after that time passes, the counter will be 0
import os
# We'll use timedelta for the time related operations
from datetime import timedelta
# We need the session object to be able to store session variables
# and we'll render an html template, so we also need render_template
from flask import Flask, session, render_template

app = Flask(__name__)

# Generate a secret random key for the session
app.secret_key = os.urandom(24)
# Set the timeout for our session to 10 seconds
# The session will be lost after 10 seconds with no interaction
# form the user.
# +INFO: http://flask.pocoo.org/docs/api/#flask.Flask.permanent_session_lifetime
app.permanent_session_lifetime = timedelta(seconds=10)


# Define a route for the webserver
@app.route('/')
def index():
    # For the timeout/session lifetime config to work we need
    # to make the sessions permanent. It's false by default
    # +INFO: http://flask.pocoo.org/docs/api/#flask.session.permanent
    session.permanent = True
    # On each page load we are going to increment a counter
    # stored on the session data.
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1
    return "Number of reloads on the current session: %d" % session['counter']

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80")
    )
