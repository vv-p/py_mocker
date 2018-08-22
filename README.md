# py_mocker
Easy mocking with python, aiohttp and docker


## Запуск веб-сервера мокера

```bash
docker run -d -p 8080:8080 py_mocker
```

## Работа с мокером

```python
from mock import get_mock, receipt

# Initialize mocker client
mock = get_mock(host='localhost', port=8080)

@mock(receipt('GET', 'ya.ru', 200, '', '{}'))
def test():
    assert True
```

## Формат файла-рецепта для мока

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

