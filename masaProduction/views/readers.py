"""
masaProduction readers view.

URLs include:

"""
import flask
import masaProduction


@masaProduction.app.route('/readers/')
def showReaders():
    """Display /readers/ route."""
    if 'logname' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    context = {}
    
    return flask.render_template("readers.html", **context)
