""" Configuration file for 'Pytest'.
    More info about conftest.py:
    https://docs.pytest.org/en/2.7.3/plugins.html?highlight

    ---------------------------------------------------------------------------
    Conftest content
    ---------------------------------------------------------------------------
    TODO: add pytest fixtures
"""
# -*- coding: utf-8 -*-
import pytest
from blog import Blog


@pytest.fixture(scope="module")
def test_get_status_code_200_resource():
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts',
        'headers': '',
        'payload': {}
    }
    return url_object

@pytest.fixture(scope="module")
def test_send_post_request_resource():
    url_object = {
        'method': 'post',
        'url': 'https://jsonplaceholder.typicode.com/posts',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_send_unknown_payload_resource():
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts',
        'headers': '',
        'payload': {'login': 'test', 'password': 'test'}
    }
    return url_object


@pytest.fixture(scope="module")
def test_wrong_request_url_resource():
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/abrakadabra',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_get_known_id_resource():
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/1',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_get_unknown_id_resource():
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/666',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_request_wrong_url_resource():
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/1/test',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_get_known_comment_id_resource():
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/1/comments',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="module")
def test_request_wrong_comment_url_resource():
    url_object = {
        'method': 'get',
        'url': 'https://jsonplaceholder.typicode.com/posts/1/comments/test',
        'headers': '',
        'payload': {}
    }
    return url_object


@pytest.fixture(scope="session")
def blog_object(request):
    """create a basic class"""
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
