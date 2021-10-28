import plotly
import plotly.express as px
from flask import Blueprint, render_template, request, session
from app import db
from app.listing.visitor2 import track_visitor
from app.models.listing import Listing


bp = Blueprint('listing',__name__)

@bp.route('/')
def index():

    return render_template('listing/index.html')

@bp.route('/other')
def other():

    return render_template('listing/index.html')

@bp.route('/dash')
def dash():

    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    plot_as_string = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div') # <- plot offline y Js en header
    return render_template("listing/dash.html", plot=plot_as_string)

@bp.route('/id/<int:id>')
def id(id):

    listing = db.session.query(Listing).filter_by(id = id).first()

    return render_template('listing/listing.html', listing = listing)


@bp.before_request
def count_view():

    track_visitor()
