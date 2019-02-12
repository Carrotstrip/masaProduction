"""REST API for editing account."""
import flask
import masaProduction
from masaProduction.util import getCursor, hashFile

@masaProduction.app.route('/api/v1.0/u/<string:initUniqname>/edit/', methods=["POST"])
def editAccount(initUniqname):
    """Docstring."""
    """Right now this function replaces everything even if you put nothing in there, maybe we make it
    only replace things that you actually changed in the edit form?"""
    context = {}
    data = {}
    cur = getCursor()
    uniqname = flask.request.form['uniqname']
    if 'profilePic' in flask.request.files:
        profilePic = hashFile(flask.request.files, 'profilePic')
    else:
        profilePic = cur.execute("SELECT profilePic FROM machinists WHERE uniqname = ?", (uniqname,)).fetchone()['profilePic']
    fullName = flask.request.form['fullName']
    password = flask.request.form['password']
    data['profilePic'] = profilePic
    data['fullName'] = fullName
    data['uniqname'] = uniqname
    data['password'] = password
    data['logname'] = initUniqname
    data['millStatus'] = flask.request.form['millStatus']
    data['latheStatus'] = flask.request.form['latheStatus']
    data['cncMillStatus'] = flask.request.form['cncMillStatus']
    data['cncLatheStatus'] = flask.request.form['cncLatheStatus']
    data['haasStatus'] = flask.request.form['haasStatus']
    data['available'] = flask.request.form['available']
    """here just check if any of these fields are empty strings, and if they are then set them to whatever
    they already are in the database, which will involve a query. better way? maybe if it's empty tell the update query to
    not update that column? how?"""
    flask.session['logname'] = uniqname
    cur.execute("UPDATE machinists SET profilePic = :profilePic, "
                           " fullname = :fullName, uniqname = :uniqname, password = :password, millStatus = :millStatus, "
                           " latheStatus = :latheStatus, cncMillStatus = :cncMillStatus, cncLatheStatus = :cncLatheStatus, "
                           " haasStatus = :haasStatus, available = :available "
                           " WHERE uniqname = :logname", data)
    resp = flask.jsonify(**context)
    resp.status_code = 201
    return resp
