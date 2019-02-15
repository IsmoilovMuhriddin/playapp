
import asyncio
import aiohttp
import json
from .db import get_app_info, insert_app_info
results = []


class Parser:
    results = []

    async def is_permission(self, item):
        if type(item) == list and len(item) == 3:
            if type(item[0]) == str and type(item[1]) == str:
                return True
        return False

    async def parsePermissions(self, items):
        for item in items:
            if await self.is_permission(item):
                self.results.append({
                    'permission': item[0],
                    'description': item[1]
                })
                # print(results)
            if type(item) == list:
                await self.parsePermissions(item)


async def fetch_page(url, ids, language):
    params = {'id': ids, 'xhr': 1, 'hl': language, 'authuser': 0}
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.post(url, params=params) as resp:

            return await resp.text()


async def get_info(url, ids,  mongo, collection, language='en'):
    # check db if exist
    result = await get_app_info(mongo, collection, ids, language)
    # print(result)
    if result is not None:

        return result
    else:
        # fetch data
        data = await fetch_page(url, ids, language)
        data = json.loads(data[5:])
        data = data[0][2][0][65]['42656262'][1]
        parser = Parser()
        parser.results = []
        await parser.parsePermissions(data)
        result = await insert_app_info(mongo, collection, ids, language, parser.results)
        return results


async def get_info_json_from_response(resp):
    data = {}
    return await data
