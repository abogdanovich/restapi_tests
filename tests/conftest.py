"""Configuration file for 'Pytest'
Last updates: 9/24/18
author: Alex Bogdanovich
"""
# -*- coding: utf-8 -*-

import pytest
from blog import Blog


@pytest.fixture(scope="module")
def test_get_status_code_200_resource():
    """test data for simple request"""
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_send_post_request_resource():
    """post data for request"""
    url_object = {
        'method': 'post',
        'url': 'https://jsonplaceholder.typicode.com/posts',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_send_unknown_payload_resource():
    """unknown data for payload"""
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts',
        'headers': '',
        'payload': {'login': 'test', 'password': 'test'}
    }
    return url_object


@pytest.fixture(scope="module")
def test_wrong_request_url_resource():
    """data for wrong request"""
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/abrakadabra',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_get_known_id_resource():
    """simple request to get post data"""
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/1',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_get_unknown_id_resource():
    """data for invalid post id"""
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/666',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_request_wrong_url_resource():
    """data for invalid post request url"""
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/1/test',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_get_comment_id_resource():
    """get all comments for simple post"""
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/1/comments',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def request_wrong_comment_url_res():
    """wrong url for post comments"""
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/1/comments/test',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="session")
def blog_object(request):
    """create an object of basic class"""
    blog = Blog('unit_testing')
    return blog


@pytest.fixture(scope="session")
def rest_api_session(request, blog_object):
    """ We can put here a lot of different preparing
        stuff for our extended unit tests
    """
    blog_object.log('info', 'STARTED check REST testing')

    def end_restapi_session():
        """teardown fixture to finish tests"""

        blog_object.log('info', 'STOPPED check REST testing')

    request.addfinalizer(end_restapi_session)
