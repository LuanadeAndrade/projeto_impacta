def register_routes(api):
    from app.user import register_routes as attach_user
    from app.matrizProspeccao import register_routes as attach_matrizProspeccao
    from app.servidor import register_routes as attach_log
    #from app.Fechamento.ajuste import register_routes as attach_ajustes
    #from app.apelido import register_routes as attach_apelido
    #from app.widget import register_routes as attach_widget

    # Add routes
    attach_user(api)
    attach_matrizProspeccao(api)
    attach_log(api)

    #attach_ajustes(api)
    #attach_apelido(api)
    #attach_widget(api)