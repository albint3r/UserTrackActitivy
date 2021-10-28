from datetime import datetime
from app import db

class TrackSite(db.Model):

    id = db.Column(db.Integer, primary_key= True, unique= True)
    no_visits = db.Column(db.Integer)
    ip_adress = db.Column(db.String(80))
    request_url = db.Column(db.String(80))
    referer_page = db.Column(db.String(80))
    page_name = db.Column(db.String(80))
    query_string = db.Column(db.String(80))
    user_agent = db.Column(db.String(80))
    is_unique = db.Column(db.String(80), default=0)
    access_date = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'))

    def __repr__(self):
        return f'Url pagina: {self.page_name}\nVisitante: {self.user_id}\nDueno:{self.listing_id}\n\n'

    def __str__(self):
        return self.request_url


