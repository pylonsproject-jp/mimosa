<!DOCTYPE html>
<html>
    <head>
        <title><%block name="title"></%block></title>
        <link rel="stylesheet" type="text/css" href="${request.static_url('deform_bootstrap:static/deform_bootstrap.css')}">
    </head>
    <body>
        <div class="navbar">
            <div class="navbar-inner">
                <a href="#" class="brand">Mimosa</a>
            </div>
        </div>
        ${next.body()}
    </body>
</html>