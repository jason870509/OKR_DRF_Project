import requests

url = "http://localhost:8000/reports/list_create"
response = requests.get(url)

print(response.json())