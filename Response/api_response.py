import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

def response(url, parameters=None):
    response = requests.post(url, params=parameters)
    print(jprint(response.json()))


if __name__ == '__main__':
    url = 'https://xyz_pip.com'
    _params = {
            'abc': 'bbc'
        }
    response(url, _params)
