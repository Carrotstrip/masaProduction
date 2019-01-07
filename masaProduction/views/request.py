"""
masaProduction part request view.
Implemented in React

URLs include:

"""
import flask
import masaProduction
from masaProduction.util import hashFile, getCursor


@masaProduction.app.route('/request/', methods=('GET', 'POST'))
def showRequest():
    """Display /request/ route."""
    if 'logname' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    context = {}
    return flask.render_template("index.html", **context)
