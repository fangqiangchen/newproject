import requests

r = requests.get('https://www.baidu.com')

r = r.text


print(r)