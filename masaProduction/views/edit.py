"""
masaProduction edit view.

URLs include:

"""
import os
import flask
import shutil
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
    context['profilePic'] = cursor.execute("SELECT profilePic FROM machinists\
        WHERE uniqname = :logname", data).fetchone()['profilePic']
    if flask.request.method == 'POST':
        data['fullname'] = flask.request.form['fullname']
        data['uniqname'] = flask.request.form['uniqname']
        if 'file' in flask.request.files:
            # Delete old file
            profilePic = cursor.execute("SELECT profilePic\
                                      FROM machinists where\
                                      uniqname = :logname\
                                      ", data).fetchone()['profilePic']
            if os.path.exists(masaProduction.app.config['UPLOAD_FOLDER'] + "/" + profilePic):
                os.remove(masaProduction.app.config['UPLOAD_FOLDER'] + "/" + profilePic)
            data['hashed_profilePic'] = hashFile(flask.request.files)
            cursor.execute("UPDATE machinists SET profilePic = :hashed_profilePic,\
                           fullname = :fullname, uniqname = :uniqname WHERE \
                           uniqname = :logname", data)
        elif 'file' not in flask.request.files:
            cursor.execute("UPDATE machinists SET fullname = :fullname,\
             uniqname = :uniqname WHERE uniqname = :logname", data)
        flask.session['logname'] = data['uniqname']
        context['logname'] = flask.session['logname']
        context['profilePic'] = cursor.execute("SELECT profilePic FROM machinists\
            WHERE uniqname = :logname", context).fetchone()['profilePic']
    return flask.render_template("edit.html", **context)
