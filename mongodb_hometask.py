import pymongo
import requests
import config

# url1 = 'mongodb+srv://<username>:<password>@newtest171123.pw6ovrr.mongodb.net/?retryWrites=true&w=majority'
url = 'mongodb+srv://{user}:{password}@' \
      'ewtest171123.pw6ovrr.mongodb.net/?retryWrites=true&w=majority'\
    .format(
    user=config.USER,
    password=config.PASSWORD,
)
client = pymongo.MongoClient(url)
db = client['quotes_db']
collection = db['quotes']

# Запис усіх 100 цитат у колекцію
url_json = "https://dummyjson.com/quotes?limit=100"
response = requests.get(url_json)
quotes = response.json()['quotes']
# collection.insert_many(quotes)
# einstein_quotes = collection.find({'author': 'Albert Einstein'})
# for quote in einstein_quotes:
#     print(quote)

# Вибір цитат, що містять текст "success"
# success_quotes = collection.find({'quote': {'$regex': 'success'}})
# for list in success_quotes:
#     print(list)

# Додавання поля "favorite: True" до цитат автора "Mark Twain"
# collection.update_many({'author': 'Mark Twain'}, {'$set': {'favorite': True}})

# Видалення цитат автора "Vincent Van Gogh"
# collection.delete_many({'author': 'Vincent Van Gogh'})
# Видалення всіх даних з колекції
# collection.delete_many({})
