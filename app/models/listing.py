from app import db

class Listing(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    body = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    visits_log = db.relationship('TrackSite', backref = 'listing', lazy = 'dynamic')