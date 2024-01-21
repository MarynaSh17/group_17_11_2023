import pymongo
import config
# url1 = 'mongodb+srv://marinka685m16:<password>@newtest171123.pw6ovrr.mongodb.net/?retryWrites=true&w=majority'
url = 'mongodb+srv://{user}:{password}@' \
      'ewtest171123.pw6ovrr.mongodb.net/?retryWrites=true&w=majority'\
    .format(
    user=config.USER,
    password=config.PASSWORD,
)

client = pymongo.MongoClient(url)
db = client['library']
classic_coll = db['classic']
fiction_coll = db['fiction']

# add single document
# romeo_and_julieta = {
#     'author': 'W. Shekspir',
#     'year': 1650,
# }
# classic_coll.insert_one(romeo_and_julieta)

# add many documents
# garry_potter_collection = [
#     {
#         'title': 'Stone',
#         'price': 600,
#         'author': 'Joan',
#     },
#     {
#         'title': 'Prison',
#         'price': 850,
#         'author': 'Joan',
#     },
# ]
# fiction_coll.insert_many(garry_potter_collection)

# GET DATA
# first document
# result = fiction_coll.find_one()
# query = {'price': 850}
# result = fiction_coll.find_one(query)
# print(result)

# all data
result = fiction_coll.find()
print(result)
for book in result:
    print(book.get('description'))

# query = {'price': 100}
# query = {'price': {'$gte': 100}}
# query = {'price': {'$gt': 100}}
# query = {'price': {'$lte': 600}}
# query = {'price': {'$lt': 600}}
# query = {'title': {'$regex': 'Prison'}}
# query = {'title': 'Prison'}
# query = {'title': {'$regex': 'Prison'}, 'price': {'$lte': 900}, 'author': 'Joan'}
# query = {}
# result = fiction_coll.find(query)
# result = fiction_coll.find(query).limit(2)
# result = fiction_coll.find(query).sort('price').limit(2)
# result = fiction_coll.find(query).sort('price', -1).limit(2)
# result = fiction_coll.find(query).sort('price', -1).skip(1).limit(2)
# for book in result:
#     # print(book)
#     pass
# UPDATE
# filter_data = {'title': 'Prison'}
# new_data = {'$set': {'in_sale': False}}
# new_data = {'$inc': {'price': -101, 'warranty': 3}}
# new_data = {'$mul': {'price': 2}}
# processed = fiction_coll.update_one(filter_data, new_data)

# processed = fiction_coll.update_many(filter_data, new_data)
#
# print(processed)

# DELETE
# document
# query = {'price': 100}
# deleted = fiction_coll.delete_many(query)
# print(deleted)

# field
# query = {'title': 'Prison'}
# operation = {'$unset': {'warranty': 1}}
# updated = fiction_coll.update_many(query, operation)
# print(updated)

# # delete all data
# query = {}
# deleted = fiction_coll.delete_many(query)
# print(deleted)

# delete collection
# fiction_coll.drop()
# classic_coll.drop()

# delete db
# client.drop_database('library')