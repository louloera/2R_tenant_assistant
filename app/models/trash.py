from app import db

class Trash(db.Model):
    __tablename__='Trash'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    days= db.Column(db.String)
    time= db.Column(db.Integer)
    #home
    home_id = db.Column(db.Integer, db.ForeignKey('homes.id'), nullable=False)
    home = db.relationship('Home', back_populates='trash')


    def to_dict(self):
        return {
                'trash_id': self.id,
                'days': self.days,
                'time': self.time,
                'host_id':self.home_id
        }

    @classmethod
    def get_attributes(cls):
        return 'days', 'time'
    
    @classmethod
    def from_dict(cls, request_body):
        trash = cls(
                    days=request_body['days'],
                    time=request_body['time'],
                    home_id=request_body.get('home_id')
                    )
        return trash
