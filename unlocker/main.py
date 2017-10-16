import requests
import json
import time

time.sleep(20)
url = 'http://vault:8200/v1/sys/unseal'
keys = [
        { 'key':'UNSEAL KEY ONE' },
        { 'key':'UNSEAL KEY TWO' },
        { 'key':'UNSEAL KEY THREE' },
]
for key in keys:
    r = requests.post(url, json=key)
    print(r.status_code)
    print(r.json())
    time.sleep(1)
