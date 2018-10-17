"""
masaProduction create view.

URLs include:
/
"""
import flask
import masaProduction
from masaProduction.util import hashPassword, hashFile


@masaProduction.app.route('/accounts/create/', methods=('GET', 'POST'))
def showCreate():
    """Show the create an account page."""
    if 'username' in flask.session:
        return flask.redirect(flask.url_for('showEdit'))
    data = {}
    db = masaProduction.model.getDb()
    cursor = db.cursor()
    if flask.request.method == 'POST':

        data['username'] = flask.request.form['username']
        data['password'] = hashPassword(flask.request.form['password'])
        data['fullname'] = flask.request.form['fullname']
        data['filename'] = hashFile(flask.request.files)
        data['email'] = flask.request.form['email']
        dbUsernames = cursor.execute("SELECT username FROM users").fetchall()
        dbUsernameList = []
        for pair in dbUsernames:
            dbUsernameList.append(pair['username'])
        if flask.request.form['username'] in dbUsernameList:
            flask.abort(409)
        elif not flask.request.form['password']:
            flask.abort(400)

        cursor.execute('INSERT INTO users \
                       (username, fullname, email, filename, password) \
                       VALUES (:username, :fullname, :email, :filename,\
                        :password)', data)
        flask.session['username'] = data['username']
        return flask.redirect(flask.url_for('showIndex'))
    context = {}

    return flask.render_template('create.html', **context)
