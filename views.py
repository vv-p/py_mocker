# views.py
import re

from dataclasses import dataclass, field
from aiohttp import web
from collections import namedtuple

MockSignature = namedtuple('MockSignature', ['method', 'path'])


@dataclass
class MockData:
    status: int = 200
    headers: dict = field(default_factory=lambda: {})
    body: str = 'MockData Placeholder'
    json: dict = field(default_factory=lambda: {})
    redirect: str = '/'
    timeout: int = 0


test_signature = MockSignature('GET', '/user/.*?/campaign/.*?/status')
MOCKS = {
    test_signature: MockData(),
}


def check_request(method, path):
    for sig in MOCKS:
        if sig.method == method and re.match(sig.path, path):
            return MOCKS[sig]
    return None


def add(request):
    """Add new mock"""
    return True


def remove(request):
    """Remove existing mock"""
    return True


mock_methods = {
    'add': add,
    'remove': remove,
}


async def index(request):
    mock_data = check_request(request.method, request.path)
    if mock_data:
        text = mock_data.body
        return web.Response(text=text)

    if 'py-mocker' not in request.headers:
        text = 'Unknown resource: {0.method} {0.path}'.format(request)
        return web.Response(text=text)

    mocker_command = request.headers['py-mocker']

    if mocker_command not in mock_methods:
        text = 'Unknown mocker command'
        return web.Response(text=text)

    mock_methods[mocker_command](request)
    text = 'Do some shit'
    return web.Response(text=text)
