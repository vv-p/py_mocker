import pytest
import requests

from py_mocker import Mock

mock_body = 'Mock installed'
mock_status = requests.codes.partial_content


@pytest.fixture(scope='module')
def mock_response():
    user_api = Mock(path='/user')
    user_api.add(
        url='/campaigns/',
        body=mock_body,
        status=mock_status,
    )
    yield requests.get('http://127.0.0.1:8080/user/campaigns')
