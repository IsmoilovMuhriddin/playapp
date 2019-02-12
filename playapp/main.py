import asyncio
import logging
import pathlib

from aiohttp import web

PROJ_ROOT = pathlib.Path(__file__).parent.parent

def main():
    app = web.Application()
    web.run_app(app,port=9000)

if __name__=='__main__':
    main()