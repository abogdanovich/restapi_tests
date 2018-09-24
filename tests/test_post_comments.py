"""Python tests to check the given endpoints like
https://jsonplaceholder.typicode.com/posts/<id>/comments
Last updates: 9/24/18
author: Alex Bogdanovich
"""
# -*- coding: utf-8 -*-

import pytest
from utils import comments_data


def test_get_known_comment_id(blog_object, test_get_comment_id_resource):
    """get status code 200"""

    blog_object.log('info', 'test_get_known_comment_id: get status code 200')
    response = blog_object.get_url(test_get_comment_id_resource)
    assert response.status_code == 200


def test_count_post_comments(blog_object, test_get_comment_id_resource):
    """get status code 200"""

    blog_object.log('info', 'test_count_post_comments: get status code 200')
    response = blog_object.get_url(test_get_comment_id_resource)
    assert len(response.json()) == 5


def test_check_postid_comments(blog_object, test_get_comment_id_resource):
    """check userid of the given comment"""

    blog_object.log('info', 'test_check_postid_comments: get correct userid')
    response = blog_object.get_url(test_get_comment_id_resource)
    assert response.json()[0]['postId'] == 1


def test_request_wrong_comment_url(blog_object, request_wrong_comment_url_res):
    """get 404 error for unknown url"""

    blog_object.log('info', 'request_wrong_comment_url_res: get code 404 error')
    response = blog_object.get_url(request_wrong_comment_url_res)
    assert response.status_code == 404


@pytest.mark.parametrize("index, name, email", comments_data)
def test_check_names_of_comments(blog_object, index, name, email, test_get_comment_id_resource):
    """check all comments names"""

    response = blog_object.get_url(test_get_comment_id_resource)
    blog_object.log('info', 'test_check_names_of_comments: {} - {}'.format(
        response.json()[index]['name'],
        comments_data[index][1])
                    )
    blog_object.log('info', 'test_check_names_of_comments: {} - {}'.format(
        response.json()[index]['email'],
        comments_data[index][1])
                    )
    assert response.json()[index]['name'] == comments_data[index][1]
    assert response.json()[index]['email'] == comments_data[index][2]
