
from db import db
class UserModel(db.Model):
    __tablename__ = 'user'
 
    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
 
    def __init__(self, name,age):
        self.name = name
        self.age = age
 
    def __repr__(self):
        return f"{self.name}:{self.age}"
    
    def json(self):
        return {
            'id':self.id,
            'name':self.name,
            'age':self.age
        }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()