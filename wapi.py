import requests, json


res = requests.get('').text

print(res)