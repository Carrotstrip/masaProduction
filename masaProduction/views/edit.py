"""
masaProduction edit view.

URLs include:

"""
import os
import flask
import masaProduction
from masaProduction.util import hashFile, getCursor, viewImage


@masaProduction.app.route('/accounts/edit/', methods=['GET', 'POST'])
def showEdit():
    """Display /accounts/edit/ route."""
    if 'logname' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    data = {}
    context = {}
    cursor = getCursor()
    data['logname'] = flask.session['logname']
    if flask.request.method == 'POST':
        data['fullname'] = flask.request.form['fullname']
        data['uniqname'] = flask.request.form['uniqname']
        if 'file' in flask.request.files:
            data['hashed_filename'] = hashFile(flask.request)
            # Delete old file
            filename = cursor.execute("SELECT filename\
                                      FROM machinists where\
                                      uniqname = :logname\
                                      ", data).fetchone()['filename']
            os.remove(masaProduction.app.config['UPLOAD_FOLDER'] + "/" + filename)
            cursor.execute("UPDATE machinists SET filename = :hashed_filename,\
                           fullname = :fullname, uniqname = :uniqname WHERE \
                           uniqname = :logname", data)
        elif 'file' not in flask.request.files:
            cursor.execute("UPDATE machinists SET fullname = :fullname,\
             uniqname = :uniqname WHERE uniqname = :logname", data)
        flask.session['logname'] = data['uniqname']
        context['logname'] = flask.session['logname']
        print(data['uniqname'], context['logname'])
        context['filename'] = cursor.execute("SELECT filename FROM machinists\
            WHERE uniqname = :logname", context).fetchone()['filename']
    return flask.render_template("edit.html", **context)
