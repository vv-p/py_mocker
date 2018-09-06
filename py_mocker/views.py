# views.py
import re

from dataclasses import dataclass, field
from aiohttp import web
from collections import namedtuple

MockSignature = namedtuple('MockSignature', ['method', 'path'])


@dataclass
class MockData:
    url: str
    method: str = 'GET'
    status: int = 200
    headers: dict = field(default_factory=lambda: {})
    body: str = 'MockData Placeholder'
    json: dict = field(default_factory=lambda: {})
    redirect: str = ''
    timeout: int = 0


# Storage for mock receipts
# Key is instance of MockSignature and value is instance of MockData
MOCKS = {}


def get_mock(method, path):
    """
    Try to get mock if exists
    """
    for sig in MOCKS:
        if sig.method == method and re.match(sig.path, path):
            return MOCKS[sig]
    return None


def add(receipt):
    """Add new mock"""
    MOCKS[
        MockSignature(receipt['method'], receipt['url'])
    ] = MockData(**receipt)
    return 201


def remove(receipt):
    """Remove existing mock"""
    return 204


async def index(request):
    mock_data = get_mock(request.method, request.path)
    if mock_data:
        response = {
            'status': mock_data.status,
            'text': mock_data.body,
        }
        return web.Response(**response)

    if 'py-mocker' not in request.headers:
        return web.Response(status=404)

    mocker_command = request.headers['py-mocker']

    mock_methods = {
        'add': add,
        'remove': remove,
    }

    if mocker_command not in mock_methods:
        text = 'Unknown mocker command {}'.format(mocker_command)
        return web.Response(text=text, status=400)

    mock_receipt = await request.json()
    status = mock_methods[mocker_command](mock_receipt[0])
    return web.Response(status=status)
