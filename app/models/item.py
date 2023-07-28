from app import db

class Item(db.Model):
    __tablename__='Items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String)
    name = db.Column(db.String)
    #home
    home_id = db.Column(db.Integer, db.ForeignKey('home.id'), nullable=True)
    home = db.relationship('Home', back_populates='items')