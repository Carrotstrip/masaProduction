"""
masaProduction user view.
Implemented in React

URLs include:

"""
import flask
import masaProduction
from masaProduction.util import hashFile, getCursor


@masaProduction.app.route('/u/<uniqname>/', methods=('GET', 'POST'))
def showUser(uniqname):
    """Display /u/<username>/ route."""
    if 'logname' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    context = {}
    return flask.render_template("index.html", **context)
