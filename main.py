# -*- coding: utf-8 -*-
"""
Run Flask app
"""
from iron_bank.index import APP

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=8501, debug=True)
