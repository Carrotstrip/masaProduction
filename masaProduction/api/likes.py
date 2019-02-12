"""REST API for likes."""
import flask
import masaProduction
from masaProduction.util import getCursor


@masaProduction.app.route('/api/v1.0/parts/<int:partId>/likes/', methods=["GET"])
def getLikes(partId):
    """Return likes and dislikes on a part."""

    """
    Example:
    {
      "lognameLikesThis": 1,
      "numLikes": 3,
      "partId": 1,
      "url": "/api/v1/p/1/likes/"
    }
    """

    # User
    logname = flask.session["username"]
    context = {}

    # Post
    context["partId"] = partId

    # Did this user like this post?
    cur = getCursor()
    cur.execute(
        "SELECT EXISTS( "
        "  SELECT 1 FROM likes "
        "    WHERE partId = ? "
        "    AND owner = ? "
        "    LIMIT 1"
        ") AS lognameLikesThis ",
        (partId, logname)
    )
    lognameLikesThis = cur.fetchone()
    context.update(lognameLikesThis)

    # Likes
    cur.execute(
        "SELECT COUNT(*) AS numLikes FROM likes WHERE partId = ? ",
        (partId,)
    )
    numLikes = cur.fetchone()
    context.update(numLikes)

    return flask.jsonify(**context)


@masaProduction.app.route("/api/v1/p/<int:postId>/likes/", methods=["POST"])
def createLike(partId):
    """Docstring."""
    # Creates a like on the given postid

    # User
    logname = flask.session["username"]
    context = {}
    context["partId"] = partId
    context["logname"] = logname
    # Does the like already exist???
    cur = getCursor()

    cur.execute(
        "  SELECT * FROM likes "
        "    WHERE partId = ? "
        "    AND owner = ?",
        (partId, logname)
    )
    lognameLikesThis = cur.fetchone()
    if lognameLikesThis:
        context["status_code"] = 409
        context["message"] = "Conflict"
        resp = flask.jsonify(**context)
        resp.status_code = 409
    else:
        cur.execute(
            "INSERT INTO likes "
            "   (owner, postid)"
            "   VALUES (?, ?)",
            (logname, partId)
        )
        resp = flask.jsonify(**context)
        resp.status_code = 201
    return resp


@masaProduction.app.route('/api/v1/p/<int:partId>/likes/',
                    methods=["DELETE"])
def deleteLike(partId):
    """Docstring."""
    # Deletes a like on the given postid

    logname = flask.session["username"]
    cur = getCursor()
    cur.execute(
        " DELETE FROM likes "
        "   WHERE partId = ? "
        "   AND owner = ?",
        (partId, logname)
        )
    context = {}
    resp = flask.jsonify(**context)
    resp.status_code = 204
    return resp
