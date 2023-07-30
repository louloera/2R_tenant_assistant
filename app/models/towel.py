from app import db

class Towel(db.Model):
    __tablename__='Towels'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String)
    # home
    home_id = db.Column(db.Integer, db.ForeignKey('homes.id'), nullable=False)