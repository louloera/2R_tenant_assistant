from app import db

class Host(db.Model):
    __tablename__='hosts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password=db.Column(db.String)
    username = db.Column(db.String, unique=True)
    # homes
    initiation_date= db.Column(db.DateTime)
    email = db.Column(db.String(120), unique=True)
    homes = db.relationship('Home', back_populates='host', lazy=True)



    
