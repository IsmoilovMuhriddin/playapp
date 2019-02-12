import os

import pytz
import yaml
from aiohttp import web
from dateutil.parser import parse



def load_config(fname):
    with open(fname, 'rt') as f:
        data = yaml.load(f)
    
    return data