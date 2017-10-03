# -*- coding: utf-8 -*-
"""
Crete Plot
"""
import requests
import pygal
from .helpers.constants import QUANDL_API_KEY


def ticker(symbol: str, rows: str):
    'Return data for given ticker symbol'
    quandl_api = 'https://www.quandl.com/api/v3/datasets'
    database_code = 'WIKI'
    dataset_code = '{}.json'.format(symbol)
    rows = 'rows={}'.format(rows)
    api_key = 'api_key={}'.format(QUANDL_API_KEY)
    return requests.get('{}/{}/{}?{}&{}'.format(
        quandl_api, database_code, dataset_code, rows, api_key)).json()


def plot(stock_data):
    'plot'
    data = stock_data['dataset']['data']
    box_plot = pygal.Box()
    box_plot.title = stock_data['dataset']['name']
    lowest = 999999
    for daily_data in data:
        box_plot.add(daily_data[0], [
            daily_data[1], daily_data[2], daily_data[3], daily_data[4]
        ])
        lowest = min(lowest, daily_data[3])
    box_plot.zero = int(lowest)
    return box_plot.render_data_uri()
