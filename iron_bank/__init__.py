# -*- coding: utf-8 -*-
"""
Initialize the APP
"""
from os.path import exists
from dotenv import load_dotenv
from flask import Flask
from flask_googlemaps import GoogleMaps
from quandl import ApiConfig
from .helpers.constants import ENV_DEV, ENV_PROD, APP_SETTINGS, QUANDL_API_KEY

# Load environment variables
if exists(ENV_DEV):
    load_dotenv(ENV_DEV)
elif exists(ENV_PROD):
    load_dotenv(ENV_PROD)

# Flask App
APP = Flask(__name__)
APP.url_map.strict_slashes = False
APP.config.from_object(APP_SETTINGS)
ApiConfig.api_key = QUANDL_API_KEY
GoogleMaps(APP)
