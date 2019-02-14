from datetime import datetime
import aiohttp_jinja2
import aiohttp
from aiohttp import web
from .tasks import fetch_page
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

        content = await fetch_page(self.base_url, ids="com.facebook.lite", language="en")
        data = json.loads(content[5:])
        await insert_app_info(self.mongo, self.collection, data[0][2][0][-1])
        print(type(data), len(data))

        return {
            'content': data[0][2][0][-1]
        }

    @aiohttp_jinja2.template('history.html')
    async def history(self, request):
        return {
            'message': 1
        }

    async def poll_info(self, request):
        data =  {
            'poll_result': {
                'time': str(datetime.now())
            }
        }
        return web.json_response(data)
