from pyramid.config import Configurator

config = Configurator()
config.include("mimosa")
application = config.make_wsgi_app()

