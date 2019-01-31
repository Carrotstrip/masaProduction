"""REST API for comments on readers."""
import flask
import masaProduction
from masaProduction.util import getCursor, hashFile

@masaProduction.app.route('/api/v1/p/<int:partId>/comments/',
                    methods=["POST"])
def addComment(partId):
    """Docstring."""
    logname = flask.session["username"]
    context = {}
    cur = getCursor()
    text = flask.request.json["text"]
    cur.execute(
        "INSERT INTO comments "
        "   (owner, partId, text)"
        "   VALUES (?, ?, ?)",
        (logname, partId, text)
    )
    context["commentId"] = cur.execute(
        " SELECT last_insert_rowid()"
        ).fetchone()["last_insert_rowid()"]
    context["owner"] = logname
    context["owner_show_url"] = "/u/"+logname
    context["partId"] = partId
    context["text"] = text
    return flask.jsonify(**context)