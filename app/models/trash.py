from app import db

class Trash(db.Model):
    __tablename__='Trash'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    days= db.Column(db.String)
    time= db.Column(db.Integer)
    #home
    home_id = db.Column(db.Integer, db.ForeignKey('homes.id'), nullable=False)