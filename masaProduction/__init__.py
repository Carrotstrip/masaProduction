"""masaProduction package initializer."""

import flask
import os
from flask_mail import Mail, Message
# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'austinwolfy@gmail.com',
    "MAIL_PASSWORD": 'jabujabu1'
}

app.config.update(mail_settings)
mail = Mail(app)
# Read settings from config module (masaProduction/config.py)
app.config.from_object('masaProduction.config')

# Overlay settings read from file specified by environment variable. This is
# useful for using different on development and production machines.
# Reference: http://flask.pocoo.org/docs/0.12/config/
app.config.from_envvar('MASAPRODUCTION_SETTINGS', silent=True)

# Tell our app about views and model.  This is dangerously close to a
# circular import, which is naughty, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/0.12/patterns/packages/)  We're
# going to tell pylint and pycodestyle to ignore this coding style violation.
import masaProduction.views  # noqa: E402  pylint: disable=wrong-import-position
import masaProduction.model  # noqa: E402  pylint: disable=wrong-import-position
import masaProduction.api  # noqa: E402  pylint: disable=wrong-import-position
