import click

from aiohttp import web
from .routes import setup_routes


@click.command()
def run():
    app = web.Application()
    setup_routes(app)
    web.run_app(app)


if __name__ == '__main__':
    run()
