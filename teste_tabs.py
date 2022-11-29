import requests

url = "https://viacep.com.br/ws/PA/BELEM/ NINA RIBEIRO /json/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
