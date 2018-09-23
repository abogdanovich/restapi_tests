"""Python tests to check the given endpoints like
https://jsonplaceholder.typicode.com/posts
https://jsonplaceholder.typicode.com/posts/<id>
https://jsonplaceholder.typicode.com/posts/<id>/comments
Last updates: 9/23/18
author: Alex Bogdanovich
"""
# -*- coding: utf-8 -*-
import pytest


def test_get_known_comment_id(blog_object, test_get_known_comment_id_resource):
    """get status code 200"""
    blog_object.log('info', 'test_get_known_comment_id: get status code 200')
    response = blog_object.get_url(test_get_known_comment_id_resource)
    assert response.status_code == 200


def test_request_wrong_comment_url(blog_object, test_request_wrong_comment_url_resource):
    """get 404 error for unknown url"""
    blog_object.log('info', 'test_request_wrong_comment_url: get status code 404 error')
    response = blog_object.get_url(test_request_wrong_comment_url_resource)
    assert response.status_code == 404
