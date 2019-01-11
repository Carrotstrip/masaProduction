"""REST API for profile."""
import flask
import masaProduction
from masaProduction.util import getCursor


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


@masaProduction.app.route('/api/v1/p/<int:postid_url_slug>/comments/',
                    methods=["POST"])
def addComment(postid_url_slug):
    """Docstring."""
    logname = flask.session["username"]
    context = {}
    cur = getCursor()
    resp = check_user(flask.session)
    if resp is not None:
        return resp
    resp = check_post_range(postid_url_slug, cur)
    if resp is not None:
        return resp
    text = flask.request.json["text"]
    postid = postid_url_slug
    cur.execute(
        "INSERT INTO comments "
        "   (owner, postid, text)"
        "   VALUES (?, ?, ?)",
        (logname, postid, text)
    )
    context["commentid"] = cur.execute(
        " SELECT last_insert_rowid()"
        ).fetchone()["last_insert_rowid()"]
    context["owner"] = logname
    context["owner_show_url"] = "/u/"+logname
    context["postid"] = postid
    context["text"] = text
    resp = flask.jsonify(**context)
    resp.status_code = 201
    return resp
