from app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(), unique= True)
    visits_log = db.relationship('TrackSite', backref = 'user', lazy = 'dynamic')
    listing = db.relationship('Listing', backref='user', lazy='dynamic')

    def __repr__(self):
        return self.username