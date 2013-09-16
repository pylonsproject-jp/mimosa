from pyramid_layout.layout import layout_config


@layout_config(template="mimosa:templates/base.mako")
class BaseLayout(object):
    def __init__(self, context, request):
        pass