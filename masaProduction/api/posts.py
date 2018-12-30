"""REST API for posts."""
import flask
import insta485
from insta485.util import get_cursor, check_post_range, check_user


@insta485.app.route('/api/v1/p/<int:postid_url_slug>/', methods=["GET"])
def get_post(postid_url_slug):
    """Docstring."""
    resp = check_user(flask.session)
    if resp is not None:
        return resp
    context = {}
    cur = get_cursor()
    resp = check_post_range(postid_url_slug, cur)
    if resp is not None:
        return resp
    context["owner"] = cur.execute(
        "SELECT owner FROM posts "
        "  WHERE postid = (?)",
        (postid_url_slug,)
        ).fetchone()["owner"]
    owner = context["owner"]
    context["age"] = cur.execute(
        "SELECT created FROM posts "
        "  WHERE postid = ? ",
        (postid_url_slug,)
        ).fetchone()["created"]
    img_url = cur.execute(
        "SELECT filename FROM posts "
        "  WHERE postid = ? ",
        (postid_url_slug,)
        ).fetchone()['filename']
    context["img_url"] = "/uploads/" + img_url
    owner_img_url = cur.execute(
        "SELECT filename FROM users "
        "  WHERE username = ? ",
        (owner,)
        ).fetchone()["filename"]
    context["owner_img_url"] = "/uploads/" + owner_img_url
    context["owner_show_url"] = "/u/" + owner + "/"
    context["post_show_url"] = "/p/" + str(postid_url_slug) + "/"
    post_url = context["post_show_url"]
    context["url"] = "api/v1" + post_url
    return flask.jsonify(**context)


@insta485.app.route('/api/v1/p/', methods=["GET"])
def get_newest_posts():
    """Docstring."""
    resp = check_user(flask.session)
    if resp is not None:
        return resp
    size = flask.request.args.get('size', default=10, type=int)
    page = flask.request.args.get('page', default=0, type=int)
    if size < 0 or page < 0:
        error = {}
        error["message"] = "Bad Request"
        error["status_code"] = 400
        resp = flask.jsonify(**error)
        resp.status_code = 400
        return resp
    logname = flask.session["username"]
    data = {}
    context = {}
    results = []
    connection = insta485.model.get_db()
    cur = connection.cursor()
    offset = page * size
    data["logname"] = logname
    data["offset"] = offset
    data["size"] = size
    data["posts"] = cur.execute("SELECT * FROM posts "
                                "  WHERE owner = :logname OR owner IN "
                                "  (SELECT username2 FROM "
                                "  following WHERE username1 = :logname) "
                                "  ORDER BY postid DESC "
                                "  LIMIT :size "
                                "  OFFSET :offset ",
                                (data)).fetchall()
    counter = 0
    for post in data["posts"]:
        counter = counter + 1
        bet = {}
        bet["postid"] = post["postid"]
        bet["url"] = "/api/v1/p/"+str(post["postid"])+"/"
        results.append(bet)
    context["results"] = results
    context["url"] = "/api/v1/p/"
    if counter is size:
        page = page + 1
        context["next"] = "/api/v1/p/?size"+str(size)+"&page="+str(page)
    else:
        context["next"] = ""
    return flask.jsonify(**context)
