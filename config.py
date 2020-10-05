import os
import mysql.connector
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column


BASE_DIR = os.path.dirname(__file__)
SECRET_KEY = "dev"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='123456789',
    url='ls-0ab8443fb7d01402f1993e62933c010a379f5cd7.c7ziynehz4xe.ap-northeast-2.rds.amazonaws.com',
    db='production')
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pw}@{url}/{db}'.format(
#     user='root',
#     pw='tkarnr90!@A',
#     url='localhost:3306',
#     db='test')
SQLALCHEMY_TRACK_MODIFICATIONS = False
