import requests

TOKEN = '384f18c42abc35fd35b8b213a74605feaa547b7dc14ff89935daba4a31a5849d'
API_URL = 'https://apiperu.dev/api/ruc'

ruc = input('Ingrese el RUC: ')

data_request = {
    "ruc": ruc
}

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL, json=data_request, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")

