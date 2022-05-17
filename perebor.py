from urllib import request
import requests

f= open('text.txt')
for url in f:
    r = requests.get(url)
    sc = r.status_code
    if sc == 200:
        valid = 'Yes'
    else:
        valid = "Not valid"

    with open('text.txt', 'a') as a:
        print(f'URL: {url}', f'code:{valid}', file=a)