"""
masaProduction user view.
Implemented in React

URLs include:

"""
import flask
import masaProduction
from masaProduction.util import hashFile, getCursor


@masaProduction.app.route('/u/<username>/', methods=('GET', 'POST'))
def showUser(username):
    """Display /u/<username>/ route."""
    if 'logname' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    cursor = getCursor()
    if flask.request.method == 'POST':
        data = {}
        data['logname'] = flask.session['logname']
        data['uniqname'] = username
    context = {}
    context['logname'] = flask.session['logname']
    context['uniqname'] = username
    context['filename'] = cursor.execute("SELECT filename\
                                         FROM machinists WHERE uniqname\
                                         = :uniqname",
                                         context).fetchone()["filename"]
    context['fullname'] = cursor.execute("SELECT fullname\
                                         FROM machinists WHERE uniqname\
                                         = :uniqname",
                                         context).fetchone()["fullname"]
    following = []
    followers = []
    return flask.render_template("user.html", **context)
