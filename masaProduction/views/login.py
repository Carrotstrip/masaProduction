"""
masaProduction login view.

URLs include:
/
"""
import flask
import masaProduction
from masaProduction.util import matchesDbPassword


@masaProduction.app.route('/accounts/login/', methods=('GET', 'POST'))
def showLogin():
    """Display /login/ route."""
    if 'username' in flask.session:
        return flask.redirect(flask.url_for('showIndex'))
    context = {}
    data = {}
    db = masaProduction.model.getDb()
    cursor = db.cursor()
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        data['username'] = username
        dbUsername = cursor.execute("SELECT username FROM users WHERE username = :username", data).fetchone()
        if not dbUsername:
            flask.abort(400)
        dbPassword = cursor.execute("SELECT password FROM users WHERE username = :username", data).fetchone()['password']
        inputPassword = flask.request.form['password']
        if not matchesDbPassword(inputPassword, dbPassword):
            flask.abort(403)
        flask.session['username'] = username
        # Upon successful certification, redirect to /.
        return flask.redirect(flask.url_for('showIndex'))
    return flask.render_template("login.html", **context)
