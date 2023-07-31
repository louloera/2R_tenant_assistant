from app import db

class Towel(db.Model):
    __tablename__='Towels'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String)
    # home
    home_id = db.Column(db.Integer, db.ForeignKey('homes.id'), nullable=False)
    home = db.relationship('Home', back_populates='towel')


    def to_dict(self):
        return {
                'towel_id': self.id,
                'location': self.location,
                'host_id':self.home_id
        }

    @classmethod
    def get_attributes(cls):
        return ['location']
    
    @classmethod
    def from_dict(cls, request_body):
        trash = cls(
                    location=request_body['location'],
                    home_id=request_body.get('home_id')
                    )
        return trash