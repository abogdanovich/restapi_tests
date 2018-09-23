"""Python tests to check the given endpoints like
https://jsonplaceholder.typicode.com/posts
https://jsonplaceholder.typicode.com/posts/<id>
https://jsonplaceholder.typicode.com/posts/<id>/comments
Last updates: 9/23/18
"""

import logging
from os import path
from time import strftime
import requests
import json


class Blog(object):
    """Main class with required funcs and helpers"""

    logging_level = 'INFO'
    time_format = '%Y-%m-%d_%H-%M-%S'

    # Unique log file name
    log_dir = './tests/logs'

    # Init logger for common messages
    logger = logging.getLogger('Common')

    def __init__(self, log_name):
        """Init func with logging setup"""

        log_path = path.join(self.log_dir, '{name}_{time}.log'.format(
            name=log_name, time=strftime(self.time_format)
        )
                             )

        if self.loging_level.upper() == 'DEBUG':
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

        # Add console handler to logger
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
        self.logger.addHandler(stream_handler)

        # Add file handler to logger
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
        self.logger.addHandler(file_handler)

        self.log('info', 'Logging is started {level}'.format(level=self.loging_level))

    def log(self, _level, _str):
        """Logging func to write logging"""

        if _level == 'info':
            self.logger.info(_str)
        else:
            self.logger.error(_str)

    def get_posts(self):
        """get all posts"""
        pass

    def get_post(self):
        """get unique post"""
        pass

    def get_post_comments(self):
        """get all comments for post"""
        pass

def main():
    """main func to create class instance"""


if __name__ == '__main__':
    main()
