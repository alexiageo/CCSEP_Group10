import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # This key is supposed to prevent CSRF attacks which you are not being tested
    # on for this lab. Please ignore it
    SECRET_KEY = "this-is-a-secret-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = False
    REMEMBER_COOKIE_SECURE = False
    REMEMBER_COOKIE_HTTPONLY = False
