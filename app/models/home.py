from app import db

class Home(db.Model):
    __tablename__='homes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    # host_id= 
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'), nullable=True)
    host = db.relationship('Host', back_populates='homes')
    address = db.Column(db.String(120))
    checkout_time= db.Column(db.Integer)
    #items=
    items = db.relationship('Item', back_populates='home', lazy=True)
    # towel
    # trash 




