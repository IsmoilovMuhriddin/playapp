
import aiohttp_jinja2
class SiteHandler:
    def __init__(self, mongo=None):
        self._mongo = mongo

    @property
    def mongo(self):
        return self._mongo

    @aiohttp_jinja2.template('main.html')
    async def mainpage(self, request):
        return {
            'message': 1
        }
