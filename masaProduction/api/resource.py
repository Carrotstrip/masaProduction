"""REST API for resources."""
import flask
import masaProduction


@masaProduction.app.route('/api/v1/', methods=["GET"])
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
