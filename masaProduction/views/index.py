"""masaProduction main view"""

import flask
from flask import send_from_directory
import arrow
import masaProduction


@masaProduction.app.route('/', methods=('GET', 'POST'))
def showIndex():
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    context = {}
    return flask.render_template("index.html", **context)