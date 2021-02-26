import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

resp = requests.get('https://api.openbrewerydb.org/breweries')

for item in resp.json():
    print(item.get('name'))