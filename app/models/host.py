from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask 

class Host(db.Model):
    __tablename__='hosts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password=db.Column(db.String)
    username = db.Column(db.String, unique=True)
    # homes
    # initiation_date= db.Column(db.DateTime, nullable=True)
    email = db.Column(db.String(120), unique=True)
    homes = db.relationship('Home', back_populates='host', lazy=True)


    def to_dict(self):
        return {
                'host_id': self.id,
                'username': self.username,
                'email': self.email,
                # 'homes': self.homes
        }

    @classmethod
    def get_attributes(cls):
        return 'username', 'password', 'email'
    
    @classmethod
    def from_dict(cls, request_body):
        host = cls(
                    username=request_body['username'],
                    password=request_body['password'],
                    email = request_body['email']
                    )
        return host




    
