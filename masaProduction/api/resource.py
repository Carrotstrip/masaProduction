"""REST API for resources."""
import flask
import insta485
from insta485.util import check_user


@insta485.app.route('/api/v1/', methods=["GET"])
def get_urls():
    """Docstring."""
    resp = check_user(flask.session)
    if resp is not None:
        return resp
    context = {}
    # url
    context["url"] = "/api/v1/"
    context["posts"] = "/api/v1/p"

    return flask.jsonify(**context)
