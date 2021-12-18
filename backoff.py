# Credit to Ben Finkel from CBT Nuggets on this script
# Import requests module to send http-based API calls
import requests


# Module that contains classes and functions that can be used for logging of other imported modules
import logging 

# Importing HTTP adapter class. Provides an interface for http requests
from requests.adapters import HTTPAdapter

# Import session class to establish session
from requests.sessions import Session

#Import retry class to create retry object
from urllib3.util.retry import Retry

url = 'https://api.discogs.com/'

logging.basicConfig(level=logging.DEBUG)

def get_releases(release_id): 
    endpoint = f'/releases/{release_id}'

    # Creates a session
    # Specifies how we will backoff and what errors to look for

    session = requests.Session()
    retries = Retry(total=3, backoff_factor=.1, status_forcelist=[429,500,502,503,504])
    session.mount(url, HTTPAdapter(max_retries=retries))

    print(f'Getting release #{release_id}')

    resp = session.get(url+endpoint)
    resp_code = resp.status_code

    return resp_code

for i in range(0,30): 
    get_releases(249504)


