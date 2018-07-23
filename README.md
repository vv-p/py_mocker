# py_mocker
Easy mocking with python, aiohttp, templates and docker

## Формат файла-рецепта для мока

```text
GET

/test/{campaign_id:\d+}?advertiser_id={advertiser_id:\d+}

200

Server: nginx/1.2.1

{
  "version": 1,
  "campaign": "{{ campaign_id }}",
  "advertiser_id": {{ advertiser_id }},
}

```

## Создание мока через апи:

POST /py_mocker/utils.resolveScreenName
```json
{
  "response": {
    "object_id": 1,
    "type": "application"
  }
}
```
## Получение рецепта мока

GET /py_mocker/utils.resolveScreenName

вернёт тело мока, если он существует

GET /py_mocker/UnknownMock

вернёт 404, если мока нет

GET /py_mocker 

вернёт список всех моков в json

```json
{
  "/utils.resolveScreenName": "{a: 1, b: 2}"
}
```
