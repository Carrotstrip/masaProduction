"""
masaProduction user view.

URLs include:

"""
import flask
import masaProduction
from masaProduction.util import hashFile, getCursor


@masaProduction.app.route('/u/<username>/', methods=('GET', 'POST'))
def showUser(username):
    """Display /u/<username>/ route."""
    if 'logname' not in flask.session:
        return flask.redirect(flask.url_for('showLogin'))
    cursor = getCursor()
    if flask.request.method == 'POST':
        data = {}
        data['logname'] = flask.session['username']
        data['username'] = username
        if 'follow' in flask.request.form:
            cursor.execute("INSERT INTO following (username1,\
                           username2) VALUES (:logname, :username)", data)
        elif 'unfollow' in flask.request.form:
            cursor.execute("DELETE FROM following WHERE\
                           username1 = :logname AND username2\
                            = :username", data)
        elif 'create_post' in flask.request.form:

            hash_filename_basename = hashFile(flask.request.files)
            cursor.execute("INSERT INTO posts (filename, owner)\
                           VALUES (?, ?)", [hash_filename_basename,
                                            flask.session['logname']])
        # return flask.redirect(flask.url_for('show_user',
        # username = username))
    context = {}
    context['logname'] = flask.session['logname']
    context['username'] = username
    context['fullname'] = cursor.execute("SELECT fullname\
                                         FROM users WHERE username\
                                         = :username",
                                         context).fetchone()["fullname"]
    context['posts'] = cursor.execute("SELECT * FROM posts\
                                      WHERE owner = :username\
                                      ORDER BY postid DESC",
                                      context).fetchall()

    following = []
    for item in cursor.execute("SELECT username2 FROM following\
                               WHERE username1 = :username",
                               context).fetchall():
        following.append(item['username2'])
    # following = cursor.execute("SELECT username2 FROM
    # following WHERE username1 = :username", context).fetchall()

    followers = []
    for item in cursor.execute("SELECT username1 FROM\
                               following WHERE username2 =\
                               :username", context).fetchall():
        followers.append(item['username1'])

    # followers = [for item in cursor.execute("SELECT username1 FROM
    # following WHERE username2 = :username", context).fetchall()
    # item["username1"]]
    context['following'] = len(following)
    context['followers'] = len(followers)
    context['total_posts'] = len(context['posts'])
    if flask.session['logname'] in followers:
        context['logname_follows_username'] = True
    elif flask.session['logname'] not in followers:
        context['logname_follows_username'] = False
    elif flask.session['logname'] == username:
        context['logname_follows_username'] = False
    return flask.render_template("user.html", **context)
