from collections import namedtuple


receipt = namedtuple('receipt', ['method', 'url', 'status', 'headers', 'body'])


class Mock:
    pass


def get_mock(host='localhost', port=8080):
    return Mock()

