from pprint import pprint
import requests
import csv

url_csv = 'https://lms.ithillel.ua/api/lms/files/647c6b4e5d195a029f06aee4'

response = requests.get(url=url_csv)

content = response.content
# print(content)

with open('airport-codes_csv.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    print(reader)
    for row in reader:
        if row['iso_country'] == 'UA':
            print(row['name'])
