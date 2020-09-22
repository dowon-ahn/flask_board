import os
import mysql.connector
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column


BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:a1299@localhost:3306/TEST'
SQLALCHEMY_TRACK_MODIFICATIONS = False
