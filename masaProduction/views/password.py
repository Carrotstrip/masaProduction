"""
masaProduction password view.

URLs include:

"""
import flask
import masaProduction
from masaProduction.util import hashPassword, matchesDbPassword, getCursor

@masaProduction.app.route('/accounts/password/', methods=('GET', 'POST'))
def showPassword():
    """Display /accounts/password/ route."""
    if 'logname' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    cursor = getCursor()
    data = {}
    if flask.request.method == 'POST':
        username = flask.session['logname']
        data['username'] = username
        old_db_password = cursor.execute("SELECT password FROM\
                                         users WHERE username =\
                                         :username",
                                         data).fetchone()['password']
        old_input_password = flask.request.form['password']
        new_input_password1 = flask.request.form['new_password1']
        new_input_password2 = flask.request.form['new_password2']
        if not matchesDbPassword(old_input_password, old_db_password):
            flask.abort(403)
        # Check if both new passwords match. abort 401 otherwise.
        if new_input_password1 != new_input_password2:
            flask.abort(401)
        data['new_hashed'] = hashPassword(new_input_password1)
        # Update hashed password entry in database. (See above).
        cursor.execute("UPDATE users SET password =\
                       :new_hashed WHERE username = :username", data)
        # Upon successful submission, redirect to /accounts/edit/.
        return flask.redirect(flask.url_for('showEdit'))
    context = {}
    return flask.render_template("password.html", **context)
