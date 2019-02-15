from datetime import datetime
import aiohttp_jinja2
import aiohttp
from aiohttp import web
from .tasks import get_info
import json
from .db import insert_app_info


class SiteHandler:
    def __init__(self, mongo=None, conf=None, loop=None):
        self._mongo = mongo
        self.base_url = conf['play_store_url']
        self.loop = loop
        self.collection = conf['mongo']['collection']

    @property
    def mongo(self):
        return self._mongo

    @aiohttp_jinja2.template('main.html')
    async def mainpage(self, request):
        return {
            'content': 'someText'
        }

    @aiohttp_jinja2.template('history.html')
    async def history(self, request):
        return {
            'message': 1
        }

    async def poll_info(self, request):
        body = await request.json()
        result_data = {}
        lang='en'
        #s(body.keys(), request, body['id'])
        if body['id']:
            if 'hl' in body.keys():
                lang = body['hl']
            
            result_data = await get_info(
                self.base_url, ids=body['id'],
                mongo=self.mongo, collection=self.collection,
                language=lang)

        return web.json_response(result_data)
