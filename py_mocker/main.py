import requests

from dataclasses import dataclass, field
from marshmallow import Schema, fields


@dataclass
class Receipt:
    url: str
    method: str = 'GET'
    status: int = requests.codes.ok
    headers: dict = field(default_factory=lambda: {})
    body: str = ''
    redirect: str = '/'
    timeout: int = 0


class ReceiptSchema(Schema):
    url = fields.Str()
    method = fields.Str()
    status = fields.Int()
    headers = fields.Dict()
    body = fields.Str()
    redirect = fields.Str()
    timeout = fields.Float()


@dataclass
class Mock:
    path: str
    host: str = '127.0.0.1'
    port: int = 8080

    def mock(self, **kwargs):
        pass

    def redirect(self, **kwargs):
        pass

    @property
    def url(self):
        return 'http://{}:{}'.format(self.host, self.port)

    def make_path(self, path):
        return '{}{}'.format(self.path, path)

    def add(self, url, **kwargs):
        headers = {
            'py-mocker': 'add'
        }

        schema = ReceiptSchema()
        mock_receipt = Receipt(url, **kwargs)
        mock_receipt.url = self.make_path(url)
        json = schema.dump(mock_receipt)

        r = requests.post(
            '{}'.format(self.url),
            headers=headers,
            json=json
        )

        return True if r.status_code == requests.codes.created else False

    def instant(self, **kwargs):
        return self

    def __enter__(self):
        print('Enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')
