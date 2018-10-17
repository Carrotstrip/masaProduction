"""
masaProduction logout view.

URLs include:

"""
import flask
import masaProduction


@masaProduction.app.route('/accounts/logout/')
def showLogout():
    """Display /accounts/logout/ route."""
    flask.session.clear()
    return flask.redirect(flask.url_for('showLogin'))
