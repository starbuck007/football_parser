import configparser
import json
import requests

def query(url, querystring = False):

    config = configparser.ConfigParser()
    config.read('config.ini')

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': config.get('api', 'token')
    }
    if not querystring:
        response = requests.request("GET", url, headers=headers)
    else:
        response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    return data['response']

