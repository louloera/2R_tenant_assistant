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
    towel = db.relationship('Towel', back_populates='home', lazy=True)
    # trash 
    trash = db.relationship('Trash', back_populates='home', lazy=True)



    def to_dict(self):
        return {
                'home_id': self.id,
                'name': self.name,
                'host_id':self.host_id,
                'address':self.address,
                'checkout': self.checkout_time
                
        }

    @classmethod
    def get_attributes(cls):
        return 'name', 'address', 'checkout'
    
    @classmethod
    def from_dict(cls, request_body):
        home = cls(
                    address=request_body['address'],
                    name=request_body['name'],
                    host_id=request_body.get('host_id'),
                    checkout_time = request_body['checkout']
                    )
        return home



