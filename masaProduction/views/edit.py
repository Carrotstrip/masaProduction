"""
masaProduction edit view.

URLs include:

"""
import os
import flask
import masaProduction
from masaProduction.util import hashFile


@masaProduction.app.route('/accounts/edit/', methods=['GET', 'POST'])
def showEdit():
    """Display /accounts/edit/ route."""
    if 'logname' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    data = {}
    d_b = masaProduction.model.getDb()
    cursor = d_b.cursor()
    data['logname'] = flask.session['logname']
    if flask.request.method == 'POST':
        data['fullname'] = flask.request.form['fullname']
        data['email'] = flask.request.form['email']
        if 'file' in flask.request.files:
            data['hashed_filename'] = hashFile(flask.request.files)

            # Delete old file
            filename = cursor.execute("SELECT filename\
                                      FROM users where\
                                      username = :logname\
                                      ", data).fetchone()['filename']
            os.remove(masaProduction.app.config['UPLOAD_FOLDER'] + "/" + filename)
            cursor.execute("UPDATE users SET filename = :hashed_filename,\
                           fullname = :fullname, email = :email WHERE \
                           username = :logname", data)
        elif 'file' not in flask.request.files:
            cursor.execute("UPDATE users SET fullname = :fullname,\
             email = :email WHERE username = :logname", data)

    context = {}
    context['logname'] = flask.session['logname']
    context['file'] = cursor.execute("SELECT filename FROM users\
        WHERE username = :logname", data).fetchone()['filename']

    return flask.render_template("edit.html", **context)
