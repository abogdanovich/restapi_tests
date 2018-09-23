"""Python tests to check the given endpoints like
https://jsonplaceholder.typicode.com/posts
https://jsonplaceholder.typicode.com/posts/<id>
https://jsonplaceholder.typicode.com/posts/<id>/comments
Last updates: 9/23/18
author: Alex Bogdanovich
"""
# -*- coding: utf-8 -*-
import pytest


def test_get_status_code_200(blog_object, test_get_status_code_200_resource):
    """get status code 200 for all posts"""
    blog_object.log('info', 'test_get_response_200: get status code 200')
    response = blog_object.get_url(test_get_status_code_200_resource)
    assert response.status_code == 200


def test_counting_of_posts(blog_object, test_get_status_code_200_resource):
    """count the list of all posts"""
    blog_object.log('info', 'test_counting_of_posts: check 100 posts')
    response = blog_object.get_url(test_get_status_code_200_resource)
    assert len(response.json()) == 100


def test_send_post_request(blog_object, test_send_post_request_resource):
    """send POST instead of GET"""
    blog_object.log('info', 'test_send_post_request: send wrong method')
    response = blog_object.get_url(test_send_post_request_resource)
    assert response.status_code == 201


def test_send_unknown_payload(blog_object, test_send_unknown_payload_resource):
    """try to send unknown payload with get"""
    blog_object.log('info', 'test_send_unknown_payload: unknown payload')
    response = blog_object.get_url(test_send_unknown_payload_resource)
    assert response.status_code == 200


def test_wrong_request_url(blog_object, test_wrong_request_url_resource):
    """check wrong url and get 404"""
    blog_object.log('info', 'test_wrong_url: we should get 404 status code')
    response = blog_object.get_url(test_wrong_request_url_resource)
    assert response.status_code == 404
