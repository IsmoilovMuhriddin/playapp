
import asyncio
import aiohttp


async def fetch_page(url, ids, language):
    params = {'id': ids, 'xhr': 1, 'hl': language, 'authuser': 0}
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.post(url, params=params) as resp:
            # print(resp.status)
            # print(await resp.text())
            return await resp.text()


async def get_info_json_from_response(resp):
    data = {}
    return await data
