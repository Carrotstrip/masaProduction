"""REST API for parts."""
import flask
import masaProduction
from masaProduction.util import getCursor, hashFile, isAdmin


@masaProduction.app.route('/api/v1.0/parts/<int:id>/', methods=["GET"])
def getPart(id):
    """Docstring."""

    context = {}
    cur = getCursor()
    context = cur.execute(
        "SELECT * FROM parts "
        "  WHERE id = (?)",
        (id,)
        ).fetchone()
    return flask.jsonify(**context)


@masaProduction.app.route('/api/v1.0/parts/', methods=["GET"])
def getParts():
    """Docstring."""

    data = {}
    context = {}
    results = []
    cur = getCursor()
    data["parts"] = cur.execute("SELECT * FROM parts "
                                "  ORDER BY deadline ASC ",
                                (data)).fetchall()
    counter = 0
    for part in data["parts"]:
        counter = counter + 1
        bet = {}
        bet["id"] = part["id"]
        bet["url"] = "/api/v1.0/parts/"+str(part["id"])+"/"
        results.append(bet)
    context["results"] = results
    context["url"] = "/api/v1.0/parts/"
    return flask.jsonify(**context)


@masaProduction.app.route('/api/v1.0/request/', methods=["POST"])
def requestPart():
    """Docstring."""
    context = {}
    cur = getCursor()
    # cadModel = hashFile(flask.request.files, 'cadModel')
    drawing = hashFile(flask.request.files, 'drawing')
    name = flask.request.form['partName']
    number = flask.request.form['partNumber']
    designer = flask.request.form['designer']
    deadline = flask.request.form['deadline']
    machinist = 'unassigned'
    designCheck = 'no'
    productionCheck = 'no'
    cur.execute(
        "INSERT INTO parts "
        "   (name, number, deadline, designer, machinist, drawing, designCheck, productionCheck)"
        "   VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (name, number, deadline, designer, machinist, drawing, designCheck, productionCheck)
    )
    resp = flask.jsonify(**context)
    resp.status_code = 201
    return resp


@masaProduction.app.route('/api/v1.0/parts/<int:id>/delete/', methods=["POST"])
def deletePart(id):
    """Docstring."""
    context = {}
    cur = getCursor()
    print('deleting')
    context = cur.execute(
        "SELECT designer FROM parts "
        "  WHERE id = ?",
        (id,)
        ).fetchone()
    designer = context['designer']
    logname = flask.session['logname']
    print(designer)
    print(logname)
    if isAdmin(logname) or logname == designer:
        cur.execute(
            "DELETE FROM parts WHERE id = ?", (id,)).fetchone()
    else:
        flask.flash('you do not have permission to delete this part')
    resp = flask.jsonify(**context)
    resp.status_code = 201
    return resp
