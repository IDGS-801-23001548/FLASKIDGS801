import os

from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "ClaveSecretaGOOOOODNoMeLaRobesPorfa"
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLACHADEMY_DATABASE_URI = 'mysql+mysqldb://root:root@localhost/bdidgs801'
    SQLACHADEMY_TRACK_MODIFICATIONS = False
    
