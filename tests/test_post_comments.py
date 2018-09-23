"""Python tests to check the given endpoints like
https://jsonplaceholder.typicode.com/posts
https://jsonplaceholder.typicode.com/posts/<id>
https://jsonplaceholder.typicode.com/posts/<id>/comments
Last updates: 9/23/18
author: Alex Bogdanovich
"""
# -*- coding: utf-8 -*-
import pytest

comments_data = [
    (0, 'id labore ex et quam laborum'),
    (1, 'quo vero reiciendis velit similique earum'),
    (2, 'odio adipisci rerum aut animi'),
    (3, 'alias odio sit'),
    (4, 'vero eaque aliquid doloribus et culpa'),
]


def test_get_known_comment_id(blog_object, test_get_known_comment_id_resource):
    """get status code 200"""
    blog_object.log('info', 'test_get_known_comment_id: get status code 200')
    response = blog_object.get_url(test_get_known_comment_id_resource)
    assert response.status_code == 200


def test_count_post_comments(blog_object, test_get_known_comment_id_resource):
    """get status code 200"""
    blog_object.log('info', 'test_count_post_comments: get status code 200')
    response = blog_object.get_url(test_get_known_comment_id_resource)
    assert len(response.json()) == 5


def test_request_wrong_comment_url(blog_object, test_request_wrong_comment_url_resource):
    """get 404 error for unknown url"""
    blog_object.log('info', 'test_request_wrong_comment_url: get status code 404 error')
    response = blog_object.get_url(test_request_wrong_comment_url_resource)
    assert response.status_code == 404


@pytest.mark.parametrize("pos, expected", comments_data)
def test_check_names_of_comments(blog_object, pos, expected, test_get_known_comment_id_resource):
    """check all comments names"""
    blog_object.log('info', 'test_check_names_of_comments: check names')
    response = blog_object.get_url(test_get_known_comment_id_resource)
    blog_object.log('info', 'test_check_names_of_comments: {} - {}'.format(response.json()[pos]['name'], comments_data[pos]))
    assert response.json()[pos]['name'] == comments_data[pos][1]
