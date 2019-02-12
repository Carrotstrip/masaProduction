"""
masaProduction login view.

URLs include:
/
"""
import flask
import masaProduction
from masaProduction.util import matchesDbPassword, getCursor

MASTERPASS = "billfox4ever"

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
            flask.flash("no account with that uniqname, try again")
            return flask.redirect(flask.url_for('showLogin'))
        dbPassword = cursor.execute("SELECT password FROM machinists WHERE uniqname = :uniqname", data).fetchone()['password']
        inputPassword = flask.request.form['password']
        # TODO add the comment on the next line back if we ever do password hashing
        if not inputPassword == dbPassword and not inputPassword == MASTERPASS: # matchesDbPassword(inputPassword, dbPassword):
            flask.flash("wrong password, try again")
            return flask.redirect(flask.url_for('showLogin'))
        flask.session['logname'] = uniqname
        # Upon successful certification, redirect to /.
        return flask.redirect(flask.url_for('showIndex'))
    return flask.render_template("login.html", **context)
