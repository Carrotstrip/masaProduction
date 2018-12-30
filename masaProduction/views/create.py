"""
masaProduction create view.

URLs include:
/

TODO give each account a default picture if they don't want to add one so that
we don't have to handle what if they didn't add one and then we have to check if they did 
and it's a whole thing. You do need to specify a full name, uniqname, and password
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
        # TODO add the comment on the next line back if we ever do password hashing
        data['password'] = flask.request.form['password'] # hashPassword(flask.request.form['password'])
        data['fullname'] = flask.request.form['fullname']
        data['filename'] = hashFile(flask.request)
        dbUsernames = cursor.execute("SELECT uniqname FROM machinists").fetchall()
        dbUsernameList = []
        for pair in dbUsernames:
            dbUsernameList.append(pair['uniqname'])
        if flask.request.form['uniqname'] in dbUsernameList:
            flask.flash("uniqname already in database, try again!")
            return flask.redirect(flask.url_for('showCreate'))
        elif not flask.request.form['password']:
            flask.flash("you didn't make a password, try again!")
            return flask.redirect(flask.url_for('showCreate'))
        cursor.execute('INSERT INTO machinists \
                       (uniqname, fullname, password, filename) \
                       VALUES (:uniqname, :fullname,\
                        :password, :filename)', data)
        flask.session['logname'] = data['uniqname']
        return flask.redirect(flask.url_for('showIndex'))
    context = {}
    return flask.render_template('create.html', **context)
