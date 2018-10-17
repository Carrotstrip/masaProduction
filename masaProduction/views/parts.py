"""
masaProduction parts view.

URLs include:

"""
import flask
import masaProduction


@masaProduction.app.route('/parts/')
def showParts():
    """Display /parts/ route."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    context = {}
    return flask.render_template("parts.html", **context)
