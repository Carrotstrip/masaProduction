"""REST API for profile."""
import flask
import masaProduction
from masaProduction.util import getCursor, isAdmin


@masaProduction.app.route('/api/v1.0/u/<string:uniqname>/',
                    methods=['GET'])
def getProfile(uniqname):
    """Gets the profile info for a user.
    
    Profiles consist of the following:
        name
        profile picture
        a list of trainings
        a list of all parts completed
    """
    cur = getCursor()
    context = cur.execute(
        "SELECT * FROM machinists "
        "   WHERE uniqname = ?",
        (uniqname,)).fetchone()
    context['img_url'] = '/uploads/' + context['profilePic']
    return flask.jsonify(**context)

@masaProduction.app.route('/api/v1.0/u/<string:uniqname>/delete/',
                    methods=['POST'])
def deleteAccount(uniqname):
    cur = getCursor()
    context = cur.execute(
        "SELECT * FROM machinists "
        "   WHERE uniqname = ?",
        (uniqname,)).fetchone()
    logname = flask.session['logname']
    if not isAdmin(logname) and uniqname != logname:
        flask.flash('you do not have permission to delete this account')
        return flask.redirect(flask.url_for('showUser', uniqname = logname))
    cur.execute(
        "DELETE FROM machinists "
        "   WHERE uniqname = ?",
        (uniqname,)).fetchone()
    return flask.jsonify(**context)
