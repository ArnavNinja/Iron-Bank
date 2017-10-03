# -*- coding: utf-8 -*-
"""
Iron Bank
"""
from flask import render_template
from . import APP
from .plot import ticker, plot


@APP.route('/')
def home():
    """
    Show home page
    """
    return render_template('index.html')


@APP.route('/<symbol>')
def show_plot(symbol):
    """
    Show daily plot
    """
    symbol = symbol.upper()
    stock_data = ticker(symbol, 5)
    page_title = stock_data['dataset']['name']
    return render_template(
        'plot.html', page_title=page_title, graph_data=plot(stock_data))
