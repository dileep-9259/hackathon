import openai
from flask import *
from flask_cors import CORS

openai.api_type = "azure"
openai.api_base = "https://hackmee1-fc.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "a2f35be0feb04e2187945ef2e7c03b0b"

app = Flask(__name__)
CORS(app)


class Product:
    def __init__(self, pid, name, category_name, image, price, rating, description, sizes):
        self.id = pid
        self.name = name
        self.category_name = category_name
        self.image = image
        self.price = price
        self.rating = rating
        self.description = description
        self.sizes = sizes

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'category_name': self.category_name,
            'image': self.image,
            'price': self.price,
            'rating': self.rating,
            'description': self.rating,
            'sizes': self.sizes
        }


def plp():
    p1 = Product(1, "pid1", "kurtas", "", 100, 4.5, "Descpriopn", "S,M,L,XL")
    p2 = Product(2, "pid2", "kurtas", "", 110, 4.6, "Descpriopn", "S,M,L,XL")
    p3 = Product(3, "pid3", "kurtas", "", 120, 4.7, "Descpriopn", "S,M,L,XL")
    p4 = Product(4, "pid1", "kurtas", "", 120, 4.7, "Descpriopn", "S,M,L,XL")
    product_list = [p1, p2, p3, p4]
    return product_list


def func1(products_list):
    product_dicts = []
    for product in products_list:
        product_dict = {
            "id": product.id,
            "name": product.name,
            "category_name": product.category_name,
            "image": product.image,
            "price": product.price,
            "rating": product.rating,
            "description": product.description,
            "sizes": product.sizes
        }
        product_dicts.append(product_dict)
    return product_dicts


@app.route("/", methods=['POST'])
def f1():
    json = request.get_json()
    input_string = json["input_string"]
    message = "Answer in single word. Categorise the statement  for shopping app user input " + input_string + " into the following search / buy / pick  / scroll down / scroll up  / exit "
    print("Input Message : " + input_string)
    response = openai.ChatCompletion.create(
        engine="TheGeneratorsGPT35-16k",
        messages=[
            {"role": "user", "content": message},
            {"role": "system", "content": "A shopping app where user is searching by voice. Search means user is trying to query for a product "},
            {"role": "system", "content":" Exit means he wants to end the conversation. Pick means he wants to select a particular one based on the index of the item or the description of the product . Buy means user likes it and  ready to take the product"}
        ]
        ,
        temperature=0.3,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    user_intention = response.choices[0].message.content
    products_list = []
    print("user intent is : " + user_intention)
    if ("search" in user_intention.lower()):
        print("Search flow started")
        extracted_attributes = search(message)
        print("Attributes Extaction : " + extracted_attributes)
        #res = json.loads(extracted_attributes)
        #print("The converted dictionary : " + str(res))
        products_list = plp()
        print(products_list)
        print("Search flow ended")

    new_obj = {
        "user_intent": user_intention.upper(),
        "plp": func1(products_list)
    }
    return new_obj


@app.route("/plp", methods=['POST'])
def fetchPlpAPI():
    products_list = plp()
    new_obj = {
        "plp": func1(products_list)
    }
    return new_obj


@app.route("/delete", methods=['POST'])
def delete():
    json = request.get_json()
    input_string = json["input_string"]
    message = input_string  # "Answer in single word Categorise the statement " + input_string + " into the following search / buy / scroll down / scroll up  / exit"
    print(message)
    response = openai.ChatCompletion.create(
        engine="TheGeneratorsGPT35-16k",
        messages=[
            {"role": "user", "content": message}
        ]
        ,
        temperature=0.3,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    user_intent = response.choices[0].message.content
    return user_intent


def search(input_string):
    message = "Can you find category, color , fabric, occasion, sleeve type ,price from the string " + input_string + " reply each in one upper case as json capital word as json"
    print(message)
    response = openai.ChatCompletion.create(
        engine="TheGeneratorsGPT35-16k",
        messages=[
            {"role": "user", "content": message}
        ]
        ,
        temperature=0.3,
        max_tokens=4000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    x = response.choices[0].message.content
    return x


if __name__ == '__main__':
    app.run(port=7777)
