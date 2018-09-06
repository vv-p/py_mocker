from conftest import mock_body, mock_status


def test_mock_status_code(mock_response):
    assert mock_status == mock_response.status_code


def test_mock_content(mock_response):
    assert mock_body == mock_response.text
