"""masaProduction about view"""

import flask
import arrow
import masaProduction


@masaProduction.app.route('/about/', methods=('GET', 'POST'))
def showAbout():
    context = {}
    return flask.render_template("about.html", **context)