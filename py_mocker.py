from collections import namedtuple


receipt = namedtuple('receipt', ['method', 'url', 'status', 'headers', 'body', 'redirect', 'timeout'])


class Mock:
    def mock(self, *args, **kwargs):
        pass

    def redirect(self, receipt):
        pass

    def instant(self, receipt):
        # ToDo: Add mock here
        return self

    def __enter__(self):
        print('Enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')



def get_mock(host='localhost', port=8080, path='/'):
    print('get_mock')
    return Mock()

