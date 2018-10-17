"""
masaProduction members view.

URLs include:

"""
import flask
import masaProduction
from masaProduction.util import getCursor


@masaProduction.app.route('/members/')
def showMembers():
    """Display /members/ route."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    context = {}
    cursor=getCursor()
    
    return flask.render_template("members.html", **context)
