from py_mocker import get_mock, receipt

# Initialize mocker client
some_api = get_mock(path='/', host='localhost', port=8080)


# Different usages of py_mocker library

@some_api.mock('example.mock')
def test_api_one():
    """
    Mock with file
    """
    assert True


@some_api.mock(method='GET', url='/user/package', status=200, body='{}', timeout=2)
def test_api_two():
    """
    Mock with direct arguments
    """
    assert True


def test_api_three():
    """
    Mock with context manager
    """
    r = receipt(
        method='GET',
        url='/user/campaign',
        status=200,
        headers={
            'x-xss-protection': '1; mode=block}',
        },
        json={
            'campaigns': [
                {
                    'id': 1,
                },
                {
                    'id': 2,
                },
            ]
        }
    )
    with some_api.instant(receipt=r):
        assert True


@some_api.redirect(url='/one/', to='', status=307, timeout=2)
def test_api_four():
    """
    Mock with redirect
    """
    assert True
