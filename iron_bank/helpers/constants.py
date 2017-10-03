# -*- coding: utf-8 -*-
"""
Constants
"""
from os import getcwd, getenv
from os.path import join

ENV_DEV = join(getcwd(), '.env-dev')
ENV_PROD = join(getcwd(), '.env')

APP_SETTINGS = getenv('APP_SETTINGS')
QUANDL_API_KEY = getenv('QUANDL_API_KEY')
