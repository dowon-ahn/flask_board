import os
import mysql.connector
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column


BASE_DIR = os.path.dirname(__file__)
SECRET_KEY = "dev"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:tkarnr90!@A@localhost:3306/TEST'
SQLALCHEMY_TRACK_MODIFICATIONS = False
