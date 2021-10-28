from flask import Flask, session
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.listing.route import bp as listing_bp
app.register_blueprint(listing_bp)

from app.models.user import User
from app.models.track_site import TrackSite
from app.models.listing import Listing
