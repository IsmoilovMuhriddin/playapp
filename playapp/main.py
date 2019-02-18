import asyncio
import pathlib
import os
import aiohttp_jinja2
import jinja2
from aiohttp import web

from playapp.routes import setup_routes
from playapp.utils import init_mongo, load_config
from playapp.views import SiteHandler

PROJ_ROOT = pathlib.Path(__file__).parent.parent
TEMPLATES_ROOT = pathlib.Path(__file__).parent / 'templates'


def setup_jinja(app):
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(str(TEMPLATES_ROOT)))


async def setup_mongo(app, conf, loop):
    mongo = await init_mongo(conf['mongo'], loop)

    async def close_mongo(app):
        mongo.client.close()

    app.on_cleanup.append(close_mongo)

    return mongo


async def init(loop):
    conf = load_config(PROJ_ROOT / 'config' / 'config.yml')

    app = web.Application(loop=loop)
    mongo = await setup_mongo(app, conf, loop)

    setup_jinja(app)

    # setup view and routes
    handler = SiteHandler(mongo, conf, loop)
    setup_routes(app, handler, PROJ_ROOT)

    host, port = conf['host'], os.environ.get('PORT',conf['port'])
    return app, host, port


def main():
    loop = asyncio.get_event_loop()
    app, host, port = loop.run_until_complete(init(loop))
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
