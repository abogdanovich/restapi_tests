"""Python tests to check the given endpoints l
https://jsonplaceholder.typicode.com/posts/<id>
Last updates: 9/24/18
author: Alex Bogdanovich
"""
# -*- coding: utf-8 -*-

import pytest


def test_get_known_id(blog_object, test_get_known_id_resource):
    """get status code 200"""

    blog_object.log('info', 'test_get_known_id: get status code 200')
    response = blog_object.get_url(test_get_known_id_resource)
    assert response.status_code == 200


def test_compare_post_title(blog_object, test_get_known_id_resource):
    """get title and check it"""

    blog_object.log('info', 'test_compare_post_title: check post title')
    response = blog_object.get_url(test_get_known_id_resource)
    post_title = response.json()
    expected_title = 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
    assert post_title['title'] == expected_title


def test_get_unknown_id(blog_object, test_get_unknown_id_resource):
    """get 404 error for unknown post id"""

    blog_object.log('info', 'test_get_unknown_id: get status code 404 error')
    response = blog_object.get_url(test_get_unknown_id_resource)
    assert response.status_code == 404


def test_request_wrong_url(blog_object, test_request_wrong_url_resource):
    """get 404 error for unknown url"""

    blog_object.log('info', 'test_request_wrong_url: get code 404 error')
    response = blog_object.get_url(test_request_wrong_url_resource)
    assert response.status_code == 404
