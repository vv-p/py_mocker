import requests

from py_mocker import Mock


# setup new mock

user_api = Mock(path='/user')
status = user_api.add(
    url='/campaigns',
    body='Mock installed'
)

if status:
    print('Mock created')
else:
    print('Mock wasn\'t created')

# Get the mock

r = requests.get('http://127.0.0.1:8080/user/campaigns')
print(r.status_code)
print(r.text)
