import pytest
from blog import Blog


@pytest.fixture(scope="session", autouse=True)
def endPoints_session(request):
    """ We can put here a lot of different preparing
        stuff for our extended unit tests
    """

    blog.log('info', '#############################')
    blog.log('info', 'STARTED check endpoints testing')
    blog.log('info', '#############################')

    def end_session():
        """teardown fixture to finish tests"""

        blog.log('info', '#############################')
        blog.log('info', 'STOPPED check endpoints testing')
        blog.log('info', '#############################')

    request.addfinalizer(end_session)
