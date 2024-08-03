import requests
import json

data = {
    'grant_type':'authorization_code',
    'client_id':'REST_ID',
    'redirect_uri':'REDIRECT_URL',
    'code': 'CODE'
    }

response = requests.post('https://kauth.kakao.com/oauth/token', data=data)
tokens = response.json()

with open("tokens.json","w") as kakao:
    json.dump(tokens, kakao)