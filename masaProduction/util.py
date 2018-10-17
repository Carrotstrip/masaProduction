"""A collection of utility functions for the views modules"""

"""masaProduction model (database) API."""
import os
import shutil
import uuid
import hashlib
import tempfile
import masaProduction


def hashPassword(password):
    """."""
    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string


def getSalt(hashed_password):
    """."""
    salt = hashed_password[hashed_password.find("$")
                           + 1:hashed_password.
                           find("$", hashed_password.find("$")+2)]
    return salt


# takes the raw input password and the hashed db password
# and returns whether the credentials are correct


def matchesDbPassword(input_pass, db_hashed):
    """."""
    algorithm = 'sha512'
    salt = getSalt(db_hashed)
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + input_pass
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string == db_hashed


def sha256sum(filename):
    """Return sha256 hash of file content, similar to UNIX sha256sum."""
    content = open(filename, 'rb').read()
    sha256_obj = hashlib.sha256(content)
    return sha256_obj.hexdigest()


def hashFile(request):
    """."""
    # Save POST request's file object to a temp file
    dummy, temp_filename = tempfile.mkstemp()
    file = request["file"]
    file.save(temp_filename)

    # Compute filename
    hash_txt = sha256sum(temp_filename)
    dummy, suffix = os.path.splitext(file.filename)
    hash_filename_basename = hash_txt + suffix
    hash_filename = os.path.join(
        masaProduction.app.config["UPLOAD_FOLDER"],
        hash_filename_basename
    )

    # Move temp file to permanent location
    shutil.move(temp_filename, hash_filename)
    masaProduction.app.logger.debug("Saved %s", hash_filename_basename)
    return hash_filename_basename


def followButton(session, request_form, cursor):
    """."""
    data = {}
    data['logname'] = session['username']
    data['username'] = request_form['username']
    if 'follow' in request_form:
        cursor.execute("INSERT INTO following \
        (username1, username2) VALUES (:logname, :username)", data)
    elif 'unfollow' in request_form:
        cursor.execute("DELETE FROM \
        following WHERE username1 = :logname \
        AND username2 = :username", data)


def getCursor():
    """."""
    d_b = masaProduction.model.getDb()
    return d_b.cursor()


def setLognameFollows(cursor, session, username, follow, data):
    """."""
    followers = []
    for item in cursor.execute("SELECT username1 FROM \
    following WHERE username2 = :username", data).fetchall():
        followers.append(item['username1'])
    if session['username'] in followers:
        follow['logname_follows_username'] = True
    elif session['username'] not in followers:
        follow['logname_follows_username'] = False
    elif session['username'] == username:
        follow['logname_follows_username'] = False
