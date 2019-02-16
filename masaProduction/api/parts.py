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
    if context['approved'] == 'true':
        context['link'] = '/parts/'
    else:
        context['link'] = '/readers/'
    return flask.jsonify(**context)


@masaProduction.app.route('/api/v1.0/parts/', methods=["GET"])
def getParts():
    """Docstring."""

    data = {}
    context = {}
    results = []
    cur = getCursor()
    data['approved'] = 'true'
    data["parts"] = cur.execute("SELECT * FROM parts "
                                "WHERE approved = :approved ORDER BY deadline ASC ",
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

@masaProduction.app.route('/api/v1.0/readers/', methods=["GET"])
def getReaders():
    """Docstring."""
    data = {}
    context = {}
    results = []
    cur = getCursor()
    data['approved'] = 'false'
    data["parts"] = cur.execute("SELECT * FROM parts "
                                "WHERE approved = :approved ORDER BY deadline ASC ",
                                (data)).fetchall()
    counter = 0
    for part in data["parts"]:
        counter = counter + 1
        bet = {}
        bet["id"] = part["id"]
        bet["url"] = "/api/v1.0/parts/"+str(part["id"])+"/"
        results.append(bet)
    context["results"] = results
    context["url"] = "/api/v1.0/readers/"
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
    submitter = flask.session['logname']
    deadline = flask.request.form['deadline']
    machinist = 'unassigned'
    designCheck = 'no'
    productionCheck = 'no'
    approved = 'false'
    cur.execute(
        "INSERT INTO parts "
        "   (name, number, deadline, designer, machinist, drawing, designCheck, productionCheck, approved, submitter)"
        "   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (name, number, deadline, designer, machinist, drawing, designCheck, productionCheck, approved, submitter)
    )
    resp = flask.jsonify(**context)
    resp.status_code = 201
    return resp


@masaProduction.app.route('/api/v1.0/parts/<int:id>/delete/', methods=["POST"])
def deletePart(id):
    """Docstring."""
    context = {}
    cur = getCursor()
    context = cur.execute(
        "SELECT designer FROM parts "
        "  WHERE id = ?",
        (id,)
        ).fetchone()
    designer = context['designer']
    logname = flask.session['logname']
    if isAdmin(logname) or logname == designer:
        cur.execute(
            "DELETE FROM parts WHERE id = ?", (id,)).fetchone()
    else:
        flask.flash('you do not have permission to delete this part')
    resp = flask.jsonify(**context)
    resp.status_code = 201
    return resp

@masaProduction.app.route('/api/v1.0/parts/<int:id>/update/', methods=["POST"])
def updatePart(id):
    """Docstring."""
    context = {}
    productionCheck = flask.request.form['productionCheck']
    designCheck = flask.request.form['designCheck']
    cur = getCursor()
    context = cur.execute(
        "SELECT designer FROM parts "
        "  WHERE id = ?",
        (id,)
        ).fetchone()
    designer = context['designer']
    logname = flask.session['logname']
    if isAdmin(logname) or logname == designer:
        cur.execute(
            "UPDATE parts SET productionCheck = ?, designCheck = ? WHERE id = ?", (productionCheck, designCheck, id)).fetchone()
        if productionCheck == 'yes' and designCheck == 'yes':
            # move from readers to parts
            print('moving')
            cur.execute(
            "UPDATE parts SET approved='true' WHERE id = ?", (id,)).fetchone()
        else:
            cur.execute(
            "UPDATE parts SET approved='false' WHERE id = ?", (id,)).fetchone()
    else:
        flask.flash('you do not have permission to update this part')
    resp = flask.jsonify(**context)
    resp.status_code = 201
    return resp

@masaProduction.app.route('/api/v1.0/parts/<int:id>/claim/', methods=["POST"])
def claimPart(id):
    """Docstring."""
    context = {}
    cur = getCursor()
    logname = flask.session['logname']
    cur.execute(
        "UPDATE parts SET machinist = ? WHERE id = ?", (logname, id)).fetchone()
    resp = flask.jsonify(**context)
    resp.status_code = 201
    return resp
