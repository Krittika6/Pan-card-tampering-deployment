# config.py
import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "krittika-secret-key"

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    UPLOADS = os.path.join(BASEDIR, "app", "static", "uploads")
    ORIGINAL = os.path.join(BASEDIR, "app", "static", "original")
    GENERATED = os.path.join(BASEDIR, "app", "static", "generated")

    SESSION_COOKIE_SECURE = True


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class ProductionConfig(Config):
    pass

