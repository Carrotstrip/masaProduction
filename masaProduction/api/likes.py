"""REST API for likes."""
import flask
import insta485
from insta485.util import get_cursor, check_post_range, check_user


@insta485.app.route('/api/v1/p/<int:postid_url_slug>/likes/', methods=["GET"])
def get_likes(postid_url_slug):
    """Return likes on postid.

    Example:
    {
      "logname_likes_this": 1,
      "likes_count": 3,
      "postid": 1,
      "url": "/api/v1/p/1/likes/"
    }
    """
    resp = check_user(flask.session)
    if resp is not None:
        return resp

    # User
    logname = flask.session["username"]
    context = {}

    # url
    context["url"] = flask.request.path

    # Post
    postid = postid_url_slug
    context["postid"] = postid

    # Did this user like this post?
    cur = get_cursor()
    resp = check_post_range(postid_url_slug, cur)
    if resp is not None:
        return resp
    cur.execute(
        "SELECT EXISTS( "
        "  SELECT 1 FROM likes "
        "    WHERE postid = ? "
        "    AND owner = ? "
        "    LIMIT 1"
        ") AS logname_likes_this ",
        (postid, logname)
    )
    logname_likes_this = cur.fetchone()
    context.update(logname_likes_this)

    # Likes
    cur.execute(
        "SELECT COUNT(*) AS likes_count FROM likes WHERE postid = ? ",
        (postid,)
    )
    likes_count = cur.fetchone()
    context.update(likes_count)

    return flask.jsonify(**context)


@insta485.app.route("/api/v1/p/<int:postid_url_slug>/likes/", methods=["POST"])
def create_like(postid_url_slug):
    """Docstring."""
    # Creates a like on the given postid
    resp = check_user(flask.session)
    if resp is not None:
        return resp
    # User
    logname = flask.session["username"]
    context = {}
    postid = postid_url_slug
    context["postid"] = postid
    context["logname"] = logname
    # Does the like already exist???
    cur = get_cursor()
    resp = check_post_range(postid_url_slug, cur)
    if resp is not None:
        return resp
    cur.execute(
        "  SELECT * FROM likes "
        "    WHERE postid = ? "
        "    AND owner = ?",
        (postid, logname)
    )
    logname_likes_this = cur.fetchone()
    if logname_likes_this:
        context["status_code"] = 409
        context["message"] = "Conflict"
        resp = flask.jsonify(**context)
        resp.status_code = 409
    else:
        cur.execute(
            "INSERT INTO likes "
            "   (owner, postid)"
            "   VALUES (?, ?)",
            (logname, postid)
        )
        resp = flask.jsonify(**context)
        resp.status_code = 201
    return resp


@insta485.app.route('/api/v1/p/<int:postid_url_slug>/likes/',
                    methods=["DELETE"])
def delete_like(postid_url_slug):
    """Docstring."""
    # Deletes a like on the given postid
    resp = check_user(flask.session)
    if resp is not None:
        return resp
    logname = flask.session["username"]
    postid = postid_url_slug
    connection = insta485.model.get_db()
    cur = connection.cursor()
    resp = check_post_range(postid_url_slug, cur)
    if resp is not None:
        return resp
    cur.execute(
        " DELETE FROM likes "
        "   WHERE postid = ? "
        "   AND owner = ?",
        (postid, logname)
        )
    context = {}
    resp = flask.jsonify(**context)
    resp.status_code = 204
    return resp
