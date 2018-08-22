from mock import get_mock, receipt

# Initialize mocker client
mock = get_mock(host='localhost', port=8080)


# Three usages of py_mocker library

@mock('example.mock')
def test_api():
    assert True


@mock(receipt('GET', 'ya.ru', 200, '', '{}'))
def test_api_two():
    assert True


def test_api_three():
    with mock('example.mock') as m:
        assert True
