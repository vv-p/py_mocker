# routes.py
from py_mocker.views import index

WILDCARD = '/{tail:.*}'


def setup_routes(app):
    # it's only one way to handle temporary routes - wildcard route
    app.router.add_get(WILDCARD, index)
    app.router.add_post(WILDCARD, index)
    app.router.add_delete(WILDCARD, index)
    app.router.add_put(WILDCARD, index)
