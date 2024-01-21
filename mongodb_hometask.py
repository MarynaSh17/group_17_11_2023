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
db = client['library']
collection = db['quotes']
response = requests.get('https://dummyjson.com/quotes?limit=100')
data = response.json()
# db.collection.insert_many([data])
# print(data)
query = {'title': {'$regex': 'Prison'}}
query = {'quotes': 'Albert Einstein'}
cursor = db.collection.find(query)
for document in cursor:
    print(document)

# for book in result:
#     print(book.get('description'))
# print(f"{len(quotes)} quotes are successfully inserted into the collection.")
# result = books.find()
# print(result)
# for book in result:
#     if book['author'] == 'Albert Einstein':
#         books.insert_one(quotes)
# print('Цитати Альберта Ейнштейна успішно додані до бази даних MongoDB.')
# query = {'author': 'Albert Einstein'}
# for item in books.find({'screen_name':'Albert Einstein'}):
#     print(item)
