from pprint import pprint
import requests

url_purchase = 'https://dummyjson.com/carts'

response = requests.get(url = url_purchase)
data_from_net = response.json()
cards = data_from_net['carts']
# pprint(cards)
for card in cards:
    user = card['userId']
    if user == 56:
        products = card['products']
        # print(products)
        for product in products:
            list = product['title'] #userId=56 full product list
            # print(list)
            if product['discountPercentage'] > 15:
                print(list)
