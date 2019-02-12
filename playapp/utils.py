import os

import pytz
import yaml
from aiohttp import web



def load_config(fname):
    with open(fname, 'rt') as f:
        data = yaml.load(f)
    
    return data

