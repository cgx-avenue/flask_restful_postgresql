from flask_sqlalchemy import SQLAlchemy
'''
YSP 2021-11-17
please do the following to create tables in db
1. flask shell
2. from models import db
3. db.create_all()

YSP 2021-11-18
it seems only in this way, the db is used as singleton in this program.
''' 
db = SQLAlchemy()