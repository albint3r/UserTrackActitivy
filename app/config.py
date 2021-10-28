import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Track user activity
    SQLALCHEMY_ECHO = False
    WTF_CSRF_SECRET_KEY = 'this-is-not-random-but-it-should-be'

    # Configuracion Session
    PERMANENT_SESSION_LIFETIME = timedelta(minutes = 30)

    # Session Config
    SESSION_TYPE = 'redis'