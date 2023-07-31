from app import db

class Item(db.Model):
    __tablename__='Items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String)
    name = db.Column(db.String)
    #home
    home_id = db.Column(db.Integer, db.ForeignKey('homes.id'))
    home = db.relationship('Home', back_populates='items')


    def to_dict(self):
        return {
                'item_id': self.id,
                'home_id': self.id,
                'name': self.name,
                'location':self.location
        }

    @classmethod
    def get_attributes(cls):
        return 'name', 'location'
    
    @classmethod
    def from_dict(cls, request_body):
        home = cls(
                    location=request_body['location'],
                    name=request_body['name'],
                    home_id=request_body.get('home_id')
                    )
        return home
