import requests

# Get known mock
r = requests.get('http://127.0.0.1:8080/user/1121/campaign/3321/status')
print(r.text)

# Get unknown mock
r = requests.get('http://127.0.0.1:8080/user/1121/campaigns/3321/status')
print(r.text)

# setup new mock
headers = {'py-mocker': 'add_me'}
r = requests.get('http://127.0.0.1:8080/user/1121/campaigns/3321/status', headers=headers)
print(r.text)
