import os

import pytz
import yaml
from aiohttp import web

import motor.motor_asyncio as aiomotor


def load_config(fname):
    with open(fname, 'rt') as f:
        data = yaml.load(f)

    return data


async def init_mongo(conf, loop):
    host = os.environ.get('DOCKER_MACHINE_IP', '127.0.0.1')
    conf['host'] = host
    mongo_uri = f'mongodb://{conf["host"]}:{conf["port"]}'
    conn = aiomotor.AsyncIOMotorClient(
        mongo_uri,
        io_loop=loop
    )
    db_name = conf['database']
    return conn[db_name]
