"""
masaProduction login view.

URLs include:
/
"""
import flask
import masaProduction
from masaProduction.util import matchesDbPassword, getCursor


@masaProduction.app.route('/accounts/login/', methods=('GET', 'POST'))
def showLogin():
    """Display /login/ route."""
    if 'logname' in flask.session:
        return flask.redirect(flask.url_for('showIndex'))
    context = {}
    data = {}
    cursor = getCursor()
    if flask.request.method == 'POST':
        uniqname = flask.request.form['uniqname']
        data['uniqname'] = uniqname
        dbUsername = cursor.execute("SELECT uniqname FROM machinists WHERE uniqname = :uniqname", data).fetchone()
        if not dbUsername:
            flask.abort(400)
        dbPassword = cursor.execute("SELECT password FROM machinists WHERE uniqname = :uniqname", data).fetchone()['password']
        inputPassword = flask.request.form['password']
        print(dbPassword, inputPassword)
        #if not matchesDbPassword(inputPassword, dbPassword):
        #    flask.abort(403)
        flask.session['logname'] = uniqname
        # Upon successful certification, redirect to /.
        return flask.redirect(flask.url_for('showIndex'))
    return flask.render_template("login.html", **context)
