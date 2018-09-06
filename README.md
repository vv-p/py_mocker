# py_mocker
Easy mocking with python, aiohttp and docker

## Installation

```bash
python3.7 -m venv venv
source venv/bin/activate
pip install -e .  # “Development Mode” setup
```

## Run mocker web-server

```bash
python -m py_mocker
======== Running on http://0.0.0.0:8080 ========
(Press CTRL+C to quit)
```

## Run tests
```bash
cd tests
pip install -r requirements.txt
pytest
```

## Examples

```python
from py_mocker import Mock, Receipt

# Initialize mocker client
some_api = Mock(path='/', host='localhost', port=8080)

# Add persistent mock
some_api.add(method='POST', url='/test/post')


# Different usages of py_mocker library

@some_api.mock(receipt='example.mock')
def test_api_one():
    """
    Mock with file
    """
    assert True


@some_api.mock(method='GET', url='/user/package', status=200, body='{}', timeout=2)
def test_api_two():
    """
    Mock with direct arguments
    """
    assert True


def test_api_three():
    """
    Mock with context manager
    """
    r = Receipt(
        method='GET',
        url='/user/campaign',
        status=200,
        headers={
            'x-xss-protection': '1; mode=block}',
        },
        json={
            'campaigns': [
                {
                    'id': 1,
                },
                {
                    'id': 2,
                },
            ]
        }
    )
    with some_api.instant(receipt=r):
        assert True


@some_api.redirect(url='/one/', to='', status=307, timeout=2)
def test_api_four():
    """
    Mock with redirect
    """
    assert True

```

## Mock-file example

```text
GET

/test/test_one/?advertiser_id=1221

200

Server: nginx/1.2.1

{
  "version": 1,
  "campaign": "test_one",
  "advertiser_id": 1121,
}

```

