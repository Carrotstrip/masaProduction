"""
masaProduction create view.

URLs include:
/
"""
import flask
import masaProduction
from masaProduction.util import hashPassword, hashFile, getCursor


@masaProduction.app.route('/accounts/create/', methods=('GET', 'POST'))
def showCreate():
    """Show the create an account page."""
    if 'logname' in flask.session:
        return flask.redirect(flask.url_for('showEdit'))
    data = {}
    cursor = getCursor()
    if flask.request.method == 'POST':
        data['uniqname'] = flask.request.form['uniqname']
        data['password'] = hashPassword(flask.request.form['password'])
        data['fullname'] = flask.request.form['fullname']
        data['filename'] = hashFile(flask.request.files)
        dbUsernames = cursor.execute("SELECT uniqname FROM machinists").fetchall()
        dbUsernameList = []
        for pair in dbUsernames:
            dbUsernameList.append(pair['uniqname'])
        if flask.request.form['uniqname'] in dbUsernameList:
            flask.abort(409)
        elif not flask.request.form['password']:
            flask.abort(400)
        cursor.execute('INSERT INTO machinists \
                       (uniqname, fullname, password) \
                       VALUES (:uniqname, :fullname,\
                        :password)', data)
        flask.session['logname'] = data['uniqname']
        return flask.redirect(flask.url_for('showIndex'))
    context = {}
    return flask.render_template('create.html', **context)
