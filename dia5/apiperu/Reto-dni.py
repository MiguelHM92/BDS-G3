import requests
import os

api_token = os.environ.get('TOKEN')

API_URL = 'https://apiperu.dev/api/dni'

dni = input('Ingrese el DNI a consultar: ')

data_request = {
    "dni": dni
}

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL, json=data_request, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
