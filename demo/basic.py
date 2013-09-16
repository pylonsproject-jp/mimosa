from pyramid.config import Configurator

def index(request):
    return ""

def setup_admin(config):
    config.add_admin_site(None, "demo")


config = Configurator()
config.include("pyramid_debugtoolbar")
config.include("pyramid_layout")
config.include("deform_bootstrap")
config.add_layout("mimosa.layouts.BaseLayout", template="mimosa:templates/base.mako")
config.add_view(index, renderer="json")
config.include("mimosa")
config.include(setup_admin, route_prefix="admin-demo")
application = config.make_wsgi_app()