"""REST API for comments."""
import flask
import insta485
from insta485.util import get_cursor, check_post_range, check_user


@insta485.app.route('/api/v1/p/<int:postid_url_slug>/comments/',
                    methods=["GET"])
def get_comments(postid_url_slug):
    """Docstring."""
    resp = check_user(flask.session)
    if resp is not None:
        return resp
    context = {}
    data = {}
    cur = get_cursor()
    resp = check_post_range(postid_url_slug, cur)
    if resp is not None:
        return resp
    comment_list = []
    postid = postid_url_slug
    data["comments"] = cur.execute(
        " SELECT * FROM comments "
        "   WHERE postid = ?",
        (postid,)).fetchall()
    for comment in data["comments"]:
        bet = {}
        bet["commentid"] = comment["commentid"]
        bet["owner"] = comment["owner"]
        bet["owner_show_url"] = "/u/"+comment["owner"]
        bet["postid"] = comment["postid"]
        bet["text"] = comment["text"]
        comment_list.append(bet)
    context["comments"] = comment_list
    context["url"] = "/api/v1/p/"+str(postid)+"/comments/"
    return flask.jsonify(**context)


@insta485.app.route('/api/v1/p/<int:postid_url_slug>/comments/',
                    methods=["POST"])
def add_comment(postid_url_slug):
    """Docstring."""
    logname = flask.session["username"]
    context = {}
    cur = get_cursor()
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
