from app import db
from app.listing import config
from flask import request, session
from app.models.track_site import TrackSite


def log_visitor(ip_address, requested_url,
                referer_page, page_name, query_string, user_agent, no_visits=None):
    id = 0

    if no_visits == None:

        traking  = TrackSite(
            no_visits= no_visits,
            ip_adress= ip_address,
            request_url= requested_url,
            referer_page= referer_page,
            page_name= page_name,
            query_string= query_string,
            user_agent= user_agent
        )

    else:
        traking = TrackSite(
            ip_adress=ip_address,
            request_url=requested_url,
            referer_page=referer_page,
            page_name=page_name,
            query_string=query_string,
            user_agent=user_agent)

    try:
        db.session.add(traking)
        db.session.commit()
        id = traking.id
        return id

    except Exception as e:
        pass
        # print(e)

def track_visitor():

    # Valida que se pueda ingresar Cookies al cliente
    if not config.is_tracking_allowed():
        print(f'No se corrio nada')
        return

    else: # <- Agrega Valores del Request del cliente

        print(f'Se esta capturando informacion ')

        ip_address = request.remote_addr
        requested_url = request.url
        referer_page = request.referrer
        page_name = request.path
        query_string = request.query_string
        user_agent = request.user_agent.string

        if config.track_session(): # <- En caso de ser permitido el trackeo el cliente
            print('se esta corriendo el if ')

            id = session['id'] if 'id' in session else 0
            no_visits = session['no_visits'] or None
            current_page = request.url
            previous_page = session['current_page'] if 'current_page' in session else ''

            if previous_page != current_page:
                log_visitor(ip_address, requested_url, referer_page, # <- Loguea nueva actividad
                            page_name, query_string, user_agent, no_visits)

        else:
            print('se esta corriendo el else')
            session.modified = True

            try:
                print('se esta corriendo el try')
                id = log_visitor(ip_address, requested_url, referer_page, page_name, query_string, user_agent)
                print('id', id)

                if id > 0:
                    pass

            except Exception as e:
                print('se esta corriendo el except')
                print(e)
                session['track_session'] = False








