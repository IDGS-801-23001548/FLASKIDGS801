import os

from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "ClaveSecretaGOOOOODNoMeLaRobesPorfa"
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/bdidgs801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
