from dataclasses import dataclass, field


@dataclass
class Receipt:
    url: str
    method: str = 'GET'
    status: int = 200
    headers: dict = field(default_factory=lambda: {})
    body: str = ''
    redirect: str = '/'
    timeout: int = 0


@dataclass
class Mock:
    path: str
    host: str = '127.0.0.1'
    port: int = 8080
    content: list = field(default_factory=lambda: [])

    def mock(self, **kwargs):
        pass

    def redirect(self, **kwargs):
        pass

    def add(self, **kwargs):
        self.content.append(Receipt(**kwargs))

    def instant(self, **kwargs):
        return self

    def __enter__(self):
        print('Enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')


m = Mock('/user/campaign')
m.add(method='GET', status=200, body='{}', timeout=2, url='/')
