from app import db
from flask import request, session
from app.models.listing import Listing
from app.models.track_site import TrackSite
from app.models.user import User

def track_visitor():
    """Seguimiento del comportamiento del Usuario web de las url que visita. Creando relaciones
    entre el usuerio y el listing que visito. La Base de datos es relacional: One to Many
    Las tablas que se relacionan en este proceso son:

        1) User
        2) Listing
        3) TrackSite (Tabla de Comportamiento del usuario)

    Esta funcion requiere correr en @bp.before_request.
    """

    # 1) Identificar si el usuario existe
    session.user = db.session.query(User).filter_by(id = 2).first()
    session.listing = db.session.query(Listing).filter_by(id= request.view_args.get('id')).first() #<- Existe listing?

    # Capturar Valores del Request
    ip_address = request.remote_addr
    requested_url = request.url # <- Current url
    referer_page = request.referrer
    page_name = request.path
    query_string = request.query_string
    user_agent = request.user_agent.string

    # El Usuario no existe o esta identificado
    if session.user is None:

        if session.listing is not None and  requested_url != referer_page: # <- Navega en un listing
            session.prev_page = requested_url
            log_visitor(ip_address, requested_url,
                        referer_page, page_name, query_string, user_agent,
                        listing_id = session.listing.id)

        elif session.listing is None and  requested_url != referer_page:  # <- No Navega a un listing
            session.prev_page = requested_url
            log_visitor(ip_address, requested_url,referer_page, page_name, query_string, user_agent)

    # El Usuario existe
    elif session.user is not None:

        if session.listing is not None and requested_url != referer_page: # <- Navega en un listing
            session.prev_page = requested_url
            log_visitor(ip_address, requested_url,
                    referer_page, page_name, query_string, user_agent,
                    user_id =session.user.id, listing_id = session.listing.id)

        elif session.listing is None and requested_url != referer_page:  # <- No Navega a un listing
            session.prev_page = requested_url
            log_visitor(ip_address, requested_url,referer_page, page_name,
                        query_string, user_agent, user_id =session.user.id)


def log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent, user_id=None,
                listing_id=None, no_visits=None):
    """Guarda el comportamiento de usuario en la tabla TrackSite"""

    traking = TrackSite(
        no_visits=no_visits,
        ip_adress=ip_address,
        request_url=requested_url,
        referer_page=referer_page,
        page_name=page_name,
        query_string=query_string,
        user_agent=user_agent,
        user_id=user_id,
        listing_id=listing_id
    )

    try:
        db.session.add(traking)
        db.session.commit()
        id = traking.id
        return id

    except Exception as e:
        pass
        print(e)