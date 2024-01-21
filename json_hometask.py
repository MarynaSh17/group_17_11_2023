import requests
import json

url = "https://dummyjson.com/quotes?limit=100"
response = requests.get(url)
data = response.json()

with open('quotes.json', mode='w') as file:
    json.dump(data, file, indent=4)

print("Дані успішно збережені в файл quotes.json.")