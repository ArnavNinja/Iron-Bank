# -*- coding: utf-8 -*-
"""
Flask App Configuration
"""
class Config(object):
    'Default configuration'
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    'Production configuration'
    DEBUG = False
    API_VERSION = '0.0.1'


class StagingConfig(Config):
    'Staging configuration'
    DEVELOPMENT = True
    DEBUG = True
    API_VERSION = 'staging'


class DevelopmentConfig(Config):
    'Development configuration'
    DEVELOPMENT = True
    DEBUG = True
    API_VERSION = 'development'


class TestingConfig(Config):
    'Testing configuration'
    TESTING = True
    API_VERSION = 'testing'
