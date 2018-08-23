# views.py
from dataclasses import dataclass, field
from aiohttp import web
from collections import namedtuple

MockSignature = namedtuple('MockSignature', ['method', 'path'])


@dataclass
class MockData:
    status: int = 200
    headers: dict = field(default_factory=lambda: {})
    body: str = ''
    json: dict = field(default_factory=lambda: {})
    redirect: str = '/'
    timeout: int = 0


test_signature = MockSignature('GET', '/dsfsdf/')
MOCKS = {
    test_signature: MockData(),
}


async def index(request):
    signature = MockSignature(request.method, request.path)
    if signature not in MOCKS:
        MOCKS[signature] = MockData()
        text = 'Unknown resource {}'.format(request.method)
    else:
        text = 'Well-known resource {}'.format(request.method)
    return web.Response(text=text)
