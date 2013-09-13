from pyramid.config import Configurator

def index(request):
    return ""

config = Configurator()
config.add_view(index, renderer="json")
config.include("mimosa")
application = config.make_wsgi_app()

