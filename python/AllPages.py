import requests
import json

base_url = 'https://webexapis.com/v1/rooms'

code = 'ODkxYWNhMDctNTJhMi00YzMzLWI3ZWUtOWFiNDEwMTU1YzMyN2Q1OTg5ZmUtMjNl_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + code }

results = []

response = requests.get( url = base_url, headers = httpHeaders)



while base_url:
    response = requests.get( url = base_url, headers = httpHeaders)
    url = response.links
    results = json.loads(response.text)
    print(json.dumps(results, indent=4, sort_keys=True))
    if 'next' in url:
          base_url = url['next']['url']
    else:
          base_url = ''