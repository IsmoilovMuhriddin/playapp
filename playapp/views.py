import aiohttp_jinja2
from aiohttp import web

from .tasks import get_info


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
            'content': ''
        }

    async def poll_info(self, request):
        body = await request.json()
        result_data = {}
        lang = 'en'
        if body['id']:
            if 'hl' in body.keys():
                lang = body['hl']
                result_data = await get_info(
                    self.base_url, ids=body['id'],
                    mongo=self.mongo, collection=self.collection,
                    language=lang)

        return web.json_response(result_data)
