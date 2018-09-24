"""Python tests to check the given endpoints like
https://jsonplaceholder.typicode.com/posts
https://jsonplaceholder.typicode.com/posts/<id>
https://jsonplaceholder.typicode.com/posts/<id>/comments
Last updates: 9/24/18
author: Alex Bogdanovich
"""
# -*- coding: utf-8 -*-

import logging
from os import path
from time import strftime
import requests
import json
import pandas


class Blog(object):
    """Main class with required funcs and helpers"""

    logging_level = 'INFO'
    time_format = '%Y-%m-%d_%H-%M-%S'

    # Unique log file name
    log_dir = './tests/logs'

    # Init logger for common messages
    logger = logging.getLogger('Common')

    def __init__(self, log_name='restapi_test'):
        """Init func with logging setup"""

        log_path = path.join(self.log_dir, '{name}_{time}.log'.format(
            name=log_name, time=strftime(self.time_format)
            )
        )

        if self.logging_level.upper() == 'DEBUG':
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

        # Add console handler to logger
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(
            logging.Formatter('%(asctime)s %(message)s')
        )
        self.logger.addHandler(stream_handler)

        # Add file handler to logger
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s %(message)s')
        )
        self.logger.addHandler(file_handler)

    def log(self, _level='info', _str=None):
        """Logging func to write logging"""

        if _level == 'error':
            self.logger.error(_str)
        else:
            self.logger.info(_str)

    def get_url(self, dto):
        """get url data"""
        if dto['method'] == 'post':
            return requests.post(
                url=dto['url'],
                headers=dto['headers'],
                data=dto['payload'])
        else:
            return requests.get(
                url=dto['url'],
                headers=dto['headers'],
                data=dto['payload'])


def main():
    """main func to create class instance"""

    # self checking for this unit

    blog = Blog()
    url_object = {
        'method': 'get',
        'url': 'http://google.com',
        'headers': '',
        'payload': {}
    }

    blog.log('info', 'self checking with google.com')
    page = blog.get_url(url_object)
    blog.log('info', 'request google.com > {}'.format(page.status_code))

    if page.status_code == 200:
        blog.log('info', 'google page is successfully transffered')
    else:
        blog.log('info', 'something is not OK with google :) ')


if __name__ == '__main__':
    main()
