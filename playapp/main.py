import asyncio
import logging
import pathlib

import aiohttp_jinja2
import jinja2

from aiohttp import web
from playapp.utils import (load_config)
from playapp.routes import setup_routes
from playapp.views import SiteHandler

PROJ_ROOT = pathlib.Path(__file__).parent.parent
TEMPLATES_ROOT = pathlib.Path(__file__).parent / 'templates'


def setup_jinja(app):
    jinja_env = aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(str(TEMPLATES_ROOT)))

    

async def init(loop):
    conf = load_config(PROJ_ROOT / 'config' / 'config.yml')
    app = web.Application(loop=loop)
    
    setup_jinja(app)
    
    handler = SiteHandler()
    setup_routes(app, handler, PROJ_ROOT)

    host,port = conf['host'],conf['port']
    return app,host,port



def main():
    loop = asyncio.get_event_loop()
    app,host,port = loop.run_until_complete(init(loop))
    web.run_app(app,host=host,port=port)

if __name__=='__main__':
    main()