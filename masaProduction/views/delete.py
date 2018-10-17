"""
masaProduction delete view.

URLs include:

"""
import flask
import masaProduction


@masaProduction.app.route('/accounts/delete/', methods=['GET', 'POST'])
def showDelete():
    """Display /accounts/delete/ route."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    context = {}
    data = {}
    d_b = masaProduction.model.getDb()
    cursor = d_b.cursor()
    data['username'] = flask.session['username']
    if flask.request.method == 'POST':
        cursor.execute("DELETE FROM users WHERE username = :username", data)
        flask.session.clear()
        return flask.redirect(flask.url_for("show_create"))
    return flask.render_template("delete.html", **context)
