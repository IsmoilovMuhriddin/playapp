import os

import motor.motor_asyncio as aiomotor
import yaml


def load_config(fname):
    with open(fname, 'rt') as f:
        data = yaml.load(f)

    return data


async def init_mongo(conf, loop):
    host = os.environ.get('DB_HOST', conf["host"])
    conf['host'] = host
    
    mongo_uri = f'mongodb://{conf["host"]}:{conf["port"]}'
    conn = aiomotor.AsyncIOMotorClient(
        mongo_uri,
        io_loop=loop
    )
    db_name = conf['database']
    return conn[db_name]
