import requests

resp = requests.get('https://api.openbrewerydb.org/breweries')

print(resp.json())